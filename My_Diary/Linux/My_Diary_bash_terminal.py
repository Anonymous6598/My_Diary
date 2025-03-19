import customtkinter, tkterminal, typing

class My_Diary_bash_terminal(customtkinter.CTkToplevel):
    
    TITLE: typing.Final[str] = f"My Diary Bash window"
    
    def __init__(self: typing.Self, *args, **kwargs):
        customtkinter.CTkToplevel.__init__(self, *args, **kwargs)
        
        self.title(self.TITLE)

        self.bash_terminal: tkterminal.Terminal = tkterminal.Terminal(master=self, pady=5, padx=5, background=f"black", foreground=f"white", font=(f"System", 14))
        self.bash_terminal.shell = True
        self.bash_terminal.pack(expand=True, fill=f"both")