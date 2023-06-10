import os

file_name = ".env"


def env_file_check():
    if not os.path.exists(file_name):
        print("A file required for saving API login data does not exist.")
        API_BASE_URI = input('Enter API address: ')
        USERNAME = input('\nEnter the username: ')
        PASSWORD = input('\nEnter the password: ')
        with open(file_name, "w") as file:
            # file.write('API_BASE_URI=\"https://buildid-vasakronan.azurewebsites.net/itemlistexport\"\nUSERNAME=huginbiuser\nPASSWORD=V55qyyJ3LgQKTkqNKgbZ')
            file.write(
                f'API_BASE_URI={API_BASE_URI}\nUSERNAME={USERNAME}\nPASSWORD={PASSWORD}')
            print("File created.")
    else:
        return True
