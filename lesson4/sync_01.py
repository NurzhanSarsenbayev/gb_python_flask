import time

def count_down(n):
    for i in range(n):
        print(i)
        time.sleep(1)

count_down(5)