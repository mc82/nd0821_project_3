# Script to train machine learning model.


from sklearn.model_selection import train_test_split

from .config import (
    DATA_INPUT_PATH,
    MODEL_PATH,
    ENCODER_PATH,
    BINARIZER_PATH,
    CAT_FEATURES,
    MODEL_METRICS_PATH,
    PERFORMANCE_TEMPLATE,
)
from python.ml.data import process_prediction_data, process_training_data
from python.ml.model import train_model, inference, compute_model_metrics, save_model
from python.ml.helper import pickle_object, load_data
from python.ml.slicer import Slicer

data = load_data(DATA_INPUT_PATH)


def log_performance(message: str):
    with open(MODEL_METRICS_PATH, "a") as f:
        f.write(f"{message}\n")


def show_performance(slice: str, precision: float, recall: float, fbeta: float):
    print


if __name__ == "__main__":
    train, test = train_test_split(data, test_size=0.20)

    X_train, y_train, encoder, label_binarizer = process_training_data(data=train)

    model = train_model(X_train, y_train)

    X_test, y_test = process_prediction_data(
        data=test, encoder=encoder, label_binarizer=label_binarizer
    )

    predictions = inference(model=model, X=X_test)

    precision, recall, fbeta = compute_model_metrics(preds=predictions, y=y_test)

    show_performance(slice="total", precision=precision, recall=recall, fbeta=fbeta)

    save_model(model, MODEL_PATH)
    pickle_object(encoder, ENCODER_PATH)
    pickle_object(label_binarizer, BINARIZER_PATH)

    # Analyze performance on slices
    slicer = Slicer(column_names=CAT_FEATURES, df=test)
    slicer.fit()
    slices = slicer.transform(dfs=[test])

    for slice in slices:
        X_test, y_test = process_prediction_data(
            slice[0], encoder=encoder, label_binarizer=label_binarizer
        )

        predictions = inference(model=model, X=X_test)

        precision, recall, fbeta = compute_model_metrics(preds=predictions, y=y_test)

        performance_message = PERFORMANCE_TEMPLATE.format(
            slice=slice[1] + " " + slice[2],
            precision=precision,
            recall=recall,
            fbeta=fbeta,
        )

        print(performance_message)
        log_performance(performance_message)
