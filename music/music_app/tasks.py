from background_task import background
from iTunes import get_top_charts, get_genres
from models import Track, Genre, Artist, Chart

@background(schedule=60)
def update_tracks():
    genres = get_genres()
    for genre_name in genres:
        Genre.objects.get_or_create(name=genre_name)
    
    top_charts = get_top_charts('top')
    for rank, track_data in enumerate(top_charts, start=1):
        genre, _ = Genre.objects.get_or_create(name=track_data['primaryGenreName'])
        artist, _ = Artist.objects.get_or_create(name=track_data['artistName'])
        track, _ = Track.objects.update_or_create(
            track_id=track_data['trackId'],
            defaults={
                'name': track_data['trackName'],
                'artist': artist,
                'genre': genre,
                'release_date': track_data['releaseDate'],
                'price': track_data.get('trackPrice')
            }
        )
        Chart.objects.update_or_create(
            track=track,
            defaults={'rank': rank}
        )
