import requests
from dotenv import dotenv_values
from get_token import get_token

config = dotenv_values(".env")  # take environment variables from .env.

API_BASE_URI = config.get("API_BASE_URI")
project_id = config.get("projectId")


def booking_request(list_of_epc):
    """
    This function is accepts a list of epc numbers and send a post
    request to change their status to 'bokad'.
    """

    # Set the bearer token
    bearer_token = get_token()

    # Set the API endpoint URL
    post_uri = f'{API_BASE_URI}changestatusonitems/{project_id}'

    # Set the request headers with the bearer token
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json"
    }

    # Set the request payload
    payload = {
        "epcs": list_of_epc,
        "status": "Booked"
    }

    # Send the POST request
    response = requests.post(post_uri, headers=headers,
                             json=payload, timeout=600)

    # Check the response status code
    if response.status_code == 200:
        # Request was successful
        print(response.json())
    else:
        # Request failed
        print(f"Request failed with status code {response.status_code}")


# booking_request(["E2004214C63060150A9B356F", "E2004215862060150A9B416E"])


def make_availabe_request(list_of_epc):
    """
    This function is accepts a list of epc numbers and send a post
    request to change their status to 'tillgänglig'.
    """
    # Set the bearer token
    bearer_token = get_token()

    # Set the API endpoint URL
    post_uri = f'{API_BASE_URI}changestatusonitems/{project_id}'

    # Set the request headers with the bearer token
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json"
    }

    # Set the request payload
    payload = {
        "epcs": list_of_epc,
        "status": "Available"
    }

    # Send the POST request
    response = requests.post(post_uri, headers=headers,
                             json=payload, timeout=600)

    # Check the response status code
    if response.status_code == 200:
        # Request was successful
        print(response.json())
    else:
        # Request failed
        print(f"Request failed with status code {response.status_code}")


# make_availabe_request(["E2004214C63060150A9B356F", "E2004215862060150A9B416E"])
