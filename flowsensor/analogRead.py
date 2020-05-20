import time

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

# Hardware SPI configuration:
SPI_PORT = 1
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))


"""Funtions to convert the bit value to voltage
and then convert the voltage to pressure"""


def convertVoltage(bitValue, decimalPlaces=3):
    voltage = ((bitValue * 3.3) / float(1023))
    voltage = round(voltage, decimalPlaces)
    return voltage


def convertPressure(voltage, decimalPlaces=4):
    # - 0.103
    pressure = ((voltage * 1.2) / 3.3)
    pressure = round(pressure, decimalPlaces)
    return pressure


print('Reading values, press Ctrl-C to quit...')
print('')

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

    print('|Sensor| Bits | Voltaje |  Presion  |')
    print('|  1   | {:^4} | {:^5} V |{:^7} MPa|'.format(
                                            sensor1Data,
                                            sensor1Voltage,
                                            pressure1
                                        ))
    print('|  2   | {:^4} | {:^5} V |{:^7} MPa|'.format(
                                            sensor2Data,
                                            sensor2Voltage,
                                            pressure2
                                        ))
    print('|  3   | {:^4} | {:^5} V |{:^7} MPa|'.format(
                                            sensor3Data,
                                            sensor3Voltage,
                                            pressure3
                                        ))
    print('|  4   | {:^4} | {:^5} V |{:^7} MPa|'.format(
                                            sensor4Data,
                                            sensor4Voltage,
                                            pressure4
                                        ))
    print('-' * 36)

    time.sleep(0.5)
