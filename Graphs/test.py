from Graph import Graph as Graph

from DepthFirstPaths import selectDepthFirstPaths as selectDepthFirstPaths

from BreadthFirstPaths import BreadthFirstPaths as BreadthFirstPaths

# create simple graph

G = Graph()
G.addEdge("A", "B")
G.addEdge("A", "C")
G.addEdge("B", "D")
G.addEdge("D", "A")
G.addEdge("C", "E")

G.toString()

print "vertices:", G.vertices()
print "vertices adjacent to B:", G.neighborsOf("B")
print

# recursive depth first paths

dfp = selectDepthFirstPaths(recursive=True)(G, "A", verbose=True);
print "depth first search path to D:", dfp.pathTo("D")
print

# stack-based depth first paths 

dfp = selectDepthFirstPaths(recursive=False)(G, "A", verbose=True);
print "depth first search path to D:", dfp.pathTo("D")
print

# breadth first paths 

bfp = BreadthFirstPaths(G, "A", verbose=True);
print "breadth first search path to D:", bfp.pathTo("D")
print
