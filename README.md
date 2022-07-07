# Imdb WebScraper

### Introduction
Web scraping is a method for obtaining large amount of datas from websites, such data are unstructured and difficult to work with hence we extract them change them to 
different file formats, modify them according to our needs. Here we have used data from the websites to populate our database.
The programming language we are using is python because (it's easier 😁) it can handle most processes easily. For library we use BeautifulSoup which is highly popular
for web scraping. BeautifulSoup handles pulling out data from html or xml.

### Installing libraries
We will install required library using pip (package installer for python).We are using beautifulSoup,requests for webscraping and mysql connector for inserting our datas in our database.
```py
pip install bs4
pip install mysql-connector-python
pip install requests
```
*You now can run the dbconnect.py and the code will execute*

### Playing with bs4
*Our webscraper is the scrape.py script which will scrape the necessary datas from the official imdb site.*
```py
response = requests.get(url = movieUrl)
soup = BeautifulSoup(response.content,'html.parser')
```
- We first specify the url from which we are going to scrape the data.
- We then use beautiful soup to initialize a soup of the above url page using the html.parser as well.Now we can use this soup to extract any information we need from that page specified above.

Let's try to get the name of the movie.

![image](https://user-images.githubusercontent.com/65499807/177748302-16e995a9-5bd2-4125-9217-e8951067f92e.png)

Here as we can see the name enclosed within html tags and their attributes. We will now use the class attribute to find the data we are looking for using `find(class_="class_name")`
also we can find tags as `find('a')`

Let's see it in code
```py
movie_name = soup.find(class_="sc-94726ce4-2 khmuXj").find('h1')
movieName = movie_name.string
print(movieName) # prints out the movie name
```

Easy Right!!

Similarly you can play around extracting and scraping datas you need for your next project.

