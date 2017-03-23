import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='user',
                             password='123456',
                             db='db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        mysql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(mysql, ('webmaster@python.org', 'very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        mysql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(mysql, ('webmaster@python.org',))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()