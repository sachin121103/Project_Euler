def factorial(num):
    
    total = 1
    
    for i in range(1, num+1):
        total *= i
        
    return total


def add_digits(num):
    num_list = [int(d) for d in str(num)]
    
    sum = 0
    
    for j in num_list:
        sum += j
        
    return sum

num = 100
factorial_num = factorial(num)
print(add_digits(factorial_num))

# Answer = 648