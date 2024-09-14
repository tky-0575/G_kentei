import mysql.connector
from mysql.connector import Error

#DBに入力内容を登録する関数
def regist(form):
    resp = False
    term = form.getvalue("term")
    detail = form.getvalue("detail")
    connection = None
    try:
        connection = mysql.connector.connect(
            host = "HanamiTakuya.local",
            user = "root",
            password = "TKY873sql%",
            database = 'test'
        )
        cursor = connection.cursor()

        sql = ('''
            INSERT INTO g_kentei (term, description)
            VALUES (%s, %s);
        ''')

        cursor.execute(sql, [term, detail])

        connection.commit()

        cursor.close()

        resp = True

    except Error as e:
        resp = e

    finally:
        if connection is not None:
            connection.close()
    return resp

#入力文字を検索して、表示する関数
def browse(form):
    term = form.getvalue("browse")
    connection = None
    try:
        connection = mysql.connector.connect(
            host = "HanamiTakuya.local",
            user = "root",
            password = "TKY873sql%",
            database = 'test'
        )
        cursor = connection.cursor()

        sql = ('''
            select * from g_kentei
            where term like %s
            or description like %s;
        ''')

        cursor.execute(sql, ('%'+term+'%', '%'+term+'%'))
        resp = cursor.fetchall()

        connection.commit()

        cursor.close()

    except Error as e:
        resp = e

    finally:
        if connection is not None:
            connection.close()
    return resp