#!python3

from Graph import Graph
class DFSGraph(Graph):
	def __init__(self):
		super().__init__()
		self.time = 0

	def dfs(self):
		for aVertex in self:
			aVertex.setColor('white')
			aVertex.setPred(-1)
		for aVertex in self:
			if self.getColor() == 'white':
				self.dfsVisit(aVertex)
	def dfsVisit(self,startVertex):
		startVertex.setColor('gray')
		self.time += 1	
		startVertex.setDiscovery(self.time)
		for nextVertex in startVertex.getNeighbors():
			if nextVertex.getColor()== 'white':
				nextVertex.setPred(startVertex)
				self.dfsvisit(nextVertex)
		startVertex.setColor('black')
		self.time += 1
		startVertex.setFinish(self.time)
				
