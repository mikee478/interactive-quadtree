from enum import Enum

class InteractionMode(Enum):
	ADD_ENTITY = 0
	QUERY_RANGE = 1

	def next(self):
		members = list(self.__class__)
		index = members.index(self) + 1
		if index >= len(members):
			index = 0
		return members[index]
