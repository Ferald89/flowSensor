"""GuiScreen Class. """

# Tkinter
import tkinter as tk


class MainApplication(tk.Tk):
  def __init__(self,tasks=None):
    super().__init__()
    self.get_screen_properties()
    self.get_screen_frame()

  def get_screen_properties(self):
    """Get screen properties of the screen. """
    self.title("Deica||Flow Sensor")
    self.geometry("1000x700")
    self.resizable(0, 0)

  def get_screen_frame(self):
    """Get screen frame"""
    self.back = tk.Frame(master=self, width=500, height=500, bg='black')
    self.back.pack_propagate(0)
    self.back.pack(fill=tk.BOTH, expand=1)

  