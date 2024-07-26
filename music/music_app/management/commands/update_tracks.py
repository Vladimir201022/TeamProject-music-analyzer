from django.core.management.base import BaseCommand
from music_app.models import Track, Genre, Artist, Chart
from music_app.iTunes import get_top_charts, get_genres
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Updates track data from iTunes'

    def handle(self, *args, **kwargs):
        try:
            # Обновление жанров
            genres = get_genres()
            for genre_name in genres:
                Genre.objects.get_or_create(name=genre_name)

            # Обновление треков и чартов
            top_charts = get_top_charts('top')
            for rank, track_data in enumerate(top_charts, start=1):
                genre, _ = Genre.objects.get_or_create(name=track_data['primaryGenreName'])
                artist, _ = Artist.objects.get_or_create(name=track_data['artistName'])

                # Преобразование даты releaseDate в нужный формат
                release_date_str = track_data.get('releaseDate')
                try:
                    release_date = datetime.strptime(release_date_str, "%Y-%m-%dT%H:%M:%SZ").date()
                except ValueError:
                    logger.error(f"Error parsing release date '{release_date_str}': Incorrect date format")
                    release_date = None  # или обработка ошибки по вашему усмотрению

                # Создание или обновление трека
                track, created = Track.objects.update_or_create(
                    track_id=track_data['trackId'],
                    defaults={
                        'name': track_data['trackName'],
                        'artist': artist,
                        'genre': genre,
                        'release_date': release_date,
                        'price': track_data.get('trackPrice')
                    }
                )

                # Создание или обновление чарта
                Chart.objects.update_or_create(
                    track=track,
                    defaults={'rank': rank,
                              'track_name': track_data['trackName']}
                    
                )

            self.stdout.write(self.style.SUCCESS('Successfully updated track data'))

        except Exception as e:
            logger.error(f"Error updating track data: {e}")
            self.stdout.write(self.style.ERROR(f"Error updating track data: {e}"))
