import tkinter as tk
import pandas as pd
from tkinter import ttk
import os

title = "Deadlock "


# Main call. This will be where all the gui happens.

class TempConverter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Temperature Converter")
        self.resizable(False, False)
        self.celsius    = tk.StringVar(value="0")
        self.fahrenheit = tk.StringVar(value="32")
        self._build_ui()
        self.celsius.trace_add("write", self._from_c)
        self.fahrenheit.trace_add("write", self._from_f)

    def _build_ui(self):
        f = ttk.Frame(self, padding=20)
        f.pack()
        ttk.Label(f, text="°C").grid(row=0, column=1)
        ttk.Entry(f, textvariable=self.celsius,    width=10).grid(row=0, column=0)
        ttk.Label(f, text=" = ").grid(row=0, column=2)
        ttk.Entry(f, textvariable=self.fahrenheit, width=10).grid(row=0, column=3)
        ttk.Label(f, text="°F").grid(row=0, column=4)

    def _from_c(self, *_):
        try: self.fahrenheit.set(f"{float(self.celsius.get())*9/5+32:.2f}")
        except: pass

    def _from_f(self, *_):
        try: self.celsius.set(f"{(float(self.fahrenheit.get())-32)*5/9:.2f}")
        except: pass

TempConverter().mainloop()