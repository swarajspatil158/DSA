import sys
sys.stdin = open("input.txt", "r")

def print2DArray(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            print(matrix[i][j],end=" ")
        print("")
    return 1

n = int(input())
e = int(input())
matrix = [[0 for x in range(n)] for x in range(n)]
print("initialised matrix:")
print2DArray(matrix)
for i in range(e):
    source,des = map(int,input().split())
    matrix[source][des] = 1
    matrix[des][source] = 1
print("implemented matrix:")
print2DArray(matrix)
#Printing Children of given Node
nodeNum = int(input())
print("children for {} node are:".format(nodeNum))
for i in range(n):
    if matrix[i][nodeNum] == 1:
        print(i,end=" ")
print("\n")

