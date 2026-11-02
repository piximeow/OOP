from shape import Shape


class EllipseShape(Shape):
    def draw(self, canvas, rubber=False):
        dash, width, tag = self._look(rubber)
        canvas.create_oval(self._x1, self._y1, self._x2, self._y2,
                           outline="black", fill="" if rubber else "orange",
                           dash=dash, width=width, tags=tag)