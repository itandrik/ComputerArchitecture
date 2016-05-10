import sqlite3
import mysql.connector
import psycopg2
from BloodPressure.Globals.globals import *

# it creates special connector it different ways
create_connector = {
        "mysql":mysql.connector.connect(user='root', password='4y4yndpiK', host='127.0.0.1', database='BloodPressure'),
        "sqlite":sqlite3.connect('/home/dron/ComputerArchitecture/BloodPressure/Databases/blood_pressure_sqlite'),
        "postgreSQL":psycopg2.connect(host='127.0.0.1', user='postgres', password='4y4yndpiK', dbname='mydb')
}


# Class, which works with 3 databases : sqlite, mysql and postgreSQL
class SqlWorker:

    def __init__(self, db_type):
        self.con = create_connector[db_type]
        self.cur = self.con.cursor()

    def load(self, table_name, person_id=""):
        self.cur.execute(select_sql[table_name] + person_id)
        return self.cur.fetchall()

    def insert(self, table_name, data_array):
        strin = "INSERT INTO "+ table_name + insert_sql[table_name] +" VALUES("
        for i in data_array:
            if isinstance(i,str):
                strin += "'" + i + "', "
            else: strin += str(i) + ", "
        strin = strin[:-2]
        strin += ")"
        self.cur.execute(strin)
        self.con.commit()

    def delete(self, table_name, id):
        self.cur.execute("DELETE FROM " + table_name + " WHERE " + delete_sql[table_name] + "=" + str(id))

    def update(self, table_name, id, data_array):
        strin = "UPDATE "+ table_name + " SET "
        for i in range(0,len(update_sql[table_name])):
            strin += update_sql[table_name][i]
            if isinstance(data_array[i],str):
                strin += "'" + data_array[i] + "', "
            else: strin += str(data_array[i]) + ", "
        strin = strin[:-2]
        strin += " WHERE " + delete_sql[table_name] + "=" + str(id)
        self.cur.execute(strin)

    def close_connection(self):
        self.con.close()
