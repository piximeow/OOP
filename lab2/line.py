from shape import Shape


class LineShape(Shape):
    def draw(self, canvas, rubber=False):
        dash, width, tag = self._look(rubber)
        canvas.create_line(self._x1, self._y1, self._x2, self._y2,
                           fill="black", dash=dash, width=width, tags=tag)