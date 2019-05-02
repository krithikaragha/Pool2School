from flask import Flask, render_template, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin123'
app.config['MYSQL_DB'] = 'pool2school'

mysql = MySQL(app)

@app.route("/")
def index():
    return render_template("index.html")


