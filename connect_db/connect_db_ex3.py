
from database_config.config_ex1 import config
import psycopg2

def conn_db():
    """ CONNECT TO THE POSTGRESQL DATABASE SERVER """

    conn = None

    try:
        params = config()

        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('select version()')
        response_server = cur.fetchone()
        print(response_server)
        cur.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('connection closed')
conn_db()

