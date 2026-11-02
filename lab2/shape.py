from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, x, y):
        self._x1 = self._x2 = x
        self._y1 = self._y2 = y

    def set_end(self, x, y):
        self._x2, self._y2 = x, y

    def _look(self, rubber):
        if rubber:
            return (4, 4), 1, "rubber"
        return None, 2, "shape"

    @abstractmethod
    def draw(self, canvas, rubber=False):
        pass