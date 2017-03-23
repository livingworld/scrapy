##pymysql的交互

注意在使用pymysql模块的，会出现pip install 其他库的情况，所以要特别注意版本。

在windows下与数据库交互时，不要使用`unix_socket='/tmp/mysql.sock'`,

2003, "Can't connect to MySQL server on %r (%s)" % (self.host, e))
pymysql.err.OperationalError: (2003, "Can't connect to MySQL server on '127.0.0.
1' (%d format: a number is required, not str)")
