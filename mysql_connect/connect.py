import mysql.connector

__cnx = None

def get_sql_connection():
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(
            # enter mysql server username
            user='root', 
            # enter mysql server password
            password='thai2003', 
            host='127.0.0.1', 
            database='food_market')
    return __cnx

