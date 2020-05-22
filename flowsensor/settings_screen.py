"""Screen Settings Class. """

# Tkinter
import tkinter as tk


class SettingScreen(tk.Tk):
    def __init__(self, task=None):
        self.windows = tk.Toplevel()
        self.windows.geometry("800x480")
