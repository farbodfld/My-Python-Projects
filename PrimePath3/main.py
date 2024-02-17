import sys
import codecs as cs


class Graph:
    # def __init__(self):

    def readGraphFromFile(self, src):
        """Read a graph structure from given file."""
        with cs.open(src, 'r', 'utf-8') as graphFile:
            # Read nodes set of graph
            graphFile.readline()
            nodes = [int(n) for n in graphFile.readline().split()]
            # Read initial nodes set of graph
            graphFile.readline()
            initNodes = [int(n) for n in graphFile.readline().split()]
            # Read end nodes set of graph
            graphFile.readline()
            endNodes = [int(n) for n in graphFile.readline().split()]
            # Read edges set of graph
            graphFile.readline()
            edges = {}
            for i in nodes:
                s = graphFile.readline().strip().split()
                if len(s) >= 1:
                    edges[i] = [int(n) for n in s if n != '-1']
                else:
                    edges[i] = []
            graph = {'nodes': nodes, 'init': initNodes,
                     'end': endNodes, 'edges': edges}
            return graph

    def printGraph(self, graph):
        print("Nodes:     ", graph['nodes'])
        print("InitNodes: ", graph['init'])
        print("EndNodes:  ", graph['end'])
        print("Edges:")
        for n in graph['nodes']:
            print("%d to " % n, graph['edges'][n])

    def isPrimePath(self, path, graph):
        # Whether the path can be extended at head, and the extended path is still a simple path or not!
        reachHead = True
        next_nodes = filter(lambda n: path[0] in graph['edges'][n], graph['nodes'])
        for n in next_nodes:
            if n == path[-1] or n not in path:
                reachHead = False

        # Whether the path can be extended at tail, and the extended path is still a simple path or not!
        reachEnd = True
        last_nodes = graph['edges'][path[-1]]
        for n in last_nodes:
            if n == path[0] or n not in path:
                reachEnd = False

        # check the path for being a prime path.
        if len(path) >= 2 and path[0] == path[-1]:
            return True
        elif reachHead and reachEnd:
            return True
        else:
            return False

    def isExtendable(self, path, graph):

        reachEnd = True
        later_nodes = graph['edges'][path[-1]]
        for n in later_nodes:
            if n not in path or n == path[0]:
                reachEnd = False

        # check is the path extendable or not!
        if self.isPrimePath(path, graph) or reachEnd:
            return False
        else:
            return True

    def SimplePath_Finder(self, graph, nodes_tuple, paths=None):
        if paths is None:
            paths = []

        paths.extend(filter(lambda p: self.isPrimePath(p, graph), nodes_tuple))
        nodes_tuple = filter(lambda p: self.isExtendable(p, graph), nodes_tuple)

        newExPaths = []
        for p in nodes_tuple:
            for nx in graph['edges'][p[-1]]:
                if nx not in p or nx == p[0]:
                    newExPaths.append(p + (nx,))
        if len(newExPaths) > 0:
            self.SimplePath_Finder(graph, newExPaths, paths)

    def PrimePaths_Finder(self, graph):
        exPaths = [(n,) for n in graph['nodes']]
        simplePaths = []

        # recursively finding the simple paths of the graph
        self.SimplePath_Finder(graph, exPaths, simplePaths)
        primePaths = sorted(simplePaths, key=lambda a: (len(a), a))

        print(len(primePaths))
        for p in primePaths:
            print(list(p))


graphFilePath = './graphs/testcase2'

graphs = Graph()
gp = graphs.readGraphFromFile(graphFilePath)

graphs.PrimePaths_Finder(gp)

graphs.printGraph(gp)

# First networkx library is imported
# along with matplotlib
import networkx as nx
import matplotlib.pyplot as plt


# Defining a Class
class GraphVisualization:

    def __init__(self):
        self.visual = []

    # addEdge function inputs the vertices of an
    # edge and appends it to the visual list
    def addEdge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)

    # In visualize function G is an object of
    # class Graph given by networkx G.add_edges_from(visual)
    # creates a graph with a given list
    # nx.draw_networkx(G) - plots the graph
    # plt.show() - displays the graph
    def visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        nx.draw_networkx(G)
        plt.show()


# Driver code
G = GraphVisualization()

dict_edges = gp['edges']
for key, value in dict_edges.items():
    if len(value) == 0:
        continue
    for val in value:
        G.addEdge(key, val)
G.visualize()
