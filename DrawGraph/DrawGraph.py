import networkx as nx
import matplotlib.pyplot as plt


class GraphVisualization:

    def __init__(self):
        # visual is a list which stores all set of edges
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


def ListOfEdges(inp):
    with open(r"Graphs\Testcase" + inp, 'r') as fp:
        # lines to read
        line_numbers = [7, 8, 9, 10, 11, 12, 13]
        # To store lines
        lines = []
        for i, line in enumerate(fp):
            # read line 7 to 12
            if i in line_numbers:
                lines.append(line.strip())
    # print(lines)
    return lines


def EdgesToSingleString(mylist):
    finalList = []
    for i in mylist:
        str = i
        tmp = str.split()
        tempList = list(map(int, tmp))
        finalList.append(tempList)
    return finalList


def MakeGraph(final_list):
    G = GraphVisualization()
    for i in range(len(final_list)):
        size = len(final_list[i])
        for j in range(len(final_list[i])):
            if final_list[i][j] != -1:
                G.addEdge(i, final_list[i][j])
    G.visualize()


def Finding_Edges(testcase_number):
    # s = '0 1 2'
    # x = s.split()
    # print(int(x[0]))
    if testcase_number == 1:
        with open(r"Graphs\Testcase1", 'r') as fp:
            # lines to read
            line_numbers = [7, 8, 9, 10, 11, 12]
            # To store lines
            lines = []
            for i, line in enumerate(fp):
                # read line 7 to 12
                if i in line_numbers:
                    lines.append(line.strip())
                elif i > 7:
                    # don't read after line 7 to save time
                    break
        print(lines)
    elif testcase_number == 2:
        with open(r"Graphs\Testcase2", 'r') as fp:
            line_numbers = [7, 8, 9, 10, 11, 12]
            lines = []
            for i, line in enumerate(fp):
                if i in line_numbers:
                    lines.append(line.strip())
                elif i > 7:
                    break
        print(lines)
    elif testcase_number == 3:
        with open(r"Graphs\Testcase3", 'r') as fp:
            line_numbers = [7, 8, 9, 10, 11, 12]
            lines = []
            for i, line in enumerate(fp):
                if i in line_numbers:
                    lines.append(line.strip())
                elif i > 7:
                    break
        print(lines)
    elif testcase_number == 4:
        with open(r"Graphs\Testcase4", 'r') as fp:
            line_numbers = [7, 8, 9, 10, 11, 12]
            lines = []
            for i, line in enumerate(fp):
                if i in line_numbers:
                    lines.append(line.strip())
                elif i > 7:
                    break
        print(lines)


def DrawTestCase(testcase_number):
    G = GraphVisualization()
    if testcase_number == 1:
        G.addEdge(0, 1)
        G.addEdge(0, 4)
        G.addEdge(1, 2)
        G.addEdge(1, 5)
        G.addEdge(2, 3)
        G.addEdge(3, 1)
        G.addEdge(4, 4)
        G.addEdge(4, 6)
        G.addEdge(5, 6)
        G.visualize()
    elif testcase_number == 2:
        G.addEdge(0, 2)
        G.addEdge(0, 7)
        G.addEdge(0, 5)
        G.addEdge(1, 3)
        G.addEdge(1, 4)
        G.addEdge(2, 2)
        G.addEdge(3, 5)
        G.addEdge(3, 6)
        G.addEdge(4, 6)
        G.addEdge(5, 1)
        G.visualize()
    elif testcase_number == 3:
        G.addEdge(0, 1)
        G.addEdge(0, 2)
        G.addEdge(0, 3)
        G.addEdge(1, 3)
        G.addEdge(3, 2)
        G.visualize()
    elif testcase_number == 4:
        G.addEdge(0, 1)
        G.addEdge(1, 2)
        G.addEdge(1, 3)
        G.addEdge(3, 4)
        G.addEdge(4, 1)
        G.visualize()


if __name__ == '__main__':
    # Finding_Edges(4)
    # DrawTestCase(4)

    edgeList = ListOfEdges("3")
    finalList = EdgesToSingleString(edgeList)
    MakeGraph(finalList)
