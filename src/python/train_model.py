# Script to train machine learning model.

from sklearn.model_selection import train_test_split

from .config import DATA_INPUT_PATH, MODEL_PATH, ENCODER_PATH, BINARIZER_PATH
from python.ml.data import process_data
from python.ml.model import train_model, inference, compute_model_metrics, save_model
from python.ml.helper import pickle_object, load_data
from python.ml.slicer import Slicer

data = load_data(DATA_INPUT_PATH)


def show_performance(slice: str, precision: float, recall: float, fbeta: float):
    PERFORMANCE_TEMPLATE = "Performance on {slice}: precision: {precision}, recall: {recall}, fbeta: {fbeta}"
    print(
        PERFORMANCE_TEMPLATE.format(
            slice=slice, precision=precision, recall=recall, fbeta=fbeta
        )
    )


train, test = train_test_split(data, test_size=0.20)

print(data)

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

show_performance(slice="total", precision=precision, recall=recall, fbeta=fbeta)

save_model(model, MODEL_PATH)
pickle_object(encoder, ENCODER_PATH)
pickle_object(lb, BINARIZER_PATH)

# Analyze performance on slices
slicer = Slicer(column_names=cat_features, df=test)
slicer.fit()
slices = slicer.transform(dfs=[test])

for slice in slices:
    X_test, y_test, encoder, lb = process_data(
        slice[0],
        categorical_features=cat_features,
        label="salary",
        training=False,
        encoder=encoder,
        lb=lb,
    )

    predictions = inference(model=model, X=X_test)

    precision, recall, fbeta = compute_model_metrics(preds=predictions, y=y_test)

    show_performance(slice=slice[1] + " " + slice[2], precision=precision, recall=recall, fbeta=fbeta)
