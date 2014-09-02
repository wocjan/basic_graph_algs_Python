from Queue import PriorityQueue

class DijkstraSP:
	"""
	This class implement Dijkstra's single source shortest paths algorithm for 
	undirected edge weighted graphs.
	"""

	def __init__(self, G, s, verbose=False):
		self.verbose = verbose
		if self.verbose:
			print "=> DijkstraSP from source", s, "results in the traversal order:"


		self.distTo = dict()
		self.edgeTo = dict()
		self.s = s
		
		self.pq = PriorityQueue()
		self.pq.put(s, 0.0)
		self.distTo[s] = 0.0

		while not self.pq.empty():
			v = self.pq.get()
			if self.verbose:
				print v
			self.relax(G, v)

	def relax(self, G, v):
		for e in G.adj[v]:
			w = e.other(v)
			if w not in self.distTo:
				self.distTo[w] = 99999

			print "weight", e.weight
			print "distance to", w, "is", self.distTo[w]

			if self.distTo[w] > self.distTo[v] + e.weight:
				self.distTo[w]  = self.distTo[v] + e.weight
				self.edgeTo[w] = v
				self.pq.put(w, self.distTo[w])

	def hasPathTo(self, v):
		return self.distTo[v] < 99999

	def pathTo(self, v):
		if not self.hasPathTo(v):
			return None
		path = []
		while v != self.s:
			path = [v] + path
			v = self.edgeTo[v]
		path = [self.s] + path
		return path
