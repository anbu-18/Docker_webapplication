from flask import Flask, request, render_template,url_for,redirect
import config
import database
import os
import json
import logging


app = Flask(__name__)

#logging creation for this application

logger = logging.getLogger(__name__)
LOGLEVEL = os.environ.get('LOGLEVEL', 'debug').upper()
logging.basicConfig(level=LOGLEVEL)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler('./Logfile.log', mode='w')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


#index page creation

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'GET':
        logger.info(" use GET method to fetch the values from Database")
        obj=database.dbconnection()
        response = obj.get_values() 
        return render_template('form.html', data=response)
       
        
    if request.method == 'POST':
        logger.info(" Use POST method to enter the values into the Database")
        fname = request.form['name']
        obj=database.dbconnection()
        response=obj.insert_values(fname)
        return redirect(url_for('index'))


if __name__ == '__main__':
    logger.info('app started to run')
    obj=database.dbconnection()
    s=obj.table_creation() #calling table creation function from database module 
    app.run()


