import random
import threading
import multiprocessing
import asyncio
import time

# Создание массива случайных чисел
arr = [random.randint(1, 100) for _ in range(1000000)]

# Многопоточность
def sum_array(arr):
    return sum(arr)

def threaded_sum(arr, num_threads):
    def worker(sub_arr, result, index):
        result[index] = sum_array(sub_arr)

    size = len(arr) // num_threads
    threads = []
    results = [0] * num_threads
    for i in range(num_threads):
        start_index = i * size
        end_index = (i + 1) * size if i != num_threads - 1 else len(arr)
        thread = threading.Thread(target=worker, args=(arr[start_index:end_index], results, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return sum(results)

# Многопроцессорность
def process_sum(arr):
    return sum(arr)

def multiprocess_sum(arr, num_processes):
    size = len(arr) // num_processes
    with multiprocessing.Pool(num_processes) as pool:
        results = pool.map(process_sum, [arr[i * size:(i + 1) * size] for i in range(num_processes)])
    return sum(results)

# Асинхронность
async def async_sum(sub_arr):
    return sum(sub_arr)

async def async_main(arr, num_chunks):
    size = len(arr) // num_chunks
    chunks = [arr[i * size:(i + 1) * size] for i in range(num_chunks)]
    tasks = [async_sum(chunk) for chunk in chunks]
    results = await asyncio.gather(*tasks)
    return sum(results)

if __name__ == '__main__':
    # Многопоточность
    start_time = time.time()
    threaded_result = threaded_sum(arr, 4)
    end_time = time.time()
    print(f"Threaded sum: {threaded_result}, Time: {end_time - start_time:.2f} seconds")

    # Многопроцессорность
    start_time = time.time()
    multiprocess_result = multiprocess_sum(arr, 4)
    end_time = time.time()
    print(f"Multiprocess sum: {multiprocess_result}, Time: {end_time - start_time:.2f} seconds")

    # Асинхронность
    start_time = time.time()
    asyncio_result = asyncio.run(async_main(arr, 4))
    end_time = time.time()
    print(f"Asyncio sum: {asyncio_result}, Time: {end_time - start_time:.2f} seconds")