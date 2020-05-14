"""GuiScreen Class. """

# Tkinter
import tkinter as tk


class MainApplication(tk.Tk):
  def __init__(self,tasks=None):
    """Initial function class"""

    super().__init__()

    self.FONT_NUMBER = (
      "Helvetica",
       33,
       'bold'
       )
    self.COLORS={
      'INK':'#062F4F',
      'EMBERS':'#B82601',
      'BLACK' :'#000000',
      'POSY' :'#813772'

    }

    self.get_screen_properties()
    self.get_screen_frame()
    self.get_screen_label()
    


  def get_screen_properties(self):
    """Get screen properties of the screen. """
    
    self.iconbitmap('../statics/pressure_4667.ico')
    self.title("Pressure Sensors || DEICA Automatismos S.A. de C.V.")
    self.geometry("800x480")
    self.resizable(0,0)


  def get_screen_label(self):


    self.label1 = tk.Label(
      self.frame1,
      font=self.FONT_NUMBER,
      justify='center',
      bg=self.COLORS['INK'],
      borderwidth=2, 
      relief="groove"
      )
    self.label1['text']="10.0 Mpa"
    self.label1.pack(fill='both',side='left')
  
    self.label2 = tk.Label(
      self.frame1,
      font=self.FONT_NUMBER,
      justify='center',
      bg=self.COLORS['INK'],
            borderwidth=2, 
      relief="groove"
      )
    self.label2['text']="10.0 Mpa"
    self.label2.pack(fill='both',side='left')

    self.label3 = tk.Label(
      self.frame1,
      font=self.FONT_NUMBER,
      justify='center',
      bg=self.COLORS['INK'],
            borderwidth=2, 
      relief="groove"
      )
    self.label3['text']="10.0 Mpa"
    self.label3.pack(fill='both',side='left')

    self.label4 = tk.Label(
      self.frame1,
      font=self.FONT_NUMBER,
      justify='center',
      bg=self.COLORS['INK'],
            borderwidth=2, 
      relief="groove"
      )
    self.label4['text']="10.0 Mpa"
    self.label4.pack(fill='both',side='left')

  def get_screen_frame(self):
    """Get screen frame"""

    self.frame = tk.Frame(master=self, width=500, height=500, bg='black',padx=1,pady=4)
    self.frame.pack()
    self.frame.pack_propagate(0)
    self.frame.pack(fill=tk.BOTH, expand=1)

    self.frame1 = tk.Frame(master=self.frame,width=900,height=600,bg='gray')
    self.frame1.pack_propagate(0)
    self.frame1.pack(fill=tk.BOTH, expand=1)
    self.frame1.pack(padx=20,pady=20)

  
