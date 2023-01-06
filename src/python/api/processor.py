import pandas
import numpy
from sklearn.preprocessing import LabelBinarizer

from .schema import PersonalAttributes


def preprocess_personal_attributes(
    personal_attributes: PersonalAttributes,
) -> pandas.DataFrame:
    personal_attributes_d = personal_attributes.dict()
    personal_attributes_d["salary"] = ">50"
    df = pandas.DataFrame(personal_attributes_d, index=[0])
    df.columns = [column.replace("_", "-") for column in df.columns]
    return df


def post_process_prediction(prediction: numpy.typing.NDArray, label_binarizer: LabelBinarizer):
    predicted_class = label_binarizer.inverse_transform(prediction[0])
    predicted_class[0]
    return {"category": predicted_class[0]}
