import requests
from bs4 import BeautifulSoup


def get_top_charts_with_stats():
    url = 'https://music.yandex.ru/chart'

    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        charts = []

        chart_blocks = soup.find_all('div', class_='d-track__title')

        for block in chart_blocks:
            chart_title = block.find('div', class_='d-track__name').text.strip()

            
            likes = block.find('span', class_='d-icon_type_like')
            likes_count = likes.text.strip() if likes else 'Недоступно'

            plays = block.find('span', class_='d-icon_type_play')
            plays_count = plays.text.strip() if plays else 'Недоступно'

            chart_info = {
                'title': chart_title,
                'likes_count': likes_count,
                'plays_count': plays_count
            }

            charts.append(chart_info)

        return charts

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None


if __name__ == '__main__':
    
    top_charts = get_top_charts_with_stats()

    if top_charts:
        for index, chart in enumerate(top_charts, start=1):
            print(f"Chart {index}:")
            print(f"Title: {chart['title']}")
            print(f"Likes: {chart['likes_count']}")
            print(f"Plays: {chart['plays_count']}")
            print("-------------------")
    
