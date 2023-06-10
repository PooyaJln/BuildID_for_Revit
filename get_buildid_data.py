import json
import os
# from fetch_items import get_buildid_data
# items = get_buildid_data()

# Get the current directory
current_dir = os.getcwd()
directory_name = 'data'
file_name = "response.json"
# Combine the directory path with the file name
file_path = os.path.join(current_dir, directory_name, file_name)

with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

items = data.get('items')


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
        if key in ['registrationStatus', 'constructionStatus', 'site']:
            item_status[key] = value

    print(item_status)
    return item_status


get_item_status('E280689400005005879328DD')
