import math

def prime_check(num):
    
    if num == 2:
        return True
    
    for i in range(2,int(math.sqrt(num)+1)):
        if num % i == 0:
            return False
        
    return True


sum = 0
for i in range(2, 2_000_000):
    if prime_check(i):
        sum += i
        
        
print(sum)

# Answer is 142913828922