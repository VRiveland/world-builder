from flask import Flask
from flask_bootstrap import Bootstrap
import mysql.connector

config = {
  'user': 'root',
  'password': 'root',
  'unix_socket': '/Applications/MAMP/tmp/mysql/mysql.sock',
  'database': 'mydtb',
  'raise_on_warnings': True,
}

mydtb = mysql.connector.connect(**config)
cur = mydtb.cursor(prepared=True)

app = Flask(__name__)

Bootstrap(app)

from app import routes