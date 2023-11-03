# Author: Render Tutorial (original)
#         Jarryd Allison (extension)
# Date: 11/3/2023
# Description: Render web hosting tutorial

from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# Test DB connection route
@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgres://flask_hello_world_2hpt_user:jHkwTTydwcluFuMOH5IakIl7gcoRriWd@dpg-cl2nca0310os73dkcku0-a/flask_hello_world_2hpt")
    conn.close()
    return "Database Connection Successful"

# Create a basketball DB
@app.route('/db_create')
def create():
    conn = psycopg2.connect("postgres://flask_hello_world_2hpt_user:jHkwTTydwcluFuMOH5IakIl7gcoRriWd@dpg-cl2nca0310os73dkcku0-a/flask_hello_world_2hpt")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
            First VARCHAR(255),
            Last VARCHAR(255),
            City VARCHAR(255),
            Name VARCHAR(255),
            Number INT
            );
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"