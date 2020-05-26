"""Settings class. """

# Utilities
import csv


class Setting:
    """ Here read and write settings in HDD"""

    def __init__(self):
        self.settings = []

    def save(self):
        with open('settings.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow((
                        'Sensor',
                        'Máximo',
                        'Minimo'
                    ))
            for sensor in self.settings:
                writer.writerow((
                        sensor.Numero,
                        sensor.Max,
                        sensor.Min
                ))

    def default_settings(self):
        for s in range(3):
            sensor = SensorSetting(s+1, 0, 0)
            self.settings.append(sensor)
            print(s)

    def __str__(self):
        return 'Setting {}'.format(self.settings)


class SensorSetting:
    def __init__(self, Numero, Max, Min):
        self.Numero = Numero
        self.Max = Max
        self.Min = Min
