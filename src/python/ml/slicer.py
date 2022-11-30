from __future__ import annotations
from typing import List
import pandas


class Slice(object):
    
    def __init__(self, df: pandas.DataFrame, column_name: str, column_value) -> None:
        self._df = df
        self._column_name = column_name
        self._column_value = column_value
        self._mask: List

    @property
    def column_name(self):
        return self._column_name
    
    @property
    def column_value(self):
        return self._column_value

    @property
    def mask(self) -> List[int]:
        return self._mask

    def fit(self) -> Slice:
        df = self._df[self._column_name] == self._column_value
        self._mask = list(df.values)
        return self

    def transform(self, df: pandas.DataFrame) -> pandas.DataFrame:
        df = df[self.mask]
        df = df.reset_index(drop=True)
        return df

    def fit_transform(self, df: pandas.DataFrame) -> pandas.DataFrame:
        return self.fit().transform(df)


class Slicer(object):

    _supported_types = (pandas.DataFrame,)

    def __init__(self, df: pandas.DataFrame, column_names: List[str]):
        self._df = df
        self._column_names = column_names
        self._slices: List[Slice]

        if not Slicer._is_type_supported(self._df):
            raise NotImplementedError("Unsupported type: {}".format(type(self._df)))

    @property
    def slices(self):
        return self._slices

    def fit(self) -> Slicer:
        self._slices = []
        for column_name in self._column_names:
            for unique_value in self._get_unique_values_of_column(column_name):
                slice = Slice(
                    df=self._df, column_name=column_name, column_value=unique_value
                )
                self._slices.append(slice.fit())
        return self

    def transform(self, dfs: List[pandas.DataFrame]) -> List[(pandas.DateOffset, str, str)]:
        sliced_dfs = []
        for df in dfs:
            for slice in self.slices:
                sliced_dfs.append((slice.transform(df), slice.column_name, slice.column_value))
        return sliced_dfs

    def _get_unique_values_of_column(self, column_name: str):
        return self._df[column_name].unique()

    @staticmethod
    def _is_type_supported(input):
        return isinstance(input, Slicer._supported_types)
