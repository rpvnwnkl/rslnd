import pydot
graph = pydot.Dot(graph_type = 'graph')

class Node(object):
    def __init__(self, name, prefix, suffix):
        self.name = name
        self.front = prefix
        self.back = suffix
    def getName(self):
        return self.name
    def getFront(self):
        return self.front
    def getBack(self):
        return self.back
    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return str(self.src) + '->' + str(self.dest)

class Digraph(object):
    def __init__(self):
        self.nodes = set([])
        self.edges = {}
    def addNode(self, node):
        if node in self.nodes:
            raise ValueError('Duplicate Node')
        else:
            self.nodes.add(node)
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in Graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.nodes
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res = res + str(k) + ' ' + str(d) + '\n'
        return res[:-1]
    
digraph = Digraph()

file = open('./graphList.txt')
rawText = file.readlines()
##print rawText

nodeList = []
for i in range(0, len(rawText), 3):
    nodeList.append(Node(rawText[i].strip('\n, >'), \
    rawText[i+1].strip('\n')[0:3], rawText[i+2].strip('\n')[-3:]))

for node in nodeList:
    digraph.addNode(node)
##    print node

for i in nodeList:
    for j in nodeList:
        if i != j:
            if i.getBack() == j.getFront():
                digraph.addEdge(Edge(i, j))
                edge = pydot.Edge(i.getName(), j.getName())
                graph.add_edge(edge)

print digraph
graph.write_png('draft_plot1.png')                  

