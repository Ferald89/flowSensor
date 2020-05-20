#Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

#Import GPIO library to manage GPIO from python
import RPi.GPIO as GPIO

#Utilities
import time

#GPIO pin mode configuration
GPIO.setmode(GPIO.BOARD)

#GPIO output pins definition
DOUT_S1 = 11
DOUT_S2 = 13
DOUT_S3 = 15
DOUT_S4 = 16

#GPIO I/O setup configuration
GPIO.setup(DOUT_S1, GPIO.OUT)
GPIO.setup(DOUT_S2, GPIO.OUT)
GPIO.setup(DOUT_S3, GPIO.OUT)
GPIO.setup(DOUT_S4, GPIO.OUT)

# Hardware SPI configuration
SPI_PORT   = 1
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

#Funtions to convert the bit value to voltage and then convert the voltage t pressure 
def convertVoltage(bitValue, decimalPlaces = 3):
    voltage = ((bitValue * 3.3) / float(1023))
    voltage = round(voltage, decimalPlaces)
    return voltage

def convertPressure(voltage, decimalPlaces = 4):
    pressure = ((voltage * 1.2) / 3.3) #- 0.103
    pressure = round(pressure, decimalPlaces)
    return pressure

#Main

print('Reading values, press Ctrl-C to quit...')
print('')

try:
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

        #Pressure limit ranges to turn on/off the outputs

        if 0.5 < pressure1 < 1.0:
            GPIO.output(DOUT_S1, True)
        else:
            GPIO.output(DOUT_S1, False)

        if 0.5 < pressure2 < 1.0:
            GPIO.output(DOUT_S2, True)
        else:
            GPIO.output(DOUT_S2, False)

        if 0.5 < pressure3 < 1.0:
            GPIO.output(DOUT_S3, True)
        else:
            GPIO.output(DOUT_S3, False)

        if 0.5 < pressure4 < 1.0:
            GPIO.output(DOUT_S4, True)
        else:
            GPIO.output(DOUT_S4, False)

       #Use input to check the state of outputs. Returns 1 if output high

        if GPIO.input(DOUT_S1) == 1:
            DOUT1_STATUS = 'ON'
        else:
            DOUT1_STATUS = 'OFF'

        if GPIO.input(DOUT_S2) == 1:
            DOUT2_STATUS = 'ON'
        else:
            DOUT2_STATUS = 'OFF'

        if GPIO.input(DOUT_S3) == 1:
            DOUT3_STATUS = 'ON'
        else:
            DOUT3_STATUS = 'OFF'

        if GPIO.input(DOUT_S4) == 1:
            DOUT4_STATUS = 'ON'
        else:
            DOUT4_STATUS = 'OFF'

        print('|Sensor| Bits | Voltaje |  Presion  | OUTPUT PIN | STATUS |')
        print('|  1   | {:^4} | {:^5} V |{:^7} MPa| {:^2}     |{:^4}|'.format(sensor1Data, sensor1Voltage, pressure1, DOUT_S1, DOUT1_STATUS))
        print('|  2   | {:^4} | {:^5} V |{:^7} MPa|'.format(sensor2Data, sensor2Voltage, pressure2))
        print('|  3   | {:^4} | {:^5} V |{:^7} MPa|'.format(sensor3Data, sensor3Voltage, pressure3))
        print('|  4   | {:^4} | {:^5} V |{:^7} MPa|'.format(sensor4Data, sensor4Voltage, pressure4))
        print('-' * 36)

        time.sleep(0.5)

except:
    GPIO.cleanup()
