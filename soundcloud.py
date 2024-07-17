import requests


def get_top_charts(client_id):
    url = 'https://api-v2.soundcloud.com/charts'
    params = {
        'kind': 'top',
        'client_id': client_id,
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()

        charts = data['collection']

        for chart in charts:
            chart_title = chart['title']
            chart_likes_count = chart['stats']['likes_count']
            chart_playback_count = chart['stats']['playback_count']

            print(f"Chart: {chart_title}")
            print(f"Likes: {chart_likes_count}")
            print(f"Playback count: {chart_playback_count}")
            print("-------------------")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    except KeyError as e:
        print(f"KeyError: {e}. Invalid API response format.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    
    client_id = 'YOUR_CLIENT_ID'

    
    get_top_charts(client_id)