import customtkinter, tkinter.messagebox, pickle, typing

with open(f"my_diary_language_settings.pickle", f"rb+") as data: language_data: str = pickle.load(data)

with open(f"my_diary_theme_settings.pickle", f"rb+") as theme_data: theme: str = pickle.load(theme_data)

class My_Diary_setting_window(customtkinter.CTkToplevel):
    WIDTH: typing.Final[int] = 655 
    HEIGHT: typing.Final[int] = 330
    TITLE: typing.Final[str] = f"My Diary settings window"

    def __init__(self, *args, **kwargs) -> None:
        customtkinter.CTkToplevel.__init__(self, *args, **kwargs)

        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.resizable(False, False)
        self.title(self.TITLE)

        if language_data == f"Српски":
            self.main_screen_settings_text: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self, text=f"Подешавања", font=(f"Roboto Bold", 75))
            self.main_screen_settings_text.place(x=0, y=0)

            self.main_screen_language_text: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self, text=f"Језици", font=(f"Roboto Bold", 50))
            self.main_screen_language_text.place(x=0, y=87)

            self.main_screen_settings_theme_mode_text: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self, text=f"Тема", font=(f"Roboto Bold", 36))
            self.main_screen_settings_theme_mode_text.place(x=0, y=187)

        elif language_data == f"English":
            self.main_screen_settings_text: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self, text=f"Settings", font=(f"Roboto Bold", 75))
            self.main_screen_settings_text.place(x=0, y=0)
            
            self.main_screen_language_text: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self, text=f"Languages", font=(f"Roboto Bold", 50))
            self.main_screen_language_text.place(x=0, y=87)
            
            self.main_screen_settings_theme_mode_text: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self, text=f"Theme", font=(f"Roboto Bold", 36))
            self.main_screen_settings_theme_mode_text.place(x=0, y=187)

        else:
            self.main_screen_settings_text: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self, text=f"Настройки", font=(f"Roboto Bold", 75))
            self.main_screen_settings_text.place(x=0, y=0)
            
            self.main_screen_language_text: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self, text=f"Языки", font=(f"Roboto Bold", 50))
            self.main_screen_language_text.place(x=0, y=87)
            
            self.main_screen_settings_theme_mode_text: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self, text=f"Тема", font=(f"Roboto Bold", 36))
            self.main_screen_settings_theme_mode_text.place(x=0, y=187)

        self.main_screen_settings_language_option: customtkinter.CTkSegmentedButton = customtkinter.CTkSegmentedButton(master=self, values=[f"Српски", f"English", f"Русский"], command=self.__language_settings__)
        self.main_screen_settings_language_option.place(x=15, y=147)

        self.main_screen_settings_language_option.set(language_data)

        self.main_screen_settings_theme_mode_option: customtkinter.CTkSegmentedButton = customtkinter.CTkSegmentedButton(master=self, values=[f"dark", f"light"], command=self.__theme_settings__)
        self.main_screen_settings_theme_mode_option.place(x=15, y=227)

        self.main_screen_settings_theme_mode_option.set(theme)

    def __language_settings__(self: typing.Self, pickle_serializer: pickle) -> None:
        self.main_screen_settings_language_option_data: str = self.main_screen_settings_language_option.get()
        with open(f"my_diary_language_settings.pickle", f"wb+") as self.data:
            pickle.dump(self.main_screen_settings_language_option_data, self.data)

        if self.main_screen_settings_language_option_data == f"Српски":
            tkinter.messagebox.showwarning(title=f"Пажња", message=f"Рестартуј програм")

        elif self.main_screen_settings_language_option_data == f"English":
            tkinter.messagebox.showwarning(title=f"Warning", message=f"Restart program")
            
        else:
            tkinter.messagebox.showwarning(title=f"Внимание", message=f"Перезагрузите программу")

    def __theme_settings__(self: typing.Self, pickle_serializer: pickle) -> None:
        self.main_screen_settings_theme_option_data: str = self.main_screen_settings_theme_mode_option.get()
        with open(f"my_diary_theme_settings.pickle", f"wb+") as self.data:
            pickle.dump(self.main_screen_settings_theme_option_data, self.data)

        if language_data == f"Српски":
            tkinter.messagebox.showwarning(title=f"Пажња", message=f"Рестартуј програм")

        elif language_data == f"English":
            tkinter.messagebox.showwarning(title=f"Warning", message=f"Restart program")
            
        else:
            tkinter.messagebox.showwarning(title=f"Внимание", message=f"Перезагрузите программу")