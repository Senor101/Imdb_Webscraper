from scrape import extractfunc
from query import insert_movie,insert_company
import mysql.connector

conn = mysql.connector.connect(host='localhost',database='movie_db',user='root',password='')

movieUrls = ["https://www.imdb.com/title/tt0993846/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=ea4e08e1-c8a3-47b5-ac3a-75026647c16e&pf_rd_r=4YRAMY5HXGYB27W8CJME&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=moviemeter&ref_=chtmvm_tt_96" , "https://www.imdb.com/title/tt0111161/?ref_=nv_sr_srsg_0" , "https://www.imdb.com/title/tt0110912/?ref_=tt_sims_tt_i_2" , "https://www.imdb.com/title/tt0109830/?ref_=tt_sims_tt_t_2","https://www.imdb.com/title/tt1375666/?ref_=tt_sims_tt_t_2","https://www.imdb.com/title/tt7286456/?ref_=tt_sims_tt_t_4","https://www.imdb.com/title/tt0468569/?ref_=tt_sims_tt_t_1","https://www.imdb.com/title/tt0816692/?ref_=tt_sims_tt_t_3","https://www.imdb.com/title/tt0114369/?ref_=tt_sims_tt_t_7","https://www.imdb.com/title/tt0133093/?ref_=tt_sims_tt_t_11","https://www.imdb.com/title/tt1745960/?ref_=nv_sr_srsg_1","https://www.imdb.com/title/tt1130884/?ref_=tt_sims_tt_t_12"]


for urls in movieUrls:
    movieds = extractfunc(urls)
    print(movieds)
    insert_company(movieds[4],movieds[5])
    insert_movie(movieds)




conn.close()