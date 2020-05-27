"""Action class ."""


class Action:
    """class that check a value and return a boolean data and also
    do a action"""
    def __init__(self, value, value_Max, value_Min):
        self.value = value
        self.value_Max = value_Max
        self.value_Min = value_Min

    def judge(self):
        if (self.value > self.value_Min) & (self.value < self.value_Max):
            return 'green'
        return 'red'

    def judge_boolean(self):
        if (self.value > self.value_Min) & (self.value < self.value_Max):
            return True
        return False
