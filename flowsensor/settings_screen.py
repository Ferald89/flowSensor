"""Screen Settings Class. """

# Tkinter
import tkinter as tk


class SettingScreen:
    """setting frame. """

    def __init__(self, windows):
        self.set_frame(windows)
        self.set_label()
        self.set_entry()
        self.set_buttom()

    def set_frame(self, windows):
        self.frame = tk.Frame(
                            master=windows,
                            width=900,
                            height=600,
                            bg='gray'
                    )
        self.frame.grid()
        self.frame.grid_propagate(0)
        self.frame.grid(column=0, row=0, columnspan=8, rowspan=9)

    def set_label(self):
        self.label1 = tk.Label(
                        self.frame,
                        # font=("Helvetica", 30, 'bold'),
                        fg="white",
                        bd=2,
                        height=1
                    )
        self.label1['text'] = "Ajustes"
        self.label1.grid(
                row=1,
                column=1,
                columnspan=8,
                rowspan=2,
                sticky="nesw",
                padx=5, pady=5
            )

        self.label2 = tk.Label(self.frame, fg="white")
        self.label2['text'] = "Sensor 1"
        self.label2.grid(column=1, row=3, columnspan=2)

        self.label3 = tk.Label(self.frame, fg="white")
        self.label3['text'] = "Sensor 2"
        self.label3.grid(column=3, row=3, columnspan=2)

        self.label4 = tk.Label(self.frame, fg="white")
        self.label4['text'] = "Sensor 3"
        self.label4.grid(column=1, row=6, columnspan=2)

        self.label5 = tk.Label(self.frame, fg="white")
        self.label5['text'] = "Sensor 4"
        self.label5.grid(column=3, row=6, columnspan=2)

        self.label6 = tk.Label(self.frame, fg="white")
        self.label6['text'] = "Máximo"
        self.label6.grid(column=1, row=4)

        self.label7 = tk.Label(self.frame, fg="white")
        self.label7['text'] = "Minimo"
        self.label7.grid(column=1, row=5)

        self.label8 = tk.Label(self.frame, fg="white")
        self.label8['text'] = "Máximo"
        self.label8.grid(column=3, row=4)

        self.label9 = tk.Label(self.frame, fg="white")
        self.label9['text'] = "Minimo"
        self.label9.grid(column=3, row=5)

        self.label10 = tk.Label(self.frame, fg="white")
        self.label10['text'] = "Máximo"
        self.label10.grid(column=1, row=7)

        self.label11 = tk.Label(self.frame, fg="white")
        self.label11['text'] = "Minimo"
        self.label11.grid(column=1, row=8)

        self.label10 = tk.Label(self.frame, fg="white")
        self.label10['text'] = "Máximo"
        self.label10.grid(column=3, row=7)

        self.label11 = tk.Label(self.frame, fg="white")
        self.label11['text'] = "Minimo"
        self.label11.grid(column=3, row=8)

    def set_entry(self):
        self.entry1 = tk.Entry(self.frame)
        self.entry1.grid(column=2, row=4)

        self.entry2 = tk.Entry(self.frame)
        self.entry2.grid(column=2, row=5)

        self.entry3 = tk.Entry(self.frame)
        self.entry3.grid(column=4, row=4)

        self.entry4 = tk.Entry(self.frame)
        self.entry4.grid(column=4, row=5)

        self.entry5 = tk.Entry(self.frame)
        self.entry5.grid(column=2, row=7)

        self.entry6 = tk.Entry(self.frame)
        self.entry6.grid(column=2, row=8)

        self.entry7 = tk.Entry(self.frame)
        self.entry7.grid(column=4, row=7)

        self.entry8 = tk.Entry(self.frame)
        self.entry8.grid(column=4, row=8)

    def set_buttom(self):
        self.save = tk.Button(self.frame, text="Save")
        self.save.grid(column=1, row=9)

    def show_frame(self):
        self.frame.grid(column=0, row=0)

    def hide_frame(self):
        self.frame.grid_forget()
