import collections

"""
Davi Baechtold Campos 
PEDA - trabalho 9
"""





# Depth First Search - DFS
# Oposto de BFS: explora mais antigo primeiro 
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

# Busca em Largura - BFS
# Explorar vértices descobertos mais antigos
def bfs(graph, root):

    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:

        vertex = queue.popleft()
        print(str(vertex) + " ", end="")

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

# SAÍDA DFS
graph = {'0': set(['1','2','3']),'1':
         set(['0', '9']),'2': 
         set(['3','6','8']),'3': 
         set(['7']),'4': 
         set(['3', '5']), '5': 
         set(['5','9']), '6':
         set(['3','4','7']), '7': 
         set(['3','8']), '8': 
         set(['4']), '9':
         set(['0','5','8'])}

print("DFS: ")
dfs(graph, '0')
print("")

# SAÍDA BFS
graph = {0: [1,2,5], 
         1: [0,9], 
         2: [3,6,8], 
         3: [7], 
         4: [3,5], 
         5: [5,9], 
         6: [3,4,7], 
         7: [3,8], 
         8: [4], 
         9: [0,5,8]}

print("BFS: ")
bfs(graph, 0)