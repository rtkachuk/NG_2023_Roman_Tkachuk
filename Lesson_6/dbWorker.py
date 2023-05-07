import sqlite3

def init_conn(path):
    conn = None
    try:
        conn = sqlite3.connect(path)
        print ("Database connection OK!")
    except Exception as e:
        print (e)
        print ("Connection to database failed!")
    return conn

def init_tables(path):
    connection = init_conn(path)
    sql = "CREATE TABLE IF NOT EXISTS users(id integer PRIMARY KEY, login text NOT NULL, password text NOT NULL);"
    connection.execute(sql)
    connection.close()

def registerUser(path, login, password):
    logins = getLogins(path)
    if login in logins:
        return;
    connection = init_conn(path)
    sql = "INSERT INTO users (`login`, `password`) VALUES('{}', '{}')".format(login, password)
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()
    connection.close()

def getLogins(path):
    connection = init_conn(path)
    sql = "SELECT login from users;"
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = map (lambda x: x[0], cursor.fetchall())
    return rows

def generateLoginsHTMLTalbe(rows):
    usersTable = "<table border='1'>"
    for login in rows:
        usersTable += "<tr><td>" + str(login) + "</td></tr>"
    usersTable += "</table>"
    return usersTable