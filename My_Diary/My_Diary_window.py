import typing
from customtkinter import *
from tkinterdnd2 import *

class Tk(CTk, TkinterDnD.DnDWrapper):
    def __init__(self: typing.Self, *args, **kwargs):
        CTk.__init__(self, *args, **kwargs)
        self.TkdndVersion = TkinterDnD._require(self)