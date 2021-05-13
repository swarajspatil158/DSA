def sort_array(a):
    n = len(a)
    for i in range(1,n):
        j = i
        while j > 0 and a[j] < a[j-1]:
            swap(j,j-1,a)
            j -= 1
    return a

def swap(i,j,a):
    a[i], a[j] = a[j], a[i]            

A = [6,2,5,3,1,7]
k = 3
sort_array(A)
print(f"sorted array A in ascending order is: {A}")
print(f"Kth Minimum element is: {A[k - 1]} and Maximum element is: {A[len(A)-k]}")
