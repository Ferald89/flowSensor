""" Main Screen Program"""

# local
from guiscreen import MainApplication
from flowsensor import FlowSensor

def main():
  """Es el control de la pantalla y la configuración y arranque de la misma"""
  # Instanciamos FlowSensor

  sensorFlow1 = FlowSensor(0)
  sensorFlow2 = FlowSensor(1)
  sensorFlow3 = FlowSensor(2)
  sensorFlow4 = FlowSensor(3)

  #Inizialisamos el tk
  root = MainApplication()
  # root.label1['text']="15.0 Mpa"
  #root.mainloop()

  while True:
      sensorFlow1.updateValue()
      sensorFlow2.updateValue()
      sensorFlow3.updateValue()
      sensorFlow4.updateValue()

      print(sensorFlow1.pressure)
      print(sensorFlow2.pressure)
      print(sensorFlow3.pressure)
      print(sensorFlow4.pressure)

if __name__ == "__main__":
  """Empieza a ejecutar la primera linea de codigo"""
  main()
