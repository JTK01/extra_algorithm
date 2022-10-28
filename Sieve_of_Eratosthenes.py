import math

N = int(input())
array = [True for i in range(N + 1)]

for i in range(2, round(math.sqrt(N)) + 1):
    if array[i] == True:
        j = 2
        while i * j <= N:
            array[i * j] = False
            j += 1

for i in range(2, N + 1):
    if array[i]:
        print(i, end = ' ')
