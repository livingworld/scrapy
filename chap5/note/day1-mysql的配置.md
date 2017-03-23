##mysql的配置

- 1.切换到mysq安装的bin目录，将默认的my-default.ini修改命名为my.ini

- 2。修改.ini文件内容，添加路径

    basedir = D:\SoftWare\MySQL\mysql-5.7.11-winx64
    datadir = D:\SoftWare\MySQL\mysql-5.7.11-winx64\Data
    port = 3306

- 3.配置环境变量

新建，MYSQL_HOME，添加上述两个路径，并在  在windows的path里，添加如下：

    ;%MYSQL_HOME\bin;（注意加分号）

- 4.初始化mysql

    mysqld.exe --initialize

- 5.执行mysqld install

- 6.执行mysqld.exe -nt --skip-grant-tables

- 7.执行mysql -u root

- 8.进入mysql操作窗口

    mysql> use mysql

    Database changed

    mysql> update user set authtication_string=Password('rootroot') where user='root'

        -> set password=Password('rootroot')

        ->

- 9.启动mysql服务：

    net start mysql

下次重新启动出现问题

键入`mysql -u root`,提示：

    ERROR 1045 (28000): Access denied for user 'ODBC'@'localhost' (using password: N
解决方法：

- 找到配置文件my.ini ，然后将其打开，可以选择用记事本打开。

- 打开后，搜索[mysqld]关键字，找到后，在mysqld下面添加skip-grant-tables，保存退出。

- 保存后重启mySQL

- 输入mysql -u root -p就可以不用密码登录了，出现password：的时候直接回车可以进入。

- 进入mysql数据库：

   mysql> use mysql;
   Database changed

- 给root用户设置新密码，蓝色部分自己输入：

    mysql> update user set password=password("123456") where user="root"

- 刷新数据库

    mysql> flush privileges

- 退出mysql：mysql> quit

下次启动

-  mysql -h localhost -u root -p 123456或mysql

注意：

为了便于启动mysql，建议在系统环境变量中添加mysql路径：

    C:\Users\lenovo\mysql-5.7.17-winx64\bin;

PS：123456为新密码，用户可根据自己需要修改成自己的密码


##密码修改补充
1、 在系统偏好设置中停止MySQL服务。


2、执行命令以安全模式启动MySQL：

cd /usr/local/mysql/bin

sudo ./mysqld_safe --skip-grant-tables

3、新打开一个命令行窗口，在MySQL中执行

update mysql.user set authentication_string=PASSWORD('你的密码') where User='root';

FLUSH PRIVILEGES;

注意，网上一般都是让执行 update mysql.user set password=PASSWORD('132456') where User='root';但是会执行失败，提示没有password这个字段

4、关闭MySQL数据库，由于无法在第2步启动的窗口关闭MySQL我就直接杀进程。



- [mysql的配置](http://www.cnblogs.com/zlslch/p/5862070.html)
