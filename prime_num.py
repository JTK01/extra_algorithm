import math

def prime_num(n):
    for i in range(2,round(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
        return True

print("4 :",prime_num(4))
print("7 :",prime_num(7))
