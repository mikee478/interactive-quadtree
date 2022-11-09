import numpy as np

import pygame
from pygame import QUIT, KEYDOWN
from pygame.locals import (
	MOUSEBUTTONUP, MOUSEBUTTONDOWN,
	MOUSEMOTION, K_ESCAPE, K_SPACE, K_m)

from config import WINDOW_TITLE, WINDOW_SIZE, QT_SIDES
from quadtree import Quadtree
from aabb import AABB
from renderer import Renderer
from entity import Entity
from interaction_mode import InteractionMode

def main():
	pygame.init()
	clock = pygame.time.Clock()

	pygame.display.set_caption(WINDOW_TITLE)
	screen = pygame.display.set_mode(WINDOW_SIZE)

	qt = Quadtree(AABB.from_sides(*QT_SIDES))
	renderer = Renderer(screen)

	entities = []

	paused = False
	drag = False
	mode = InteractionMode.ADD_ENTITY
	query_range_pnts = [None,None]

	while True:
		event = pygame.event.poll()

		if is_quit_event(event):
			break
		elif event.type == KEYDOWN:
			if event.key == K_SPACE:
				paused = not paused
			elif event.key == K_m:
				mode = mode.next()

		elif event.type == MOUSEBUTTONDOWN:
			if mode == InteractionMode.ADD_ENTITY:
				if qt.boundary.contains(event.pos):
					entities.append(Entity(event.pos, qt.boundary))
			elif mode == InteractionMode.QUERY_RANGE:
				if not drag:
					query_range_pnts = [event.pos,None]
			drag = True

		elif event.type == MOUSEMOTION:
			if mode == InteractionMode.QUERY_RANGE and drag:
				query_range_pnts[1] = event.pos

		elif event.type == MOUSEBUTTONUP:
			drag = False

		dt = clock.tick() / 1000 # seconds

		qt.clear()
		for e in entities:
			if not paused:
				e.update(dt)
			qt.insert(e)

		renderer.clear()
		renderer.draw_quadtree(qt)

		if all(query_range_pnts):
			left,top = np.min(query_range_pnts, axis=0)
			right,bottom = np.max(query_range_pnts, axis=0)

			r = AABB.from_sides(left,right,top,bottom)
			in_range = qt.query_range(r)

			renderer.draw_range_query(r, in_range)

		renderer.draw_info(paused, mode)

		pygame.display.flip()

def is_quit_event(event):
	'Returns true iff event is a quit event'
	return event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE

if __name__ == '__main__':
	main()
