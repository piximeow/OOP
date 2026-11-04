import tkinter as tk

from icons import create_icon
from tooltip import ToolTip


class Toolbar(tk.Frame):
    def __init__(self, parent, items, on_select):
        super().__init__(parent, bd=1, relief="raised")
        self._icons = []
        for name, icon, tip in items:
            image = create_icon(icon, self)
            self._icons.append(image)
            button = tk.Button(self, image=image, command=lambda n=name: on_select(n))
            button.pack(side="left", padx=2, pady=2)
            ToolTip(button, tip)
