# Tkinter
import tkinter as tk


class MainApplication(tk.Tk):
  def __init__(self,tasks=None):
    super().__init__()

    self.title("Deica||Flow Sensor")
    self.geometry("1000x700")
    self.resizable(0, 0)

    self.back = tk.Frame(master=self, width=500, height=500, bg='black')
    self.back.pack_propagate(0)
    self.back.pack(fill=tk.BOTH, expand=1)


    #Create popupmenu
    self.menu_bar = tk.Menu(self)
    self.popup_menu = tk.Menu(self.menu_bar,tearoff=0)
    self.popup_menu.add_separator()
    
    self.config(menu=self.menu_bar)





def main():
  """Es el control de la pantalla y la configuración y arranque de la misma"""

  #Inizialisamos el tk
  root = MainApplication()
  root.mainloop()

if __name__ == "__main__":
  """Empieza a ejecutar la primera linea de codigo"""
  main()