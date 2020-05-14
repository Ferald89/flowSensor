"""GuiScreen Class. """

# Tkinter
import tkinter as tk


class MainApplication(tk.Tk):
  def __init__(self,tasks=None):
    """Initial function class"""

    super().__init__()

    self.FONT_NUMBER = (
      "Helvetica",
       32,
       'bold'
       )
    self.COLORS={
      'INK':'#062F4F',
      'EMBERS':'#B82601',
      'BLACK' :'#000000',
      'POSY' :'#813772'
    }
    self.SIZE_DATA ={
      'height':5,
      'width' :17
    }

    self.get_screen_properties()
    self.get_screen_frame()
    self.get_screen_label()
    


  def get_screen_properties(self):
    """Get screen properties of the screen. """
    
    
    self.title("Pressure Sensors || DEICA Automatismos S.A. de C.V.")
    self.geometry("800x480")
    self.resizable(0,0)


  def get_screen_label(self):
    """Get srcreen_label"""

    self.label1 = tk.Label(
      self.frame1,
      font=self.FONT_NUMBER,
      justify='center',
      bg=self.COLORS['BLACK'],
      borderwidth=1, 
      relief="groove",
      height = self.SIZE_DATA['height'],
      width  = self.SIZE_DATA['width'] 
      )
    self.label1['text']="0.044 Mpa"
    self.label1.grid(column=1,row=1)
  
    self.label2 = tk.Label(
      self.frame1,
      font=self.FONT_NUMBER,
      justify='center',
      bg=self.COLORS['BLACK'],
            borderwidth=1, 
      relief="groove",
      fg=self.COLORS['POSY'],
      height = self.SIZE_DATA['height'],
      width  = self.SIZE_DATA['width'] 
      )
    self.label2['text']="0.4444 Mpa"
    self.label2.grid(column=1,row=2)

    self.label3 = tk.Label(
      self.frame1,
      font=self.FONT_NUMBER,
      justify='center',
      bg=self.COLORS['BLACK'],
            borderwidth=1, 
      relief="groove",
      height = self.SIZE_DATA['height'],
      width  = self.SIZE_DATA['width'] 
      )
    self.label3['text']="0.444 Mpa"
    self.label3.grid(column=2,row=1)

    self.label4 = tk.Label(
      self.frame1,
      font=self.FONT_NUMBER,
      justify='center',
      bg=self.COLORS['BLACK'],
            borderwidth=1, 
      relief="groove",
      height = self.SIZE_DATA['height'],
      width  = self.SIZE_DATA['width'] 
      )
    self.label4['text']="0.444 Mpa"
    self.label4.grid(column=2,row=2)

  def get_screen_frame(self):
    """Get screen frame"""

    self.frame = tk.Frame(master=self, width=500, height=500, bg='black',padx=0,pady=0)
    self.frame.pack()
    self.frame.pack_propagate(0)
    self.frame.pack(fill=tk.BOTH, expand=1)

    self.frame1 = tk.Frame(master=self.frame,width=900,height=600,bg='gray')
    # self.frame1.pack_propagate(0)
    # self.frame1.pack(fill=tk.BOTH, expand=1)
    # self.frame1.pack(padx=10,pady=10)
    self.frame1.grid_propagate(0)
    self.frame1.grid_location(0,0)
    self.frame1.grid(column=0,row=0,columnspan=2,rowspan=2)

  
