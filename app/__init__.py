from flask import Flask
from flask_bootstrap import Bootstrap
import mysql.connector
from mysql.connector import errorcode

config = {
  'user': 'root',
  'password': 'root',
  'unix_socket': '/Applications/MAMP/tmp/mysql/mysql.sock',
  'database': 'mydtb',
  'raise_on_warnings': True,
}

conn = mysql.connector.connect(**config)
cur = conn.cursor()
app = Flask(__name__)

Bootstrap(app)

from app import routes