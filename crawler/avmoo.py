from urllib import request
from bs4 import BeautifulSoup
data = request.Request("https://avmo.club/cn")
data.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36')
data.add_header('Referer','https://avmo.club/cn')
data.add_header('Upgrade-Insecure-Requests',1)
with request.urlopen(data) as f:
    data=f.read().decode('utf-8')
    soup = BeautifulSoup(data, 'html.parser')
    for movie in soup.find_all('div', class_="photo-info"):
        for text in movie.stripped_strings:
            if text != '/':
                print(text)
        print(movie.parent.parent.a['href'])
        print()