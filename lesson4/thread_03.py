import threading

counter = 0

def increment():
    global counter
    for _ in range(1_000_000):
        counter += 1
    print(f'Counter: {counter}')

threads = []
for i in range(5):
    t = threading.Thread(target=increment)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f'Final counter: {counter}')