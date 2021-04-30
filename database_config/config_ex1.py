

import json

def config(CONFIG_FILE_PATH = '../database_config/config.json'):
    """ OPEN JSON FILE """
    with open(CONFIG_FILE_PATH, 'r') as file:
        conf_file_db = json.load(file)
        return conf_file_db

# if __name__ == '__main__':
#
#     CONFIG_FILE_PATH = '../database_config/config.json'
#
#     config(CONFIG_FILE_PATH)