from shape import Shape


class PointShape(Shape):
    def draw(self, canvas, rubber=False):
        width, tag = self._look(rubber)
        r = 3
        canvas.create_oval(self._x1 - r, self._y1 - r, self._x1 + r, self._y1 + r,
                           outline="black", fill="" if rubber else "black",
                           width=width, tags=tag)