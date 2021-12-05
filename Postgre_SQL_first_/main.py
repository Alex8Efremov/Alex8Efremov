import pymysql
from config import host, password, user, db_name

# =)
# connect to base: create object pymysql
try:
    connection = pymysql.connect(
        host = host,
        port = 3306,
        user = user,
        password = password,
        database = db_name,
        cursorclass = pymysql.cursors.DictCursor
    )
    print("successfully////")

    # для начала работы с mysql нужно создать объект курсор:
    try:
        """это объект который содержит различные методы для sql команд """
        # create table
        # cursor = connection.cursor()
        # with connection.cursor() as cursor:
        #     create_table_query = "CREATE TABLE `users`(id int AUTO_INCREMENT, name varchar(32)," \
        #                          "password varchar(32)," \
        #                          "email varchar(32)," \
        #                          "PRIMARY KEY (id));"
        #     cursor.execute(create_table_query)
        #     print("Table created successfully")
        # insert data
        # with connection.cursor() as cursor:
        #     insert_query = "INSERT INTO `users` (name, password, email) VALUES ('Jon', 'qwerty', 'jon@mai.com');"
        #     cursor.execute(insert_query)
        #
        #     # to save data need use method commit:
        #     connection.commit()
        # with connection.cursor() as cursor:
        #     insert_query = "INSERT INTO `users` (name, password, email) VALUES ('Ban', 'werty', 'ban@mai.com');"
        #     cursor.execute(insert_query)
        #
        #     # to save data need use method commit:
        #     connection.commit()
        # with connection.cursor() as cursor:
        #     insert_query = "INSERT INTO `users` (name, password, email) VALUES ('Ann', 'qwety', 'ann@mai.com');"
        #     cursor.execute(insert_query)
        #
        #     # to save data need use method commit:
        #     connection.commit()

        # update data
        # with connection.cursor() as cursor:
        #     # here i can use 'name' SET email = 'jon_change@mail.com'
        #     update_query = "UPDATE `users` SET password = '2234112' WHERE id = '1';"
        #     cursor.execute(update_query)
        #     # to save data in host: use method commit()
        #     connection.commit()

        #delete data
        # with connection.cursor() as cursor:
        #     delete_query = "DELETE FROM `users` WHERE id = 2;"
        #     cursor.execute(delete_query)
        #     connection.commit()
        #
        # # drop table
        # with connection.cursor() as cursor:
        #     drop_table_query = "DROP TABLE `users`;"
        #     cursor.execute(drop_table_query)
        #     # для этой окманды метод commit не нужен!!!
        #
        # # select all data from table
        # with connection.cursor() as cursor:
        #     select_all_rows = "SELECT * FROM `users`"
        #     cursor.execute(select_all_rows)
        #     # cursor.execute("SELECT * FROM `users`")
        #     # fetchall извлекает из страницы все строки
        #     rows = cursor.fetchall()
        #     for row in rows:
        #         print(row)

        # get list data bases
        with connection.cursor() as cursor:
            cursor.execute("SHOW DATABASES")
            print(cursor.fetchall())
    finally:
        connection.close()
except Exception as ex:
    print(f"Connection error: {ex}")\

