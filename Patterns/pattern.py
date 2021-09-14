n = 4
original_n = n
n = 2*n
for i in range(1, n, 1):
    for j in range(1, n, 1):
        print(original_n-min(min(i, j), min(n-i, n-j)), " ", end="")
    print("\n")
