import sys


class Graph:
    def __init__(self) -> None:
        self.nodes = dict()
        self.V = len(self.nodes)
        self.edges = dict()

    def add_node(self, node, **attrs):
        if not node in self.nodes:
            self.nodes[node] = attrs

    def add_edge(self, node1, node2, **attrs):
        if not node1 in self.nodes:
            self.add_node(node1)

        if not node2 in self.nodes:
            self.add_node(node2)

        if ((node1, node2) not in self.edges) and ((node2, node1) not in self.edges):
            self.edges[(node1, node2)] = attrs

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def graph(self, **attrs):
        selfgraph = sorted(self.edges.items(), key=lambda x: x[1].get("weight"))
        graph = [[0 for column in range(len(self.nodes))] for row in range(len(self.nodes))]

        for i in range(len(self.edges)):
            graph[selfgraph[i][0][0]][selfgraph[i][0][1]] = selfgraph[i][1]['weight']
            graph[selfgraph[i][0][1]][selfgraph[i][0][0]] = selfgraph[i][1]['weight']
        return graph

    def minKey(self, key, mstSet):
        min = sys.maxsize
        for v in range(len(self.nodes)):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
        return min_index

    def primMST(self, graph):
        nodes = len(self.nodes)
        key = [sys.maxsize] * nodes
        parent = [None] * nodes
        key[0] = 0
        mstSet = [False] * nodes
        parent[0] = -1

        for count in range(nodes):
            u = self.minKey(key, mstSet)
            mstSet[u] = True

            for v in range(nodes):
                if graph[u][v] > 0 and mstSet[v] == False and key[v] > graph[u][v]:
                    key[v] = graph[u][v]
                    parent[v] = u

        print("Edge \tWeight")
        for i in range(1, len(self.nodes)):
            print(parent[i], "-", i, "\t", graph[i][parent[i]])

    # Applying Kruskal algorithm
    def kruskal_algo(self):
        print ("Kruskal’s algorithm")
        result = []
        i, e = 0, 0
        selfgraph = sorted(g.edges.items(), key=lambda x: x[1].get("weight"))
        parent = []
        rank = []
        for node in range(len(self.nodes)):
            parent.append(node)
            rank.append(0)
        while e < len(self.nodes) - 1:
            u, v, w = selfgraph[i][0][0], selfgraph[i][0][1], selfgraph[i][1]['weight']
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        print("Edge \tWeight")
        for u, v, weight in result:
            print("%d - %d\t%d" % (u, v, weight))

    # Applying Prim’s algorithm
    def prim_algo(self):
        print("Prim’s algorithm")
        g.primMST(g.graph())


# Call function's
g = Graph()

# g.add_edge(0, 1, weight=4)
# g.add_edge(0, 7, weight=8)
# g.add_edge(1, 7, weight=11)
# g.add_edge(1, 2, weight=8)
# g.add_edge(7, 8, weight=7)
# g.add_edge(7, 6, weight=1)
# g.add_edge(2, 8, weight=2)
# g.add_edge(8, 6, weight=6)
# g.add_edge(6, 5, weight=2)
# g.add_edge(2, 5, weight=4)
# g.add_edge(3, 2, weight=7)
# g.add_edge(3, 5, weight=14)
# g.add_edge(4, 3, weight=9)
# g.add_edge(5, 4, weight=10)

# g.add_edge(0, 1, weight=2)
# g.add_edge(0, 3, weight=6)
# g.add_edge(1, 2, weight=3)
# g.add_edge(1, 3, weight=8)
# g.add_edge(1, 4, weight=5)
# g.add_edge(2, 4, weight=7)
# g.add_edge(3, 4, weight=9)

g.add_edge(0, 2, weight=3)
g.add_edge(2, 1, weight=4)
g.add_edge(1, 0, weight=9)

g.kruskal_algo()
g.prim_algo()
