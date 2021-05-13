def sort012( a, arr_size): 
    low = 0
    mid = 0
    high = arr_size - 1
    while mid <= high: 
        if a[mid] == 0: 
            a[low], a[mid] = a[mid], a[low] 
            low = low + 1
            mid = mid + 1
        elif a[mid] == 1: 
            mid = mid + 1
        else: 
            a[mid], a[high] = a[high], a[mid]  
            high = high - 1
    return a 

# def sort012(arr,n):
#         # code here
#         zeros,ones,twos = 0,0,0
#         for i in arr:
#             if i == 0:
#                 zeros += 1
#             elif i == 1:
#                 ones += 1
#             else:
#                 twos += 1
                
#         for i in range(n):
#             if zeros != 0:
#                 arr[i] = 0
#                 zeros -= 1
#             elif ones != 0:
#                 arr[i] = 1
#                 ones -= 1
#             elif twos != 0:
#                 arr[i] = 2
#                 twos -= 1
#         return arr

A = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1] 
len_of_arr = len(A) 
arr = sort012(A, len_of_arr) 
print(arr)
