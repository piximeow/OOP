import math
import tkinter as tk
from abc import ABC, abstractmethod

ICON_SIZE = 24
ICON_COLOR = "#000000"
PEN = 2


class Icon(ABC):
    def __init__(self, master=None):
        self.image = tk.PhotoImage(master=master, width=ICON_SIZE, height=ICON_SIZE)
        self.draw()

    @abstractmethod
    def draw(self):
        pass

    def pixel(self, x, y, size=PEN):
        x, y = int(round(x)), int(round(y))
        x2 = min(x + size, ICON_SIZE)
        y2 = min(y + size, ICON_SIZE)
        if 0 <= x < x2 and 0 <= y < y2:
            self.image.put(ICON_COLOR, to=(x, y, x2, y2))

    def line(self, x1, y1, x2, y2):
        steps = max(abs(x2 - x1), abs(y2 - y1), 1)
        for i in range(steps + 1):
            t = i / steps
            self.pixel(x1 + (x2 - x1) * t, y1 + (y2 - y1) * t)


class PointIcon(Icon):
    def draw(self):
        self.pixel(10, 10, size=4)


class LineIcon(Icon):
    def draw(self):
        self.line(3, 19, 19, 3)


class RectIcon(Icon):
    def draw(self):
        x1, y1, x2, y2 = 3, 6, 19, 16
        self.line(x1, y1, x2, y1)
        self.line(x1, y2, x2, y2)
        self.line(x1, y1, x1, y2)
        self.line(x2, y1, x2, y2)


class EllipseIcon(Icon):
    def draw(self):
        cx, cy, a, b = 11, 11, 8, 5
        steps = 120
        for i in range(steps):
            angle = 2 * math.pi * i / steps
            self.pixel(cx + a * math.cos(angle), cy + b * math.sin(angle))


ICONS = {
    "point": PointIcon,
    "line": LineIcon,
    "rect": RectIcon,
    "ellipse": EllipseIcon,
}


def create_icon(name, master=None):
    return ICONS[name](master).image
