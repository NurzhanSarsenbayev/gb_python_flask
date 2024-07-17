import time

def slow_function():
    print('Start function')
    time.sleep(5)
    print('End function')

print('Start app')
slow_function()
print('End app')