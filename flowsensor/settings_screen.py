"""Screen Settings Class. """

# Local
from setting import Setting

# Tkinter
import tkinter as tk


class SettingScreen:
    """setting frame. """

    def __init__(self, windows):

        self.settings = Setting()

        self.FONT_NUMBER = (
          "Helvetica",
          22,
          'bold'
          )

        self.SIZE_DATA = {
                      'height': 5,
                      'width': 10,
                      'pady': 10
        }

        self.validation = windows.register(self.only_numbers)

        self.set_frame(windows)
        self.set_fonts()
        self.set_label()
        self.set_entry()
        self.set_entry_default()
        self.set_buttom()

    def set_entry_default(self):
        settings = self.settings.read()
        try:
            self.entry1.insert(tk.END, settings[0].Max)
            self.entry2.insert(tk.END, settings[0].Min)
            self.entry3.insert(tk.END, settings[1].Max)
            self.entry4.insert(tk.END, settings[1].Min)
            self.entry5.insert(tk.END, settings[2].Max)
            self.entry6.insert(tk.END, settings[2].Min)
            self.entry7.insert(tk.END, settings[3].Max)
            self.entry8.insert(tk.END, settings[3].Min)
        except :
            self.settings.default_settings()
            self.set_entry_default()

    def only_numbers(self, char):
        try:
            float(char)
            return True
        except:
            return False

    def set_fonts(self):
        self.fonts_title2 = {
            'master': self.frame,
            'fg': 'black',
            'font': ("Helvetica", 12, 'bold'),
            'width': 43,
            'height': 1
        }
        self.grid_title2 = {
            'padx': 4,
            'pady': 1
        }
        self.fonts_title3 = {
            'master': self.frame,
            'fg': 'black',
            'font': ("Helvetica", 20, 'bold'),
            'width': 10,
            'height': 1
        }
        self.grid_title3 = {
            'padx': 1,
            'pady': 2
        }
        self.fonts_buttom1 = {
            'master': self.frame,
            'fg': 'black',
            'font': ('Helvetica', 12, 'bold'),
            'width': 20,
            'height': 2,
        }
        self.grid_buttom1 = {
            'padx': 1,
            'pady': 1
        }

    def set_frame(self, windows):
        self.frame = tk.Frame(
                            master=windows,
                            width=800,
                            height=480,
                            bg='gray'
                    )
        self.frame.grid_propagate(0)
        self.frame.grid_location(0, 0)
        self.frame.grid(
                    column=0,
                    row=0,
                    columnspan=8,
                    rowspan=9,
                )

    def set_label(self):
        self.label1 = tk.Label(
                        self.frame,
                        font=("Helvetica", 30, 'bold'),
                        fg="white",
                        bd=2,
                        width=35,
                        height=1
                    )
        self.label1['text'] = "AJUSTES"
        self.label1.grid(
                row=1,
                column=1,
                columnspan=8,
                rowspan=2,
                sticky="nesw",
                padx=5, pady=5
            )

        self.label2 = tk.Label(
                        self.fonts_title2['master'],
                        fg=self.fonts_title2['fg'],
                        font=self.fonts_title2['font'],
                        width=self.fonts_title2['width'],
                        height=self.fonts_title2['height']
                    )
        self.label2['text'] = "SENSOR 1"
        self.label2.grid(
                    column=1,
                    row=3,
                    columnspan=2,
                    padx=self.grid_title2['padx'],
                    pady=self.grid_title2['pady']
                )

        self.label3 = tk.Label(
                        self.fonts_title2['master'],
                        fg=self.fonts_title2['fg'],
                        font=self.fonts_title2['font'],
                        width=self.fonts_title2['width'],
                        height=self.fonts_title2['height']
                    )
        self.label3['text'] = "SENSOR 2"
        self.label3.grid(
                    column=3,
                    row=3,
                    columnspan=2,
                    padx=self.grid_title2['padx'],
                    pady=self.grid_title2['pady']
                )

        self.label4 = tk.Label(
                        self.fonts_title2['master'],
                        fg=self.fonts_title2['fg'],
                        font=self.fonts_title2['font'],
                        width=self.fonts_title2['width'],
                        height=self.fonts_title2['height']
                    )
        self.label4['text'] = "SENSOR 3"
        self.label4.grid(
                    column=1,
                    row=6,
                    columnspan=2,
                    padx=self.grid_title2['padx'],
                    pady=self.grid_title2['pady']
                )

        self.label5 = tk.Label(
                        self.fonts_title2['master'],
                        fg=self.fonts_title2['fg'],
                        font=self.fonts_title2['font'],
                        width=self.fonts_title2['width'],
                        height=self.fonts_title2['height']
                    )
        self.label5['text'] = "SENSOR 4"
        self.label5.grid(
                    column=3,
                    row=6,
                    columnspan=2,
                    padx=self.grid_title2['padx'],
                    pady=self.grid_title2['pady']
                )

        self.label6 = tk.Label(
                        self.fonts_title3['master'],
                        fg=self.fonts_title3['fg'],
                        font=self.fonts_title3['font'],
                        width=self.fonts_title3['width'],
                        height=self.fonts_title3['height']
        )
        self.label6['text'] = "Máximo"
        self.label6.grid(
                    column=1,
                    row=4,
                    padx=self.grid_title3['padx'],
                    pady=self.grid_title3['pady']
                    )

        self.label7 = tk.Label(
                        self.fonts_title3['master'],
                        fg=self.fonts_title3['fg'],
                        font=self.fonts_title3['font'],
                        width=self.fonts_title3['width'],
                        height=self.fonts_title3['height']
        )
        self.label7['text'] = "Minimo"
        self.label7.grid(
                    column=1,
                    row=5,
                    padx=self.grid_title3['padx'],
                    pady=self.grid_title3['pady']
                    )

        self.label8 = tk.Label(
                        self.fonts_title3['master'],
                        fg=self.fonts_title3['fg'],
                        font=self.fonts_title3['font'],
                        width=self.fonts_title3['width'],
                        height=self.fonts_title3['height']
        )
        self.label8['text'] = "Máximo"
        self.label8.grid(
                    column=3,
                    row=4,
                    padx=self.grid_title3['padx'],
                    pady=self.grid_title3['pady']
                    )

        self.label9 = tk.Label(
                        self.fonts_title3['master'],
                        fg=self.fonts_title3['fg'],
                        font=self.fonts_title3['font'],
                        width=self.fonts_title3['width'],
                        height=self.fonts_title3['height']
        )
        self.label9['text'] = "Minimo"
        self.label9.grid(
                    column=3,
                    row=5,
                    padx=self.grid_title3['padx'],
                    pady=self.grid_title3['pady']
                    )

        self.label10 = tk.Label(
                        self.fonts_title3['master'],
                        fg=self.fonts_title3['fg'],
                        font=self.fonts_title3['font'],
                        width=self.fonts_title3['width'],
                        height=self.fonts_title3['height']
        )
        self.label10['text'] = "Máximo"
        self.label10.grid(
                    column=1,
                    row=7,
                    padx=self.grid_title3['padx'],
                    pady=self.grid_title3['pady']
                    )

        self.label11 = tk.Label(
                    self.fonts_title3['master'],
                    fg=self.fonts_title3['fg'],
                    font=self.fonts_title3['font'],
                    width=self.fonts_title3['width'],
                    height=self.fonts_title3['height']
        )
        self.label11['text'] = "Minimo"
        self.label11.grid(
                    column=1,
                    row=8,
                    padx=self.grid_title3['padx'],
                    pady=self.grid_title3['pady']
                    )

        self.label10 = tk.Label(
                        self.fonts_title3['master'],
                        fg=self.fonts_title3['fg'],
                        font=self.fonts_title3['font'],
                        width=self.fonts_title3['width'],
                        height=self.fonts_title3['height']
        )
        self.label10['text'] = "Máximo"
        self.label10.grid(
                    column=3,
                    row=7,
                    padx=self.grid_title3['padx'],
                    pady=self.grid_title3['pady']
                    )

        self.label11 = tk.Label(
                        self.fonts_title3['master'],
                        fg=self.fonts_title3['fg'],
                        font=self.fonts_title3['font'],
                        width=self.fonts_title3['width'],
                        height=self.fonts_title3['height']
        )
        self.label11['text'] = "Minimo"
        self.label11.grid(
                    column=3,
                    row=8,
                    padx=self.grid_title3['padx'],
                    pady=self.grid_title3['pady']
                    )

    def set_entry(self):
        self.entry1 = tk.Entry(
                        self.frame,
                        validate="key",
                        validatecommand=(self.validation, '%P'),
                        justify='center',
                        width=self.SIZE_DATA['width'],
                        font=self.FONT_NUMBER
                )
        self.entry1.grid(column=2, row=4, pady=self.SIZE_DATA['pady'])

        self.entry2 = tk.Entry(
                        self.frame,
                        validate='key',
                        validatecommand=(self.validation, '%P'),
                        justify='center',
                        width=self.SIZE_DATA['width'],
                        font=self.FONT_NUMBER
                )
        self.entry2.grid(column=2, row=5, pady=self.SIZE_DATA['pady'])

        self.entry3 = tk.Entry(
                        self.frame,
                        validate='key',
                        validatecommand=(self.validation, '%P'),
                        justify='center',
                        width=self.SIZE_DATA['width'],
                        font=self.FONT_NUMBER
                )
        self.entry3.grid(column=4, row=4, pady=self.SIZE_DATA['pady'])

        self.entry4 = tk.Entry(
                        self.frame,
                        validate='key',
                        validatecommand=(self.validation, '%P'),
                        justify='center',
                        width=self.SIZE_DATA['width'],
                        font=self.FONT_NUMBER
                )
        self.entry4.grid(column=4, row=5, pady=self.SIZE_DATA['pady'])

        self.entry5 = tk.Entry(
                        self.frame,
                        validate='key',
                        validatecommand=(self.validation, '%P'),
                        justify='center',
                        width=self.SIZE_DATA['width'],
                        font=self.FONT_NUMBER
                )
        self.entry5.grid(column=2, row=7, pady=self.SIZE_DATA['pady'])

        self.entry6 = tk.Entry(
                        self.frame,
                        validate='key',
                        validatecommand=(self.validation, '%P'),
                        justify='center',
                        width=self.SIZE_DATA['width'],
                        font=self.FONT_NUMBER
                )
        self.entry6.grid(column=2, row=8, pady=self.SIZE_DATA['pady'])

        self.entry7 = tk.Entry(
                        self.frame,
                        validate='key',
                        validatecommand=(self.validation, '%P'),
                        justify='center',
                        width=self.SIZE_DATA['width'],
                        font=self.FONT_NUMBER
                )
        self.entry7.grid(column=4, row=7, pady=self.SIZE_DATA['pady'])

        self.entry8 = tk.Entry(
                        self.frame,
                        validate='key',
                        validatecommand=(self.validation, '%P'),
                        justify='center',
                        width=self.SIZE_DATA['width'],
                        font=self.FONT_NUMBER
                )
        self.entry8.grid(column=4, row=8, pady=self.SIZE_DATA['pady'])

    def buttom_save(self):
        self.settings.settings[0].Max = self.entry1.get()
        self.settings.settings[0].Min = self.entry2.get()
        self.settings.settings[1].Max = self.entry3.get()
        self.settings.settings[1].Min = self.entry4.get()
        self.settings.settings[2].Max = self.entry5.get()
        self.settings.settings[2].Min = self.entry6.get()
        self.settings.settings[3].Max = self.entry7.get()
        self.settings.settings[3].Min = self.entry8.get()
        self.settings.save()

    def set_buttom(self):
        self.save = tk.Button(
                        self.fonts_buttom1['master'],
                        text="GUARDAR",
                        fg=self.fonts_buttom1['fg'],
                        font=self.fonts_buttom1['font'],
                        width=self.fonts_buttom1['width'],
                        height=self.fonts_buttom1['height'],
                        command=self.buttom_save
                    )

        self.save.grid(
                column=1,
                row=9,
                columnspan=8,
                rowspan=2,
                sticky="nesw",
                padx=1, pady=1
            )

    def show_frame(self):
        self.frame.grid_propagate(0)
        self.frame.grid_location(0, 0)
        self.frame.grid(
                    column=0,
                    row=0,
                    columnspan=8,
                    rowspan=9,
                )

    def hide_frame(self):
        self.frame.grid_forget()
