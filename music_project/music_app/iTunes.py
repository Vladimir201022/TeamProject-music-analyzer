import requests

def get_top_charts(term='top', country='US', limit=10):
    url = 'https://itunes.apple.com/search'
    params = {
        'term': term,
        'country': country,
        'media': 'music',
        'entity': 'musicTrack',  # Используем 'musicTrack' для поиска треков
        'limit': limit
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()['results']
    else:
        print(f"Error fetching top charts: {response.status_code}, {response.text}")
        return []

def get_genres():
    # iTunes API не предоставляет отдельный эндпоинт для жанров,
    # поэтому мы можем использовать существующие данные для их получения.
    url = 'https://itunes.apple.com/search'
    params = {
        'term': 'genre',
        'country': 'US',
        'media': 'music',
        'limit': 200
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        results = response.json()['results']
        genres = set()
        for result in results:
            genres.add(result.get('primaryGenreName'))
        return list(genres)
    else:
        print(f"Error fetching genres: {response.status_code}, {response.text}")
        return []

def get_reviews(track_id):
    # iTunes Search API не предоставляет отзывы, но мы можем получить информацию о треках.
    url = f'https://itunes.apple.com/lookup?id={track_id}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['results']
    else:
        print(f"Error fetching reviews: {response.status_code}, {response.text}")
        return []

if __name__ == '__main__':
    top_tracks = get_top_charts(limit=10)

    print("Top 10 Tracks in iTunes:")
    for index, track in enumerate(top_tracks, start=1):
        print(f"Track {index}:")
        print(f"Track Name: {track['trackName']}")
        print(f"Artist Name: {track['artistName']}")
        print(f"Genre: {track['primaryGenreName']}")
        print(f"Track ID: {track['trackId']}")
        print("-------------------")

    genres = get_genres()
    print("Genres:")
    for genre in genres:
        print(genre)

    if top_tracks:
        track_id = top_tracks[0]['trackId']
        reviews = get_reviews(track_id)
        print("Track Info:")
        for review in reviews:
            print(f"Track Name: {review.get('trackName')}")
            print(f"Artist Name: {review.get('artistName')}")
            print(f"Album Name: {review.get('collectionName')}")
            print(f"Release Date: {review.get('releaseDate')}")
            print(f"Genre: {review.get('primaryGenreName')}")
            print(f"Track Price: {review.get('trackPrice')}")
            print("-------------------")
