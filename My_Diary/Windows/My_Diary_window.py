import customtkinter, tkinterdnd2, typing

class My_Diary_window(customtkinter.CTk, tkinterdnd2.TkinterDnD.DnDWrapper):
    def __init__(self: typing.Self, *args, **kwargs):
        customtkinter.CTk.__init__(self, *args, **kwargs)
        self.TkdndVersion = tkinterdnd2.TkinterDnD._require(self)