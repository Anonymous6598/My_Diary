import customtkinter, tkinter.messagebox, pickle, typing, My_Calculus_settings_window_interface, My_Calculus, locale

with open(f"my_calculus_text_color.pickle", f"rb+") as text_color_data: text_color: str = pickle.load(text_color_data)

with open(f"my_calculus_expression_entry_color.pickle", f"rb+") as expression_entry_color_data: expression_entry_color: str = pickle.load(expression_entry_color_data)

with open(f"my_calculus_expression_entry_text_color.pickle", f"rb+") as expression_entry_text_color_data: expression_entry_text_color: str = pickle.load(expression_entry_text_color_data)

with open(f"my_calculus_button_color.pickle", f"rb+") as button_color_data: button_color: str = pickle.load(button_color_data)

class Settings_window(customtkinter.CTkToplevel, My_Calculus_settings_window_interface.My_Calculus_settings_window_interface):
     
    WIDTH: typing.Final[int] = 655 
    HEIGHT: typing.Final[int] = 571
    TITLE: typing.Final[str] = f"My Calculus settings window"
    ICON: typing.Final[str] = f"my calculus icon.ico"

    def __init__(self, *args, **kwargs) -> None:
        customtkinter.CTkToplevel.__init__(self, *args, **kwargs)

        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.resizable(False, False)
        self.title(self.TITLE)
        self.after(250, lambda: self.iconbitmap(self.ICON))
        
        self.main_screen_settings_customatization_text: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self, text=f"Спољни изглед", text_color=text_color, font=(f"Roboto Bold", 36))
        self.main_screen_settings_customatization_text.place(x=15, y=1)

        self.main_screen_settings_customatization_table: customtkinter.CTkTabview = customtkinter.CTkTabview(master=self, height=50, width=400, border_width=1, border_color=(f"black", f"white"), segmented_button_selected_color=button_color, text_color=text_color)
        self.main_screen_settings_customatization_table.place(x=15, y=37)

        self.main_screen_settings_customatization_table.add("1")
        self.main_screen_settings_customatization_table.add("2")
        self.main_screen_settings_customatization_table.add("3")

        self.main_screen_settings_customatization_text_color_text: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self.main_screen_settings_customatization_table.tab(f"1"), text=f"Боја текста", text_color=text_color, font=(f"Roboto Bold", 36))
        self.main_screen_settings_customatization_text_color_text.grid(column=0, row=0)

        self.main_screen_settings_customatization_text_color_option: customtkinter.CTkSegmentedButton = customtkinter.CTkSegmentedButton(master=self.main_screen_settings_customatization_table.tab(f"1"), text_color=text_color, values=[f"red", f"blue", f"green", f"black", f"white"], selected_color=button_color, command=self.__change_text_color__)
        self.main_screen_settings_customatization_text_color_option.grid(column=0, row=1)


        self.main_screen_settings_customatization_expression_entry_color_text: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self.main_screen_settings_customatization_table.tab(f"2"), text=f"Боја поља", text_color=text_color, font=(f"Roboto Bold", 36))
        self.main_screen_settings_customatization_expression_entry_color_text.grid(column=0, row=0)

        self.main_screen_settings_customatization_expression_entry_color_option: customtkinter.CTkSegmentedButton = customtkinter.CTkSegmentedButton(master=self.main_screen_settings_customatization_table.tab(f"2"), values=[f"red", f"blue", f"green", f"black", f"white", f"transparent"], text_color=text_color, selected_color=button_color, command=self.__change_expression_entry_color__)
        self.main_screen_settings_customatization_expression_entry_color_option.grid(column=0, row=1)

        self.main_screen_settings_customatization_expression_entry_color_text_color_text: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self.main_screen_settings_customatization_table.tab(f"2"), text=f"Боја текста поља", text_color=text_color, font=(f"Roboto Bold", 36))
        self.main_screen_settings_customatization_expression_entry_color_text_color_text.grid(column=0, row=2)

        self.main_screen_settings_customatization_expression_entry_text_color_option: customtkinter.CTkSegmentedButton = customtkinter.CTkSegmentedButton(master=self.main_screen_settings_customatization_table.tab(f"2"), values=[f"red", f"blue", f"green", f"black", f"white"], text_color=text_color, selected_color=button_color, command=self.__change_expression_entry_text_color__)
        self.main_screen_settings_customatization_expression_entry_text_color_option.grid(column=0, row=3)


        self.main_screen_settings_customatization_button_color_text: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self.main_screen_settings_customatization_table.tab(f"3"), text=f"Боја дугма", text_color=text_color, font=(f"Roboto Bold", 36))
        self.main_screen_settings_customatization_button_color_text.grid(column=0, row=0)

        self.main_screen_settings_customatization_button_color_option: customtkinter.CTkSegmentedButton = customtkinter.CTkSegmentedButton(master=self.main_screen_settings_customatization_table.tab(f"3"), values=[f"red", f"blue", f"green", f"black", f"orange", f"yellow", f"purple"], text_color=text_color, selected_color=button_color, command=self.__change_button_color__)
        self.main_screen_settings_customatization_button_color_option.grid(column=0, row=1)

        self.main_screen_settings_customatization_text_color_option.set(text_color)

        self.main_screen_settings_customatization_expression_entry_color_option.set(expression_entry_color)

        self.main_screen_settings_customatization_expression_entry_text_color_option.set(expression_entry_text_color)

        self.main_screen_settings_customatization_button_color_option.set(button_color)

        self.main_screen_settings_customatization_text.configure(text=f"Customatization")
        self.main_screen_settings_customatization_text_color_text.configure(text=f"Text color")
        self.main_screen_settings_customatization_expression_entry_color_text.configure(text=f"Expression entry color")
        self.main_screen_settings_customatization_expression_entry_color_text.configure(text=f"Expression entry text color")
        self.main_screen_settings_customatization_button_color_text.configure(text=f"Button color")
    
    @typing.override
    def __change_text_color__(self, pickle_serializer: pickle) -> None:
        self.main_screen_settings_customatization_text_color_option_data: str = self.main_screen_settings_customatization_text_color_option.get()
        with open(f"my_calculus_text_color.pickle", f"wb+") as self.text_color_data: pickle.dump(self.main_screen_settings_customatization_text_color_option_data, self.text_color_data)            
        tkinter.messagebox.showwarning(title=f"Warning", message=f"Restart program")

    @typing.override
    def __change_expression_entry_color__(self, pickle_serialization: pickle) -> None:
        self.main_screen_settings_customatization_expression_entry_color_option_data: str = self.main_screen_settings_customatization_expression_entry_color_option.get()
        with open(f"my_calculus_expression_entry_color.pickle", f"wb+") as self.expression_entry_color_data: pickle.dump(self.main_screen_settings_customatization_expression_entry_color_option_data, self.expression_entry_color_data)
        tkinter.messagebox.showwarning(title=f"Warning", message=f"Restart program")

    @typing.override
    def __change_expression_entry_text_color__(self, pickle_serialization: pickle) -> None:
        self.main_screen_settings_customatization_expression_entry_text_color_option_data: str = self.main_screen_settings_customatization_expression_entry_text_color_option.get()
        with open(f"my_calculus_expression_entry_text_color.pickle", f"wb+") as self.expression_entry_text_color_data: pickle.dump(self.main_screen_settings_customatization_expression_entry_text_color_option_data, self.expression_entry_text_color_data)
        tkinter.messagebox.showwarning(title=f"Warning", message=f"Restart program")

    @typing.override
    def __change_button_color__(self, pickle_serialization: pickle) -> None:
        self.main_screen_settings_customatization_button_color_option_data: str = self.main_screen_settings_customatization_button_color_option.get()
        with open(f"my_calculus_button_color.pickle", f"wb+") as self.button_color_data: pickle.dump(self.main_screen_settings_customatization_button_color_option_data, self.button_color_data)
        tkinter.messagebox.showwarning(title=f"Warning", message=f"Restart program")

program: My_Calculus.Program = My_Calculus.Program()