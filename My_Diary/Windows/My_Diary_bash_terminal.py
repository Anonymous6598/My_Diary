import customtkinter, tkterm, typing

class My_Diary_bash_terminal(customtkinter.CTkToplevel):
    
    TITLE: typing.Final[str] = f"My Diary Bash window"
    ICON: typing.Final[str] = f"my_diary_icon.ico"
    
    def __init__(self: typing.Self, *args, **kwargs):
        customtkinter.CTkToplevel.__init__(self, *args, **kwargs)
        
        self.title(self.TITLE)
        self.after(250, lambda: self.iconbitmap(self.ICON))

        self.bash_terminal: tkterm.Terminal = tkterm.Terminal(self)
        self.bash_terminal.shell = True
        self.bash_terminal.pack(expand=True, fill=f"both")