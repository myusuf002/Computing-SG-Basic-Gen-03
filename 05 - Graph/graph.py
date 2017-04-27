#Graph tidak berarah dan tidak berbobot
class Graph(object):
    def __init__(self, graph_dict=None):
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def getVertices(self):
        #mengembalikan semua vertex pada graf
        return list(self.__graph_dict.keys())

    def getEdges(self):
        #mengembalikan semua sisi pada graf
        return self.__generate_edges()

    def add_vertex(self, vertex):
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        #menghasilkan semua sisi pada graf
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges

    def __str__(self):
        res = "vertices : "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges : "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res

    def __getitem__(self,vertex):
      return self.__graph_dict[vertex]

    def dfs(self, start):
        visited = []
        stack = [start]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.append(vertex)
                for neighbour in self[vertex]:
                    stack.append(neighbour)
        return visited

    def bfs(self, start):
        visited = []
        queue = [start]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.append(vertex)
                for neighbour in self[vertex]:
                    queue.append(neighbour)
        return visited

G = { 1 : set([2,3]),
      2 : set([1,4,5]),
      3 : set([1,6,7]),
      4 : set([2,8]),
      5 : set([2,8]),
      6 : set([3,8]),
      7 : set([3,8]),
      8 : set([4,5,6,7]) }
"""
G = Graph()
for i in range(1,9):
    G.add_vertex(i)
print(G.getVertices())

G.add_edge({1,2})
G.add_edge({1,3})
G.add_edge({2,4})
G.add_edge({2,5})
G.add_edge({3,6})
G.add_edge({3,7})
G.add_edge({4,8})
G.add_edge({5,8})
G.add_edge({6,8})
G.add_edge({7,8})
"""
graph = Graph(G)
print(graph)
print("DFS :", graph.dfs(1))
print("BFS :", graph.bfs(1))

