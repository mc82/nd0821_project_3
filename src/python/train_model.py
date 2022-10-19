# Script to train machine learning model.

from sklearn.model_selection import train_test_split
import pandas as pd
from yaml import load
import pickle

from .config import DATA_INPUT_PATH, MODEL_PATH, ENCODER_PATH, BINARIZER_PATH
from python.ml.data import process_data
from python.ml.model import train_model, inference, compute_model_metrics


data = load_data(DATA_INPUT_PATH)


# Optional enhancement, use K-fold cross validation instead of a train-test split.
train, test = train_test_split(data, test_size=0.20)

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

X_train, y_train, encoder, lb = process_data(
    train, categorical_features=cat_features, label="salary", training=True
)

X_test, y_test, encoder, lb = process_data(
    train,
    categorical_features=cat_features,
    label="salary",
    training=False,
    encoder=encoder,
    lb=lb,
)

model = train_model(X_train, y_train)

predictions = inference(model=model, X=X_test)

precision, recall, fbeta = compute_model_metrics(preds=predictions, y=y_test)

print(precision)

pickle_objects(model, MODEL_PATH)
pickle_objects(encoder, ENCODER_PATH)
pickle_objects(lb, BINARIZER_PATH)
