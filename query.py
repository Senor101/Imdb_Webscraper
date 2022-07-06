import mysql.connector
from mysql.connector import Error

conn = mysql.connector.connect(host='localhost',database='movie_db',user='root',password='')


addCompany = "INSERT INTO production_company " \
        "VALUES(%s,%s)"
addMovies = "INSERT INTO movie " \
            "VALUES(%s,%s,%s,%s,%s)"
addGenre = "INSERT INTO moviegenre " \
        "VALUES(%s,%s)"


def insert_company(name,address):
    args = (name,address)
    try:
        cursor = conn.cursor()
        cursor.execute(addCompany,args)
        conn.commit()
    except Error as error:
        print(error)
    # finally:
    #     cursor.close()
    #     conn.close()



def insert_movie(data):
    g = data[5]
    args = data[0:5] 
    try:
        cursor = conn.cursor()
        cursor.execute(addMovies,args)
        # cursor.commit()
        cursor.execute(addGenre,(data[0],g))
        conn.commit()
    except Error as error:
        print(error)
    finally:
        cursor.close()
        conn.close()


