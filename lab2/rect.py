from shape import Shape


class RectShape(Shape):
    def draw(self, canvas, rubber=False):
        dash, width, tag = self._look(rubber)
        dx = self._x2 - self._x1
        dy = self._y2 - self._y1
        canvas.create_rectangle(self._x1 - dx, self._y1 - dy,
                                self._x1 + dx, self._y1 + dy,
                                outline="black", dash=dash, width=width, tags=tag)