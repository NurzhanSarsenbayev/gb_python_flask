import time

import requests

urls = [
    'https://www.google.com/',
    'https://www.youtube.com/',
    'https://www.facebook.com/',
    'https://www.instagram.com/',
]

start_time = time.time()

for url in urls:
    response = requests.get(url)
    filename = 'sync_' + url.replace('https://', '').replace('.', '_').replace('/', '_') + '.html'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(response.text)
    print(f'Downloaded {url} in {time.time() - start_time:.2f} seconds')