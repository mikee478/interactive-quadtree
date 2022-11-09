import pygame

from config import BLACK, WHITE, RED

class QuadtreeRenderer:

	BOUNDARY_THICKNESS = 1
	POINT_RADIUS = 3

	def __init__(self, quadtree, surface_size):
		self.quadtree = quadtree
		self.surface = pygame.Surface(surface_size)

	def __call__(self, screen):
		'Render qt'
		self._clear_surface()
		self._draw_quadtree(self.quadtree)

		# Only draw in qt boundary
		b = self.quadtree.boundary
		screen.blit(self.surface,(b.left,b.top),area=(b.left,b.top,b.w,b.h))

	def _draw_quadtree(self, quadtree):
		'Recursively draw qt and entities'
		b = quadtree.boundary
		r = pygame.Rect(b.left,b.top,b.w,b.h)
		pygame.draw.rect(self.surface, WHITE, r, QuadtreeRenderer.BOUNDARY_THICKNESS)
		
		if quadtree.divided:
			self._draw_quadtree(quadtree.tl)
			self._draw_quadtree(quadtree.tr)
			self._draw_quadtree(quadtree.bl)
			self._draw_quadtree(quadtree.br)

		for e in quadtree.entities:
			pygame.draw.circle(self.surface, RED, e.pos, QuadtreeRenderer.POINT_RADIUS)

	def _clear_surface(self):
		'Draw the surface black'
		self.surface.fill(BLACK)
