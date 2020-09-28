import random as rd
import pymysql as db
import subprocess as sp

def getver():
	retCode=sp.run(['mysql','-V'],stdout=sp.PIPE)
	if retCode.returncode==0:
		return retCode.stdout.split()[4][:4]
def connRoot():
	return db.connect(user='root',password='',unix_socket="/var/run/mysqld/mysqld.sock")
def createDB(dbName):
	conn=connRoot()
	try:
		with  conn.cursor() as cursor:
			cursor.execute('create database '+dbName)
	finally:
		conn.close()
def createUser(userName,passwd,dbname):
# creating user 
	conn=connRoot()
	sql='grant select ,insert, update  on '+dbname +'.* to '+userName
	sql+='@localhost identified by \''+passwd+'\''
	try:
                with  conn.cursor() as cursor:
                        cursor.execute(sql)
	finally:
		conn.close()

def createTables(dbName): 
	conn=connRoot()
	try:
		with  conn.cursor() as cursor:
			cursor.execute("use "+dbName)
		sqlStr="CREATE TABLE customers (   id INT NOT NULL,\
			  name VARCHAR(45) NULL,\
			  PRIMARY KEY (id))"
		with conn.cursor() as cursor:
                        cursor.execute(sqlStr)
		sqlStr="CREATE TABLE orders ( \
		  id INT NOT NULL,\
		  orders VARCHAR(45) NULL,\
		  Custid INT NOT NULL,\
		  PRIMARY KEY (id),\
		  INDEX custom_idx (Custid ASC),\
		  CONSTRAINT custom \
		  FOREIGN KEY (Custid) \
		  REFERENCES customers (id) \
		  ON DELETE  CASCADE \
		  ON UPDATE NO ACTION)"
		with conn.cursor() as cursor:
                        cursor.execute(sqlStr)

		sqlStr= "CREATE TABLE contacts ( \
		id INT NOT NULL, \
		name VARCHAR(45) NULL,  \
		custid INT NULL,\
		PRIMARY KEY (id),\
		INDEX fk_cust_cont_idx (custid ASC),\
		CONSTRAINT fk_cust_cont\
		FOREIGN KEY (custid)\
		REFERENCES customers (id)\
		ON DELETE NO ACTION \
		ON UPDATE NO ACTION)"
		with conn.cursor() as cursor:
                	cursor.execute(sqlStr)
	finally:
		conn.close()

def insData(conn):
	try:
		sql="INSERT INTO customers (id, name) VALUES (%s,%s)"
		with conn.cursor() as cursor:
			for i in range(5):
				cursor.execute(sql, (i, "a" *i ) )
		conn.commit()
		sql="INSERT INTO orders (id,orders, Custid) VALUES (%s,%s,%s)"
		with conn.cursor() as cursor:
                        for i in range(10):
                                cursor.execute(sql,(i,"b"*i,rd.randrange(0,5)))
		conn.commit()
		sql="INSERT INTO contacts(id,name,custid) VALUES (%s,%s,%s)"
		with conn.cursor() as cursor:
                	for i in range(10):
                        	cursor.execute(sql,(i,"c"*i,rd.randrange(0,5)))
		conn.commit()
	finally:
		conn.close()

def userConn(userName,pwd,dbName):
	retCode=db.connect(host='localhost',
		user=userName,
		password=pwd,
		db=dbName)
	return retCode

def zadanie():
	createDB("testVlg")
	createUser("tester","qwerty123","testVlg")
	createTables("testVlg")
	connect=userConn("tester","qwerty123","testVlg")
	insData(connect)

if __name__ =="__main__":
	print("This is the test")


























