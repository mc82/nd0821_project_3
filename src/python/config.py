DATA_INPUT_PATH = "data/census_clean.csv"
MODEL_PATH = "data/model.pkl"
ENCODER_PATH = "data/encoder.pkl"
BINARIZER_PATH = "data/binarizer.pkl"
CAT_FEATURES = [
    "workclass",
    "education",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native-country",
]
MODEL_METRICS_PATH = "slice_output.txt"
PERFORMANCE_TEMPLATE = (
    "Performance on {slice}: precision: {precision}, recall: {recall}, fbeta: {fbeta}"
)
