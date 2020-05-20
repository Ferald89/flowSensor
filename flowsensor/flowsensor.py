"""Flow Sensor Class. """

# Adafruit
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008


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
