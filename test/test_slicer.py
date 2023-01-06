import pytest
import pandas as pd
from python.ml.slicer import Slice, Slicer


@pytest.fixture
def given_df():
    df = pd.DataFrame({"cat_1": [1, 2, 4, 1], "cat_2": [1, 2, 3, 1]})
    return df


def test_slice_mask(given_df):
    given_column = "cat_1"
    given_column_value = 1
    expected_indices = [True, False, False, True]
    slice = Slice(given_df, given_column, given_column_value)
    result = slice.fit().mask
    assert result == expected_indices


def test_slice_transform(given_df):
    given_column = "cat_2"
    given_column_value = 3
    expected_df = pd.DataFrame({"cat_1": [4], "cat_2": [3]})

    slice = Slice(given_df, given_column, given_column_value)
    result = slice.fit().transform(given_df)

    pd.testing.assert_frame_equal(expected_df, result)


def test_slicer_number_of_slices(given_df):
    given_columns = ["cat_1", "cat_2"]

    expected_number_of_slicer = 6

    slicer = Slicer(given_df, given_columns)
    slicer = slicer.fit()
    result = len(slicer.slices)

    assert expected_number_of_slicer == result
