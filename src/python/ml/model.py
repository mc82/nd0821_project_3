from sklearn.metrics import fbeta_score, precision_score, recall_score
from sklearn.linear_model import LogisticRegression
import numpy as np
from numpy.typing import NDArray
from typing import Tuple

from python.ml.helper import pickle_object, unpickle_object


# Optional: implement hyperparameter tuning.
def train_model(
    X_train: np.typing.NDArray, y_train: np.typing.NDArray
) -> LogisticRegression:
    """
    Trains a machine learning model and returns it.

    Inputs
    ------
    X_train : np.array
        Training data.
    y_train : np.array
        Labels.
    Returns
    -------
    model
        Trained machine learning model.
    """

    model = LogisticRegression()
    model.fit(X_train, y_train)
    return model


def compute_model_metrics(
    y: NDArray, preds: NDArray
) -> Tuple[np.float64, np.float64, np.float64]:
    """
    Validates the trained machine learning model using precision, recall, and F1.

    Inputs
    ------
    y : np.array
        Known labels, binarized.
    preds : np.array
        Predicted labels, binarized.
    Returns
    -------
    precision : float
    recall : float
    fbeta : float
    """
    fbeta = fbeta_score(y, preds, beta=1, zero_division=1)
    precision = precision_score(y, preds, zero_division=1)
    recall = recall_score(y, preds, zero_division=1)
    return precision, recall, fbeta


def inference(model, X):
    """Run model inferences and return the predictions.

    Inputs
    ------
    model : ???
        Trained machine learning model.
    X : np.array
        Data used for prediction.
    Returns
    -------
    preds : np.array
        Predictions from the model.
    """
    return model.predict(X)


def save_model(model, path):
    pickle_object(model, path)


def load_model(path):
    return unpickle_object(path)
