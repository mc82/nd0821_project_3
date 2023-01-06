import pandas as pd
import pickle


def load_data(path):
    return pd.read_csv(path, header=0)


def pickle_object(object, path):
    with open(path, "wb") as f:
        pickle.dump(object, f)


def unpickle_object(path):
    with open(path, "rb") as f:
        object = pickle.load(f)
    return object
