# def separate(a, array_size):
#     low = 0
#     high = array_size - 1
#     while low < high:
#         if a[low] < 0 and a[high] >=0:
#             low += 1
#             high -= 1
#         elif a[low] >= 0 and a[high] < 0:
#             a[low], a[high] = a[high], a[low]
#             low += 1
#             high -= 1
#         elif a[low] > 0 and a[high] > 0:
#             high -= 1
#         else:
#             low += 1
#     return a

def separate(a,n):
    j = 0
    for i in range(0,n):
        if a[i] < 0:
            a[i],a[j] = a[j],a[i]
            j += 1
    return a

A = [-10, 25, -9, 5, -17, 67, -76, 28, -43]
print(A)
separate(A, len(A))
print(A)
