from urllib import request
from bs4 import BeautifulSoup
data = request.urlopen("file:///C:/Users/saber/Desktop/avmp.html")
data=data.read().decode('utf-8')
soup = BeautifulSoup(data, 'html.parser')
for movie in soup.find_all('div', class_="photo-info"):
    for text in movie.stripped_strings:
        if text != '/':
            print(text)
    print(movie.parent.parent.a['href'])
    print()