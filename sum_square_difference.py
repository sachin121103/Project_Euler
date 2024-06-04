def square_sum(num):
    squared = 0
    for i in range(1, num+1):
        squared += i
        
    return (squared * squared)

def sum_square(num):
    squared = 0
    for j in range(1, num+1):
        squared += (j*j)
        
    return squared


print(square_sum(100)-sum_square(100))

# Answer = 25164150