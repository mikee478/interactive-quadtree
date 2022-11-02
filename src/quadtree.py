from aabb import AABB

class Quadtree:

	CAPACITY = 1
	MAX_DEPTH = 6

	def __init__(self, boundary, depth=0):
		self.boundary = boundary
		self.points = []
		self.depth = depth

		self.divided = False
		self.tl = None
		self.tr = None
		self.bl = None
		self.br = None

	def clear(self):
		self.points = []
		self.divided = False
		self.tl = None
		self.tr = None
		self.bl = None
		self.br = None

	def insert(self, p):
		# stop if point not in current boudary
		if not self.boundary.contains(p):
			return False

		if not self.divided:
			# add point to current qt
			if len(self.points) < Quadtree.CAPACITY or self.depth == Quadtree.MAX_DEPTH:
				self.points.append(p)
				return True
			else:
				self._subdivide()
		
		return (self.tl.insert(p) or self.tr.insert(p) or
			self.bl.insert(p) or self.br.insert(p))

	def _subdivide(self):
		# divide into 4 qts of half width and half height
		self.divided = True
		x = self.boundary.x
		y = self.boundary.y
		w = self.boundary.w
		h = self.boundary.h

		# For odd width/height
		w1 = w//2
		w2 = w-w1
		h1 = h//2
		h2 = h-h1

		self.tl = Quadtree(AABB(x,		y, 		w1, h1), depth=self.depth+1)
		self.tr = Quadtree(AABB(x+w1, 	y, 		w2, h1), depth=self.depth+1)
		self.bl = Quadtree(AABB(x, 		y+h1, 	w1, h2), depth=self.depth+1)
		self.br = Quadtree(AABB(x+w1, 	y+h1, 	w2, h2), depth=self.depth+1)

		# only leaf qt have points
		for p in self.points:
			(self.tl.insert(p) or self.tr.insert(p) or
			self.bl.insert(p) or self.br.insert(p))

		self.points = []
