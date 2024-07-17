import requests
import threading
import time

urls = [
    'https://t.me/pyhon3k',
    'https://www.youtube.com',
    'https://gitlab.com/dzhoker1/function-list-or-square-brackets',
    'https://docs.python.org/3/library/asyncio.html',
    'https://habr.com/ru/articles/671602/',
]

def download(url):
    response = requests.get(url)
    filename = 'sync_' + url.replace('https://', '').replace('.', '_').replace('/', '_') + '.html'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(response.text)
    print(f'Downloaded {url} in {time.time() - start_time:.2f} seconds')

threads = []
start_time = time.time()

for url in urls:
    t = threading.Thread(target=download, args=[url])
    threads.append(t)
    t.start()
for t in threads:
    t.join()