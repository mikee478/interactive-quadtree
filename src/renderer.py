import pygame

from config import WHITE, RED, BLACK, GREEN
from interaction_mode import InteractionMode

class Renderer:
	BOUNDARY_THICKNESS = 1
	BOUNDARY_COLOR = WHITE
	POINT_RADIUS = 3
	POINT_COLOR = RED

	BOUNDARY_THICKNESS = 1
	RQ_BOUNDARY_COLOR = GREEN
	RQ_POINT_COLOR = GREEN

	FONT_SIZE = 14

	def __init__(self, surface):
		self.surface = surface
		self.font = pygame.font.SysFont('arial', Renderer.FONT_SIZE)

	def clear(self):
		'Draw the screen black'
		self.surface.fill(BLACK)

	def draw_quadtree(self, quadtree):
		'Recursively draw qt and entities'
		b = quadtree.boundary
		r = pygame.Rect(b.left,b.top,b.w,b.h)
		pygame.draw.rect(self.surface, Renderer.BOUNDARY_COLOR, 
			r, Renderer.BOUNDARY_THICKNESS)
		
		if quadtree.divided:
			self.draw_quadtree(quadtree.tl)
			self.draw_quadtree(quadtree.tr)
			self.draw_quadtree(quadtree.bl)
			self.draw_quadtree(quadtree.br)

		for e in quadtree.entities:
			pygame.draw.circle(self.surface, Renderer.POINT_COLOR, 
				e.pos, Renderer.POINT_RADIUS)

	def draw_range_query(self, r, in_range):
		'Draw range query boundary and entities in range'
		pygame.draw.rect(self.surface, GREEN, 
			pygame.Rect(r.left,r.top,r.w,r.h), Renderer.BOUNDARY_THICKNESS)
		for e in in_range:
			pygame.draw.circle(self.surface, Renderer.RQ_POINT_COLOR, 
				e.pos, Renderer.POINT_RADIUS)

	def draw_info(self, paused, interaction_mode):
		'Draw simulation info'
		info = []
		if interaction_mode == InteractionMode.ADD_ENTITY:
			info.append('Click to add points')
		elif interaction_mode == InteractionMode.QUERY_RANGE:
			info.append('Drag to create range for query')

		info.append('')
		info.append(f'M = Change interaction mode ({interaction_mode.name})')
		info.append(f'Space = Pause ({paused})')

		for i,s in enumerate(info):
			self.surface.blit(self.font.render(s, True, WHITE), 
				(4,2+i*Renderer.FONT_SIZE))
