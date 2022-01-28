from flask import jsonify,request
import json
import mysql.connector
import config
from mainfile import logger

#creating a class
class dbconnection():
    #database configuration setting
    def __init__(self):      
        try:
            logger.info("successfully connected to the database")
            self.conn = mysql.connector.connect(
            host=config.host,
            user=config.user,
            password=config.password,
            database=config.database
            )
            self.cursor = self.conn.cursor()

        except Exception as e:
            logger.debug(" Check the variables used in config file, incase you are unable to connect database")
            logger.error("Error while connecting database : {}".format(e))
            print(" Error while connecting database",e)
            return "Error while connecting database"
    
# create a table in database using function
    def table_creation(self):
        try:
            self.cursor.execute('CREATE TABLE IF NOT EXISTS lof(Name TEXT)')
            logger.info("table successfully created in the databsae!")
        except Exception as e:
            logger.exception(" Error while creating table : {}".format(e))
            print("Error while creating table: ",e)
            return "Error while creating table"
        
# insert a values into the database       
    def  insert_values(self,data):
        try:
            logger.debug(" check the data passed and method used in the forms")
            self.cursor.execute("INSERT INTO lof VALUES ('"+data+"')")
            self.conn.commit()
            logger.info("values inserted successfully")
            return "inserted successfully"
        except Exception as e:
            logger.exception(" Error while enter the values in the DB : {}".format(e))
            print("Error while enter the values into the DB: ",e)
            return "Error while enter the values into the DB"
        finally:
            self.cursor.close()
            self.conn.close()

#fetching the values from the database
    def get_values(self):
        try:
            self.cursor.execute("SELECT * from lof")
            value = self.cursor.fetchall()
            logger.info("fetching data from the database")
            return value
        except Exception as e:
            logger.error("Error while fetching data from DB : {}".format(e))
            print ("Error while fetching data: ",e)
            return "Error while fetching data"
        finally:
            self.cursor.close()
            self.conn.close()
