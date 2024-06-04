product_list = []
palindrome_list = []

for i in range(100, 1000):
    for j in range(100, 1000):
        product_list.append(i*j)
    
    
for i in product_list:
    reversed_list = list(reversed(str(i)))
    if list(str(i)) == reversed_list:
        palindrome_list.append(i)
        
print(max(palindrome_list))

# Answer = 906609