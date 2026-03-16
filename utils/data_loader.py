import json


def load_test_data(path="config/test_data.json"):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)