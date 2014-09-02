class Stack:
	"""
	This class implements a stack (FIFO)
	"""
	def __init__(self):
		self.list = []

	def push(self, item):
		self.list.append(item)

	def pop(self):
		return self.list.pop()

	def isEmpty(self):
		return len(self.list) == 0

	def content(self):
		return self.list

class Queue:
	"""
	This class implements a simple API for a queue
	"""

	def __init__(self):
		self.list = []

	def enqueue(self, item):
		self.list.append(item)

	def dequeue(self):
		return self.list.pop(0)

	def isEmpty(self):
		return len(self.list) == 0
