from multiprocessing import Process
import time
import requests

urls = [
    'https://t.me/pyhon3k',
    'https://www.youtube.com',
    'https://gitlab.com/dzhoker1/function-list-or-square-brackets',
    'https://docs.python.org/3/library/asyncio.html',
    'https://habr.com/ru/articles/671602/',
]


def download(url):
    r = requests.get(url)
    filename = 'multiproccess_' + url.replace('https://', '').replace('.', '_').replace('/', '_') + '.html'
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(r.text)
    print(f'Downloaded {url} in {time.time() - start_time:.2f} seconds')


processes = []
start_time = time.time()

if __name__ == '__main__':
    for url in urls:
        process = Process(target=download, args=(url,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
