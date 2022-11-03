import pygame

from config import BLACK, WHITE, GREEN

class QuadtreeRenderer:

	BOUNDARY_THICKNESS = 1
	POINT_RADIUS = 2

	def __init__(self, quadtree, window_size, window_title):
		self._quadtree = quadtree
		pygame.display.set_caption(window_title)
		self._screen = pygame.display.set_mode(window_size)
		self.__call__()

	def __call__(self):
		'Render qt'
		self._clear_screen()
		self._draw_quadtree(self._quadtree)
		self._update_display()

	def _draw_quadtree(self, quadtree):
		'Recursively draw qt and entities'
		b = quadtree.boundary
		r = pygame.Rect(b.left,b.top,b.w,b.h)
		pygame.draw.rect(self._screen, WHITE, r, QuadtreeRenderer.BOUNDARY_THICKNESS)
		
		if quadtree.divided:
			self._draw_quadtree(quadtree.tl)
			self._draw_quadtree(quadtree.tr)
			self._draw_quadtree(quadtree.bl)
			self._draw_quadtree(quadtree.br)

		for e in quadtree.entities:
			pygame.draw.circle(self._screen, GREEN, e.pos, QuadtreeRenderer.POINT_RADIUS)

	def _clear_screen(self):
		'Draw the screen black'
		self._screen.fill(BLACK)

	def _update_display(self):
		'Update the full display Surface to the screen'
		pygame.display.flip()
