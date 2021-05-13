import sys
sys.stdin = open("input.txt", "r")


n = int(input()) # Number of nodes

edges = int(input()) # Number of edges
adjlist = [[] for x in range(n)]

# Building Graph
for i in range(edges):
    source,des = map(int,input().split())
    temp1 = adjlist[source]
    temp1.append(des)
    temp2=adjlist[des]
    temp2.append(source)

# Printing Graph
for i in range(n):
    print(i," : ",adjlist[i])

