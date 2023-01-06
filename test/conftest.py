import pytest
import numpy as np
from python.ml.model import train_model

TEST_SET_SIZE = 100


@pytest.fixture
def given_X():
    return np.random.rand(TEST_SET_SIZE, 3)


@pytest.fixture
def given_y():
    return np.random.randint(0, 2, size=TEST_SET_SIZE)


@pytest.fixture
def given_predictions():
    return np.random.randint(0, 2, size=TEST_SET_SIZE)


@pytest.fixture
def given_model(given_X, given_y):
    return train_model(given_X, given_y)
