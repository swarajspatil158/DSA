t= [[1],[0,2,3],[1,4],[1,4],[2,3]]
p = [[2,3],[4],[0],[0],[1]]
vis = list()
def dfs(comp,i):
    vis.append(i)
    print(i)
    for j in comp[i]:
        if j not in vis:
            dfs(comp,j)


def dfsOfGraph(Graph):
    for i in range(len(Graph)-1):
        if i not in vis:
            dfs(p,i)

dfsOfGraph(p)


