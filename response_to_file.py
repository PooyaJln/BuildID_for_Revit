# -*- coding: utf-8 -*-

import os
import json
import codecs
from datetime import datetime
from api_calls import get_itemlistexport
from buildid_data_from_file import get_all_items_from_file
import requests
__fullframeengine__ = True

def response_file_check(grandpar_dir,API_BASE_URI,username, password):
    """
    This function checks whether ./data/response.json exists or not.
    if it exists it checks how old it is and if it is older than 900 sec
    it will update it.
    """
    print('running response_file_check')
    data_directory_name = 'data'
    file_name = "response.json"
    if not os.path.exists(os.path.join(grandpar_dir, data_directory_name)):
        # Create the directory if it doesn't exist
        os.makedirs(os.path.join(grandpar_dir, data_directory_name))

    # create path with the file name
    file_path = os.path.join(grandpar_dir, data_directory_name, file_name)

    time_now = datetime.now()
    # checking if "items.json" exists
    if os.path.exists(file_path):
        timestamp = os.path.getmtime(file_path)
        # Convert the timestamp to a readable format
        last_modified_time = datetime.fromtimestamp(timestamp)
        time_difference = time_now - last_modified_time
        if time_difference.total_seconds() > 60:  # if the time difference is smaller than 15 min
            items = get_itemlistexport(API_BASE_URI,username, password)
            with codecs.open(file_path, "w",encoding='utf-8') as file:
                # we update the file
                print("fetching new data ...")
                
                json.dump(items, file, ensure_ascii=False)
                # print("update finished.")
            return items
        else:
            print('file with recent data, getting the data from the file')
            return get_all_items_from_file(grandpar_dir)
        
    else:  # if the file does not exists it is created and populated.
        print("file does not exist. creating the file ...")
        items = get_itemlistexport(API_BASE_URI,username, password)
        with codecs.open(file_path, "w",encoding='utf-8') as file:
            json.dump(items, file, ensure_ascii=False)
            print("File created.")
        return items
