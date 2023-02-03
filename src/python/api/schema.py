from pydantic import BaseModel, Field


class PersonalAttributes(BaseModel):
    age: int
    fnlgt: int
    workclass: str
    education: str
    education_num: int = Field(alias="education-num")
    marital_status: str = Field(alias="marital-status")
    occupation: str
    relationship: str
    race: str
    sex: str
    capital_gain: int = Field(alias="capital-gain")
    capital_loss: int = Field(alias="capital-loss")
    hours_per_week: int = Field(alias="hours-per-week")
    native_country: str = Field(alias="native-country")
    
    class Config:
        schema_extra = {
            "example": {
                "age": 59,
                "fnlgt": 236596,
                "workclass": "State-gov",
                "education": "HS-grad",
                "education-num": 9,
                "marital-status": "Married-civ-spouse",
                "occupation": "Exec-managerial",
                "relationship": "Husband",
                "race": "White",
                "sex": "Male",
                "capital-gain": 7688,
                "capital-loss": 0,
                "hours-per-week": 45,
                "native-country": "United-States",
            }
        }


class SalaryCategory(BaseModel):
    category: str
