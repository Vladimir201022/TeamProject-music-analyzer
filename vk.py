import requests


def get_popular_audios(access_token, count=10):
    url = 'https://api.vk.com/method/audio.getPopular'
    params = {
        'access_token': access_token,
        'v': '5.131',  
        'count': count
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()

        if 'response' in data:
            popular_audios = data['response']['items']
            return popular_audios
        else:
            print(f"Error in response: {data}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


if __name__ == '__main__':
    
    access_token = ''

    
    popular_audios = get_popular_audios(access_token)

    if popular_audios:
        for index, audio in enumerate(popular_audios, start=1):
            print(f"Track {index}:")
            print(f"Title: {audio['title']}")
            print(f"Artist: {audio['artist']}")
            print(f"Likes: {audio['likes']['count']}")
            print(f"Plays: {audio['plays']}")
            print("-------------------")
    else:
        print("No popular audios found or error occurred.")