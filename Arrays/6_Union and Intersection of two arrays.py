def doUnion(a,n,b,m):
    U = a[:]
    for i in range(m):
        if b[i] not in U:
            U.append(b[i])
        else:
            pass
    return U
def doInter(a,n,b,m):
    I = []
    for i in range(m):
        for j in range(n):
            if b[i] == a[j]:
                I.append(b[j])
    return I    

A = [1,3,4,6,8]
B = [1,2,3,4,5,9,8]
n = len(A)
m = len(B)
union_ab = doUnion(A,len(A),B,len(B))
inter_ab = doInter(A,len(A),B,len(B))
print(f"Union is {union_ab} and Intersection is {inter_ab}")
