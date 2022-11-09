import numpy as np

import pygame
from pygame import QUIT, KEYDOWN
from pygame.locals import (
	MOUSEBUTTONUP, MOUSEBUTTONDOWN,
	MOUSEMOTION, K_ESCAPE, K_SPACE, K_m)

from config import WINDOW_TITLE, WINDOW_SIZE, QT_SIDES, GREEN
from quadtree import Quadtree
from aabb import AABB
from quadtree_renderer import QuadtreeRenderer
from entity import Entity
from interaction_mode import InteractionMode

def main():
	pygame.init()
	clock = pygame.time.Clock()

	pygame.display.set_caption(WINDOW_TITLE)
	screen = pygame.display.set_mode(WINDOW_SIZE)

	qt = Quadtree(AABB.from_sides(*QT_SIDES))
	qt_renderer = QuadtreeRenderer(qt, WINDOW_SIZE)

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
				query_range_pnts = [None,None]
		elif event.type == MOUSEBUTTONDOWN:
			if mode == InteractionMode.ADD_ENTITY:
				if not paused and qt.boundary.contains(event.pos):
					entities.append(Entity(event.pos, qt.boundary))
			elif mode == InteractionMode.QUERY_RANGE:
				if not drag:
					query_range_pnts[0] = event.pos
					query_range_pnts[1] = None
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
		qt_renderer(screen)

		if all(query_range_pnts):
			lt = np.min(query_range_pnts, axis=0)
			rb = np.max(query_range_pnts, axis=0)

			r = AABB.from_sides(lt[0],rb[0],lt[1],rb[1])
			pygame.draw.rect(screen, GREEN, pygame.Rect(r.left,r.top,r.w,r.h), 1)

			in_range = qt.query_range(r)
			for e in in_range:
				pygame.draw.circle(screen, GREEN, e.pos, 3)

		pygame.display.flip()

def is_quit_event(event):
	'Returns true iff event is a quit event'
	return event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE

if __name__ == '__main__':
	main()
