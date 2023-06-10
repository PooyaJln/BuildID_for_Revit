import requests
from dotenv import dotenv_values
config = dotenv_values(".env")  # take environment variables from .env.

username = config.get("USERNAME")
password = config.get("PASSWORD")
API_BASE_URI = config.get("API_BASE_URI")

session = requests.Session()

# Set the username and password for the session
session.auth = (username, password)


def get_buildid_data():
    """
    this function returns the items fetched from buildID
    as a List containg a dictionaries.
    """
    response = session.get(API_BASE_URI)
    # Check the response
    if response.status_code == 200:
        # Request was successful
        data = response.json()
        return data
        # items = data.get('items')
        # return items
    else:
        # Request failed
        print("Request failed with status code:", response.status_code)
