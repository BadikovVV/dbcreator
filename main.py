import subprocess as sp
import dbwork as db
def upd():
	retCode=sp.run(["apt","update"])
	return 0 if retCode.returncode==0 else 1
def isInst(pakName):
# return 1 if package is installed and 0 if not
	retCode=sp.run(["dpkg-query","-l",pakName],stdout=sp.DEVNULL)
	return 1 if retCode.returncode==0 else 0

def installPack(packName):
# install package with packName
	retCode=sp.run(["apt-get","install","-y",packName])
	if retCode.returncode !=0 :
		print("Sorry, can not install package with name "+packName)
	return 0 if retCode.returncode==0 else 1

def installPyMod (modName):
#installing python  module
	retCode=sp.run(["pip3","show",modName],stdout=sp.DEVNULL)
	if retCode.returncode!=0 :
		retCode=sp.run(["pip3","install",modName]) #,stdout=sp.DEVNULL)
	return 0 if retCode.returncode ==0 else 1

if __name__=='__main__':
# updating package cache
	if upd():
		print('Something gone wrong!!!!')
		exit(1)
# installing  pip3 for python
	if not isInst('python3-pip') :
		installPack('python3-pip')
#installing mariadb server
	if not isInst('mariadb-server'):
		if installPack('mariadb-server')==0 :
			print('****Server installed successfully****')
			sp.run(['systemctl','enable','mariadb'])
		else:
			print ("Someting gone wrong!!!")
			exit(1)
#	sp.run(['systemctl','enable','mariadb'])
#installing client parts
	if not isInst('mariadb-client'):
		if installPack('mariadb-client')==0:
			print  ('**** Client installed successfully****')
		else:
			print('Something gone wrong!!!!')
			exit(1)
	if not isInst('mariadb-common'):
                if installPack('mariadb-common')==0:
                        print  ('**** Client installed successfully****')
                else:
                        print('Something gone wrong!!!!')
                        exit(1)
        
	if db.getver()==b'10.1':
		if not isInst('libmysqlclient20'):
			if  installPack('libmysqlclient20')>0:
				print('Something gone wrong!!!!')
				exit(1)
		if not isInst('libmysqlclient-dev'):
                        if  installPack('libmysqlclient-dev')>0:
                                print('Something gone wrong!!!!')
                                exit(1)

	else:
		if not isInst('libmariadb3'):
			if installPack('libmariadb3')>0:
				print('Something gone wrong!!!!')
				exit(1)
#installing python connector to mariaDB
	installPyMod('pymysql')
	installPyMod('mysql-connector-python')
	db.zadanie()
