import mariadb
import dbcreds

def run_procedures(sql, args):
    try:
        results = None
        conn = mariadb.connect(**dbcreds.conn_params)
        cursor = conn.cursor()
        cursor.execute(sql, args)
        results = cursor.fetchall()
    except mariadb.IntegrityError:
        print("Sorry, what you entered doesn't exist")
    except Exception as error:
        print('Error:', error)
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()
        return results