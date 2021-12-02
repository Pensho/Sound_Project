import sys
if sys.version_info[0] == 3:
    import tkinter as tk
else:
    import Tkinter as tk

class UIManager:
    window = tk.Tk()

    def __init__(self, windowName):
        self.window.winfo_toplevel().title(windowName)
        self.window.geometry("1290x720")
        self.window.configure(bg="#333333")

    def start(self):
        self.window.mainloop()
