import basicDataStructures

# this lets you chose between 
#   the recursive implementation and
#   the stack-based implementation 
# of depth first search paths

def selectDepthFirstPaths(recursive=False):
	if recursive:
		return DepthFirstPaths
	else:
		return DepthFirstPaths_StackBased

class DepthFirstPaths:
	"""
	This class implements a simple API for Depth First Search.
	It uses recursive calls.
	"""
	def __init__(self, G, s, verbose=False):
		# has dfs been called for this vertex?
		self.marked = set()
		# last vertex on known path to this vertex
		self.edgeTo = dict()
		# source
		self.s = s
		
		self.verbose = verbose
		if self.verbose:
			print "=> running recursive DepthFirstPaths from source", s, "results in the traversal order:"

		self.dfs(G, s)

	def dfs(self, G, v):
		if self.verbose:
			print v

		self.marked.add(v)

		for w in G.adj[v]:
			if w not in self.marked:
				self.edgeTo[w] = v
				self.dfs(G, w)

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

class DepthFirstPaths_StackBased:
	"""
	This class implements depth first search using an explicit stack.
	This implementation produces the same output as the recursive implementation because we reverse
	the list of the vertices adjacent to v like so: for w in reversed(G.adj[v])
	"""

	def __init__(self, G, s, verbose=False):
		self.marked = set()
		self.edgeTo = dict()
		self.s = s

		self.verbose = verbose
		if self.verbose:
			print "=> running stack-based DepthFirstPaths from source", s, "results in the traversal order:"

		self.dfs(G, s)

	def dfs(self, G, s):
		stack = basicDataStructures.Stack()
		stack.push((s, None))

		while not stack.isEmpty():
			(v, u) = stack.pop()

			if self.verbose:
				if v not in self.marked:
					print v, "unmarked"
				else:
					print v, "marked"

			if v not in self.marked:
				self.marked.add(v)
				self.edgeTo[v] = u

				for w in reversed(G.adj[v]):
					stack.push((w, v))

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
