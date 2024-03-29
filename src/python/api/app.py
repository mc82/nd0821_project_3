# Put the code for your API here.
from fastapi import FastAPI
import json
import os

from python.ml.model import load_model, inference
from python.ml.data import process_prediction_data
from python.ml.helper import unpickle_object
from python.config import MODEL_PATH, BINARIZER_PATH, ENCODER_PATH
from .schema import PersonalAttributes, SalaryCategory
from .processor import preprocess_personal_attributes, post_process_prediction


if "DYNO" in os.environ and os.path.isdir(".dvc"):
    os.system("dvc config core.no_scm true")
    if os.system("dvc pull --remote s3") != 0:
        exit("dvc pull failed")
    os.system("rm -r .dvc .apt/usr/lib/dvc")


app = FastAPI(debug=True)


@app.get("/")
async def say_hello():
    return json.dumps({"Greeting": "Moin Moin!"})


@app.post("/income/", response_model=SalaryCategory)
def classify_income(personal_attributes: PersonalAttributes):

    encoder = unpickle_object(ENCODER_PATH)
    label_binarizer = unpickle_object(BINARIZER_PATH)

    prediction_data = preprocess_personal_attributes(
        personal_attributes=personal_attributes
    )

    X_test, _ = process_prediction_data(
        prediction_data, encoder=encoder, label_binarizer=label_binarizer
    )

    model = load_model(path=MODEL_PATH)

    prediction = inference(model, X_test)

    return post_process_prediction(
        prediction=prediction, label_binarizer=label_binarizer
    )
