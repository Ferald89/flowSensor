""" Main Screen Program"""

# Local
from guiscreen import MainApplication
# from flowsensor import FlowSensor, GpioOut
from action import Action
from setting import Setting

# Utilities
import time


def main():
    """Es el control de la pantalla y la
    configuración y arranque de la misma"""

    # Instanciamos FlowSensor
    # sensorFlow1 = FlowSensor(0)
    # sensorFlow2 = FlowSensor(1)
    # sensorFlow3 = FlowSensor(2)
    # sensorFlow4 = FlowSensor(3)

    sett = Setting()
    actions = []
    outs = []

    # Pines Salida

    DOUT_S1 = 11
    DOUT_S2 = 13
    DOUT_S3 = 15
    DOUT_S4 = 16

    settings = sett.settings

    # Inicializamos el tk
    root = MainApplication()

    for setting in settings:
        actions.append(Action(
                        0.0,
                        float(setting.Max),
                        float(setting.Min)
                    ))

    # GpioOut
    # outs.append(GpioOut(DOUT_S1))
    # outs.append(GpioOut(DOUT_S2))
    # outs.append(GpioOut(DOUT_S3))
    # outs.append(GpioOut(DOUT_S4))

    while True:

        # Update Setting
        settings = sett.read()

        for sens in range(3):
            actions[sens].value_Max = float(settings[sens].Max)
            actions[sens].value_Min = float(settings[sens].Min)

        # sensorFlow1.updateValue()
        # sensorFlow2.updateValue()
        # sensorFlow3.updateValue()
        # sensorFlow4.updateValue()

        # root.label1['text'] = "FP 1 \n {:.2f} MPa".format(sensorFlow1.pressure)
        # root.label2['text'] = "FP 2 \n {:.2f} MPa".format(sensorFlow2.pressure)
        # root.label3['text'] = "FP 3 \n {:.2f} MPa".format(sensorFlow3.pressure)
        # root.label4['text'] = "FP 4 \n {:.2f} MPa".format(sensorFlow4.pressure)

        # actions[0].value = sensorFlow1.pressure
        # actions[1].value = sensorFlow2.pressure
        # actions[2].value = sensorFlow3.pressure
        # actions[3].value = sensorFlow4.pressure

        # Actions

        root.label1['fg'] = actions[0].judge()
        root.label2['fg'] = actions[1].judge()
        root.label3['fg'] = actions[2].judge()
        root.label4['fg'] = actions[3].judge()

        for idx, out in enumerate(outs):
            if actions[idx].judge_boolean():
                out.turnOn()
            else:
                out.turnOff()

        root.update_idletasks()
        root.update()
        time.sleep(0.1)


if __name__ == "__main__":
    """Empieza a ejecutar la primera linea de codigo"""
    main()
