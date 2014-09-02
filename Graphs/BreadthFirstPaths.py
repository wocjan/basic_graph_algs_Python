import basicDataStructures

class BreadthFirstPaths:
	"""
	This class implement BFS traversal.
	"""

	def __init__(self, G, s, verbose=False):
		self.marked = set()
		self.edgeTo = dict()
		self.s = s
		
		self.verbose = verbose
		if self.verbose:
			print "=> BreadthFirstPaths from source", s, "results in the traversal order:"

		self.bfs(G, s)

	def bfs(self, G, s):
		queue = basicDataStructures.Queue()
		
		queue.enqueue(s)
		self.marked.add(s)

		while not queue.isEmpty():
			v = queue.dequeue()
			if self.verbose:
				print v

			for w in G.adj[v]:
				if w not in self.marked:
					queue.enqueue(w)
					self.marked.add(w)
					self.edgeTo[w] = v

	def hasPathTo(self, v):
		return v in self.marked

	def pathTo(self, v):
		if not self.hasPathTo(v):
			return None
		path = []
		while v != self.s:
			path = [v] + path
			v = self.edgeTo[v]
		path = [self.s] + path
		return path
