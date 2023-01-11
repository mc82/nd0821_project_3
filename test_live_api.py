import requests


url = "https://income-prediction.herokuapp.com/income"

post_data = {
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

x = requests.post(url, json=post_data)

print(x.text)
