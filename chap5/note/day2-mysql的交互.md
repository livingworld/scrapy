##mysql的交互

- 创建数据库及切换数据库操作：

    mysql> CREATE DATABASE scraping;
    mysql> USE scraping;

- 创建库表

    mysql> CREATE TABLE pages (id BIGINT(7) NOT NULL AUTO_INCREMENT, title VARCHAR(200),content VARCHAR(10000),created TIMESTAMP DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY(id));

- 查看库表结构

    mysql> DESCRIBE pages;
    +---------+----------------+------+-----+-------------------+----------------+
    | Field   | Type           | Null | Key | Default           | Extra          |
    +---------+----------------+------+-----+-------------------+----------------+
    | id      | bigint(7)      | NO   | PRI | NULL              | auto_increment |
    | title   | varchar(200)   | YES  |     | NULL              |                |
    | content | varchar(10000) | YES  |     | NULL              |                |
    | created | timestamp      | NO   |     | CURRENT_TIMESTAMP |                |
    +---------+----------------+------+-----+-------------------+----------------+
    4 rows in set (0.02 sec)

- 插入测试数据

    > INSERT INTO pages (title, content) VALUES ("Test page title", "This is some test page content. It can be up to 10,000 characters long.");

- 查询库表数据

    >SELECT * FROM pages WHERE id = 2;
    >SELECT * FROM pages WHERE title LIKE "%test%";
    >SELECT id, title FROM pages WHERE content LIKE "%page content%";

- 删除库表数据

与查询类似，注意别忘了在语句中放WHERE，否则会将数据全部删除。

    >DELETE FROM pages WHERE id = 1;

- 更新数据

相当于替换数据

    >UPDATE pages SET title="A new title", content="Some new content" WHERE id=2;

- 查询数据库

    mysql> SHOW DATABASES;

- 初始设置时的密码设定

    [root@host]# mysqladmin -u root password "new_password";

    [root@host]# mysql -u root -p   #登入

- 重置密码

    mysql> set password for root@localhost = password('123456');#千万记住加分号
    Query OK, 0 rows affected, 1 warning (0.04 sec)

INSERT INTO root(host, user, password,select_priv, insert_priv, update_priv)
    VALUES ('localhost', 'guest',PASSWORD('guest123'), 'Y', 'Y', 'Y');

-

If you decide you do not want to execute a query that you are in the process of entering, cancel it by typing \c:

    mysql> SELECT
        -> USER()
        -> \c
    mysql>

- [MySQL——修改root密码的4种方法(以windows为例)](http://www.jb51.net/article/39454.htm)

##推荐书籍

- [MySQL Cookbook](http://shop.oreilly.com/product/0636920032274.do)。
