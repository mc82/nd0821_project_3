from fastapi.testclient import TestClient
import json


from python.api.app import app

client = TestClient(app)


def test_root_status_code_200():
    r = client.get("/")
    assert r.status_code == 200


def test_income_classification():
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
    print(r.json())
    assert r.status_code == 200
    