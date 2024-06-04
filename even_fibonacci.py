fibonacci_list = [1, 2]

num1 = 1
num2 = 2

while num1 < 4_000_000:
    num1 = num1 + num2
    if num1 > 4_000_000:
        break
    fibonacci_list.append(num1)

    num2 = num2 + num1
    if num2 > 4_000_000:
        break
    fibonacci_list.append(num2)
    
sum = 0
        
for i in fibonacci_list:
    if i % 2 ==0:
        sum += i
        
print(sum)

# Answer = 4613732