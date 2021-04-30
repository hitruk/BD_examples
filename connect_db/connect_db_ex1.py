import psycopg2
import json


def open_json(CONFIG_FILE_PATH):
    """ OPEN JSON FILE """
    with open(CONFIG_FILE_PATH, 'r') as file:
        conf_file_db = json.load(file)
        return conf_file_db


def connect_db(conf_file_db):
    """ CONNECT TO THE POSTGRESQL DATABASE SERVER """

    conn =None

    try:
        conn = psycopg2.connect(**conf_file_db)
        cur = conn.cursor()
        cur.execute('select version()')
        response = cur.fetchone()
        print(response)
        cur.close()
        # conn.close() # не используем не используем, так как он в любом случае закроется в finally

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def main():
    CONFIG_FILE_PATH = '../database_config/config.json'
    config_file = open_json(CONFIG_FILE_PATH)
    connect_db(config_file)



if __name__ == '__main__':
    main()
