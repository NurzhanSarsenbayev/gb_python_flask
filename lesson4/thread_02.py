import threading
import time

def worker(num):
    print(f'Starting thread work {num}')
    time.sleep(3)
    print(f'Finished thread work {num}')

threads=[]
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)

for t in threads:
    t.start()
    t.join()

print('All threads done')