""" Main Screen Program"""
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

SPI_PORT   = 1
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
 
def convertVoltage(bitValue, decimalPlaces = 3):
    voltage = ((bitValue * 3.3) / float(1023))
    voltage = round(voltage, decimalPlaces)
    return voltage

def convertPressure(voltage, decimalPlaces = 4):
    pressure = ((voltage * 1.2) / 3.3) - 0.103
    pressure = round(pressure, decimalPlaces)
    return pressure

# local
from guiscreen import MainApplication

def main():
  """Es el control de la pantalla y la configuración y arranque de la misma"""

  #Inizialisamos el tk
  root = MainApplication()
  # root.label1['text']="15.0 Mpa"
  root.mainloop()

if __name__ == "__main__":
  """Empieza a ejecutar la primera linea de codigo"""
  main()
  
  while True:
    sensor1Data = mcp.read_adc(0)
    sensor2Data = mcp.read_adc(1)
    sensor3Data = mcp.read_adc(2)
    sensor4Data = mcp.read_adc(3)
    
    sensor1Voltage = convertVoltage(sensor1Data)
    sensor2Voltage = convertVoltage(sensor2Data)
    sensor3Voltage = convertVoltage(sensor3Data)
    sensor4Voltage = convertVoltage(sensor4Data)
    
    pressure1 = convertPressure(sensor1Voltage)
    pressure2 = convertPressure(sensor2Voltage)
    pressure3 = convertPressure(sensor3Voltage)
    pressure4 = convertPressure(sensor4Voltage)
    
    if pressure1 < 0:
        pressure1 = 0
    else:
        pressure1 = pressure1
        
    if pressure2 < 0:
        pressure2 = 0
    else:
        pressure2 = pressure2
    
    if pressure3 < 0:
        pressure3 = 0
    else:
        pressure3 = pressure3
        
    if pressure4 < 0:
        pressure4 = 0
    else:
        pressure4 = pressure4