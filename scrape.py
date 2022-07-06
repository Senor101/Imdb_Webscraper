import requests
from bs4 import BeautifulSoup
import random
import re

response = requests.get(url = "https://www.imdb.com/title/tt0111161/?ref_=nv_sr_srsg_0")

soup = BeautifulSoup(response.content,'html.parser')

movie_name = soup.find(class_="sc-94726ce4-2 khmuXj").find('h1')
print("MOVIE: " + movie_name.string)

plists = soup.findAll(class_="ipc-page-section ipc-page-section--base celwidget")
movieDetails = plists[7]
mdetail = movieDetails.find(class_="sc-f65f65be-0 ktSkVi").findAll(class_="ipc-metadata-list__item ipc-metadata-list-item--link")
# print(mdetail[3])
production_company = mdetail[3].find(class_="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link")

print(production_company.string)


year_of_release = soup.find(class_="ipc-link ipc-link--baseAlt ipc-link--inherit-color sc-8c396aa2-1 WIUyh")
print("Release: " + year_of_release.string)


director = soup.find(class_ = "ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link")
print("Director: "+ director.string)

print("Outline:")
plot_outline = soup.find(class_="sc-16ede01-0 fMPjMP")
print(plot_outline.string)




moviegenre=[]
genres = soup.findAll(class_="sc-16ede01-3 bYNgQ ipc-chip ipc-chip--on-baseAlt")
for genre in genres:
    moviegenre.append(genre.string)
print("Genre:")
print(moviegenre)


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
print("CASTS:")
for x,y in zip(moviecast[:3],moviechar[:3]):
    print(x + " : "+y)


# scraping length of movie
length = soup.find(class_="ipc-metadata-list ipc-metadata-list--dividers-none ipc-metadata-list--compact ipc-metadata-list--base").find(class_="ipc-metadata-list-item__content-container")
# regex application taking the substring we need
result = re.search('<div class="ipc-metadata-list-item__content-container">(.*)</div>',str(length))
rest = result.group(1)
# replacing unwanted comments 
movielength = rest.replace('<!-- -->','')
print(movielength)


# print(response.status_code)


