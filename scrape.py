import requests
from bs4 import BeautifulSoup
import random
import re



def extractfunc(movieUrl):
    response = requests.get(url = movieUrl)

    soup = BeautifulSoup(response.content,'html.parser')


    movie_name = soup.find(class_="sc-94726ce4-2 khmuXj").find('h1')
    movieName = movie_name.string
    # print("MOVIE: " + movie_name.string)



    plists = soup.findAll(class_="ipc-page-section ipc-page-section--base celwidget")
    movieDetail = plists[7]
    mdetail = movieDetail.find(class_="sc-f65f65be-0 ktSkVi").findAll(class_="ipc-metadata-list__item ipc-metadata-list-item--link")
    # print(mdetail[3])
    production_compani = mdetail[3].find(class_="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link")
    production_company = production_compani.string


    pc = production_company.replace(" ","_")
    newUrl = "https://en.wikipedia.org/wiki/"+pc
    try:
        pcresponse = requests.get(url = newUrl)
        soup2 = BeautifulSoup(pcresponse.content,'html.parser')
        pcadress = soup2.find(class_="infobox-data label").find('a')
        Company_address = pcadress.string
    except:
        Company_address = "California USA"



    yor = soup.find(class_="ipc-link ipc-link--baseAlt ipc-link--inherit-color sc-8c396aa2-1 WIUyh")
    year_of_release = yor.string



    director = soup.find(class_ = "ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link")
    directorName = director.string




    plot_outline = soup.find(class_="sc-16ede01-8 hXeKyz sc-910a7330-11 GYbFb").find(class_="sc-16ede01-2 gXUyNh")
    movieOutline = plot_outline.string




    movieGenre=""
    genres = soup.findAll(class_="sc-16ede01-3 bYNgQ ipc-chip ipc-chip--on-baseAlt")
    for genre in genres:
        movieGenre+=genre.string+","



    casts = soup.find(class_="ipc-sub-grid ipc-sub-grid--page-span-2 ipc-sub-grid--wraps-at-above-l ipc-shoveler__grid").findAll(class_="sc-36c36dd0-1 QSQgP")
    character = soup.find(class_="ipc-sub-grid ipc-sub-grid--page-span-2 ipc-sub-grid--wraps-at-above-l ipc-shoveler__grid").findAll(class_="sc-36c36dd0-4 hGTQna")

    moviecast=[]
    moviechar=[]
    for cast in casts:
        for c in cast:
            moviecast.append(c)

    for char in character:
        for ch in char:
            moviechar.append(ch)

    # cast : character pair
    castCharacter = []
    # print("CASTS:")
    for x,y in zip(moviecast[:3],moviechar[:3]):
        castCharacter.append(x + " : "+y)



    # scraping length of movie
    length = soup.find(class_="ipc-metadata-list ipc-metadata-list--dividers-none ipc-metadata-list--compact ipc-metadata-list--base").find(class_="ipc-metadata-list-item__content-container")
    # regex application taking the substring we need
    result = re.search('<div class="ipc-metadata-list-item__content-container">(.*)</div>',str(length))
    rest = result.group(1)
    # replacing unwanted comments 
    movielength = rest.replace('<!-- -->','')
    # print(movielength)

    movie_d = (movieName,movielength,year_of_release,movieOutline, production_company,Company_address,movieGenre)
    return movie_d


# print(response.status_code)

# movieDetails = {
#     "movieName" : movieName,
#     "movieCompany" : production_company,
#     # "companyAddress":Company_address,
#     "movieRelease" : year_of_release,
#     "movieDirector" : directorName,
#     "movieOutline" : movieOutline,
#     "movieGenre" : movieGenre,
#     "movieCharacter" : castCharacter,
#     "movieLength" : movielength
# }
