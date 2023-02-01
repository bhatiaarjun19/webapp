import base64
from distutils.log import error
import email
import errno
from http.client import BAD_REQUEST
from multiprocessing.connection import wait
from flask import abort, request,make_response
import requests
from assignment import app
from database import SqlAlchemy as mysql
from flask import jsonify
import pymysql

#from werkzeug.security import generate_password_hash
from datetime import datetime

import bcrypt
import logging
# logging.basicConfig(level=logging.DEBUG)

s =b'$2b$12$5bLd8.tAyVOYX66Y2KLNROtA86OappyUFvMtpSYsMDGnH2z1HNnUO'

@app.route("/healthz")

def myname():
    return jsonify({"Application is healthy": "200"})
