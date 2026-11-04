from shape import Shape


class RectShape(Shape):
    def draw(self, canvas, rubber=False):
        width, tag = self._look(rubber)
        canvas.create_rectangle(self._x1, self._y1, self._x2, self._y2,
                                outline="black", width=width, tags=tag)