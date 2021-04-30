
import psycopg2
from configparser import ConfigParser


def config(filename='../database_config/database.ini', section='postgresql'):
    # create_tables a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db

def conn_db(db):
    """ CONNECT TO THE POSTGRESQL DATABASE SERVER """

    conn = None
    try:
        conn = psycopg2.connect(**db)
        cur = conn.cursor()
        cur.execute('select version()')
        response_bd = cur.fetchone()
        print(response_bd)
        cur.close()
        # conn.close() # не используем не используем, так как он в любом случае закроется в finally

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed')

def main():

    conf = config()
    conn_db(conf)

if __name__ =='__main__':
    main()