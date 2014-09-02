class Edge:
  def __init__(self, v, w, weight):
    self.v = v
    self.w = w
    self.weight = weight

  #def weight(self):
  #	return self.weight

  def either(self):
  	return self.v

  def other(self, vertex):
  	if vertex == self.v:
  		return self.w
  	if vertex == self.w:
  		return self.v

  def toString(self):
  	return self.v + "-" + self.w + " " + self.weight
