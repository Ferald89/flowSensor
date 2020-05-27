"""Flow Sensor Class. """

# Adafruit
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

# GPIO
import RPi.GPIO as GPIO


class FlowSensor():

    def __init__(self, chanel):

        self.CHANEL = chanel
        self.SPI_PORT = 1
        self.SPI_DEVICE = 0
        self.mcp = Adafruit_MCP3008.MCP3008(
                              spi=SPI.SpiDev(
                                  self.SPI_PORT,
                                  self.SPI_DEVICE
                              ))

        self.RAW = self.mcp.read_adc(self.CHANEL)

        self.voltaje = self.convertVoltage(self.RAW)

        self.pressure = self.convertPressure(self.voltaje)

    def updateValue(self):
        self.RAW = self.mcp.read_adc(self.CHANEL)

        self.voltaje = self.convertVoltage(self.RAW)

        self.pressure = self.convertPressure(self.voltaje)

    def convertVoltage(self, bitValue, decimalPlaces=3):
        voltage = ((bitValue * 3.3) / float(1023))
        voltage = round(voltage, decimalPlaces)
        return voltage

    def convertPressure(self, voltage, decimalPlaces=4):
        pressure = ((voltage * 1.2) / 3.3)
        pressure = round(pressure, decimalPlaces)
        if pressure < 0:
            pressure = 0
        else:
            pressure = pressure
        return pressure


class GpioOut:

    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BOARD)

        # GPIO output pins definition

        # GPIO I/O setup configuration
        GPIO.setup(self.pin, GPIO.OUT)

    def turnOff(self):
        GPIO.output(self.pin, False)

    def turnOn(self):
        GPIO.output(self.pin, True)
