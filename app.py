from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgres://flask_hello_world_2hpt_user:jHkwTTydwcluFuMOH5IakIl7gcoRriWd@dpg-cl2nca0310os73dkcku0-a/flask_hello_world_2hpt")
    conn.close()
    return "Database Connection Successful"