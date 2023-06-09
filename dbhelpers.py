import mariadb
import dbcreds
#this just has the imports for mariadb and dbcreds it also has the run_procedures that s has some axcepts to check for some errors
def run_procedures(sql, args):
    try:
        results = None
        conn = mariadb.connect(**dbcreds.conn_params)
        cursor = conn.cursor()
        cursor.execute(sql, args)
        results = cursor.fetchall()
    except mariadb.IntegrityError:
        print("Sorry, what you entered doesn't exist")
    except mariadb.OperationalError:
        print('there is an error in the data base')
    except mariadb.ProgrammingError:
        print('Error in the sql syntax or query execution')
    except Exception as error:
        print('Error:', error)
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()
        return results