from collections import Counter

def triangle_num(num):
    
    triangle = ((num)*(num+1))/2
    return int(triangle)


for i in range(1, 100000):
    num = triangle_num(i)
    i = 2
    prime_factors = []

    while num != 1:
        if num % i == 0:
            num /=i
            prime_factors.append(i)
        else:
            i += 1
        
    primes = Counter(prime_factors)
    primes_dict = dict(primes)
    total_v = 1
    
    for k, v in primes_dict.items():
        new_v = v+1
        
        print(f"{k}: {new_v}")
        total_v *= new_v
    
    
    if total_v >= 500:
        print(f"Total V: {total_v}"'\n')
        print(4*9*125*7*11*13*17)
        break
    
# Answer: 76576500
        
    

        