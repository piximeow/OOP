import tkinter as tk
from tkinter import messagebox

from point import PointShape
from line import LineShape
from rect import RectShape
from ellipse import EllipseShape

ZH = 23
N = ZH + 100

TYPES = [
    ("Крапка", PointShape),
    ("Лінія", LineShape),
    ("Прямокутник", RectShape),
    ("Еліпс", EllipseShape),
]


class Editor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x500")

        self._pcshape = [None] * N
        self._count = 0
        self._current = TYPES[0]
        self._rubber = None

        self._create_menu()
        self._canvas = tk.Canvas(self, bg="white", highlightthickness=0)
        self._canvas.pack(fill="both", expand=True)

        self._canvas.bind("<ButtonPress-1>", self._on_press)
        self._canvas.bind("<B1-Motion>", self._on_motion)
        self._canvas.bind("<ButtonRelease-1>", self._on_release)
        self._canvas.bind("<Configure>", self._on_configure)

        self._update_title()

    def _create_menu(self):
        menubar = tk.Menu(self)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Очистити", command=self._clear)
        file_menu.add_separator()
        file_menu.add_command(label="Вихід", command=self.destroy)
        menubar.add_cascade(label="Файл", menu=file_menu)

        obj_menu = tk.Menu(menubar, tearoff=0)
        for name, cls in TYPES:
            obj_menu.add_command(
                label=name, command=lambda n=name, c=cls: self._select(n, c))
        menubar.add_cascade(label="Об’єкти", menu=obj_menu)

        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="Про програму", command=self._about)
        menubar.add_cascade(label="Довідка", menu=help_menu)

        self.config(menu=menubar)

    def _select(self, name, cls):
        self._current = (name, cls)
        self._update_title()

    def _update_title(self):
        self.title(f"Lab2 – {self._current[0]}")

    def _about(self):
        messagebox.showinfo(
            "Довідка",
            "Lab2 – графічний редактор об’єктів\n"
            "Виконала: Поліщук Анна, ІМ-55\n"
            "Варіант: 23")

    def _clear(self):
        for i in range(self._count):
            self._pcshape[i] = None
        self._count = 0
        self._rubber = None
        self._canvas.delete("all")

    def _on_press(self, event):
        if self._count >= N:
            messagebox.showwarning("Увага", f"Масив заповнено ({N} об’єктів).")
            self._rubber = None
            return
        self._rubber = self._current[1](event.x, event.y)

    def _on_motion(self, event):
        if self._rubber is None:
            return
        self._rubber.set_end(event.x, event.y)
        self._canvas.delete("rubber")
        self._rubber.draw(self._canvas, rubber=True)

    def _on_release(self, event):
        if self._rubber is None:
            return
        shape, self._rubber = self._rubber, None
        shape.set_end(event.x, event.y)
        self._canvas.delete("rubber")
        self._pcshape[self._count] = shape
        self._count += 1
        shape.draw(self._canvas)

    def _on_configure(self, _event):
        self._canvas.delete("shape")
        for i in range(self._count):
            self._pcshape[i].draw(self._canvas)


if __name__ == "__main__":
    Editor().mainloop()