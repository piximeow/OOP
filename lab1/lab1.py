
import tkinter as tk
from tkinter import ttk

import module1
import module2


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lab1")
        self.geometry("480x240")
        self._dialog = None 

        menubar = tk.Menu(self)
        menubar.add_command(label="Робота1", command=self._work1)
        menubar.add_command(label="Робота2", command=self._work2)
        self.config(menu=menubar)

        self._text = tk.StringVar(value="")
        ttk.Label(self, textvariable=self._text, font=("Segoe UI", 16),
                  wraplength=440, anchor="center").pack(expand=True, fill="both")

    def _close_current_dialog(self):
       
        if self._dialog is not None and self._dialog.winfo_exists():
            self._dialog.destroy()
        self._dialog = None

    def _show(self, text: str):
        self._text.set(text)

    def _work1(self):
        self._close_current_dialog()
        self._dialog = module1.open_dialog(self, self._show)

    def _work2(self):
        self._close_current_dialog()
        self._dialog = module2.open_dialog(self, self._show)


if __name__ == "__main__":
    MainWindow().mainloop()