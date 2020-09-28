# dbcreator
для тестирования 
Забираем в одну папку оба файла
Запускаем под sudo

python3 main.py

Устанавливается mariaDB из стандартного репо.
По умолчанию это версия 10.1.44
Создаются:

база testVlg

пользователь tester c правами select , insert ,update

Три таблицы и заполняются данными.

MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| testVlg            |
+--------------------+
4 rows in set (0.00 sec)
MariaDB [(none)]> show tables from testVlg;
+-------------------+
| Tables_in_testVlg |
+-------------------+
| contacts          |
| customers         |
| orders            |
+-------------------+
3 rows in set (0.01 sec)
MariaDB [(none)]> show grants for tester@localhost;
+---------------------------------------------------------------------------------------------------------------+
| Grants for tester@localhost                                                                                   |
+---------------------------------------------------------------------------------------------------------------+
| GRANT USAGE ON *.* TO 'tester'@'localhost' IDENTIFIED BY PASSWORD '*C***************************************' |
| GRANT SELECT, INSERT ON `testVlg`.* TO 'tester'@'localhost'                                                   |
+---------------------------------------------------------------------------------------------------------------+

