import time

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008


# Software SPI configuration:
#CLK  = 23
#MISO = 21
#MOSI = 19
#CS   = 24
#mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))


#Funtions to convert the bit value to voltage and then convert the voltage to pressure 
def convertVoltage(bitValue, decimalPlaces = 3):
  voltage = ((bitValue * 3.3) / float(1023)) #- 1.362       #Formula to convert the bit value to voltage
  voltage = round(voltage, decimalPlaces)                   #Round the data to two decimals
  return voltage                                            #Return the value in terms of voltage

def convertPressure(voltage, decimalPlaces = 3):
  pressure = ((voltage * 1.2) / 3.3) #+ 0.0023              #Formula to convert the voltage to pressure
  pressure = round(pressure, decimalPlaces)                 #Round the data to two decimals
  return pressure                                           #Return the value in terms of pressure

#Reads the value all the time, needs to be modified according the application
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
  
  print("FP1: {}bits --> {}V --> {}MPa".format(sensor1Data, sensor1Voltage, pressure1))
  print("FP2: {}bits --> {}V --> {}MPa".format(sensor2Data, sensor2Voltage, pressure2))
  print("FP3: {}bits --> {}V --> {}MPa".format(sensor3Data, sensor3Voltage, pressure3))
  print("FP4: {}bits --> {}V --> {}MPa".format(sensor4Data, sensor4Voltage, pressure4))
  print('-' * 33)
  
  time.sleep(0.5)
