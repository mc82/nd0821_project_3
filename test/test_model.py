import numpy as np
from sklearn.linear_model import LogisticRegression
from python.ml.model import train_model, compute_model_metrics, inference


def test_train_model(given_X, given_y):
    given_X = given_X
    given_y = given_y
    expected_data_type = LogisticRegression

    result = train_model(X_train=given_X, y_train=given_y)

    assert isinstance(result, expected_data_type)


def test_compute_model_metrics(given_y, given_predictions):
    given_y = given_y
    given_predictions = given_predictions
    expected_result_data_types = (np.float64, np.float64, np.float64)
    result = compute_model_metrics(y=given_y, preds=given_predictions)
    assert expected_result_data_types == tuple([type(obj) for obj in result])


def test_inference(given_X, given_model):
    given_X = given_X
    given_model = given_model
    expected_result_data_type = np.ndarray
    result = inference(model=given_model, X=given_X)
    assert type(result) == expected_result_data_type
