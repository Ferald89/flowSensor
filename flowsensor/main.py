""" Main Screen Program"""

# Local
from guiscreen import MainApplication
from flowsensor import FlowSensor
from action import Action
from setting import Setting, SensorSetting

# Utilities
import time


def main():
    """Es el control de la pantalla y la
    configuración y arranque de la misma"""

    # Instanciamos FlowSensor
    sensorFlow1 = FlowSensor(0)
    sensorFlow2 = FlowSensor(1)
    sensorFlow3 = FlowSensor(2)
    sensorFlow4 = FlowSensor(3)
    test = 15.5
    setting = Setting()
    setting.read()
    # sensors = []

    # sensors.append(SensorSetting(1, 50.0, 10.0))
    # sensors.append(SensorSetting(2, 80.0, 50.0))
    # sensors.append(SensorSetting(3, 90.0, 10.0))
    # setting.update_settings(sensors)
    settings = setting.read()

    # Inicializamos el tk
    root = MainApplication()

    while True:
        sensorFlow1.updateValue()
        sensorFlow2.updateValue()
        sensorFlow3.updateValue()
        sensorFlow4.updateValue()

        root.label1['text'] = "FP 1 \n {:.2f} MPa".format(sensorFlow1.pressure)
        root.label2['text'] = "{:.2f} MPa".format(sensorFlow2.pressure)
        root.label3['text'] = "{:.2f} MPa".format(sensorFlow3.pressure)
        root.label4['text'] = "{:.2f} MPa".format(sensorFlow4.pressure)

        actions = (Action(
                        sensorFlow1.pressure,
                        float(settings[0].Max),
                        float(settings[0].Min)
                    ))

        root.label1['fg'] = actions.judge()
        # root.label1['text'] = "{:^} MPa".format(test)
        root.update_idletasks()
        root.update()
        time.sleep(0.1)


if __name__ == "__main__":
    """Empieza a ejecutar la primera linea de codigo"""
    main()
