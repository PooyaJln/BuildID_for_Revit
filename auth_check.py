import os

FILE_NAME = ".env"


def env_file_check():
    """ this function checks whether the '.env' file exists or not
    if not it asks the user to fill in the data and it creates one"""
    if not os.path.exists(FILE_NAME):
        print("A file required for saving API login data does not exist.")
        API_BASE_URI = input('Enter API address: ')
        USERNAME = input('\nEnter the username: ')
        PASSWORD = input('\nEnter the password: ')
        with open(FILE_NAME, "w") as file:
            file.write(
                f'API_BASE_URI={API_BASE_URI}\nUSERNAME={USERNAME}\nPASSWORD={PASSWORD}')
            print("File created.")
    else:
        return True
