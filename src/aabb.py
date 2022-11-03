class AABB:
	def __init__(self, left, top, w, h):
		self.left = left
		self.top = top
		self.w = w
		self.h = h
		
		self.right = left + w
		self.bottom = top + h

		if self.w < 0:
			raise ValueError(f'AABB width ({self.w}) cannot be negative')
		if self.h < 0:
			raise ValueError(f'AABB height ({self.h}) cannot be negative')

	@classmethod
	def from_sides(cls, left, right, top, bottom):
		return cls(left, top, right-left+1, bottom-top+1)

	def contains(self, p):
		'Returns true iff point is contained within the AABB'
		return (self.left <= p[0] and p[0] <= self.right and
			self.top <= p[1] and p[1] <= self.bottom)
