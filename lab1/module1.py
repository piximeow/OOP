
import tkinter as tk
from tkinter import ttk

import utils

__all__ = ["open_dialog"]  


_TITLE = "Вибір групи"

_GROUPS = ["IM-51", "IM-52", "IM-53", "IM-54", "IM-55", "IM-o51", "IO-51"]


def open_dialog(parent: tk.Misc, on_ok) -> tk.Toplevel:
    
    dlg = tk.Toplevel(parent)
    dlg.title(_TITLE)

    ttk.Label(dlg, text="Оберіть групу:").pack(padx=12, pady=(12, 4), anchor="w")

    listbox = tk.Listbox(dlg, height=7, exportselection=False)
    for name in _GROUPS:
        listbox.insert(tk.END, name)
    listbox.pack(padx=12, pady=4, fill="both", expand=True)


    def _ok():
        selection = listbox.curselection()
        if not selection:
            return  
        on_ok(listbox.get(selection[0]))
        dlg.destroy()

    def _cancel():
        dlg.destroy()

    buttons = ttk.Frame(dlg)
    buttons.pack(padx=12, pady=12)
    ttk.Button(buttons, text="Так", command=_ok).pack(side="left", padx=4)
    ttk.Button(buttons, text="Відміна", command=_cancel).pack(side="left", padx=4)

    listbox.bind("<Double-Button-1>", lambda _e: _ok())
    dlg.bind("<Escape>", lambda _e: _cancel())

    utils.make_modal(dlg, parent)
    return dlg