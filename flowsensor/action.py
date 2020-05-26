"""Action class ."""


class Action:
    """class that check a value and return a boolean data and also
    do a action"""
    def __init__(self, value, value_setting, value_action):
        self.value = value
        self.value_setting = value_setting
        self.value_action = value_action

    def judge(self):
        if (self.value > 10.0) & (self.value < 25.0):
            return 'green'
        return 'red'
