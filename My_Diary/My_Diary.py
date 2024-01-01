import tkinter, tkinter.messagebox, pickle, os, sys, docx, docx.shared, aspose.words, subprocess, functools, typing, My_Diary_interface, functools
from tkinterdnd2 import *
from customtkinter import *

with open(f"my_diary_settings.pickle", f"rb+") as data: language_data: str = pickle.load(data)

with open(f"my_diary_saved_text.pickle", f"rb+") as text_data: autosaved_text: str = pickle.load(text_data)

with open(f"my_diary_autosave_settings.pickle", f"rb+") as autosave_data: new_autosaved_data: str = pickle.load(autosave_data)

with open(f"my_diary_theme_settings.pickle", f"rb+") as theme_data: theme: str = pickle.load(theme_data)

with open(f"my_diary_text_color.pickle", f"rb+") as text_color_data: text_color: str = pickle.load(text_color_data)

with open(f"my_diary_text_field_color.pickle", f"rb+") as text_field_color_data: text_field_color: str = pickle.load(text_field_color_data)

with open(f"my_diary_text_field_text_height.pickle", f"rb+") as text_field_text_height_data: text_field_text_height: str = pickle.load(text_field_text_height_data)

with open(f"my_diary_button_color.pickle", f"rb+") as button_color_data: button_color: str = pickle.load(button_color_data)


def memorise(function_param: str) -> str:

    cache: dict = {}

    @functools.wraps(function_param)
    def wrapper(*args, **kwargs) -> str:
        key: str = str(args) + str(kwargs)
        if key not in cache:
            cache[key]: function = function_param(*args, **kwargs)

        return cache[key]
    
    return wrapper


class Tk(CTk, TkinterDnD.DnDWrapper):
    def __init__(self: typing.Self, *args, **kwargs):
        CTk.__init__(self, *args, **kwargs)
        self.TkdndVersion = TkinterDnD._require(self)

