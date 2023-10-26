import requests
import json
from app import *

data = {
    "fullname": "George",
    "characteristics": {
        "sex": "male",
        "age": 27
    },
    "skills": ["smart", "strong"],
    "experience": [
        {
            "position": "developer",
            "workplace": "netflix",
            "salary": "7000"
        },
        {
            "position": "engineer",
            "workplace": "facebook",
            "id_card": 56117,
            "Country": "Scotland"
        }
    ]
}

response = requests.post('http://127.0.0.1:5000/json_to_xml', json=data)
print(response.text)
