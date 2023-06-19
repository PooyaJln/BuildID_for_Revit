import json
import os
import requests
import codecs
__fullframeengine__ = True

directory_name = 'data'
file_name = "response.json"
# Combine the directory path with the file name
# file_path = os.path.join(current_dir, directory_name, file_name)

def get_all_items_from_file(grandpar_dir):
    print('running get_all_items_from_file')
    file_path = os.path.join(grandpar_dir, directory_name, file_name)
    with codecs.open(file_path, 'r',encoding='utf-8') as file:
        data = json.load(file)

    # items = data.get('items')
    return data


# def get_item_type_names():
#     """
#     this function returns a list of itemTypes from buildID.
#     """
#     itemTypeNames = []
#     for item in items:
#         if item.get('itemTypeName') in itemTypeNames:
#             continue
#         else:
#             itemTypeNames.append(item.get('itemTypeName'))

#     print(itemTypeNames)
#     return itemTypeNames


def get_item_by_epc_number(grandpar_dir, epc_number):
    """
    this function returns an item from buildID using an EPC number.
    """
    file_path = os.path.join(grandpar_dir, directory_name, file_name)
    with codecs.open(file_path, 'r',encoding='utf-8') as file:
        data = json.load(file)

    items = data.get('items')
    for item in items:
        if item.get('epc') == epc_number:
            print(item)
            return item
        else:
            continue


# def get_item_status_by_epc_number(epc_number):
#     """
#     this function returns an item's different statuses 
#     from buildID using an EPC number.
#     """
#     item = get_item_by_epc_number(epc_number)
#     item_statuses = {}
#     for key, value in item.items():
#         if key in ['registrationStatus', 'constructionStatus', 'site']:
#             item_statuses[key] = value

#     print(item_statuses)
#     return item_statuses