class Program(Tk, My_Diary_interface.My_Diary_interface):

	TITLE: typing.Final[str] = f"My Diary"
	ICON: typing.Final[str] = f"my diary icon.ico"
	COLOR_THEME: typing.Final[str] = f"dark-blue"
	WIDGET_SCALING: typing.Final[float] = 1.251

	def __init__(self: typing.Self, *args, **kwargs) -> None:
		Tk.__init__(self, *args, **kwargs)

		set_widget_scaling(self.WIDGET_SCALING)
		set_default_color_theme(self.COLOR_THEME)
		set_appearance_mode(theme)
		deactivate_automatic_dpi_awareness()

		self.title(self.TITLE)
		self.iconbitmap(self.ICON)
  
		self.bind(f"<Control_L>" + f"<f>", self.__fullscreen__) 
		self.bind(f"<Alt_L>" + f"<F4>", self.__exit__)
		self.bind(f"<Alt_L>" + f"<t>", self.__open_terminal__)
		self.bind(f"<Escape>", self.__close_taskbar__)
		self.bind(f"<Button-3>", self.__right_click_menu__)
		self.bind(f"<Control_L>" + f"<s>", self.__save_text__)
		self.bind(f"<Control_L>" + f"<o>", self.__open_file__)
		self.protocol(f"WM_DELETE_WINDOW", self.__exit__)
		
		self.main_screen_fullscreen_numbers: int = 1

		self.main_screen_taskbar_button: CTkButton = CTkButton(master=self, text=f"☰", text_color=text_color, height=20, width=10, corner_radius=0, fg_color=button_color, command=self.__open_taskbar__)
		self.main_screen_taskbar_button.grid(column=0, row=0)

		self.main_screen_undo_button: CTkButton = CTkButton(master=self, text=f"⟲", text_color=text_color, height=20, width=10, corner_radius=0, fg_color=button_color, command=self.__undo__)
		self.main_screen_undo_button.grid(column=1, row=0)

		self.main_screen_redo_button: CTkButton = CTkButton(master=self, text=f"⟳", text_color=text_color, height=20, width=10, corner_radius=0, fg_color=button_color, command=self.__redo__)
		self.main_screen_redo_button.grid(column=2, row=0)

		self.main_screen_frame: CTkFrame = CTkFrame(master=self, height=769, width=1535, border_width=1, border_color=(f"black", f"white"), corner_radius=0)
		self.main_screen_frame.place(x=0, y=22.35)

		self.bind(f"<Configure>", self.__frame_resize__)

		self.main_screen_frame_texbox_font: CTkFont = CTkFont(family=f"Ubuntu", size=int(text_field_text_height), weight=f"normal", slant=f"roman", underline=False, overstrike=False)

		self.main_screen_frame_textbox: CTkTextbox = CTkTextbox(master=self.main_screen_frame, height=767.5, width=1533.57, corner_radius=0, undo=True, fg_color=text_field_color, font=self.main_screen_frame_texbox_font, text_color=(f"black", f"white"))
		self.main_screen_frame_textbox.place(x=1, y=1)

		self.main_screen_frame_textbox.drop_target_register(DND_ALL)
		self.main_screen_frame_textbox.dnd_bind(f"<<Drop>>", self.__drop_file_into_textbox__)

		self.main_screen_frame_textbox.bind(f"<KeyRelease>", self.__word_count__)
		self.main_screen_frame_textbox.bind(f"<F1>", self.__html_script__)
		self.main_screen_frame_textbox.bind(f"<KeyPress>", self.__close_taskbar__)
		self.main_screen_frame_textbox.bind(f"<ButtonRelease>", self.__close_taskbar__)

		self.main_screen_taskbar: CTkFrame = CTkFrame(master=self, width=300, height=791, border_width=0, corner_radius=5, fg_color=f"transparent")

		self.main_screen_taskbar_exit_button: CTkButton = CTkButton(master=self.main_screen_taskbar, text=f"↵", text_color=text_color, height=20, width=10, corner_radius=5, fg_color=button_color)
		self.main_screen_taskbar_exit_button.place(x=278, y=2)

		self.main_screen_taskbar_exit_button.bind(f"<Button-1>", self.__close_taskbar__)

		self.main_screen_save_button: CTkButton = CTkButton(master=self.main_screen_taskbar, text=f"сачувај текст", text_color=text_color, height=20, width=295, corner_radius=5, fg_color=button_color, font=(f"Roboto Bold", 22))
		self.main_screen_save_button.place(x=2, y=32)
		
		self.main_screen_save_button.bind(f"<Button-1>", self.__save_text__)

		self.main_screen_clear_button: CTkButton = CTkButton(master=self.main_screen_taskbar, text=f"обриши текст", text_color=text_color, height=20, width=295, corner_radius=5, fg_color=button_color, font=(f"Roboto Bold", 22), command=self.__clear_text__)
		self.main_screen_clear_button.place(x=2, y=67)

		self.main_screen_edit_text_button: CTkButton = CTkButton(master=self.main_screen_taskbar, text=f"уреди текст", text_color=text_color, height=20, width=295, corner_radius=5, fg_color=button_color, font=(f"Roboto Bold", 22), command=self.__edit_text__)
		self.main_screen_edit_text_button.place(x=2, y=102)

		self.main_screen_edit_font_button: CTkComboBox = CTkComboBox(master=self, height=20, width=75, corner_radius=0, values=[f"System", f"Terminal", f"Ubuntu", f"Script", f"Roman", f"Modern", f"MS Serif"], text_color=text_color, fg_color=button_color, border_color=button_color, button_color=button_color, button_hover_color=button_color, dropdown_fg_color=button_color, dropdown_text_color=text_color, command=self.__edit_text_font__)

		self.main_screen_edit_size_button: CTkComboBox = CTkComboBox(master=self, height=20, width=75, corner_radius=0, values=[f"1", f"2", f"4", f"5", f"6", f"8", f"11", f"12", f"13", f"14", f"16", f"18", f"20", f"22", f"24", f"26", f"28", f"30", f"32", f"34", f"36", f"38", f"40", f"42", f"44", f"46", f"48", f"50", f"60", f"70", f"80", f"90", f"100"], text_color=text_color, fg_color=button_color, border_color=button_color, button_color=button_color, button_hover_color=button_color, dropdown_fg_color=button_color, dropdown_text_color=text_color, command=self.__edit_text_font__)

		self.main_screen_edit_color_button: CTkComboBox = CTkComboBox(master=self, height=20, width=75, corner_radius=0, values=[f"black", f"white", f"red", f"green", f"blue"], text_color=text_color, fg_color=button_color, border_color=button_color, button_color=button_color, button_hover_color=button_color, dropdown_fg_color=button_color, dropdown_text_color=text_color, command=self.__edit_text_font__)

		self.main_screen_edit_slant_button: CTkComboBox = CTkComboBox(master=self, height=20, width=75, corner_radius=0, values=[f"roman", f"italic"], text_color=text_color, fg_color=button_color, border_color=button_color, button_color=button_color, button_hover_color=button_color, dropdown_fg_color=button_color, dropdown_text_color=text_color, command=self.__edit_text_font__)

		self.main_screen_edit_weight_button: CTkComboBox = CTkComboBox(master=self, height=20, width=75, corner_radius=0, values=[f"normal", f"bold"], text_color=text_color, fg_color=button_color, border_color=button_color, button_color=button_color, button_hover_color=button_color, dropdown_fg_color=button_color, dropdown_text_color=text_color, command=self.__edit_text_font__)

		self.main_screen_edit_underline_button: CTkComboBox = CTkComboBox(master=self, height=20, width=75, corner_radius=0, values=[f"not underlined", f"underlined"], text_color=text_color, fg_color=button_color, border_color=button_color, button_color=button_color, button_hover_color=button_color, dropdown_fg_color=button_color, dropdown_text_color=text_color, command=self.__edit_text_font__)

		self.main_screen_edit_overstrike_button: CTkComboBox = CTkComboBox(master=self, height=20, width=75, corner_radius=0, values=[f"not overstriked", f"overstriked"], text_color=text_color, fg_color=button_color, border_color=button_color, button_color=button_color, button_hover_color=button_color, dropdown_fg_color=button_color, dropdown_text_color=text_color, command=self.__edit_text_font__)

		self.main_screen_open_button: CTkButton = CTkButton(master=self.main_screen_taskbar, text=f"отвори фајл", text_color=text_color, height=20, width=295, corner_radius=5, fg_color=button_color, font=(f"Roboto Bold", 22), command=self.__open_file__)
		self.main_screen_open_button.place(x=2, y=137)
		
		self.main_screen_open_button.bind(f"<Button-1>", self.__open_file__)
	
		self.main_screen_converter_button: CTkButton = CTkButton(master=self.main_screen_taskbar, text=f"претварач", text_color=text_color, height=20, width=295, corner_radius=5, fg_color=button_color, font=(f"Roboto Bold", 22), command=self.__convert__)
		self.main_screen_converter_button.place(x=2, y=172)

		self.main_screen_pdf_to_word_converter_button: CTkButton = CTkButton(master=self, text=f"из Pdf у docx", text_color=text_color, height=20, width=25, corner_radius=0, fg_color=button_color, command=self.__pdf_to_docx__)

		self.main_screen_word_to_pdf_converter_button: CTkButton = CTkButton(master=self, text=f"из docx у Pdf", text_color=text_color, height=20, width=25, corner_radius=0, fg_color=button_color, command=self.__docx_to_pdf__)

		self.main_screen_pdf_to_txt_converter_button: CTkButton = CTkButton(master=self, text=f"из Pdf у txt", text_color=text_color, height=20, width=25, corner_radius=0, fg_color=button_color, command=self.__pdf_to_txt__)

		self.main_screen_txt_to_pdf_converter_button: CTkButton = CTkButton(master=self, text=f"из txt у Pdf", text_color=text_color, height=20, width=25, corner_radius=0, fg_color=button_color, command=self.__txt_to_pdf__)

		self.main_screen_word_to_txt_converter_button: CTkButton = CTkButton(master=self, text=f"из docx y txt", text_color=text_color, height=20, width=25, corner_radius=0, fg_color=button_color, command=self.__docx_to_txt__)

		self.main_screen_txt_to_word_converter_button: CTkButton = CTkButton(master=self, text=f"из txt у docx", text_color=text_color, height=20, width=25, corner_radius=0, fg_color=button_color, command=self.__txt_to_docx__)

		self.main_screen_code_editor_button: CTkButton = CTkButton(master=self.main_screen_taskbar, text=f"редактор кода", text_color=text_color, height=20, width=295, corner_radius=5, fg_color=button_color, font=(f"Roboto Bold", 22), command=self.__code_editor__)
		self.main_screen_code_editor_button.place(x=2, y=207)

		self.main_screen_open_powershell_button: CTkButton = CTkButton(master=self, text=f"отвори powershell", text_color=text_color, height=20, width=25, corner_radius=0, fg_color=button_color, command=self.__open_powershell__)

		self.main_screen_open_terminal_button: CTkButton = CTkButton(master=self, text=f"отвори терминал", text_color=text_color, height=20, width=25, corner_radius=0, fg_color=button_color, command=self.__open_shell__)

		self.main_screen_save_code_as_button: CTkButton = CTkButton(master=self, text=f"сачувај код", text_color=text_color, height=20, width=25, corner_radius=0, fg_color=button_color)

		self.main_screen_save_code_as_button.bind(f"<Button-1>", self.__save_code__)

		self.main_screen_open_code_button: CTkButton = CTkButton(master=self, text=f"отвори код", text_color=text_color, height=20, width=25, corner_radius=0, fg_color=button_color, command=self.__open_code__)

		self.main_screen_right_click_menu: tkinter.Menu = tkinter.Menu(self, tearoff=0)

		self.main_screen_right_click_save_menu: tkinter.Menu = tkinter.Menu(self, tearoff=0)

		self.main_screen_right_click_open_menu: tkinter.Menu = tkinter.Menu(self, tearoff=0)

		self.main_screen_right_click_convert_menu: tkinter.Menu = tkinter.Menu(self, tearoff=0)

		self.main_screen_right_click_code_menu: tkinter.Menu = tkinter.Menu(self, tearoff=0)

		self.main_screen_settings_button: CTkButton = CTkButton(master=self.main_screen_taskbar, text=f"подешавања", text_color=text_color, height=20, width=295, corner_radius=5, fg_color=button_color, font=(f"Roboto Bold", 22), command=self.__settings__)
		self.main_screen_settings_button.place(x=2, y=242)

		self.main_screen_settings_text: CTkLabel = CTkLabel(master=self, text=f"подешавања", text_color=text_color, font=(f"Roboto Bold", 72))

		self.main_screen_settings_language_text: CTkLabel = CTkLabel(master=self, text=f"језици", text_color=text_color, font=(f"Roboto Bold", 36))

		self.main_screen_settings_language_option: CTkSegmentedButton = CTkSegmentedButton(master=self, values=[f"Српски", f"English", f"Русский"], text_color=text_color, selected_color=button_color, command=self.__language_settings__)

		self.main_screen_settings_language_option.set(language_data)

		self.main_screen_settings_autosave_text: CTkLabel = CTkLabel(master=self, text=f"ауточување", text_color=text_color, font=(f"Roboto Bold", 36))

		self.main_screen_settings_autosave_value: tkinter.StringVar = tkinter.StringVar(value=new_autosaved_data)

		self.main_screen_settings_autosave_switch: CTkSwitch = CTkSwitch(master=self, text=f"ауточување", text_color=text_color, variable=self.main_screen_settings_autosave_value, onvalue=f"on", offvalue=f"off", progress_color=button_color, command=lambda: self.__autosave_settings__(pickle))

		self.main_screen_settings_autosave_switch_value: str = self.main_screen_settings_autosave_value.get()
			
		self.main_screen_settings_theme_mode_text: CTkLabel = CTkLabel(master=self, text=f"тема", text_color=text_color, font=(f"Roboto Bold", 36))

		self.main_screen_settings_theme_mode_option: CTkSegmentedButton = CTkSegmentedButton(master=self, values=[f"system", f"dark", f"light"], text_color=text_color, selected_color=button_color, command=self.__theme_settings__)

		self.main_screen_settings_theme_mode_option.set(theme)

		self.main_screen_settings_customatization_text: CTkLabel = CTkLabel(master=self, text=f"Спољни изглед", text_color=text_color, font=(f"Roboto Bold", 36))

		self.main_screen_settings_customatization_table: CTkTabview = CTkTabview(master=self, height=50, width=400, border_width=1, border_color=(f"black", f"white"), segmented_button_selected_color=button_color, text_color=f"white")

		self.main_screen_settings_customatization_table.add(f"1")
		self.main_screen_settings_customatization_table.add(f"2")
		self.main_screen_settings_customatization_table.add(f"3")

		self.main_screen_settings_customatization_text_color_text: CTkLabel = CTkLabel(master=self.main_screen_settings_customatization_table.tab(f"1"), text=f"Боја текста", text_color=text_color, font=(f"Roboto Bold", 36))
		self.main_screen_settings_customatization_text_color_text.grid(column=0, row=0)

		self.main_screen_settings_customatization_text_color_option: CTkSegmentedButton = CTkSegmentedButton(master=self.main_screen_settings_customatization_table.tab(f"1"), text_color=text_color, values=[f"red", f"blue", f"green", f"black", f"white"], selected_color=button_color, command=self.__change_text_color__)
		self.main_screen_settings_customatization_text_color_option.grid(column=0, row=1)


		self.main_screen_settings_customatization_text_field_color_text: CTkLabel = CTkLabel(master=self.main_screen_settings_customatization_table.tab(f"2"), text=f"Боја поља", text_color=text_color, font=(f"Roboto Bold", 36))
		self.main_screen_settings_customatization_text_field_color_text.grid(column=0, row=0)

		self.main_screen_settings_customatization_text_field_color_option: CTkSegmentedButton = CTkSegmentedButton(master=self.main_screen_settings_customatization_table.tab(f"2"), values=[f"red", f"blue", f"green", f"black", f"white", f"transparent"], text_color=text_color, selected_color=button_color, command=self.__change_text_field_color__)
		self.main_screen_settings_customatization_text_field_color_option.grid(column=0, row=1)

		self.main_screen_settings_customatization_text_field_height_text: CTkLabel = CTkLabel(master=self.main_screen_settings_customatization_table.tab(f"2"), text=f"Висина текста поља", text_color=text_color, font=(f"Roboto Bold", 36))
		self.main_screen_settings_customatization_text_field_height_text.grid(column=0, row=2)

		self.main_screen_settings_customatization_text_field_height_option: CTkSegmentedButton = CTkSegmentedButton(master=self.main_screen_settings_customatization_table.tab(f"2"), values=[f"14", f"22", f"28", f"32"], text_color=text_color, selected_color=button_color, command=self.__change_text_field_text_height__)
		self.main_screen_settings_customatization_text_field_height_option.grid(column=0, row=3)


		self.main_screen_settings_customatization_button_color_text: CTkLabel = CTkLabel(master=self.main_screen_settings_customatization_table.tab(f"3"), text=f"Боја дугма", text_color=text_color, font=(f"Roboto Bold", 36))
		self.main_screen_settings_customatization_button_color_text.grid(column=0, row=0)

		self.main_screen_settings_customatization_button_color_option: CTkSegmentedButton = CTkSegmentedButton(master=self.main_screen_settings_customatization_table.tab(f"3"), values=[f"red", f"blue", f"green", f"black", f"orange", f"yellow", f"purple"], text_color=text_color, selected_color=button_color, command=self.__change_button_color__)
		self.main_screen_settings_customatization_button_color_option.grid(column=0, row=1)

		self.main_screen_settings_customatization_text_color_option.set(text_color)

		self.main_screen_settings_customatization_text_field_color_option.set(text_field_color)

		self.main_screen_settings_customatization_text_field_height_option.set(text_field_text_height)

		self.main_screen_settings_customatization_button_color_option.set(button_color)

		match language_data:
			case "Српски":
				self.main_screen_save_button.configure(text=f"сачувај текст")
	
				self.main_screen_clear_button.configure(text=f"обриши текст")
				self.main_screen_edit_text_button.configure(text=f"уреди текст")
			
				self.main_screen_open_button.configure(text=f"отвори фајл")

				self.main_screen_converter_button.configure(text=f"претварач")
				self.main_screen_pdf_to_word_converter_button.configure(text=f"из Pdf у docx")
				self.main_screen_word_to_pdf_converter_button.configure(text=f"из docx у Pdf")
				self.main_screen_pdf_to_txt_converter_button.configure(text=f"из Pdf у txt")
				self.main_screen_txt_to_pdf_converter_button.configure(text=f"из txt у Pdf")
				self.main_screen_word_to_txt_converter_button.configure(text=f"из docx у txt")
				self.main_screen_txt_to_word_converter_button.configure(text=f"из txt у docx")
				
				self.main_screen_code_editor_button.configure(text="кодови редактор")
				self.main_screen_open_powershell_button.configure(text="отвори powershell")
				self.main_screen_open_terminal_button.configure(text="отвори терминал")
				self.main_screen_save_code_as_button.configure(text="сачувај код као")
				self.main_screen_open_code_button.configure(text="отвори код")

				self.main_screen_settings_button.configure(text=f"подешавања")
				self.main_screen_settings_text.configure(text=f"подешавања")
				self.main_screen_settings_language_text.configure(text=f"језици")
				self.main_screen_settings_autosave_text.configure(text=f"ауточување")
				self.main_screen_settings_autosave_switch.configure(text=f"ауточување")
				self.main_screen_settings_theme_mode_text.configure(text=f"теме")
				self.main_screen_settings_customatization_text.configure(text=f"Спољни изглед")
				self.main_screen_settings_customatization_text_color_text.configure(text=f"Боја текста")
				self.main_screen_settings_customatization_text_field_color_text.configure(text=f"Боја поља")
				self.main_screen_settings_customatization_text_field_height_text.configure(text=f"Висина текста поља")
				self.main_screen_settings_customatization_button_color_text.configure(text=f"Боја дугма")

				self.main_screen_right_click_menu.add_command(label=f"сачувај као", font=(f"Roman", 16), background=button_color, foreground=text_color, command=lambda: self.__save_text__(None))

				self.main_screen_right_click_menu.add_command(label=f"отвори као", font=(f"Roman", 16), background=button_color, foreground=text_color, command=lambda: self.__open_file__(None))

				self.main_screen_right_click_menu.add_cascade(label=f"конвертирај", font=(f"Roman", 16), background=button_color, foreground=text_color, menu=self.main_screen_right_click_convert_menu)
				self.main_screen_right_click_convert_menu.add_command(label=f"из docx у pdf", font=(f"Roman", 16), background=button_color, foreground=text_color, command=self.__docx_to_pdf__)
				self.main_screen_right_click_convert_menu.add_command(label=f"из pdf у docx", font=(f"Roman", 16), background=button_color, foreground=text_color, command=self.__pdf_to_docx__)
				self.main_screen_right_click_convert_menu.add_command(label=f"из txt у pdf", font=(f"Roman", 16), background=button_color, foreground=text_color, command=self.__txt_to_pdf__)
				self.main_screen_right_click_convert_menu.add_command(label=f"из pdf у txt", font=(f"Roman", 16), background=button_color, foreground=text_color, command=self.__pdf_to_txt__)
				self.main_screen_right_click_convert_menu.add_command(label=f"из txt у docx", font=(f"Roman", 16), background=button_color, foreground=text_color, command=self.__txt_to_docx__)
				self.main_screen_right_click_convert_menu.add_command(label=f"из docx у txt", font=(f"Roman", 16), background=button_color, foreground=text_color, command=self.__docx_to_txt__)

				self.main_screen_right_click_menu.add_cascade(label=f"кодирај", font=(f"Roman", 16), background=button_color, foreground=text_color, menu=self.main_screen_right_click_code_menu)
				self.main_screen_right_click_code_menu.add_command(label=f"отвори powershell", font=(f"Roman", 16), background=button_color, foreground=text_color, command=self.__open_powershell__)
				self.main_screen_right_click_code_menu.add_command(label=f"отвори терминал", font=(f"Roman", 16), background=button_color, foreground=text_color, command=self.__open_shell__)
				self.main_screen_right_click_code_menu.add_command(label=f"сачувај код", font=(f"Roman", 16), background=button_color, foreground=text_color, command=lambda: self.__save_code__(None))
				self.main_screen_right_click_code_menu.add_command(label=f"отвори код", font=(f"Roman", 16), background=button_color, foreground=text_color, command=self.__open_code__)

				self.main_screen_right_click_menu.add_separator()

				self.main_screen_right_click_menu.add_command(label=f"обриши текст", font=(f"Roman", 16), background=button_color, foreground=text_color, command=self.__clear_text__)

				self.main_screen_right_click_menu.add_separator()

				self.main_screen_right_click_menu.add_command(label=f"копирај", font=(f"Roman", 16), background=button_color, foreground=text_color, command=self.__copy__)
				self.main_screen_right_click_menu.add_command(label=f"залепи", font=(f"Roman", 16), background=button_color, foreground=text_color, command=self.__paste__)
				self.main_screen_right_click_menu.add_command(label=f"исеци", font=(f"Roman", 16), background=button_color, foreground=text_color, command=self.__cut__)

				self.main_screen_right_click_menu.add_separator()

				self.main_screen_right_click_menu.add_command(label=f"изаћи", font=(f"Roman", 16), background=button_color, foreground=text_color, command=self.__exit__)

			case "English":
				self.main_screen_save_button.configure(text=f"save text")

				self.main_screen_clear_button.configure(text=f"clear text")
				self.main_screen_edit_text_button.configure(text=f"edit text")
			
				self.main_screen_open_button.configure(text=f"open file")

				self.main_screen_converter_button.configure(text=f"converterer")
				self.main_screen_pdf_to_word_converter_button.configure(text=f"from Pdf to docx")
				self.main_screen_word_to_pdf_converter_button.configure(text=f"from docx to Pdf")
				self.main_screen_pdf_to_txt_converter_button.configure(text=f"from Pdf to txt")
				self.main_screen_txt_to_pdf_converter_button.configure(text=f"from txt to Pdf")
				self.main_screen_word_to_txt_converter_button.configure(text=f"from docx to txt")
				self.main_screen_txt_to_word_converter_button.configure(text=f"from txt to docx")

				self.main_screen_code_editor_button.configure(text=f"code editor")
				self.main_screen_open_powershell_button.configure(text=f"open powershell")
				self.main_screen_open_terminal_button.configure(text=f"open terminal")
				self.main_screen_save_code_as_button.configure(text=f"save code as")
				self.main_screen_open_code_button.configure(text=f"open code")

				self.main_screen_settings_button.configure(text=f"settings")
				self.main_screen_settings_text.configure(text=f"settings")
				self.main_screen_settings_language_text.configure(text=f"languages")
				self.main_screen_settings_autosave_text.configure(text=f"autosave")
				self.main_screen_settings_autosave_switch.configure(text=f"autosave")
				self.main_screen_settings_theme_mode_text.configure(text=f"theme")
				self.main_screen_settings_customatization_text.configure(text=f"Customatization")
				self.main_screen_settings_customatization_text_color_text.configure(text=f"Text color")
				self.main_screen_settings_customatization_text_field_color_text.configure(text=f"Text field color")
				self.main_screen_settings_customatization_text_field_height_text.configure(text=f"Text field text height")
				self.main_screen_settings_customatization_button_color_text.configure(text=f"Button color")

				self.main_screen_right_click_menu.add_command(label=f"save as", font=(f"Roman", 16), background=button_color, foreground=text_color, command=lambda: self.__save_text__(None))
			
				self.main_screen_right_click_menu.add_command(label=f"open as", font=(f"Roman", 16), background=button_color, foreground=text_color, command=lambda: self.__open_file__(None))

				self.main_screen_right_click_menu.add_cascade(label=f"convert", font=(f"Roman", 16), background=button_color, foreground=text_color, menu=self.main_screen_right_click_convert_menu)
				self.main_screen_right_click_convert_menu.add_command(label=f"from docx to pdf", font=(f"Roman", 16), background=button_color, foreground=text_color, command=self.__docx_to_pdf__)
				self.main_screen_right_click_convert_menu.add_command(label=f"from pdf to docx", font=(f"Roman", 16), background=button_color, foreground=text_color, command=self.__pdf_to_docx__)
				self.main_screen_right_click_convert_menu.add_command(label=f"from txt to pdf", font=(f"Roman", 16), background=button_color, foreground=text_color, command=self.__txt_to_pdf__)
				self.main_screen_right_click_convert_menu.add_command(label=f"from pdf to txt", font=(f"Roman", 16), background=button_color, foreground=text_color, command=self.__pdf_to_txt__)
				self.main_screen_right_click_convert_menu.add_command(label=f"from txt to docx", font=(f"Roman", 16), background=button_color, foreground=text_color, command=self.__txt_to_docx__)
				self.main_screen_right_click_convert_menu.add_command(label=f"from docx to txt", font=(f"Roman", 16), background=button_color, foreground=text_color, command=self.__docx_to_txt__)

				self.main_screen_right_click_menu.add_cascade(label=f"code", font=(f"Roman", 16), background=button_color, foreground=text_color, menu=self.main_screen_right_click_code_menu)
				self.main_screen_right_click_code_menu.add_command(label=f"open powershell", font=(f"Roman", 16), background=button_color, foreground=text_color, command=self.__open_powershell__)
				self.main_screen_right_click_code_menu.add_command(label=f"open terminal", font=(f"Roman", 16), background=button_color, foreground=text_color, command=self.__open_shell__)
				self.main_screen_right_click_code_menu.add_command(label=f"save code", font=(f"Roman", 16), background=button_color, foreground=text_color, command=lambda: self.__save_code__(None))
				self.main_screen_right_click_code_menu.add_command(label=f"open code", font=(f"Roman", 16), background=button_color, foreground=text_color, command=self.__open_code__)

				self.main_screen_right_click_menu.add_separator()

				self.main_screen_right_click_menu.add_command(label=f"delete text", font=(f"Roman", 16), background=button_color, foreground=text_color, command=self.__clear_text__)

				self.main_screen_right_click_menu.add_separator()

				self.main_screen_right_click_menu.add_command(label=f"copy", font=(f"Roman", 16), background=button_color, foreground=text_color, command=self.__copy__)
				self.main_screen_right_click_menu.add_command(label=f"paste", font=(f"Roman", 16), background=button_color, foreground=text_color, command=self.__paste__)
				self.main_screen_right_click_menu.add_command(label=f"cut", font=(f"Roman", 16), background=button_color, foreground=text_color, command=self.__cut__)

				self.main_screen_right_click_menu.add_separator()

				self.main_screen_right_click_menu.add_command(label=f"exit", font=(f"Roman", 16), background=button_color, foreground=text_color, command=self.__exit__)

			case _:
				self.main_screen_save_button.configure(text=f"сохранить текст")

				self.main_screen_clear_button.configure(text=f"удалить текст")
				self.main_screen_edit_text_button.configure(text=f"редактировать текст")
			
				self.main_screen_open_button.configure(text=f"открыть файл")
		
				self.main_screen_converter_button.configure(text=f"конвертер")
				self.main_screen_pdf_to_word_converter_button.configure(text=f"из Пдф в ворд")
				self.main_screen_word_to_pdf_converter_button.configure(text=f"из ворд в Пдф")
				self.main_screen_pdf_to_txt_converter_button.configure(text=f"из Пдф в текстовый файл")
				self.main_screen_txt_to_pdf_converter_button.configure(text=f"из текстового файла в Пдф")
				self.main_screen_word_to_txt_converter_button.configure(text=f"из ворд в текстовый файл")
				self.main_screen_txt_to_word_converter_button.configure(text=f"из текстового файла в ворд")

				self.main_screen_code_editor_button.configure(text=f"кодовый редактор")
				self.main_screen_open_powershell_button.configure(text=f"открыть powershell")
				self.main_screen_open_terminal_button.configure(text=f"открыть терминал")
				self.main_screen_save_code_as_button.configure(text=f"сохранить код как")
				self.main_screen_open_code_button.configure(text=f"открыть код")

				self.main_screen_settings_button.configure(text=f"настройки")
				self.main_screen_settings_text.configure(text=f"настройки")
				self.main_screen_settings_language_text.configure(text=f"языки")
				self.main_screen_settings_autosave_text.configure(text=f"автосохранение")
				self.main_screen_settings_autosave_switch.configure(text=f"автосохранение")
				self.main_screen_settings_theme_mode_text.configure(text=f"темы")
				self.main_screen_settings_customatization_text.configure(text=f"Внешний вид")
				self.main_screen_settings_customatization_text_color_text.configure(text=f"Цвет текста")
				self.main_screen_settings_customatization_text_field_color_text.configure(text=f"Цвет поля")
				self.main_screen_settings_customatization_text_field_height_text.configure(text=f"Высота текста поля")
				self.main_screen_settings_customatization_button_color_text.configure(text=f"Цвет кнопки")

				self.main_screen_right_click_menu.add_command(label=f"сохранить как", font=(f"Roman", 16), background=button_color, foreground=text_color, command=lambda: self.__save_text__(None))
			
				self.main_screen_right_click_menu.add_command(label=f"открыть как", font=(f"Roman", 16), background=button_color, foreground=text_color, command=lambda: self.__open_file__(None))

				self.main_screen_right_click_menu.add_cascade(label=f"конвертировать", font=(f"Roman", 16), background=button_color, foreground=text_color, menu=self.main_screen_right_click_convert_menu)
				self.main_screen_right_click_convert_menu.add_command(label=f"из ворд в Пдф", font=(f"Roman", 16), background=button_color, foreground=text_color, command=self.__docx_to_pdf__)
				self.main_screen_right_click_convert_menu.add_command(label=f"из Пдф в ворд", font=(f"Roman", 16), background=button_color, foreground=text_color, command=self.__pdf_to_docx__)
				self.main_screen_right_click_convert_menu.add_command(label=f"из текста в Пдф", font=(f"Roman", 16), background=button_color, foreground=text_color, command=self.__txt_to_pdf__)
				self.main_screen_right_click_convert_menu.add_command(label=f"из Пдф в текст", font=(f"Roman", 16), background=button_color, foreground=text_color, command=self.__pdf_to_txt__)
				self.main_screen_right_click_convert_menu.add_command(label=f"из текста в ворд", font=(f"Roman", 16), background=button_color, foreground=text_color, command=self.__txt_to_docx__)
				self.main_screen_right_click_convert_menu.add_command(label=f"из ворда в текст", font=(f"Roman", 16), background=button_color, foreground=text_color, command=self.__docx_to_txt__)

				self.main_screen_right_click_menu.add_cascade(label=f"кодирование", font=(f"Roman", 16), background=button_color, foreground=text_color, menu=self.main_screen_right_click_code_menu)
				self.main_screen_right_click_code_menu.add_command(label=f"открыть терминал", font=(f"Roman", 16), background=button_color, foreground=text_color, command=self.__open_powershell__)
				self.main_screen_right_click_code_menu.add_command(label=f"открыть терминал", font=(f"Roman", 16), background=button_color, foreground=text_color, command=self.__open_shell__)
				self.main_screen_right_click_code_menu.add_command(label=f"сохранить код", font=(f"Roman", 16), background=button_color, foreground=text_color, command=lambda: self.__save_code__(None))
				self.main_screen_right_click_code_menu.add_command(label=f"открыть код", font=(f"Roman", 16), background=button_color, foreground=text_color, command=self.__open_code__)

				self.main_screen_right_click_menu.add_separator()

				self.main_screen_right_click_menu.add_command(label=f"удалить текст", font=(f"Roman", 16), background=button_color, foreground=text_color, command=self.__clear_text__)

				self.main_screen_right_click_menu.add_separator()

				self.main_screen_right_click_menu.add_command(label=f"копировать", font=(f"Roman", 16), background=button_color, foreground=text_color, command=self.__copy__)
				self.main_screen_right_click_menu.add_command(label=f"вставить", font=(f"Roman", 16), background=button_color, foreground=text_color, command=self.__paste__)
				self.main_screen_right_click_menu.add_command(label=f"вырезать", font=(f"Roman", 16), background=button_color, foreground=text_color, command=self.__cut__)

				self.main_screen_right_click_menu.add_separator()

				self.main_screen_right_click_menu.add_command(label=f"выход", font=(f"Roman", 16), background=button_color, foreground=text_color, command=self.__exit__)


		match new_autosaved_data:
			case "on":
				self.main_screen_frame_textbox.insert(f"1.0", autosaved_text)

				self.bind(f"<Return>", self.__text_autosave__)

			case _: self.unbind(f"<Return>")


		self.main_screen_word_counter_variable: int = 0

		self.main_screen_word_counter_data_variable: tkinter.IntVar = tkinter.IntVar(value=self.main_screen_word_counter_variable)

		self.main_screen_word_counter: CTkLabel = CTkLabel(master=self, width=25, height=20, corner_radius=0, textvariable=self.main_screen_word_counter_data_variable)
		self.main_screen_word_counter.place(x=1500, y=0)
				 
	def __frame_resize__(self: typing.Self, event: str | None = None) -> None:
		if self.winfo_width() <= 958:
			self.main_screen_frame.configure(width=1535 / 2 - 2)
			self.main_screen_frame_textbox.configure(width=1535 / 2 - 5)

		else:
			self.main_screen_frame.configure(width=1535)
			self.main_screen_frame_textbox.configure(width=1533.57)

	def __open_taskbar__(self: typing.Self) -> None:
		self.main_screen_taskbar.grid(column=0, row=0)
		self.main_screen_taskbar_button.grid_forget()

	def __close_taskbar__(self: typing.Self, event: str | None = None) -> None:
		self.main_screen_taskbar_button.grid(column=0, row=0)
		self.main_screen_taskbar.grid_forget()

	def __quit_operation__(self: typing.Self) -> None:
		self.main_screen_taskbar_button.configure(text=f"☰", command=self.__open_taskbar__)

		self.main_screen_undo_button.grid(column=1, row=0)
		self.main_screen_redo_button.grid(column=2, row=0)
		self.main_screen_frame.place(x=0, y=22.35)
		self.main_screen_word_counter.place(x=1500, y=0)

		self.main_screen_edit_font_button.grid_forget()
		self.main_screen_edit_size_button.grid_forget()
		self.main_screen_edit_color_button.grid_forget()
		self.main_screen_edit_slant_button.grid_forget()
		self.main_screen_edit_weight_button.grid_forget()
		self.main_screen_edit_underline_button.grid_forget()
		self.main_screen_edit_overstrike_button.grid_forget()

		self.main_screen_pdf_to_word_converter_button.grid_forget()
		self.main_screen_word_to_pdf_converter_button.grid_forget()
		self.main_screen_pdf_to_txt_converter_button.grid_forget()
		self.main_screen_txt_to_pdf_converter_button.grid_forget()
		self.main_screen_word_to_txt_converter_button.grid_forget()
		self.main_screen_txt_to_word_converter_button.grid_forget()

		self.main_screen_open_powershell_button.grid_forget()
		self.main_screen_open_terminal_button.grid_forget()
		self.main_screen_save_code_as_button.grid_forget()
		self.main_screen_open_code_button.grid_forget()

		self.main_screen_settings_text.place_forget()
		self.main_screen_settings_language_text.place_forget()
		self.main_screen_settings_language_option.place_forget()						          
		self.main_screen_settings_autosave_text.place_forget()
		self.main_screen_settings_autosave_switch.place_forget()
		self.main_screen_settings_theme_mode_text.place_forget()
		self.main_screen_settings_theme_mode_option.place_forget()
		self.main_screen_settings_customatization_text.place_forget()
		self.main_screen_settings_customatization_table.place_forget()

	def __undo__(self: typing.Self) -> None:
		try: self.main_screen_frame_textbox.edit_undo()

		except tkinter.TclError: pass

	def __redo__(self: typing.Self) -> None:
		try: self.main_screen_frame_textbox.edit_redo()

		except tkinter.TclError: pass

	@memorise
	def __save_text__(self: typing.Self, event: str | None = None) -> None:
		self.file_name: tkinter.filedialog.asksaveasfilename = tkinter.filedialog.asksaveasfilename(filetypes=[(f"All Files (*.*)", f"*.*"), (f"Text file (*.txt)", f"*.txt"), (f"Docx file (*.docx)", f"*.docx"), (f"Python file (*.py)", f"*.py"), (f"Java file (*.java)", f"*.java"), (f"C# file (*.cs)", f"*.cs"), (f"HTML file (*.html)", f"*.html"), (f"CSS file (*.css)", f"*.css"), (f"JavaScript file (*.js)", f"*.js"), (f"C++ file (*.cpp)", f"*.cpp")], defaultextension=[(f"All Files (*.*)", f"*.*"), (f"Text file (*.txt)", f"*.txt"), (f"Docx file (*.docx)", f"*.docx"), (f"Python file (*.py)", f"*.py"), (f"Java file (*.java)", f"*.java"), (f"C# file (*.cs)", f"*.cs"), (f"HTML file (*.html)", f"*.html"), (f"CSS file (*.css)", f"*.css"), (f"JavaScript file (*.js)", f"*.js"), (f"C++ file (*.cpp)", f"*.cpp")])
		match os.path.splitext(self.file_name)[1]:
			case ".docx":
				try:
					self.file: docx.Document = docx.Document()
					self.file_data: str = self.main_screen_frame_textbox.get(f"1.0", tkinter.END)
					self.file_run: docx.Document = self.file.add_paragraph().add_run(self.file_data)
					self.font: docx.Document = self.file_run.font
					self.font.name: str = self.main_screen_edit_font_button_data
					self.font.size: docx.shared.Pt = docx.shared.Pt(int(self.main_screen_edit_size_button_data))
					match self.main_screen_edit_color_button_data:
						case "black": self.font.color.rgb: docx.shared.RGBColor = docx.shared.RGBColor(0, 0, 0)

						case "white": self.font.color.rgb: docx.shared.RGBColor = docx.shared.RGBColor(255, 255, 255)

						case "red": self.font.color.rgb: docx.shared.RGBColor = docx.shared.RGBColor(250, 0, 0)

						case "green": self.font.color.rgb: docx.shared.RGBColor = docx.shared.RGBColor(0, 255, 0)

						case _: self.font.color.rgb: docx.shared.RGBColor = docx.shared.RGBColor(0, 0, 255)


					match self.main_screen_edit_slant_button_data:
						case "italic": self.file_run.italic: bool = True

						case _: self.file_run.italic: bool = False


					match self.main_screen_edit_weight_button_data:
						case "bold": self.file_run.bold: bool = True

						case _: self.file_run.bold: bool = False


					match self.main_screen_edit_underline_button_data: 
						case "underlined": self.file_run.underline: bool = True

						case _: self.file_run.underline: bool = False


					match self.main_screen_edit_overstrike_button_data:
						case "overstriked": self.font.strike: bool = True

						case _: self.font.strike: bool = False

					self.file.save(self.file_name)

				except FileNotFoundError: pass

				except AttributeError:
					match language_data:
						case "Српски": tkinter.messagebox.showwarning(title=f"Пажња", message=f"Заборавили сте да отредактирате текст")

						case "English": tkinter.messagebox.showwarning(title=f"Warning", message=f"You forgot to edit your text")

						case _: tkinter.messagebox.showwarning(title=f"Внимание", message=f"Вы забыли отредактировать свой текст")

			case _:
				with open(self.file_name, f"w+", encoding=f"UTF-8") as self.file:
					try:
						self.file_data: str = self.main_screen_frame_textbox.get("1.0", tkinter.END)
						self.file.write(self.file_data)
					
					except FileNotFoundError:
						pass
			
	def __clear_text__(self: typing.Self) -> None:
		self.main_screen_frame_textbox.delete(f"1.0", tkinter.END)

	def __edit_text__(self: typing.Self) -> None:
		self.main_screen_taskbar_button.grid(column=0, row=0)
		self.main_screen_edit_font_button.grid(column=1, row=0)
		self.main_screen_edit_size_button.grid(column=2, row=0)
		self.main_screen_edit_color_button.grid(column=3, row=0)
		self.main_screen_edit_slant_button.grid(column=4, row=0)
		self.main_screen_edit_weight_button.grid(column=5, row=0)
		self.main_screen_edit_underline_button.grid(column=6, row=0)
		self.main_screen_edit_overstrike_button.grid(column=7, row=0)

		self.main_screen_taskbar_button.configure(text=f"↵", command=self.__quit_operation__)

		self.main_screen_taskbar.grid_forget()
		
		self.main_screen_undo_button.grid_forget()
		self.main_screen_redo_button.grid_forget()
		self.main_screen_word_counter.place_forget()

	def __edit_text_font__(self: typing.Self, configure: str | None = None) -> None:
		self.main_screen_edit_font_button_data: str = self.main_screen_edit_font_button.get()															 
		self.main_screen_edit_size_button_data: str = self.main_screen_edit_size_button.get()
		self.main_screen_edit_color_button_data: str = self.main_screen_edit_color_button.get()
		self.main_screen_edit_slant_button_data: str = self.main_screen_edit_slant_button.get()
		self.main_screen_edit_weight_button_data: str = self.main_screen_edit_weight_button.get()
		self.main_screen_edit_underline_button_data: str = self.main_screen_edit_underline_button.get()
		self.main_screen_edit_overstrike_button_data: str = self.main_screen_edit_overstrike_button.get()

		self.main_screen_frame_texbox_font.configure(family=self.main_screen_edit_font_button_data, size=int(self.main_screen_edit_size_button_data), slant=self.main_screen_edit_slant_button_data, weight=self.main_screen_edit_weight_button_data)
		self.main_screen_frame_textbox.configure(text_color=self.main_screen_edit_color_button_data)

		match self.main_screen_edit_underline_button_data:
			case "not underlined": self.main_screen_frame_texbox_font.configure(underline=False)			

			case _:	self.main_screen_frame_texbox_font.configure(underline=True)
		
		match self.main_screen_edit_overstrike_button_data:
			case "not overstriked": self.main_screen_frame_texbox_font.configure(overstrike=False)

			case _:	self.main_screen_frame_texbox_font.configure(overstrike=True)

	@memorise
	def __open_file__(self: typing.Self, event: str | None = None) -> None:
		self.opened_name_file: tkinter.filedialog = tkinter.filedialog.askopenfilename(title=f"open file", filetypes=[(f"All Files (*.*)", f"*.*"), (f"Word file (*.docx)", f"*.docx"), (f"Text file (*.txt)", f"*.txt"), (f"Python file (*.py)", f"*.py"), (f"Java file (*.java)", f"*.java"), (f"C# file (*.cs)", f"*.cs"), (f"HTML file (*.html)", f"*.html"), (f"CSS file (*.css)", f"*.css"), (f"JavaScript file (*.js)", f"*.js"), (f"C++ file (*.cpp)", f"*.cpp")], defaultextension=[(f"All Files (*.*)", f"*.*"), (f"Text file (*.txt)", f"*.txt"), (f"Word file (*.docx)", f"*.docx"), (f"Python file (*.py)", f"*.py"), (f"Java file (*.java)", f"*.java"), (f"C# file (*.cs)", f"*.cs"), (f"HTML file (*.html)", f"*.html"), (f"CSS file (*.css)", f"*.css"), (f"JavaScript file (*.js)", f"*.js"), (f"C++ file (*.cpp)", f"*.cpp")])
		match os.path.splitext(self.opened_name_file)[1]:
			case ".docx":
				try:
					self.openned_file: docx.Document = docx.Document(self.opened_name_file)
					self.openned_file_data: list[str] = []
					for self.paragraphs in self.openned_file.paragraphs: self.openned_file_data.append(self.paragraphs.text)

					self.main_screen_frame_textbox.insert(f"1.0", f"\n".join(self.openned_file_data))

				except docx.opc.exceptions.PackageNotFoundError: pass
			
			case _:
				try:
					with open(self.opened_name_file, f"r+", encoding=f"UTF-8") as self.openned_file:
						self.main_screen_frame_textbox.insert(f"1.0", self.openned_file.read())

				except FileNotFoundError: pass

	def __convert__(self: typing.Self) -> None:
		self.main_screen_taskbar_button.grid(column=0, row=0)
		self.main_screen_pdf_to_word_converter_button.grid(column=1, row=0)
		self.main_screen_word_to_pdf_converter_button.grid(column=2, row=0)
		self.main_screen_pdf_to_txt_converter_button.grid(column=3, row=0)
		self.main_screen_txt_to_pdf_converter_button.grid(column=4, row=0)
		self.main_screen_word_to_txt_converter_button.grid(column=5, row=0)
		self.main_screen_txt_to_word_converter_button.grid(column=6, row=0)

		self.main_screen_taskbar_button.configure(text=f"↵", command=self.__quit_operation__)

		self.main_screen_taskbar.grid_forget()

		self.main_screen_undo_button.grid_forget()
		self.main_screen_redo_button.grid_forget()
		self.main_screen_word_counter.place_forget()

	@memorise
	def __pdf_to_docx__(self: typing.Self) -> None:
		try:
			self.file: tkinter.filedialog.askopenfilename = tkinter.filedialog.askopenfilename(title=f"convert pdf file", filetypes=[(f"Pdf file (*.pdf)", f"*.pdf")], defaultextension=[(f"Pdf file (*.pdf)", f"*.pdf")])
			self.converted_file: aspose.words.Document = aspose.words.Document(self.file)
			self.converted_file.save(f"{self.file}.docx")

		except RuntimeError: pass

	@memorise	
	def __docx_to_pdf__(self: typing.Self) -> None:
		try:
			self.file: tkinter.filedialog.askopenfilename = tkinter.filedialog.askopenfilename(title=f"convert docx file", filetypes=[(f"Word file (*.docx)", f"*.docx")], defaultextension=[(f"Word file (*.docx)", f"*.docx")])
			self.converted_file: aspose.words.Document = aspose.words.Document(self.file)
			self.converted_file.save(f"{self.file}.pdf")

		except RuntimeError: pass

	@memorise
	def __pdf_to_txt__(self: typing.Self) -> None:
		try:
			self.file: tkinter.filedialog.askopenfilename = tkinter.filedialog.askopenfilename(title=f"convert pdf file", filetypes=[(f"Pdf file (*.pdf)", f"*.pdf")], defaultextension=[(f"Pdf file (*.pdf)", f"*.pdf")])
			self.converted_file: aspose.words.Document = aspose.words.Document(self.file)
			self.converted_file.save(f"{self.file}.txt")

		except RuntimeError: pass
	
	@memorise	
	def __txt_to_pdf__(self: typing.Self) -> None:
		try:
			self.file: tkinter.filedialog.askopenfilename = tkinter.filedialog.askopenfilename(title=f"convert txt file", filetypes=[(f"Text file (*.txt)", f"*.txt")], defaultextension=[(f"Text file (*.txt)", f"*.txt")])
			self.converted_file: aspose.words.Document = aspose.words.Document(self.file)
			self.converted_file.save(f"{self.file}.pdf")

		except RuntimeError: pass
	
	@memorise
	def __docx_to_txt__(self: typing.Self) -> None:
		try:
			self.file: tkinter.filedialog.askopenfilename = tkinter.filedialog.askopenfilename(title=f"convert docx file", filetypes=[(f"Word file (*.docx)", f"*.docx")], defaultextension=[(f"Word file (*.docx)", f"*.docx")])
			self.converted_file: aspose.words.Document = aspose.words.Document(self.file)
			self.converted_file.save(f"{self.file}.txt")
		
		except RuntimeError: pass

	@memorise
	def __txt_to_docx__(self: typing.Self) -> None:
		try:
			self.file: tkinter.filedialog.askopenfilename = tkinter.filedialog.askopenfilename(title=f"convert txt file", filetypes=[(f"Text file (*.txt)", "*.txt")], defaultextension=[(f"Text file (*.txt)", f"*.txt")])
			self.converted_file: aspose.words.Document = aspose.words.Document(self.file)
			self.converted_file.save(f"{self.file}.docx")

		except RuntimeError: pass

	def __code_editor__(self: typing.Self) -> None:
		self.main_screen_taskbar_button.grid(column=0, row=0)
		self.main_screen_open_powershell_button.grid(column=3, row=0)
		self.main_screen_open_terminal_button.grid(column=4, row=0)
		self.main_screen_save_code_as_button.grid(column=5, row=0)
		self.main_screen_open_code_button.grid(column=6, row=0)

		self.main_screen_taskbar_button.configure(text=f"↵", command=self.__quit_operation__)

		self.main_screen_taskbar.grid_forget()
		self.main_screen_word_counter.place_forget()

	def __open_powershell__(self: typing.Self) -> None:
		subprocess.run([f"powershell.exe"])

	def __open_shell__(self: typing.Self) -> None:
		subprocess.run([f"cmd.exe"])

	@memorise
	def __save_code__(self: typing.Self, event: str | None = None) -> None:
		try:
			with open(tkinter.filedialog.asksaveasfilename(filetypes=[(f"Python file (*.py)", f"*.py")], defaultextension=[(f"Python file (*.py)", f"*.py")]), f"w+", encoding=f"UTF-8") as self.script_file:
				self.script_file_data: str = self.main_screen_frame_textbox.get(f"1.0", tkinter.END)
				self.script_file.write(self.script_file_data)
				
		
		except FileNotFoundError: pass

	@memorise
	def __open_code__(self: typing.Self) -> None:
		try:
			with open(tkinter.filedialog.askopenfilename(title=f"open script file", filetypes=[(f"Python file (*.py)", f"*.py")], defaultextension=[(f"Python file (*.py)", f"*.py")]), f"r+", encoding=f"UTF-8") as self.openned_script_file:
				self.main_screen_frame_textbox.insert(f"1.0", self.openned_script_file.read())

		except FileNotFoundError: pass
		
	def __settings__(self: typing.Self) -> None:
		self.main_screen_taskbar_button.grid(column=0, row=0)
		self.main_screen_settings_text.place(x=3, y=21)
		self.main_screen_settings_language_text.place(x=3, y=102)
		self.main_screen_settings_language_option.place(x=18, y=142)
		self.main_screen_settings_autosave_text.place(x=3, y=182)
		self.main_screen_settings_autosave_switch.place(x=18, y=222)
		self.main_screen_settings_theme_mode_text.place(x=3, y=262)
		self.main_screen_settings_theme_mode_option.place(x=18, y=302)
		self.main_screen_settings_customatization_text.place(x=18, y=342)
		self.main_screen_settings_customatization_table.place(x=3, y=382)

		self.main_screen_taskbar_button.configure(text=f"↵", command=self.__quit_operation__)

		self.main_screen_taskbar.grid_forget()

		self.main_screen_undo_button.grid_forget()
		self.main_screen_redo_button.grid_forget()
		self.main_screen_word_counter.place_forget()
		self.main_screen_frame.place_forget()

	def __language_settings__(self: typing.Self, pickle_serialization: pickle) -> None:
		self.main_screen_settings_language_option_variable: str = self.main_screen_settings_language_option.get()
		with open(f"my_diary_settings.pickle", f"wb+") as self.data:
			pickle.dump(self.main_screen_settings_language_option_variable, self.data)

		match self.main_screen_settings_language_option_variable: 
			case "Српски": tkinter.messagebox.showwarning(title=f"Пажња", message=f"Рестартуј програм")

			case "English": tkinter.messagebox.showwarning(title=f"Warning", message=f"Restart program")

			case _: tkinter.messagebox.showwarning(title=f"Внимание", message=f"Перезагрузите программу")

	def __autosave_settings__(self: typing.Self, pickle_serialization: pickle) -> None:
		self.main_screen_settings_autosave_switch_value: str = self.main_screen_settings_autosave_value.get()
		with open(f"my_diary_autosave_settings.pickle", f"wb+") as self.autosave_data:
			pickle.dump(self.main_screen_settings_autosave_switch_value, self.autosave_data)

		match language_data: 
			case "Српски": tkinter.messagebox.showwarning(title=f"Пажња", message=f"Рестартуј програм")

			case "English": tkinter.messagebox.showwarning(title=f"Warning", message=f"Restart program")

			case _: tkinter.messagebox.showwarning(title=f"Внимание", message=f"Перезагрузите программу")

	def __text_autosave__(self: typing.Self, pickle_serialization: pickle) -> None:
		self.main_screen_frame_textbox_text_data: str = self.main_screen_frame_textbox.get("1.0", tkinter.END)
		with open(f"settings\my_diary_saved_text.pickle", f"wb+") as self.text_data:
			pickle.dump(self.main_screen_frame_textbox_text_data, self.text_data)

	def __theme_settings__(self: typing.Self, pickle_serialization: pickle) -> None:
		self.main_screen_settings_theme_mode_option_data: str = self.main_screen_settings_theme_mode_option.get()
		with open(f"my_diary_theme_settings.pickle", f"wb+") as self.theme_data:
			pickle.dump(self.main_screen_settings_theme_mode_option_data, self.theme_data)

		match language_data: 
			case "Српски": tkinter.messagebox.showwarning(title=f"Пажња", message=f"Рестартуј програм")

			case "English": tkinter.messagebox.showwarning(title=f"Warning", message=f"Restart program")

			case _: tkinter.messagebox.showwarning(title=f"Внимание", message=f"Перезагрузите программу")

	def __change_text_color__(self: typing.Self, pickle_serialization: pickle) -> None:
		self.main_screen_settings_customatization_text_color_option_data: str = self.main_screen_settings_customatization_text_color_option.get()
		with open(f"my_diary_text_color.pickle", f"wb+") as self.text_color_data:
			pickle.dump(self.main_screen_settings_customatization_text_color_option_data, self.text_color_data)

		match language_data: 
			case "Српски": tkinter.messagebox.showwarning(title=f"Пажња", message=f"Рестартуј програм")

			case "English": tkinter.messagebox.showwarning(title=f"Warning", message=f"Restart program")

			case _: tkinter.messagebox.showwarning(title=f"Внимание", message=f"Перезагрузите программу")

	def __change_text_field_color__(self: typing.Self, pickle_serialization: pickle) -> None:
		self.main_screen_settings_customatization_text_field_color_option_data: str = self.main_screen_settings_customatization_text_field_color_option.get()
		with open(f"my_diary_text_field_color.pickle", f"wb+") as self.text_field_color_data:
			pickle.dump(self.main_screen_settings_customatization_text_field_color_option_data, self.text_field_color_data)

		match language_data: 
			case "Српски": tkinter.messagebox.showwarning(title=f"Пажња", message=f"Рестартуј програм")

			case "English": tkinter.messagebox.showwarning(title=f"Warning", message=f"Restart program")

			case _: tkinter.messagebox.showwarning(title=f"Внимание", message=f"Перезагрузите программу")

	def __change_text_field_text_height__(self: typing.Self, pickle_serialization: pickle) -> None:
		self.main_screen_settings_customatization_text_field_height_option_data: str = self.main_screen_settings_customatization_text_field_height_option.get()
		with open(f"my_diary_text_field_text_height.pickle", f"wb+") as self.text_field_text_height_data:
			pickle.dump(self.main_screen_settings_customatization_text_field_height_option_data, self.text_field_text_height_data)

		match language_data: 
			case "Српски": tkinter.messagebox.showwarning(title=f"Пажња", message=f"Рестартуј програм")

			case "English": tkinter.messagebox.showwarning(title=f"Warning", message=f"Restart program")

			case _: tkinter.messagebox.showwarning(title=f"Внимание", message=f"Перезагрузите программу")

	def __change_button_color__(self: typing.Self, pickle_serialization: pickle) -> None:
		self.main_screen_settings_customatization_button_color_option_data: str = self.main_screen_settings_customatization_button_color_option.get()
		with open(f"my_diary_button_color.pickle", f"wb+") as self.button_color_data:
			pickle.dump(self.main_screen_settings_customatization_button_color_option_data, self.button_color_data)

		match language_data: 
			case "Српски": tkinter.messagebox.showwarning(title=f"Пажња", message=f"Рестартуј програм")

			case "English": tkinter.messagebox.showwarning(title=f"Warning", message=f"Restart program")

			case _: tkinter.messagebox.showwarning(title=f"Внимание", message=f"Перезагрузите программу")

	def __word_count__(self: typing.Self, event: str | None = None) -> None:
		self.main_screen_frame_textbox_data: str = self.main_screen_frame_textbox.get(f"0.0", tkinter.END)
		self.main_screen_word_counter_data_variable.set(value=len(self.main_screen_frame_textbox_data.split()))
		
	def __drop_file_into_textbox__(self: typing.Self, event: str | None = None) -> None:
		self.main_screen_frame_textbox.delete(f"1.0", tkinter.END)
		if event.data.endswith(f".docx"):
			try:
				self.openned_file: docx.Document = docx.Document(event.data)
				self.openned_file_data: list[str] = []
				for self.paragraphs in self.openned_file.paragraphs: self.openned_file_data.append(self.paragraphs.text)

				self.main_screen_frame_textbox.insert(f"1.0", f"\n".join(self.openned_file_data))

			except docx.opc.exceptions.PackageNotFoundError: pass

		else:
			try:
				with open(event.data, f"r+", encoding=f"UTF-8") as self.openned_file:
					self.main_screen_frame_textbox.insert(f"1.0", self.openned_file.read())

			except FileNotFoundError: pass
				

	def __fullscreen__(self: typing.Self, event: str | None = None) -> None:
		self.main_screen_fullscreen_numbers += 1
		if self.main_screen_fullscreen_numbers % 2 == 0:
			self.attributes(f"-fullscreen", True)
			
			self.main_screen_frame.configure(height=840.55)
			self.main_screen_frame_textbox.configure(height=839)
		
		else:
			self.attributes(f"-fullscreen", False)

			self.main_screen_frame.configure(height=769)
			self.main_screen_frame_textbox.configure(height=767.5)

	def __open_terminal__(self: typing.Self, event: str | None = None) -> None:
		try:
			import My_Diary_command_prompt
		
			self.terminal_frame: My_Diary_command_prompt.Terminal = My_Diary_command_prompt.Terminal()
		
		except ImportError:
			match language_data: 
				case "Српски": tkinter.messagebox.showerror(title=f"Грешка", message=f"Нема те фајл са терминалом")

				case "English": tkinter.messagebox.showerror(title=f"Error", message=f"You don't have terminal file")

				case _: tkinter.messagebox.showerror(title=f"Ошибка", message=f"У вас нет файла с терминалом")

	def __html_script__(self: typing.Self, event: str | None = None) -> None:
		self.main_screen_frame_textbox.insert(f"0.0", f"<!DOCTYPE html> \n  \n  <html lang='en'> \n <head> \n <meta charset='utf-8' /> \n <title></title> \n </head> \n <body> \n \n </body> \n </html>")

	def __right_click_menu__(self: typing.Self, event: str | None = None)-> None:
		try: self.main_screen_right_click_menu.tk_popup(event.x_root, event.y_root)

		finally: self.main_screen_right_click_menu.grab_release()

	def __copy__(self: typing.Self) -> str:
		self.main_screen_frame_textbox_text_data: str = self.main_screen_frame_textbox.selection_get()
		return self.main_screen_frame_textbox_text_data

	def __paste__(self: typing.Self) -> None:
		self.main_screen_frame_textbox.insert(self.main_screen_frame_textbox.index(f"insert"), str(self.main_screen_frame_textbox_text_data))

	def __cut__(self: typing.Self) -> None:
		self.main_screen_frame_textbox.delete(self.main_screen_frame_textbox.index(f"sel.first"), self.main_screen_frame_textbox.index(f"sel.last"))	  																																			   

	def __exit__(self: typing.Self) -> None:
		match language_data: 
			case "Српски":
				self.main_screen_exit: tkinter.messagebox.askyesno = tkinter.messagebox.askyesno(title=f"излаз", message=f"желите да изађете?")
				if self.main_screen_exit: sys.exit()
				else: pass

			case "English":
				self.main_screen_exit: tkinter.messagebox.askyesno = tkinter.messagebox.askyesno(title=f"exit", message=f"would you like to exit?")
				if self.main_screen_exit: sys.exit()
				else: pass

			case _:
				self.main_screen_exit: tkinter.messagebox.askyesno = tkinter.messagebox.askyesno(title=f"выход", message=f"желайте выйти?")
				if self.main_screen_exit: sys.exit()
				else: pass
			
	def __run__(self: typing.Self) -> None:
		try: self.mainloop()
															 
		except FileNotFoundError: tkinter.messagebox.showerror(title=f"file not found error", message=f"срб: грешка: није нађен фајл \n eng: error: missing data file \nрус: ошибка: не найден файл")

		except tkinter.TclError: tkinter.messagebox.showerror(title=f"icon file not found error", message=f"срб: грешка: није нађен фајл иконица \neng: error: missing icon file \nрус: ошибка: не найден файл с иконкой")

		except EOFError: tkinter.messagebox.showerror(title=f"corrupted file error", message=f"срб: грешка: повређен фајл \n eng: error: corrupted data file \nрус: ошибка: повреждён файл")

if __name__ == f"__main__":
    program: Program = Program()
    program.__run__()