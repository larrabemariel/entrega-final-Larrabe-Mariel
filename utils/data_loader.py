import json

def load_test_data(filename):
    with open(filename) as f:
        data = json.load(f)
    return data['tests']  
