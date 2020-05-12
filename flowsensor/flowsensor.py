""" Main Screen Program"""

# local
from guiscreen import MainApplication

def main():
  """Es el control de la pantalla y la configuración y arranque de la misma"""

  #Inizialisamos el tk
  root = MainApplication()
  root.mainloop()

if __name__ == "__main__":
  """Empieza a ejecutar la primera linea de codigo"""
  main()