import requests
import re

url = "https://www.last.fm/music/+charts/artists"

response = requests.get(url)

if response.status_code == 200:
    html_content = response.text
    
    artist_pattern = re.compile(r'<a href="/music/[^"]+" class="link-block-target">([^<]+)</a>')
    
    
    artists = artist_pattern.findall(html_content)
    
    
    print("Популярные артисты:")
    for index, artist in enumerate(artists, start=1):
        print(f"{index}. {artist}")
