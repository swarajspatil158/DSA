def reverse_array(A,start,end):
	if start>= end:
		return
	A[start],A[end]=A[end],A[start]  # swapping elements if end is smaller than start
	reverse_array(A,start+1,end-1)  # recursive call of function

A = [10,11,12,13,14,15,16,17]
print(A)
reverse_array(A,0,len(A)-1)
print(A)
