from Edge import Edge
from EdgeWeightedGraph import EdgeWeightedGraph
from DijkstraSP import DijkstraSP

e1 = Edge("A", "B", 1.0)
e2 = Edge("B", "C", 1.0)
e3 = Edge("C", "D", 1.0)
e4 = Edge("A", "D", 2.0)

G = EdgeWeightedGraph()

G.addEdge(e1)
G.addEdge(e2)
G.addEdge(e3)
G.addEdge(e4)

sp = DijkstraSP(G, "A")

print sp.pathTo("D")
print sp.distTo["D"]



