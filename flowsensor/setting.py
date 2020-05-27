"""Settings class. """

# Utilities
import csv


class Setting:
    """ Here read and write settings in CSV File"""

    def __init__(self):
        self.auth = "settings.csv"
        self.settings = []

    def save(self):
        with open(self.auth, 'w') as file:
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

    def read(self):
        self.settings.clear()
        with open(self.auth, 'r') as file:
            reader = csv.reader(file)
            for idx, row in enumerate(reader):
                if idx == 0:
                    continue
                sensor = SensorSetting(idx, row[1], row[2])
                self.settings.append(sensor)
            self.save()
            return self.settings

    def default_settings(self):
        self.settings.clear()
        for s in range(3):
            sensor = SensorSetting(s+1, 999.9, 0)
            self.settings.append(sensor)
            print(s)
        self.save()

    def update_settings(self, Sensors):
        """Update owner settings of the instance"""
        self.settings.clear()
        for sensor in Sensors:
            self.settings.append(sensor)
        self.save()

    def __str__(self):
        return 'Setting {}'.format(self.settings)

    def __repr__(self):
        return 'Setting {}'.format(self.settings)


class SensorSetting:
    def __init__(self, Numero, Max, Min):
        self.Numero = Numero
        self.Max = Max
        self.Min = Min

    def __repr__(self):
        return 'SensorSetting Sensor {}, Max {}, Min{}'.format(
                            self.Numero,
                            self.Max,
                            self.Min
                        )
