import pygame
from pygame import QUIT, KEYDOWN
from pygame.locals import MOUSEBUTTONDOWN, MOUSEMOTION, K_ESCAPE

from config import WINDOW_TITLE, WINDOW_SIZE, QT_SIDES
from quadtree import Quadtree
from aabb import AABB
from quadtree_renderer import QuadtreeRenderer
from entity import Entity

def main():
	pygame.init()
	clock = pygame.time.Clock()

	qt = Quadtree(AABB.from_sides(*QT_SIDES))
	qt_renderer = QuadtreeRenderer(qt, WINDOW_SIZE, WINDOW_TITLE)
	entities = []

	while True:
		event = pygame.event.poll()

		if is_quit_event(event):
			break
		elif event.type == MOUSEBUTTONDOWN:
			if qt.boundary.contains(event.pos):
				entities.append(Entity(event.pos, qt.boundary))

		dt = clock.tick() / 1000 # seconds

		qt.clear()
		for e in entities:
			e.update(dt)
			qt.insert(e)
		qt_renderer()

def is_quit_event(event):
	'Returns true iff event is a quit event'
	return event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE

if __name__ == '__main__':
	main()
