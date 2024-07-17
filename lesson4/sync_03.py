import random
import time

def long_running_task():
    for i in range(5):
        print(f"Implementing task {i}")
        time.sleep(random.randint(1, 3))

def main():
    print('Start app')
    long_running_task()
    print('End app')

main()