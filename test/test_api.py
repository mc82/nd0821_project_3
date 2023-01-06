from fastapi.testclient import TestClient
import json


from python.api.app import app

client = TestClient(app)


def test_root_status_code_200():
    r = client.get("/")
    assert r.status_code == 200


def test_income_classification_lte_50k():
    post_data = json.dumps(
        {
            "age": 39,
            "fnlgt": 45781,
            "workclass": "Private",
            "education": "Bachelors",
            "education-num": 3,
            "marital-status": "Divorced",
            "occupation": "Prof-specialty",
            "relationship": "Not-in-family",
            "race": "White",
            "sex": "Female",
            "capital-gain": 20,
            "capital-loss": 30,
            "hours-per-week": 40,
            "native-country": "United-State",
        }
    )

    r = client.post("/income/", data=post_data)
    assert r.status_code == 200
    assert r.json()["category"] == "<=50K"


def test_income_classification_gt_50k():
    post_data = json.dumps(
        {
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
    )

    r = client.post("/income/", data=post_data)
    assert r.status_code == 200
    assert r.json()["category"] == ">50K"
