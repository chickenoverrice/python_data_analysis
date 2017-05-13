# 6.00.2x Problem Set 5
# Graph optimization
#
# A set of data structures to represent graphs
#

class Node(object):
    def __init__(self, name):
        self.name = str(name)
    def getName(self):
        return self.name
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
    def __eq__(self, other):
        return self.name == other.name
    def __ne__(self, other):
        return not self.__eq__(other)
    def __hash__(self):
        # Override the default hash method
        # Think: Why would we want to do this?
        return self.name.__hash__()

class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return '{0}->{1}'.format(self.src, self.dest)

class Digraph(object):
    """
    A directed graph
    """
    def __init__(self):
        # A Python Set is basically a list that doesn't allow duplicates.
        # Entries into a set must be hashable (where have we seen this before?)
        # Because it is backed by a hashtable, lookups are O(1) as opposed to the O(n) of a list (nifty!)
        # See http://docs.python.org/2/library/stdtypes.html#set-types-set-frozenset
        self.nodes = set([])
        self.edges = {}
    def addNode(self, node):
        if node in self.nodes:
            # Even though self.nodes is a Set, we want to do this to make sure we
            # don't add a duplicate entry for the same node in the self.edges list.
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.nodes
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[str(k)]:
                res = '{0}{1}->{2}\n'.format(res, k, d)
        return res[:-1]

class WeightedEdge(Edge):
    def __init__(self, src, dest, weight1, weight2):
        self.src = src
        self.dest = dest
        self.total = weight1
        self.outdoor = weight2        
    def getTotalDistance(self):
        return self.total        
    def getOutdoorDistance(self):
        return self.outdoor        
    def __str__(self):
        return str(self.src)+'->'+str(self.dest)+'('+str(self.total)+','+str(self.outdoor)+')'

class WeightedDigraph(Digraph):
    def __init__(self):
        Digraph.__init__(self)
    def addEdge(self,edge):
        src = edge.getSource()
        dest = edge.getDestination()
        weight1 = edge.getTotalDistance()
        weight2 = edge.getOutdoorDistance()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append([dest,(weight1,weight2)])        
    def childrenOf(self,node):
        if len(self.edges[node]) == 0:
            return []
        ans = []
        for item in self.edges[node]:
            ans.append(item[0])    
        return ans
    def edgeCost(self,src,dest):
        for item in self.edges[src]:
            if item[0] == dest:
                return item[1]
        return (0,0)            
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res = '{0}{1}->{2} {3}\n'.format(res, k, d[0],(float(d[1][0]),float(d[1][1])))
        return res[:-1]
        
#nodes = []
#nodes.append(Node("ABC")) # nodes[0]
#nodes.append(Node("ACB")) # nodes[1]
#nodes.append(Node("BAC")) # nodes[2]
#nodes.append(Node("BCA")) # nodes[3]
#nodes.append(Node("CAB")) # nodes[4]
#nodes.append(Node("CBA")) # nodes[5]
#
#g = WeightedDigraph()
#
#for n in nodes:
#    g.addNode(n)
#
#g.addEdge(WeightedEdge(nodes[0],nodes[1],100,30))
#g.addEdge(WeightedEdge(nodes[0],nodes[5],200,70))
#g.addEdge(WeightedEdge(nodes[2],nodes[3],60,40)) 
#g.addEdge(WeightedEdge(nodes[4],nodes[5],20,20))
#
#print g.edgeCost(nodes[0],nodes[1])             
                                   