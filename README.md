# cloudproject
Steps to follow:
1) Install python and MySQL if you don't have it installed on your local machine. 
2) Run the below command to install the python flask's libraries
- pip install flask
3) Run the below commands to intall mysql, bcrypt libraries
- pip install PyMySQL
- pip install flask-mysql
- pip install py-bcrypt
4) In MySQL create a table tbl_Create_User using the below query or run database.py with below command
- python3 database.py
CREATE TABLE `tbl_Create_User` (
  `u_id` bigint Auto Increment Primary Key,
  `u_email` varchar(45)  Unique,
  `u_password` varchar(255) DEFAULT NULL,
  `u_fname` varchar(45)  DEFAULT NULL,
  `u_lname` varchar(45)  DEFAULT NULL,
  `acc_created` varchar(45)  DEFAULT NULL,
  `acc_updated` varchar(45) DEFAULT NULL
 ) ENGINE=InnoDB AUTO_INCREMENT=1;
5)  Run the below command to build and execute your python file
- python User.py
6) After running you'll get the webapplication link
7) Call the API using Postman
