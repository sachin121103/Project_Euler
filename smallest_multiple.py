i = 2520
is_divisible = True

while is_divisible:
    divisible_list = []
    i += 10
    
    for j in range(1,21):
        if i % j == 0:
            divisible_list.append(j)
            
    if len(divisible_list) == 20:
        is_divisible = False
        print(i)
        
# Answer = 232792560