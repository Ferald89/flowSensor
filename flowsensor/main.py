""" Main Screen Program"""

# local
from guiscreen import MainApplication
from flowsensor import FlowSensor

# utilities
import time

def main():
  """Es el control de la pantalla y la configuración y arranque de la misma"""
  #Instanciamos FlowSensor

  sensorFlow1 = FlowSensor(0)
  sensorFlow2 = FlowSensor(1)
  sensorFlow3 = FlowSensor(2)
  sensorFlow4 = FlowSensor(3)

  #Inicializamos el tk
  root = MainApplication()

  

  while True:

      sensorFlow1.updateValue()
      sensorFlow2.updateValue()
      sensorFlow3.updateValue()
      sensorFlow4.updateValue()

      root.label1['text']="{:^} MPa".format(sensorFlow1.pressure)
      root.label2['text']="{:^} MPa".format(sensorFlow2.pressure)
      root.label3['text']="{:^} MPa".format(sensorFlow3.pressure)
      root.label4['text']="{:^} MPa".format(sensorFlow4.pressure)

      #root.mainloop()
      root.update_idletasks()
      root.update()

      # print(sensorFlow1.pressure)
      # print(sensorFlow2.pressure)
      # print(sensorFlow3.pressure)
      # print(sensorFlow4.pressure)
      time.sleep(0.5)

if __name__ == "__main__":
  """Empieza a ejecutar la primera linea de codigo"""
  main()
