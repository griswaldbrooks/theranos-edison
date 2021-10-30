#!/usr/bin/env python3
import serial
from time import time, sleep
import tkinter as tk
import os
from PIL import Image, ImageTk

class Detector:
    def __init__(self):
            self.window = tk.Tk()
            self.window.configure(background="white")
            self.window.wm_title("Theranos: Changing the face of medicine")
            self.state = tk.Label(self.window,
                text="Awaiting sample",
                background="white",
                font=("Arial", 40))
            self.state.place(relx = 0.5, rely = 0.5, anchor="w")

            self.disclaimer = tk.Label(self.window,
                text="""By providing a blood sample, you consent to providing us your medical information for diagnostic purposes.
                                                    For more information, click on this link about our policies and practices.""",
                background="white",
                font=("Arial", 13))
            self.disclaimer.place(relx = 0.50, rely = 0.95, anchor="w")

            self.src_ceo = ImageTk.PhotoImage(Image.open("ceo.jpeg").resize((822, 1024)))
            self.ceo = tk.Label(self.window, image=self.src_ceo)
            self.ceo.place(relx=0.0, y=0.5, anchor="nw")

            self.src_logo = ImageTk.PhotoImage(Image.open("logo.png"))
            self.logo = tk.Label(self.window, image=self.src_logo, background="white",)
            self.logo.place(relx=0.76, y=0.5, anchor="ne")
            self.moto = tk.Label(self.window,
                text="Changing the face of medicine",
                background="white",
                fg="#508f81",
                font=("Arial", 20, "italic"))
            self.moto.place(relx = 0.50, rely = 0.13, anchor="w")

            self.window.after(100, self.read_serial)
            self.window.mainloop()

    def read_serial(self):
        with serial.Serial('/dev/ttyACM0', 115200) as edison:
            print_timestamp = time()
            while True:
                if edison.readline().strip() == b'1':
                    if (time() - print_timestamp) > 30:
                        print_timestamp = time()
                        print("Analyzing...")
                        self.state["text"] = "Analyzing sample"
                        self.window.update()
                        sleep(5)
                        self.state["text"] = "Analysis complete"
                        self.window.update()
                        sleep(1)
                        self.state["text"] = "Generating report"
                        self.window.update()
                        sleep(5)
                        # os.system('lp report.pdf')
                    else:
                        print(time() - print_timestamp)
                        self.state["text"] = "Awaiting sample..."
                        self.window.update()
                else:
                    print("Waiting...")
                    self.state["text"] = "Awaiting sample"
                    self.window.update()


if __name__ == '__main__':
    Detector()



# Theranos: Changing the face of medicine
