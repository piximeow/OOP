from shape import Shape


class EllipseShape(Shape):
    def draw(self, canvas, rubber=False):
        width, tag = self._look(rubber)
        dx = self._x2 - self._x1
        dy = self._y2 - self._y1
        canvas.create_oval(self._x1 - dx, self._y1 - dy,
                           self._x1 + dx, self._y1 + dy,
                           outline="black", fill="" if rubber else "gray",
                           width=width, tags=tag)