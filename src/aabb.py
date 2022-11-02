class AABB:
	# (x,y) is upper left corner, width, height
	def __init__(self, x, y, w, h):
		self.x = x
		self.y = y
		self.w = w
		self.h = h

		self.left = x
		self.right = x + w
		self.top = y
		self.bottom = y + h

	def contains(self, p):
		return (self.left <= p[0] and p[0] <= self.right and
			self.top <= p[1] and p[1] <= self.bottom)
