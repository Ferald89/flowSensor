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
    test = 0.80
    sett = Setting()
    actions = []
    # sensors = []

    # sensors.append(SensorSetting(1, 50.0, 10.0))
    # sensors.append(SensorSetting(2, 80.0, 50.0))
    # sensors.append(SensorSetting(3, 90.0, 10.0))
    # setting.update_settings(sensors)
    settings = sett.read()

    # Inicializamos el tk
    root = MainApplication()

    for setting in settings:
        actions.append(Action(
                        0.0,
                        float(setting.Max),
                        float(setting.Min)
                    ))

    while True:

        # Update Setting
        settings = sett.read()

        for sens in range(3):
            actions[sens].value_Max = float(settings[sens].Max)
            actions[sens].value_Min = float(settings[sens].Min)

        sensorFlow1.updateValue()
        sensorFlow2.updateValue()
        sensorFlow3.updateValue()
        sensorFlow4.updateValue()

        root.label1['text'] = "FP 1 \n {:.2f} MPa".format(sensorFlow1.pressure)
        root.label2['text'] = "FP 2 \n {:.2f} MPa".format(sensorFlow2.pressure)
        root.label3['text'] = "FP 3 \n {:.2f} MPa".format(sensorFlow3.pressure)
        root.label4['text'] = "FP 4 \n {:.2f} MPa".format(sensorFlow4.pressure)

        actions[0].value = sensorFlow1.pressure
        actions[1].value = sensorFlow2.pressure
        actions[2].value = sensorFlow3.pressure
        actions[3].value = sensorFlow4.pressure

        # actions[0].value = test

        root.label1['fg'] = actions[0].judge()
        root.label2['fg'] = actions[1].judge()
        root.label3['fg'] = actions[2].judge()
        root.label4['fg'] = actions[3].judge()

        root.label1['text'] = "{:^} MPa".format(test)
        root.update_idletasks()
        root.update()
        time.sleep(0.1)


if __name__ == "__main__":
    """Empieza a ejecutar la primera linea de codigo"""
    main()
