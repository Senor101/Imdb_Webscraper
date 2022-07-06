from scrape import movieDetails
from query import insert_movie,insert_company
import mysql.connector

conn = mysql.connector.connect(host='localhost',database='movie_db',user='root',password='')



insert_company(movieDetails["movieCompany"],"California, US")

movie_d = (movieDetails["movieName"],movieDetails["movieLength"],movieDetails["movieRelease"],movieDetails["movieOutline"],movieDetails["movieCompany"],movieDetails["movieGenre"])
insert_movie(movie_d)



