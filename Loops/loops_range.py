import random

start, stop = 1, 100
step = 1
while start < stop:
    print(start, end=" ")
    step *= 2
    start += step #Output: 1 3 7 15 31 63 

for _ in range(5):
    print(random.choice(range(1, 100)))  #Output: Random 5 value between 1 and 100


def custom_range(start, stop, step):
    while start < stop:
        yield start
        start += step

for value in custom_range(1, 10, 3): 
    print(value) #Output: 1, 4, 7