from tkinter import *
from tkinter import ttk
from statistics import mean, median
from datetime import date
import lpoDB

__version__ = '0.3.2'

class lpoApp:

    def __init__(self, master):
        self.master = master
        self.createGUI()
        self.database = lpoDB