import numpy as np

class Entity:

	SPEED_RANGE = (50,200)

	def __init__(self, pos, boundary):
		self.pos = np.array(pos, dtype='float')
		self.boundary = boundary

		# random velocity vector
		self.v = np.random.uniform(-1,1,2)
		speed = np.random.uniform(*Entity.SPEED_RANGE) # px/sec
		self.v *= speed / np.linalg.norm(self.v)

	def update(self, dt):
		'Update the entity'
		pos2 = self.pos + self.v * dt

		# Hit top or bottom boundary
		if pos2[0] <= self.boundary.left or pos2[0] >= self.boundary.right:
			self.v[0] *= -1

		# Hit left or right boundary
		if pos2[1] <= self.boundary.top or pos2[1] >= self.boundary.bottom:
			self.v[1] *= -1

		self.pos += self.v * dt
