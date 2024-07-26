import requests
from bs4 import BeautifulSoup
from collections import Counter

# Функция для парсинга жанров
def get_genres(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    genres = soup.select("li")
    popular_genres = [genre.text.strip() for genre in genres if genre.text.strip()]
    return popular_genres

# Примеры URL для парсинга данных
url_genres_1 = "https://audiocaptain.com/music-genres/"
url_genres_2 = "https://primesound.org/most-popular-music-genres/"

# Получение данных о жанрах с разных сайтов
genres_1 = get_genres(url_genres_1)
genres_2 = get_genres(url_genres_2)

# Объединение данных о жанрах
all_genres = genres_1 + genres_2

# Подсчет частоты упоминаний жанров
genre_counts = Counter(all_genres)

# Получение топ-10 популярных жанров
top_10_genres = genre_counts.most_common(10)

# Вывод топ-10 популярных жанров
print("Топ-10 популярных музыкальных жанров:")
for genre, count in top_10_genres:
    print(f"{genre}: {count} упоминаний")
