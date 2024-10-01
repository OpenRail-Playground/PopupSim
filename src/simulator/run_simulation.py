import json

import requests

if __name__ == "__main__":

    # Define the API endpoint (assuming the FastAPI app is running locally on port 8000)
    url = "http://localhost:8000/process"

    # Define the JSON data to send in the request body
    data = {
        "configuration": {
            "popupSite": 1,
            "workshops": ["z1", "10"],
            "retrofitted": ["7"],
            "toBeRetrofitted": ["6"],
            "stationHead": ["1A"],
            "parking": ["8", "9", "17", "18", "19", "22", "23", "24"],
            "parameters": {
                "workshop": 180,
                "shuntingMovement": 8,
                "movement": 5,
                "coupling": 8,
            },
        }
    }

    # Send a POST request
    response = requests.post(url, json=data)

    # Check the response status code and print the JSON response
    if response.status_code == 200:
        print("Response from API:")
        print(json.dumps(response.json(), indent=4))  # Pretty print the JSON response
    else:
        print(f"Request failed with status code {response.status_code}")
