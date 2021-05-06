from collections import defaultdict
class Graph(object):
    def __init__(self, verticies):
        self.graph = defaultdict(list)
        self.V = verticies
    
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topologicalSortHelper(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortHelper(i, visited, stack)
        stack.insert(0, v)

    def topologicalSort(self):
        visited = [False] * self.V
        stack = []
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortHelper(i, visited, stack)
        
        return stack

    def detectCycle(self):
        result = self.topologicalSort()
        for i in range(self.V):
            for j in self.graph[i]:
                pointer = 0 if i not in result else result.index(i)
                pointed = 0 if j not in result else result.index(j)
                # if parent vertex, pointer, appears later then there is cycle
                if pointer > pointed:
                    return True

        return False


# Vertices = 0 1 2 3 4 5 
# 5 -> 0, 2 / 4 -> 0, 1 / 2 -> 3 / 3 -> 1
if __name__ == '__main__':
    g = Graph(6)
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)
    print(g.topologicalSort())
    print(g.detectCycle())