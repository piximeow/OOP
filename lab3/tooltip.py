import tkinter as tk


class ToolTip:
    def __init__(self, widget, text, delay=500):
        self._widget = widget
        self._text = text
        self._delay = delay
        self._after_id = None
        self._window = None
        widget.bind("<Enter>", self._on_enter, add="+")
        widget.bind("<Leave>", self._on_leave, add="+")
        widget.bind("<ButtonPress>", self._on_leave, add="+")

    def _on_enter(self, _event):
        self._after_id = self._widget.after(self._delay, self._show)

    def _show(self):
        x = self._widget.winfo_rootx() + 10
        y = self._widget.winfo_rooty() + self._widget.winfo_height() + 4
        self._window = tk.Toplevel(self._widget)
        self._window.wm_overrideredirect(True)
        self._window.wm_geometry(f"+{x}+{y}")
        tk.Label(self._window, text=self._text, background="#ffffe0",
                 relief="solid", borderwidth=1, padx=4, pady=2).pack()

    def _on_leave(self, _event):
        if self._after_id is not None:
            self._widget.after_cancel(self._after_id)
            self._after_id = None
        if self._window is not None:
            self._window.destroy()
            self._window = None