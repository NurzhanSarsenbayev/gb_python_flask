import multiprocessing
import time

def worker(i):
    print(f'Starting process {i}')
    time.sleep(3)
    print(f'Finished process {i}')

if __name__ == '__main__':
    processes = []

    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)

    for p in processes:
        p.start()
        p.join()

    print('All processes finished')