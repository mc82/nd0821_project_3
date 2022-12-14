# Put the code for your API here.
from fastapi import FastAPI
import json

from pydantic import BaseModel, Field

from python.ml.model import load_model, inference
from python.ml.data import process_data
from python.ml.helper import unpickle_object
from python.config import MODEL_PATH, BINARIZER_PATH, ENCODER_PATH


class PersonalAttributes(BaseModel):
    age: int
    fnlgt: int
    workclass: str
    education: str
    education_num: int = Field(alias="education-num")
    marital_status: str = Field(alias="marital-status")
    occupation: str
    relationship: str
    race: str
    sex: str
    capital_gain: int = Field(alias="capital-gain")
    capital_loss: int = Field(alias="capital-loss")
    hours_per_week: int = Field(alias="hours-per-week")
    native_country: str = Field(alias="native-country")


class SalaryCategory(BaseModel):
    category: str


app = FastAPI()


@app.get("/")
async def say_hello():
    return {"Greeting": "Moin Moin!"}


@app.post("/income/", response_model=SalaryCategory)
def classify_income(personal_attributes: PersonalAttributes):

    import pandas as pd

    personal_attributes_d = personal_attributes.dict()
    personal_attributes_d["salary"] = ">50"
    df = pd.DataFrame(personal_attributes_d, index=[0])
    df.columns = [column.replace("_", "-") for column in df.columns]

    print(MODEL_PATH)
    model = load_model(path=MODEL_PATH)

    cat_features = [
        "workclass",
        "education",
        "marital-status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "native-country",
    ]

    encoder = unpickle_object(ENCODER_PATH)
    lb = unpickle_object(BINARIZER_PATH)
    X_test, y_test, encoder, lb = process_data(
        df,
        categorical_features=cat_features,
        label="salary",
        training=False,
        encoder=encoder,
        lb=lb,
    )

    prediction = inference(model, X_test)
    print(prediction)

    predicted_class = lb.inverse_transform(prediction[0])
    predicted_class[0]
    return {"category": predicted_class[0]}
