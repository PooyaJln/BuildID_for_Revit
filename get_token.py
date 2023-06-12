import requests
from dotenv import dotenv_values
config = dotenv_values(".env")  # take environment variables from .env.

username = config.get("USERNAME")
password = config.get("PASSWORD")
API_BASE_URI = config.get("API_BASE_URI")

session = requests.Session()

# Set the username and password for the session
session.auth = (username, password)


def get_token():
    """
    this function returns the token from buildID
    that is required for POST requests.
    """
    get_token_uri = API_BASE_URI + "gettoken"
    response = session.get(get_token_uri)
    # Check the response
    if response.status_code == 200:
        # Request was successful
        response_json = response.json()
        data = response_json.get('data')
        token = data.get('sessionToken')
        # print(token)
        return token
    else:
        # Request failed
        print("Request failed with status code:", response.status_code)
