import requests
from dotenv import dotenv_values
config = dotenv_values(".env")  # take environment variables from .env.

username = config.get("USERNAME")
password = config.get("PASSWORD")
API_BASE_URI = config.get("API_BASE_URI")

session = requests.Session()

# Set the username and password for the session
session.auth=(username,password)

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
        items = data.get('items')
        return items
    else:
        # Request failed
        print("Request failed with status code:", response.status_code)


items= get_buildid_data()

def get_item_type_names():
    """
    this function returns a list of itemTypes from buildID.
    """
    # items= get_buildid_data()

    itemTypeNames = []
    for item in items:
        if item.get('itemTypeName') in itemTypeNames:
            continue
        else:
            itemTypeNames.append(item.get('itemTypeName'))

    print(itemTypeNames)
    return itemTypeNames


def get_item(epc_number):
    """
    this function returns an item from buildID using an EPC number.
    """
    # items= get_buildid_data()
    for item in items:
        if item.get('epc') == epc_number:
            # print(item)
            return item
        else:
            continue


def get_item_status(epc_number):
    """
    this function returns an item's different statuses 
    from buildID using an EPC number.
    """    
    # items= get_buildid_data()
    item = get_item(epc_number)
    item_status = {}
    for key, value in item.items():
        if key in ['registrationStatus','constructionStatus','site']:
            item_status[key] = value
    
    print(item_status)
    return item_status

get_item_status('E280689400005005879328DD')
