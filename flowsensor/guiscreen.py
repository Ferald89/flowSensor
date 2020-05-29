"""GuiScreen Class. """

# Tkinter
import tkinter as tk

# Local
from settings_screen import SettingScreen


class MainApplication(tk.Tk):

    def __init__(self, tasks=None):
        """Initial function class"""

        super().__init__()

        self.FONT_NUMBER = (
          "Helvetica",
          48,
          'bold'
          )
        self.COLORS = {
                  'INK': '#062F4F',
                  'EMBERS': '#B82601',
                  'BLACK': '#000000',
                  'POSY': '#813772',
                  'GREEN': 'green',
                  'RED': 'red'
        }
        self.SIZE_DATA = {
                      'height': 3,
                      'width': 11
        }

        self.get_screen_frame()
        self.setting_frame = SettingScreen(self.frame)
        self.hide_frame_initial()
        self.get_screen_properties()
        self.get_screen_label()

    def get_screen_properties(self):
        """Get screen properties of the screen. """

        self.title("Pressure Sensors || DEICA Automatismos S.A. de C.V.")
        self.geometry("795x440")
        self.resizable(0, 0)
        self.popup_menu = tk.Menu(self.frame1, tearoff=0)
        self.popup_menu.add_command(
                                label="Home",
                                command=self.show_home
                            )
        self.popup_menu.add_command(
                                label="Settings",
                                command=self.menu_setting
                            )
        self.popup_menu.add_command(
                                label="About",
                                command=self.hide_frames
                            )
        self.bind("<Button-3>", self.do_popup)

    def menu_setting(self):
        self.hide_frames()
        self.setting_frame.show_frame()

    def hide_frames(self):
        self.frame1.grid_forget()
        self.setting_frame.hide_frame()

    def hide_frame_initial(self):
        self.setting_frame.hide_frame()

    def show_home(self):
        self.hide_frames()
        self.frame1.grid(column=0, row=0, columnspan=2, rowspan=2)

    def do_popup(self, event):
        try:
            self.popup_menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.popup_menu.grab_release()

    def get_screen_label(self):
        """Get srcreen_label"""

        self.label1 = tk.Label(
                    self.frame1,
                    font=self.FONT_NUMBER,
                    justify='center',
                    bg=self.COLORS['BLACK'],
                    borderwidth=1,
                    relief="groove",
                    fg=self.COLORS['RED'],
                    height=self.SIZE_DATA['height'],
                    width=self.SIZE_DATA['width']
                    )
        self.label1['text'] = "FP 1 \n 0.044 Mpa"
        self.label1.grid(column=1, row=1)

        self.label2 = tk.Label(
                    self.frame1,
                    font=self.FONT_NUMBER,
                    justify='center',
                    bg=self.COLORS['BLACK'],
                    borderwidth=1,
                    relief="groove",
                    fg=self.COLORS['GREEN'],
                    height=self.SIZE_DATA['height'],
                    width=self.SIZE_DATA['width']
                    )
        self.label2['text'] = "FP 1 \n 0.044 Mpa"
        self.label2.grid(column=1, row=2)

        self.label3 = tk.Label(
                    self.frame1,
                    font=self.FONT_NUMBER,
                    justify='center',
                    bg=self.COLORS['BLACK'],
                    borderwidth=1,
                    relief="groove",
                    fg=self.COLORS['GREEN'],
                    height=self.SIZE_DATA['height'],
                    width=self.SIZE_DATA['width']
                    )

        self.label3['text'] = "FP 1 \n 0.044 Mpa"
        self.label3.grid(column=2, row=1)

        self.label4 = tk.Label(
                      self.frame1,
                      font=self.FONT_NUMBER,
                      justify='center',
                      bg=self.COLORS['BLACK'],
                      borderwidth=1,
                      relief="groove",
                      fg=self.COLORS['GREEN'],
                      height=self.SIZE_DATA['height'],
                      width=self.SIZE_DATA['width']
                      )
        self.label4['text'] = "FP 1 \n 0.044 Mpa"
        self.label4.grid(column=2, row=2)

    def get_screen_frame(self):
        """Get screen frame"""

        self.frame = tk.Frame(master=self,
                              width=500,
                              height=500,
                              bg='black',
                              padx=0,
                              pady=0)
        self.frame.pack()
        self.frame.pack_propagate(0)
        self.frame.pack(fill=tk.BOTH, expand=1)

        self.frame1 = tk.Frame(
                            master=self.frame,
                            width=900,
                            height=600,
                            bg='gray'
                      )
        # self.frame1.pack_propagate(0)
        # self.frame1.pack(fill=tk.BOTH, expand=1)
        # self.frame1.pack(padx=10,pady=10)
        self.frame1.grid_propagate(0)
        self.frame1.grid_location(0, 0)
        self.frame1.grid(column=0, row=0, columnspan=2, rowspan=2)
