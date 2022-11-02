import numpy as np

class Entity:
	def __init__(self, pos, boundary):
		self.pos = np.array(pos, dtype='float')
		self.boundary = boundary

		# random velocity vector
		self.v = np.random.uniform(-1,1,2)
		self.v *= np.random.uniform(0.25,2) / np.linalg.norm(self.v)

	def update(self):

		# Hit top or bottom boundary
		if (self.v[0] < 0 and self.pos[0] <= self.boundary.left or 
		self.v[0] > 0 and self.pos[0] >= self.boundary.right):
			self.v[0] *= -1

		# Hit left or right boundary
		if (self.v[1] < 0 and self.pos[1] <= self.boundary.top or 
		self.v[1] > 0 and self.pos[1] >= self.boundary.bottom):
			self.v[1] *= -1

		self.pos += self.v
