def reverse_array(A,start,end):
	if start>= end:
		return
	A[start],A[end]=A[end],A[start]  # swapping elements if end is smaller than start
	reverse_array(A,start+1,end-1)  # recursive call of function

A = [1,2,3,4,5,6,7]
print(A)
reverse_array(A,0,len(A)-1)
print(A)
