import requests
from dotenv import dotenv_values
config = dotenv_values(".env")  # take environment variables from .env.

username = config.get("USERNAME_itemlistexport")
password = config.get("PASSWORD_itemlistexport")
API_BASE_URI = config.get("API_BASE_URI")

session = requests.Session()

# Set the username and password for the session
session.auth = (username, password)


def get_itemlistexport():
    """
    this function returns the items fetched from buildID
    as a List containg a dictionaries.
    """
    item_list_export = API_BASE_URI + "itemlistexport"
    response = session.get(item_list_export)
    # Check the response
    if response.status_code == 200:
        # Request was successful
        data = response.json()
        # print(data)
        return data
    else:
        # Request failed
        print("Request failed with status code:", response.status_code)


def get_by_item_type_id(item_type_id):
    """
    this function returns the items fetched from buildID
    as a List containg a dictionaries.
    """
    item_list_export = f'{API_BASE_URI}itemlistexport/{str(item_type_id)}'
    print(item_list_export)
    response = session.get(item_list_export)
    # Check the response
    if response.status_code == 200:
        # Request was successful
        data = response.json()
        # print(data)
        return data
    else:
        # Request failed
        print("Request failed with status code:", response.status_code)
