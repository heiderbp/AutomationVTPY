import pymysql

class MysqlDB:
    def __init__(self):
            self.hostname = 'localhost'
            self.port = 3306
            self.username = 'root'
            self.password = 'Elavon@2021'
            self.database = 'AutomationVT'
            self.condb = None
            self.cur = None

    def connectmysql(self):
        try:
            self.condb = pymysql.connect(host=self.hostname, port=self.port, user=self.username, passwd=self.password, db=self.database)
            self.cur = self.condb.cursor()
            print ("Enlace exitoso")
            return self.condb
        except Exception as e:
            print ("Error de conexión", e)


    def close(self):
        self.condb.close()

    def select(self, query):
        result = None
        self.connectmysql()

        self.cur.execute(query+"s")
        fetchData = self.cur.fetchall()
        self.close()

        return fetchData

    '''
    def read_database_version():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print("You are connected to MySQL version: ", db_version)
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)
    '''
