#! python3

import os
import json
from pyrevit import forms
import codecs
from rpw.ui.forms import FlexForm, Label, TextBox, TextBox, Separator, Button

FILE_NAME = ".env"
test_file_name = "config.json"

def get_user_input_form():
    components = [ Label("Some data is required for saving BuildID database and"),
               Label("login data does not exist"),
               Separator(),
               Label('API_BASE_URI:'),
               TextBox('API_BASE_URI', Text="https://biddemo1.azurewebsites.net/"),
               Label('username:'),
               TextBox('USERNAME', Text=""),
               Label('password:'),
               TextBox('PASSWORD', Text=""),
               Label('username for itemlistexport URL:'),
               TextBox('USERNAME_itemlistexport', Text=""),
               Label('password for itemlistexport URL:'),
               TextBox('PASSWORD_itemlistexport', Text=""),
               Label('Project ID:'),
               TextBox('projectId', Text="1"),

               Button('Ok'),
            ]
    form = FlexForm('Missing BuildId login data', components)
    if form.show():
        return form.values
    
def get_missing_config_values(missing_list):
    components = []
    for item in missing_list:
        components.append(Label(item))
        components.append(TextBox(item, text=""))
    components.append(Button('Ok'))
    form = FlexForm('Missing BuildId login data', components)
    if form.show():
        return form.values

  
# def create_env_file(file_path,input_dictionary): 
#     for key, value in input_dictionary:
#         with open(file_path, "w") as file:
#             file.write('{}={}\n'.format(key,value))
                    
def save_config_file(file_path,input_dictionary): 
    with open(file_path, "w") as file:
        file.write(str(input_dictionary).replace("\'","\""))

def fetch_config_file_data(file_path): 
    with codecs.open(file_path,'r', encoding='utf-8') as file:
             data = json.load(file)
    config = dict(data)
    return config


def config_file_check(directory_name):
    """ this function checks whether 'config.json' file exists or not.
    if not it asks the user to fill in the data and it creates one"""
    file_path = os.path.join(directory_name,test_file_name)
    if not os.path.exists(file_path):
        config = get_user_input_form()
        save_config_file(file_path,config)
        return config
        
    if os.path.exists(file_path):
        with open(file_path) as file:
             data = json.load(file)
        config = dict(data)
        # print(config)
        empty_config_keys = []
        
        for key,value in config.items():
            if not value or value == "":
                empty_config_keys.append(key)
        if len(empty_config_keys) != 0:
            empty_config_keys_string = ", ".join(empty_config_keys)
            forms.alert("missing "+empty_config_keys_string + "\nFill in the next window")
            filled_in_value = get_missing_config_values(empty_config_keys)
            for item in empty_config_keys:
                 config.update({item:filled_in_value.get(item)})
            save_config_file(file_path,config)
            return fetch_config_file_data(file_path)
        else:
            return fetch_config_file_data(file_path)


