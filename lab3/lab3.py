import tkinter as tk
from tkinter import messagebox

from point import PointShape
from line import LineShape
from rect import RectShape
from ellipse import EllipseShape
from toolbar import Toolbar

ZH = 24
N = ZH + 100

TYPES = [
    ("Крапка", PointShape, "point", "Крапка"),
    ("Лінія", LineShape, "line", "Лінія"),
    ("Прямокутник", RectShape, "rect", "Прямокутник"),
    ("Еліпс", EllipseShape, "ellipse", "Еліпс"),
]
CLASSES = {name: cls for name, cls, _icon, _tip in TYPES}


class Editor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lab3")
        self.geometry("800x500")

        self._pcshape = []
        self._current = TYPES[0][0]
        self._rubber = None
        self._type_var = tk.StringVar(value=self._current)

        self._create_menu()
        toolbar = Toolbar(self, [(n, i, t) for n, _c, i, t in TYPES], self._select)
        toolbar.pack(side="top", fill="x")

        self._canvas = tk.Canvas(self, bg="white", highlightthickness=0)
        self._canvas.pack(fill="both", expand=True)

        self._canvas.bind("<ButtonPress-1>", self._on_press)
        self._canvas.bind("<B1-Motion>", self._on_motion)
        self._canvas.bind("<ButtonRelease-1>", self._on_release)
        self._canvas.bind("<Configure>", self._on_configure)

    def _create_menu(self):
        menubar = tk.Menu(self)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Очистити", command=self._clear)
        file_menu.add_separator()
        file_menu.add_command(label="Вихід", command=self.destroy)
        menubar.add_cascade(label="Файл", menu=file_menu)

        obj_menu = tk.Menu(menubar, tearoff=0, postcommand=self._on_init_menu_popup)
        for name, _cls, _icon, _tip in TYPES:
            obj_menu.add_radiobutton(label=name, variable=self._type_var, value=name,
                                     command=lambda n=name: self._select(n))
        menubar.add_cascade(label="Об’єкти", menu=obj_menu)

        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="Про програму", command=self._about)
        menubar.add_cascade(label="Довідка", menu=help_menu)

        self.config(menu=menubar)

    def _on_init_menu_popup(self):
        self._type_var.set(self._current)

    def _select(self, name):
        self._current = name

    def _about(self):
        messagebox.showinfo(
            "Довідка",
            "Lab3 – графічний редактор з панеллю інструментів\n"
            "Виконала: Поліщук Анна Валентинівна, ІМ-55\n"
            "Варіант: 24")

    def _clear(self):
        self._pcshape.clear()
        self._rubber = None
        self._canvas.delete("all")

    def _on_press(self, event):
        if len(self._pcshape) >= N:
            messagebox.showwarning("Увага", f"Масив заповнено ({N} об’єктів).")
            self._rubber = None
            return
        self._rubber = CLASSES[self._current](event.x, event.y)

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
        self._pcshape.append(shape)
        shape.draw(self._canvas)

    def _on_configure(self, _event):
        self._canvas.delete("shape")
        for shape in self._pcshape:
            shape.draw(self._canvas)


if __name__ == "__main__":
    Editor().mainloop()