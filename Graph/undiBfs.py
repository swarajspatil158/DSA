graph = {
   1: [2],
   2: [1,3,7],
   3: [2,5],
   4: [6],
   5: [3,7],
   6: [4],
   7: [2,5]
}
n = 8
visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue
track = [0 for _ in range(n)] # List to keep track of all visited nodes(includes components).
def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)
  track[node] = 1
  while queue:
    s = queue.pop(0)
    print (s, end = " ") 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        track[neighbour] = 1
        queue.append(neighbour)

# Driver Code
for i in graph:
    if track[i] == 0:
        bfs(visited, graph, i)