class EdgeWeightedGraph:
	"""
	This class implements a simple API for undirected edge weighted graphs.
	"""

	def __init__(self):
		self.V = set()
		self.adj = dict()

	def addEdge(self, e):
		v = e.either()
		w = e.other(v)
		self.V.add(v)
		self.V.add(w)

		if v not in self.adj:
			self.adj[v] = []
		if w not in self.adj:
			self.adj[w] = []
		
		self.adj[v].append(e)
		self.adj[w].append(e)

	def vertices(self):
		return list(self.V)

	def neighborsOf(self, v):
		return self.adj[v]

	def toString(self):
		for v in self.V:
			print v, ": ", self.adj[v]

