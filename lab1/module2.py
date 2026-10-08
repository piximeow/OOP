
import tkinter as tk
from tkinter import ttk

import utils

__all__ = ["open_dialog"]

_TITLE = "Введення тексту"


def open_dialog(parent: tk.Misc, on_ok) -> tk.Toplevel:
    dlg = tk.Toplevel(parent)
    dlg.title(_TITLE)

    ttk.Label(dlg, text="Введіть текст:").pack(padx=12, pady=(12, 4), anchor="w")

    entry = ttk.Entry(dlg, width=40)
    entry.pack(padx=12, pady=4)
    entry.focus_set()

    def _ok():
        on_ok(entry.get())
        dlg.destroy()

    def _cancel():
        dlg.destroy()

    buttons = ttk.Frame(dlg)
    buttons.pack(padx=12, pady=12)
    ttk.Button(buttons, text="Так", command=_ok).pack(side="left", padx=4)
    ttk.Button(buttons, text="Відміна", command=_cancel).pack(side="left", padx=4)

    dlg.bind("<Return>", lambda _e: _ok())
    dlg.bind("<Escape>", lambda _e: _cancel())

    utils.make_modal(dlg, parent)
    return dlg