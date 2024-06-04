def prime_check(num):
    
    if num == 2:
        return True
    
    for i in range(2, int((num/2)+2)):
        if num % i == 0:
            return False
        
    return True

prime_list = []
i = 2

while True:

    if prime_check(i):
        prime_list.append(i)
        
    i += 1
        
    if len(prime_list) == 10001:
        break
            
print(prime_list[-1])

# Answer = 104743