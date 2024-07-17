import os
import threading
from multiprocessing import Process
import asyncio
from urllib.parse import urlparse

import aiohttp
import requests
import time

urls = [
    'https://example.com/image1.jpg',
    'https://example.com/image2.png',
    'https://example.com/image3.gif',
    'https://example.com/image4.bmp',
    'https://example.com/image5.svg',
]
start_time = time.time()
def get_filename_from_url(url, suffix=''):
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    return f'{suffix}_{filename}'

def download_image(url, suffix='unknown'):
    response = requests.get(url)
    filename = get_filename_from_url(url, suffix)
    with open(filename, 'wb') as f:
        f.write(response.content)
    print(f'Downloaded {url} as {filename} in {time.time() - start_time:.2f} seconds')


def thread_function(suffix='unknown', *urls):
    threads = []
    for url in urls:
        t = threading.Thread(target=download_image, args=(url,suffix,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
        print(f'Finished {suffix} threads in {time.time() - start_time:.2f} seconds')
def multiprocess_function(suffix = 'unknown',*urls):
    processes = []
    for url in urls:
        p = Process(target=download_image, args=(url,suffix,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
        print(f'Finished {suffix} processes in {time.time() - start_time:.2f} seconds')
async def async_download_image(url, suffix='unknown'):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            content = await response.read()
            filename = get_filename_from_url(url, suffix)
            with open(filename, 'wb') as f:
                f.write(content)
            print(f'Downloaded {url} as {filename} in {time.time() - start_time:.2f} seconds')


async def async_function(suffix='unknown', *urls):
    start_time = time.time()
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(async_download_image(url, suffix))
        tasks.append(task)
    await asyncio.gather(*tasks)
    print(f'Finished {suffix} async downloads in {time.time() - start_time:.2f} seconds')


def main():
    global start_time
    thread_function('thread', *urls)
    multiprocess_function('process', *urls)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_function('async', *urls))
if __name__ == '__main__':
    main()