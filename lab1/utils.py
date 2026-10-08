import tkinter as tk

__all__ = ["center_on_parent", "make_modal"]


def center_on_parent(win: tk.Toplevel, parent: tk.Misc) -> None:
    """Розташовує вікно діалогу по центру батьківського вікна."""
    win.update_idletasks()
    x = parent.winfo_rootx() + (parent.winfo_width() - win.winfo_width()) // 2
    y = parent.winfo_rooty() + (parent.winfo_height() - win.winfo_height()) // 2
    win.geometry(f"+{max(x, 0)}+{max(y, 0)}")


def make_modal(win: tk.Toplevel, parent: tk.Misc) -> None:
    """Робить вікно модальним (аналог DialogBox у WinAPI)."""
    win.transient(parent)
    win.resizable(False, False)
    center_on_parent(win, parent)
    win.grab_set()
    win.focus_set()