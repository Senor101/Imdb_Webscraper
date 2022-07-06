import mysql.connector

conn = mysql.connector.connect(host='localhost',database='movie_db',user='root',password='')


addCompany = "INSERT INTO production_company " \
        "VALUES(%s,%s)"
addMovies = "INSERT INTO movie " \
            "VALUES(%s,%s,%s,%s,%s)"
addGenre = "INSERT INTO moviegenre " \
        "VALUES(%s,%s)"


# def insert_company(name,address):
#     args = (name,address)
#     cursor = conn.cursor()
#     cursor.execute(addCompany,args)
#     conn.commit()
#     cursor.close()
#     conn.close()


def insert_movie(data):
    g = data[5]
    args = data[0:5] 
    cursor = conn.cursor()
    cursor.execute(addMovies,args)
    # cursor.commit()
    cursor.execute(addGenre,(data[0],g))
    conn.commit()
    cursor.close()
    conn.close()



# insert_company("20 Century","California")
data = ("Django Unchained","2h 45m","2012","When Django, a slave, is freed, he joins forces with a bounty hunter to rescue his wife, who has been enslaved by Calvin, a hard-hearted plantation owner.","Columbia Pictures","Action,Comedy")
# print(data[0:5])
# print(data[5])
insert_movie(data)

# displayTable = {
#     "showMovie": "select * from production_company",
#     "showCompany": "select * from movie"
# }