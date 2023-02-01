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

@app.route('/createuser', methods=['POST'])
def create_user():

	#dbcon =None
	csr =None

	try:

		js = request.json
		username =js['username']
		password =js['password']
		fname =js['fname']
		lname=js['lname']

		# datetime object containing current date and time
		now = datetime.now()

		# dd/mm/YY H:M:S
		u_crdate = now.strftime("%d/%m/%Y %H:%M:%S")


		# validate the received values
		if fname and lname and username and password and request.method == 'POST':
			# bcrypt password
			bytes = password.encode('utf-8')
			# salt = bcrypt.gensalt()
			hash_pwd = bcrypt.hashpw(bytes, s)

			# insert data into db
			query = "INSERT INTO tbl_create_user(username, u_password, u_fname, u_lname,acc_created,acc_updated) VALUES(%s,%s,%s,%s,%s,%s)"
			field = (username,hash_pwd,fname,lname,u_crdate,u_crdate)

			# # connect with mysql
			# #dbcon = mysql.connect()
			csr = mysql.cursor()

			# # execute the query
			csr.execute(query, field)

			mysql.commit()

			# rows = csr.fetchone()
			csr.close()	

			csr = mysql.cursor()

			query = "SELECT u_id,username,u_fname,u_lname,acc_created,acc_updated from tbl_create_user where username= %s"
			field = (username,)
			csr.execute(query, field)
			keys = [column[0] for column in csr.description]
			data=csr.fetchone()
			result = dict(zip(keys, data))
			result = jsonify(result)

			# result = jsonify('User added successfully!',201)
			result.status_code = 201

			return result
		else:
			#dbcon = mysql.connect()
			csr = mysql.cursor()
			return not_found()
	# except mysql.connector.Error:
	# 	print("error duplicacy")
	except Exception as e:
		# print(e)
		db_error=True		
		# dbcon = mysql.connect()
		# csr = dbcon.cursor()

	finally:
		#dbcon = mysql.connect()
		csr = mysql.cursor()
		csr.close() 
		#dbcon.close()

	if db_error:
		# print("duplicate error")
		result=jsonify(Error="BAD_REQUEST", Code = 400  )	
		result.status=400

		# return jsonify((400, 'Record Not Found')) 
		# result.status_code="400 BAD_REQUEST"
		return result

@app.route("/healthz")

def myname():
    return jsonify({"Application is healthy": "200"})
