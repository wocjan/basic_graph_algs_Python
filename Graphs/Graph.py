class Graph:
	"""
	This class implements a simple API for undirected graphs.
	"""

	def __init__(self):
		self.V = set()
		self.adj = dict()

	def addEdge(self, v, w):
		self.V.add(v)
		self.V.add(w)

		if v not in self.adj:
			self.adj[v] = []
		if w not in self.adj:
			self.adj[w] = []
		
		self.adj[v].append(w)
		self.adj[w].append(v)

	def vertices(self):
		return list(self.V)

	def neighborsOf(self, v):
		return self.adj[v]

	def toString(self):
		for v in self.V:
			print v, ": ", self.adj[v]

