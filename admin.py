from cgitb import handler
from tkinter import EXCEPTION
from unicodedata import name

from azure.data.tables import TableServiceClient
from azure.data.tables import TableClient
from azure.core.exceptions import ResourceExistsError

from flask import (abort,Flask, g,jsonify,render_template, redirect, url_for, request, session,url_for)
app = Flask(__name__)
app.secret_key = 'somesecretkey'

@app.route('/adminindex')
def route():
    my_filter = ""
    list_users = None
    table_service_client = TableServiceClient.from_connection_string(conn_str="DefaultEndpointsProtocol=https;AccountName=aiforgenstudentlogindb;AccountKey=CrbcSXYUQZjB/ZQWCnW9puPZjTScaZMs9dJHbaMf4GLkylUN/6uTq331dQbP1H1fjnf8qY8OUa3dzKnFppnDLA==;EndpointSuffix=core.windows.net")
    table_client = table_service_client.get_table_client(table_name="StudentDB")

    entities = table_client.query_entities(my_filter)
    
    if entities is not None:
        return render_template('adminIndex.html', entities=entities)

   #if no records found then return to same page with error    
    return render_template('adminIndex.html', error="No Records Found!")

#updating the record
@app.route('/update/<string:phoneid>')
def update(phoneid):
    print("Hello updating record..."+phoneid)
   

   
   
    return render_template('adminIndex.html', error=phoneid)

#delete the record
@app.route('/delete')
def delete():
    print("Hello deleting record...")
    return render_template('adminIndex.html')

