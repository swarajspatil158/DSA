def insertionSort(array,k):
    # array.sort()
    # return array
    for i in range(1,len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            swap(j, j - 1, array)
            j -= 1
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]



arr = [55,66,43,11,55,35,-1,83]
k = 2
print(insertionSort(arr,k))
print("'kth' min ele is <"+ str(arr[k-1]) + "> and max ele is <" + str(arr[len(arr)-k])+ ">")













