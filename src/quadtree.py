from aabb import AABB

class Quadtree:

	CAPACITY = 1
	MAX_DEPTH = 6

	def __init__(self, boundary, depth=0):
		self.boundary = boundary
		self.depth = depth
		self.clear()

	def clear(self):
		'Clears qt'
		self.entities = []
		self.divided = False
		self.tl = None
		self.tr = None
		self.bl = None
		self.br = None

	def insert(self, e):
		'Returns true iff the entity was successfully inserted in the qt'

		# stop if entity not in current boundary
		if not self.boundary.contains(e.pos):
			return False

		if not self.divided:
			# add entity to current qt
			if len(self.entities) < Quadtree.CAPACITY or self.depth == Quadtree.MAX_DEPTH:
				self.entities.append(e)
				return True
			else:
				self._subdivide()
		
		# add entity to one of the subdivided qt
		return (self.tl.insert(e) or self.tr.insert(e) or
			self.bl.insert(e) or self.br.insert(e))

	def _subdivide(self):
		'Divide into 4 qts of half width and half height'
		self.divided = True

		left = self.boundary.left
		top = self.boundary.top
		w = self.boundary.w
		h = self.boundary.h

		# For odd width/height
		w1 = w//2
		w2 = w-w1
		h1 = h//2
		h2 = h-h1

		self.tl = Quadtree(AABB(left,	 top,    w1, h1), self.depth+1)
		self.tr = Quadtree(AABB(left+w1, top,    w2, h1), self.depth+1)
		self.bl = Quadtree(AABB(left,	 top+h1, w1, h2), self.depth+1)
		self.br = Quadtree(AABB(left+w1, top+h1, w2, h2), self.depth+1)

		# only leaf qt have entities
		for e in self.entities:
			(self.tl.insert(e) or self.tr.insert(e) or
			self.bl.insert(e) or self.br.insert(e))

		self.entities = []
