import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
webpage = response.text
soup = BeautifulSoup(webpage, 'html.parser')
movie_titles = [movie.text for movie in soup.find_all(name='h3', class_='title')]
movie_titles.reverse()

with open('movies.txt', 'w') as movie_file:
    for movie in movie_titles:
        movie_file.write(f'{movie}\n')
movie_file.close()