import json
from Helpers.db_connect import MysqlDB

class Mysql_CRUD():

    def __init__(self):
        conn = MysqlDB()

        elements = conn.select('select * from Elements where name="locators"')

        for row in elements:
            print(row)
            info = json.loads(row[2])

        print(info['url'])

Mysql_CRUD()
