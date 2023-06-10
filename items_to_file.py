import os
import json
from datetime import datetime
from dotenv import dotenv_values
from fetch_items import get_buildid_data

config = dotenv_values(".env")  # take environment variables from .env.

username = config.get("USERNAME")
password = config.get("PASSWORD")
API_BASE_URI = config.get("API_BASE_URI")


# Get the current directory
current_dir = os.getcwd()
directory_name = 'data'
file_name = "response.json"
# Combine the directory path with the file name
file_path = os.path.join(current_dir, directory_name, file_name)
# Create the directory if it doesn't exist
os.makedirs(os.path.join(current_dir, directory_name), exist_ok=True)

time_now = datetime.now()

# checking if "items.json" exists
if os.path.exists(file_path):
    timestamp = os.path.getmtime(file_path)
    # Convert the timestamp to a readable format
    last_modified_time = datetime.fromtimestamp(timestamp)
    time_difference = time_now - last_modified_time
    if time_difference.total_seconds() > 900:  # if the time difference is bigger than 15 min
        with open(file_path, "w", encoding='utf-8') as file:
            # we update the file
            print("updating the data ...")
            items = get_buildid_data()
            json.dump(items, file, ensure_ascii=False)
            print("update finished.")
else:  # if the file does not exists it is created and populated.
    print("items.txt does not exist.\nfetching the data ...")
    with open(file_path, "w", encoding='utf-8') as file:
        items = get_buildid_data()
        json.dump(items, file, ensure_ascii=False)
        print("File created.")
