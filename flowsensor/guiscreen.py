"""GuiScreen Class. """

# Tkinter
import tkinter as tk


class MainApplication(tk.Tk):
  def __init__(self,tasks=None):
    """Initial function class"""

    super().__init__()

    self.FONT_NUMBER = ("Garamond", 44,'bold')

    self.get_screen_properties()
    self.get_screen_frame()
    self.get_screen_label()
    


  def get_screen_properties(self):
    """Get screen properties of the screen. """

    self.title("Deica || Flow Sensor")
    self.geometry("800x480")
    self.resizable(0,0)


  def get_screen_label(self):


    self.label1 = tk.Label(self.frame1,text="Hello wordl",font=("Garamond", 44,'bold'),justify='center',)
    self.label1.pack(fill='both',side='left')
    self.label1['text']="10.0 Mpa"

    self.label2 = tk.Label(self.frame1,text="Hello wordl",font=("Garamond", 44,'bold'),justify='center',)
    self.label2.pack(fill='both',side='left')
    self.label2['text']="10.0 Mpa"

    self.label2 = tk.Label(self.frame1,text="Hello wordl",font=self.FONT_NUMBER,justify='center',)
    self.label2.pack(fill='both',side='left')
    self.label2['text']="10.0 Mpa"


  def get_screen_frame(self):
    """Get screen frame"""

    self.frame = tk.Frame(master=self, width=500, height=500, bg='black',padx=1,pady=4)
    self.frame.pack()
    self.frame.pack_propagate(0)
    self.frame.pack(fill=tk.BOTH, expand=1)

    self.frame1 = tk.Frame(master=self.frame,width=900,height=600,bg='white')
    self.frame1.pack_propagate(0)
    self.frame1.pack(fill=tk.BOTH, expand=1)
    self.frame1.pack(padx=50,pady=20)

  