import json



def get_profiles():
    with open("data.json", "r") as f:
        return json.load(f)

def set_profiles(data):
    with open("data.json", "w") as f:
        json.dump(data, f)

