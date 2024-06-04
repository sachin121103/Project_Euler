for i in range(1, 1000):
    for j in range(i, 1000):
        for k in range(j, 1000):
            if (i*i) + (j*j) == (k*k):
                if (i+j+k == 1000):
                    print(f"{i}^2 + {j}^2 = {k}^2")
                    print(i*j*k)
                    
# Answer = 31875000