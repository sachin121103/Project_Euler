def prime_check(num):
    
    for i in range(2, int((num/2)+2)):
        if num % i == 0:
            return False
        
    return True

number = 600851475143

for j in range(3, int((number/2)+2)):
    if number % j == 0:
        if prime_check(j):
            print(j)
        
# Answer = 6857
