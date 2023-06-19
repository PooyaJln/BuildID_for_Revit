# -*- coding: utf-8 -*-
import requests
__fullframeengine__ = True
from pyrevit import forms

# from dotenv import dotenv_values
# config = dotenv_values(".env")  # take environment variables from .env.
# API_BASE_URI = config.get("API_BASE_URI")
# project_id = config.get("projectId")

def get_token(API_BASE_URI,username, password):
    """
    this function returns the token from buildID
    that is required for POST requests.
    """
    session = requests.Session()

    # Set the username and password for the session
    session.auth = (username, password)
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
        # print("Request failed with status code:", response.status_code)
        forms.alert("fetching token was unsuccessfel",exitscript=False)

def extract_EPC_in_error_message(error):
    """
    this function is run when the response contains errorMessage list
    and extracts the EPC numbers that were not updated. 
    """
    start_index = error[0].find(":") + 1
    end_index = error[0].find("No") - 1
    result = error[0][start_index:end_index].strip()
    result_list = result.split(",")
    striped_result_list = [item.strip() for item in result_list]
    return striped_result_list

def get_itemlistexport(API_BASE_URI,username, password):
    """
    this function returns the items fetched from buildID
    as a List containg a dictionaries.
    """
    session = requests.Session()

    # Set the username and password for the session
    session.auth = (username, password)
    item_list_export_url = API_BASE_URI + "itemlistexport"
    response = session.get(item_list_export_url)
    # Check the response
    if response.status_code == 200:
        # Request was successful
        data = response.json()
        print('get_itemlistexport, request successful')
        return data
    else:
        # Request failed
        print("get_itemlistexport, Request failed with status code:", response.status_code)
        return {}


def get_by_item_type_id(API_BASE_URI,username, password, item_type_id):
    """
    this function returns the items fetched from buildID
    as a List containg a dictionaries by a specific typeId
    """
    session = requests.Session()

    # Set the username and password for the session
    session.auth = (username, password)
    item_list_export_url = '{}itemlistexport/{}'.format(API_BASE_URI,str(item_type_id))
    # print(item_list_export_url)
    response = session.get(item_list_export_url)
    # Check the response
    if response.status_code == 200:
        # Request was successful
        data = response.json()
        # print(data)
        return data
    else:
        # Request failed
        # print("Request failed with status code:", response.status_code)
        return {}

def get_item_by_EPC_no(API_BASE_URI,username, password, EPC_no):
    """
    this function returns the items fetched from buildID
    as a List containg a dictionaries b7 a specific EPC number
    """
    session = requests.Session()

    # Set the username and password for the session
    session.auth = (username, password)
    item_list_export_uri = API_BASE_URI + "itemlistexport"
    response = session.get(item_list_export_uri)
    item_list = []
    # Check the response
    if response.status_code == 200:
        # Request was successful
        
        data = response.json()
        for item in data.get("items"):
            if item.get('epc') == EPC_no:
                item_list.append(item)
            else:
                continue
        return item_list
    else:
        # Request failed
        print("Request failed with status code:", response.status_code)
        return item_list
        

def booking_request(list_of_epc,API_BASE_URI,USERNAME,PASSWORD,project_id):
    """
    This function accepts a list of epc numbers and send a post
    request to change their status to 'bokad'.
    """
    print('booking {}'.format(list_of_epc))
    # Set the bearer token
    bearer_token = get_token(API_BASE_URI,USERNAME,PASSWORD)
    print('token: ', bearer_token)

    # Set the API endpoint URL
    post_uri = '{}changestatusonitems/{}'.format(API_BASE_URI,project_id)

    # Set the request headers with the bearer token
    headers = {
        "Authorization": "Bearer {}".format(bearer_token),
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
    if response.status_code == 200 and len(response.json().get('errorMessages')) == 0:
        # Request was successful
        for item in list_of_epc:
            print('{} is successfully booked'.format(item))
    elif response.status_code == 200 and len(response.json().get('errorMessages')) == 1:
        # Request failed
        response_json = response.json()
        error_message_list = response_json.get('errorMessages')
        unsuccessful_epc_list = extract_EPC_in_error_message(
            error_message_list)
        for item in unsuccessful_epc_list:
            print("{} was not updated".format(item))
    elif response.status_code == 400:
        print("Request failed with status code:", response.status_code)

def make_item_availabe(list_of_epc,API_BASE_URI,USERNAME,PASSWORD,project_id):
    """
    This function accepts a list of epc numbers and send a post
    request to change their status to 'bokad'.
    """
    print('making {} available'.format(list_of_epc))
    # Set the bearer token
    bearer_token = get_token(API_BASE_URI,USERNAME,PASSWORD)
    print('token: ', bearer_token)

    # Set the API endpoint URL
    post_uri = '{}changestatusonitems/{}'.format(API_BASE_URI,project_id)

    # Set the request headers with the bearer token
    headers = {
        "Authorization": "Bearer {}".format(bearer_token),
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
    if response.status_code == 200 and len(response.json().get('errorMessages')) == 0:
        # Request was successful
        for item in list_of_epc:
            print('{} is successfully released'.format(item))
    elif response.status_code == 200 and len(response.json().get('errorMessages')) == 1:
        # Request failed
        response_json = response.json()
        error_message_list = response_json.get('errorMessages')
        unsuccessful_epc_list = extract_EPC_in_error_message(
            error_message_list)
        for item in unsuccessful_epc_list:
            print("{} was not released".format(item))
    elif response.status_code == 400:
        print("Request failed with status code:", response.status_code)

