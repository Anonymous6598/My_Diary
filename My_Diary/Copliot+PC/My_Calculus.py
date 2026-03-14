from math import *
from My_Calculus_math_functions import *
import customtkinter, tkinter, pickle, unicodedata, sys, numpy, matplotlib, matplotlib.pyplot, typing, My_Calculus_interface, locale, re, warnings, My_Calculus_AI_window_interface, My_Calculus_AI, speech_recognition, threading

with open(f"my_calculus_text_color.pickle", f"rb+") as text_color_data: text_color: str = pickle.load(text_color_data)

with open(f"my_calculus_expression_entry_color.pickle", f"rb+") as expression_entry_color_data: expression_entry_color: str = pickle.load(expression_entry_color_data)

with open(f"my_calculus_expression_entry_text_color.pickle", f"rb+") as expression_entry_text_color_data: expression_entry_text_color: str = pickle.load(expression_entry_text_color_data)

with open(f"my_calculus_button_color.pickle", f"rb+") as button_color_data: button_color: str = pickle.load(button_color_data)

matplotlib.use(f"TKAgg")

warnings.filterwarnings(f"ignore")

SLM: My_Calculus_AI.My_Calculus_LM = My_Calculus_AI.My_Calculus_LM().__initialize_model__()

class Program(customtkinter.CTk, My_Calculus_interface.My_Calculus_interface):

	WIDTH: typing.Final[int] = 500
	HEIGHT: typing.Final[int] = 565
	TITLE: typing.Final[str] = f"My Calculus (Copliot+PC edition)"
	COLOR_THEME: typing.Final[str] = f"dark-blue"
	ICON: typing.Final[str] = f"my calculus icon.ico"
	WIDGET_SCALING: typing.Final[float] = 1.251

	def __init__(self: typing.Self, *args, **kwargs) -> None:
		customtkinter.CTk.__init__(self, *args, **kwargs)

		customtkinter.set_widget_scaling(self.WIDGET_SCALING)
		customtkinter.set_default_color_theme(self.COLOR_THEME)
		customtkinter.deactivate_automatic_dpi_awareness()

		self.minsize(width=self.WIDTH, height=self.HEIGHT)
		self.resizable(False, False)
		self.title(self.TITLE)
		self.iconbitmap(self.ICON)
		self.protocol(f"WM_DELETE_WINDOW", lambda: sys.exit())

		self.main_screen_entry_frame: customtkinter.CTkFrame = customtkinter.CTkFrame(master=self, width=480, height=200, fg_color=expression_entry_color)
		self.main_screen_entry_frame.grid(column=0, row=0, columnspan=5000)

		self.main_screen_expression_entry: customtkinter.CTkEntry = customtkinter.CTkEntry(master=self.main_screen_entry_frame, width=475, height=120, fg_color=f"transparent", border_width=0, text_color=expression_entry_text_color, font=(f"Roboto Bold", 135))
		self.main_screen_expression_entry.place(x=2, y=2)

		self.main_screen_expression_entry.bind("<Button-3>", lambda event: self.main_screen_right_click_expression_entry_menu.post(event.x_root, event.y_root))

		self.main_screen_result_entry: customtkinter.CTkEntry = customtkinter.CTkEntry(master=self.main_screen_entry_frame, width=475, height=20, fg_color=f"transparent", border_width=0, text_color=expression_entry_text_color, font=(f"Roboto Bold", 25), state=f"disabled")
		self.main_screen_result_entry.place(x=2, y=165)

		self.main_screen_result_entry.bind("<Button-3>", lambda event: self.main_screen_right_click_result_entry_menu.post(event.x_root, event.y_root))

		self.main_screen_procent_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"%", height=50, width=60, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: self.__button_operation__(f"%"))
		self.main_screen_procent_button.grid(column=0, row=1, sticky=f"w")

		self.main_screen_sqrt_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=fr"\/", height=50, width=60, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: self.__button_operation__(f"sqrt()"))
		self.main_screen_sqrt_button.grid(column=1, row=1, sticky=f"w")

		self.main_screen_one_divided_by_x_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"1/x", height=50, width=60, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: self.__button_operation__(f"1/"))
		self.main_screen_one_divided_by_x_button.grid(column=2, row=1, sticky=f"w")

		self.main_screen_number_in_second_degree_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"x2", height=50, width=60, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: self.__button_operation__(f"**2"))
		self.main_screen_number_in_second_degree_button.grid(column=3, row=1, sticky=f"w")

		self.main_screen_clear_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"C", height=50, width=60, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: self.main_screen_expression_entry.delete(f"0", tkinter.END))
		self.main_screen_clear_button.grid(column=4, row=1, sticky=f"w")
		
		self.main_screen_clear_everything_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"CE", height=50, width=60, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=self.__clear_everything__)
		self.main_screen_clear_everything_button.grid(column=5, row=1, sticky=f"w")
																												  
		self.main_screen_clear_number_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"<-", height=50, width=60, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: self.main_screen_expression_entry.delete(len(self.main_screen_expression_entry.get()) - 1, tkinter.END))
		self.main_screen_clear_number_button.grid(column=6, row=1, sticky=f"w")

		self.main_screen_plus_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"+", height=50, width=60, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: self.__button_operation__(f"+"))
		self.main_screen_plus_button.grid(column=7, row=1, sticky=f"w")

		self.main_screen_minus_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"-", height=50, width=60, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: self.__button_operation__(f"-"))
		self.main_screen_minus_button.grid(column=7, row=2, sticky=f"w")

		self.main_screen_multiply_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"*", height=50, width=60, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: self.__button_operation__(f"*"))
		self.main_screen_multiply_button.grid(column=7, row=3, sticky=f"e")

		self.main_screen_divide_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"/", height=50, width=60, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: self.__button_operation__(f"/"))
		self.main_screen_divide_button.grid(column=7, row=4, sticky=f"e")

		self.main_screen_equal_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"=", height=50, width=60, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=self.__equation__)
		self.main_screen_equal_button.grid(column=7, row=5, sticky=f"e")

		self.main_screen_number_one_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"1", height=67, width=100, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: self.__button_operation__(f"1"))
		self.main_screen_number_one_button.place(x=0, y=250)
		
		self.main_screen_number_two_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"2", height=67, width=100, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: self.__button_operation__(f"2"))
		self.main_screen_number_two_button.place(x=100, y=250)

		self.main_screen_number_three_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"3", height=67, width=100, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: self.__button_operation__(f"3"))
		self.main_screen_number_three_button.place(x=200, y=250)

		self.main_screen_number_four_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"4", height=67, width=100, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: self.__button_operation__(f"4"))
		self.main_screen_number_four_button.place(x=0, y=317.5)

		self.main_screen_number_five_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"5", height=67, width=100, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: self.__button_operation__(f"5"))
		self.main_screen_number_five_button.place(x=100, y=317.5)

		self.main_screen_number_six_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"6", height=67, width=100, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: self.__button_operation__(f"6"))
		self.main_screen_number_six_button.place(x=200, y=317.5)

		self.main_screen_number_seven_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"7", height=67, width=100, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: self.__button_operation__(f"7"))
		self.main_screen_number_seven_button.place(x=0, y=385)

		self.main_screen_number_eight_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"8", height=67, width=100, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: self.__button_operation__("8"))
		self.main_screen_number_eight_button.place(x=100, y=385)

		self.main_screen_number_nine_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"9", height=67, width=100, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: self.__button_operation__(f"9"))
		self.main_screen_number_nine_button.place(x=200, y=385)

		self.main_screen_number_zero_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"0", height=50, width=119.902, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: self.__button_operation__(f"0"))
		self.main_screen_number_zero_button.place(x=300, y=250)

		self.main_screen_negative_number_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"+/-", height=50, width=119.902, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: self.__button_operation__(f"-"))
		self.main_screen_negative_number_button.place(x=300, y=300.5)

		self.main_screen_comma_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f".", height=50, width=119.902, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: self.__button_operation__(f"."))
		self.main_screen_comma_button.place(x=300, y=351)

		self.main_screen_mode_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"режим", height=50, width=119.902, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=self.__mode_option__)
		self.main_screen_mode_button.place(x=300, y=401)

		self.main_screen_pi_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=unicodedata.lookup(f"GREEK SMALL LETTER PI"), height=50, width=60, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: self.__button_operation__(f"pi"))

		self.main_screen_e_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"e", height=50, width=60, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: self.__button_operation__(f"e"))

		self.main_screen_cbrt_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=fr"3\/", height=50, width=60, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: self.__button_operation__(f"cbrt()"))

		self.main_screen_number_in_third_degree_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"x3", height=50, width=60, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: self.__button_operation__(f"**3"))

		self.main_screen_number_module_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"|x|", height=50, width=60, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: self.__button_operation__(f"fabs()"))

		self.main_screen_factorial_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"x!", height=50, width=60, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: self.__button_operation__(f"factorial()"))

		self.main_screen_left_bracket_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"(", height=50, width=60, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: self.__button_operation__(f"("))

		self.main_screen_right_bracket_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f")", height=50, width=60, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: self.__button_operation__(f")"))   

		self.main_screen_base_option: customtkinter.CTkComboBox = customtkinter.CTkComboBox(master=self, values=[f"binary-octal", f"binary-decimal", f"binary-hexadecimal", f"octal-binary", f"octal-decimal", f"octal-hexadecimal", f"decimal-binary", f"decimal-octal", f"decimal-hexadecimal", f"hexadecimal-binary", f"hexadecimal-octal", f"hexadecimal-decimal"], height=50, width=479.7,  fg_color=button_color, border_color=button_color, button_color=button_color, button_hover_color=button_color, dropdown_fg_color=button_color, text_color=text_color, dropdown_text_color=text_color, font=(f"Roboto Bold", 32), dropdown_font=(f"Roboto Bold", 32), command=self.__change_base__)  

		self.main_screen_x_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"x", height=50, width=60, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: self.__button_operation__(f"x"))   

		self.main_screen_right_click_expression_entry_menu: tkinter.Menu = tkinter.Menu(self.main_screen_expression_entry, tearoff=0)
		
		self.main_screen_right_click_result_entry_menu: tkinter.Menu = tkinter.Menu(self.main_screen_result_entry, tearoff=0)     

		self.main_screen_mode_button.configure(text=f"mode")

		self.main_screen_right_click_expression_entry_menu.add_command(label=f"copy", command=self.__copy__)
		self.main_screen_right_click_expression_entry_menu.add_command(label=f"paste", command=self.__paste__)
		self.main_screen_right_click_expression_entry_menu.add_command(label=f"cut", command=self.__cut__)

		self.main_screen_right_click_result_entry_menu.add_command(label=f"copy result", command=self.__copy_result__)

	@typing.override
	def __classical__(self: typing.Self) -> None:
		self.main_screen_expression_entry.configure(height=120)
		self.main_screen_equal_button.configure(command=self.__equation__)

		self.minsize(width=self.WIDTH, height=self.HEIGHT)
		
		self.main_screen_result_entry.place(x=2, y=165)

		self.main_screen_number_zero_button.configure(width=119.902)
		self.main_screen_negative_number_button.configure(width=119.902)
		self.main_screen_comma_button.configure(width=119.902)
		self.main_screen_mode_button.configure(width=119.902)

		self.main_screen_procent_button.grid(column=0, row=1, sticky=f"w")
		self.main_screen_sqrt_button.grid(column=1, row=1, sticky=f"w")
		self.main_screen_one_divided_by_x_button.grid(column=2, row=1, sticky=f"w")
		self.main_screen_number_in_second_degree_button.grid(column=3, row=1, sticky=f"w")
		self.main_screen_clear_button.grid(column=4, row=1, sticky=f"w")
		self.main_screen_clear_everything_button.grid(column=5, row=1, sticky=f"w")
		self.main_screen_clear_number_button.grid(column=6, row=1, sticky=f"w")
		self.main_screen_plus_button.grid(column=7, row=1, sticky=f"w")
		self.main_screen_minus_button.grid(column=7, row=2, sticky=f"w")
		self.main_screen_multiply_button.grid(column=7, row=3, sticky=f"e")
		self.main_screen_divide_button.grid(column=7, row=4, sticky=f"e")
		self.main_screen_equal_button.grid(column=7, row=5, sticky=f"e")

		self.main_screen_number_one_button.place(x=0, y=250)
		self.main_screen_number_two_button.place(x=100, y=250)
		self.main_screen_number_three_button.place(x=200, y=250)
		self.main_screen_number_four_button.place(x=0, y=317.5)
		self.main_screen_number_five_button.place(x=100, y=317.5)
		self.main_screen_number_six_button.place(x=200, y=317.5)
		self.main_screen_number_seven_button.place(x=0, y=385)
		self.main_screen_number_eight_button.place(x=100, y=385)
		self.main_screen_number_nine_button.place(x=200, y=385)

		self.main_screen_number_zero_button.place(x=300, y=250)
		self.main_screen_negative_number_button.place(x=300, y=300.5)
		self.main_screen_comma_button.place(x=300, y=351)
		self.main_screen_mode_button.place(x=300, y=401)

		self.main_screen_pi_button.grid_forget()
		self.main_screen_e_button.grid_forget()
		self.main_screen_cbrt_button.grid_forget()
		self.main_screen_number_in_third_degree_button.grid_forget()
		self.main_screen_number_module_button.grid_forget()
		self.main_screen_factorial_button.grid_forget()
		self.main_screen_left_bracket_button.grid_forget()
		self.main_screen_right_bracket_button.grid_forget()

		try:
			self.main_screen_scientific_calculator_additional_layout.destroy()
			self.main_screen_graphical_calculator_additional_layout.destroy()

		except AttributeError: pass

		self.main_screen_base_option.place_forget()
		self.main_screen_x_button.grid_forget()

	@typing.override
	def __scientific__(self: typing.Self) -> None: 
		self.main_screen_expression_entry.configure(height=120) 
		self.main_screen_equal_button.configure(command=self.__equation__)
		
		self.minsize(width=self.WIDTH, height=628)
		
		self.main_screen_result_entry.place(x=2, y=165)

		self.main_screen_number_zero_button.configure(width=119.902)
		self.main_screen_negative_number_button.configure(width=119.902)
		self.main_screen_comma_button.configure(width=119.902)
		self.main_screen_mode_button.configure(width=119.902)

		self.main_screen_pi_button.grid(column=0, row=1, sticky=f"w")
		self.main_screen_e_button.grid(column=1, row=1, sticky=f"w")
		self.main_screen_cbrt_button.grid(column=2, row=1, sticky=f"w")
		self.main_screen_number_in_third_degree_button.grid(column=3, row=1, sticky=f"w")
		self.main_screen_number_module_button.grid(column=4, row=1, sticky=f"w")
		self.main_screen_factorial_button.grid(column=5, row=1, sticky=f"w")
		self.main_screen_left_bracket_button.grid(column=6, row=1, sticky=f"w")
		self.main_screen_right_bracket_button.grid(column=7, row=1, sticky=f"w")

		self.main_screen_procent_button.grid(column=0, row=2, sticky=f"w")
		self.main_screen_sqrt_button.grid(column=1, row=2, sticky=f"w")
		self.main_screen_one_divided_by_x_button.grid(column=2, row=2, sticky=f"w")
		self.main_screen_number_in_second_degree_button.grid(column=3, row=2, sticky=f"w")
		self.main_screen_clear_button.grid(column=4, row=2, sticky=f"w")
		self.main_screen_clear_everything_button.grid(column=5, row=2, sticky=f"w")
		self.main_screen_clear_number_button.grid(column=6, row=2, sticky=f"w")
		self.main_screen_plus_button.grid(column=7, row=2, sticky=f"w")
		self.main_screen_minus_button.grid(column=7, row=3, sticky=f"w")
		self.main_screen_multiply_button.grid(column=7, row=4, sticky=f"e")
		self.main_screen_divide_button.grid(column=7, row=5, sticky=f"e")
		self.main_screen_equal_button.grid(column=7, row=6, sticky=f"e")

		self.main_screen_number_one_button.place(x=0, y=300)
		self.main_screen_number_two_button.place(x=100, y=300)
		self.main_screen_number_three_button.place(x=200, y=300)
		self.main_screen_number_four_button.place(x=0, y=367.5)
		self.main_screen_number_five_button.place(x=100, y=367.5)
		self.main_screen_number_six_button.place(x=200, y=367.5)
		self.main_screen_number_seven_button.place(x=0, y=436)
		self.main_screen_number_eight_button.place(x=100, y=436)
		self.main_screen_number_nine_button.place(x=200, y=436)

		self.main_screen_number_zero_button.place(x=300, y=300)
		self.main_screen_negative_number_button.place(x=300, y=350.5)
		self.main_screen_comma_button.place(x=300, y=401)
		self.main_screen_mode_button.place(x=300, y=452)

		self.main_screen_base_option.place_forget()
		self.main_screen_x_button.grid_forget()

		self.main_screen_scientific_calculator_additional_layout: Scientific_calculator_additional_layout = Scientific_calculator_additional_layout()

	@typing.override
	def __programming__(self: typing.Self) -> None:
		self.main_screen_expression_entry.configure(height=120)
		self.main_screen_equal_button.configure(command=self.__equation__)
		
		self.minsize(width=self.WIDTH, height=self.HEIGHT)
		
		self.main_screen_result_entry.place(x=2, y=165)

		self.main_screen_number_zero_button.configure(width=179.902)
		self.main_screen_negative_number_button.configure(width=179.902)
		self.main_screen_comma_button.configure(width=179.902)
		self.main_screen_mode_button.configure(width=179.902)

		self.main_screen_base_option.place(x=0, y=200)

		self.main_screen_number_one_button.place(x=0, y=250)
		self.main_screen_number_two_button.place(x=100, y=250)
		self.main_screen_number_three_button.place(x=200, y=250)
		self.main_screen_number_four_button.place(x=0, y=317.5)
		self.main_screen_number_five_button.place(x=100, y=317.5)
		self.main_screen_number_six_button.place(x=200, y=317.5)
		self.main_screen_number_seven_button.place(x=0, y=385)
		self.main_screen_number_eight_button.place(x=100, y=385)
		self.main_screen_number_nine_button.place(x=200, y=385)

		self.main_screen_number_zero_button.place(x=300, y=250)
		self.main_screen_negative_number_button.place(x=300, y=300.5)
		self.main_screen_comma_button.place(x=300, y=351)
		self.main_screen_mode_button.place(x=300, y=401)

		self.main_screen_pi_button.grid_forget()
		self.main_screen_e_button.grid_forget()
		self.main_screen_cbrt_button.grid_forget()
		self.main_screen_number_in_third_degree_button.grid_forget()
		self.main_screen_number_module_button.grid_forget()
		self.main_screen_factorial_button.grid_forget()
		self.main_screen_left_bracket_button.grid_forget()
		self.main_screen_right_bracket_button.grid_forget()

		self.main_screen_procent_button.grid_forget()
		self.main_screen_sqrt_button.grid_forget()
		self.main_screen_one_divided_by_x_button.grid_forget()
		self.main_screen_number_in_second_degree_button.grid_forget()
		self.main_screen_clear_button.grid_forget()
		self.main_screen_clear_everything_button.grid_forget()
		self.main_screen_clear_number_button.grid_forget()
		self.main_screen_plus_button.grid_forget()
		self.main_screen_minus_button.grid_forget()
		self.main_screen_multiply_button.grid_forget()
		self.main_screen_divide_button.grid_forget()
		self.main_screen_equal_button.grid_forget()
		self.main_screen_x_button.grid_forget()
	
	@typing.override
	def __graphical__(self: typing.Self) -> None:
		self.main_screen_expression_entry.configure(height=195)
		self.main_screen_equal_button.configure(command=self.__plot__)

		self.main_screen_base_option.place_forget()
		
		self.main_screen_result_entry.place_forget()
		
		self.minsize(width=self.WIDTH, height=self.HEIGHT)

		self.main_screen_number_zero_button.configure(width=119.902)
		self.main_screen_negative_number_button.configure(width=119.902)
		self.main_screen_comma_button.configure(width=119.902)
		self.main_screen_mode_button.configure(width=119.902)

		self.main_screen_left_bracket_button.grid(column=0, row=1, sticky=f"w")
		self.main_screen_right_bracket_button.grid(column=1, row=1, sticky=f"w")
		self.main_screen_one_divided_by_x_button.grid(column=2, row=1, sticky=f"w")
		self.main_screen_number_in_second_degree_button.grid(column=3, row=1, sticky=f"w")
		self.main_screen_x_button.grid(column=4, row=1, sticky=f"w")
		self.main_screen_clear_everything_button.grid(column=5, row=1, sticky=f"w")
		self.main_screen_clear_number_button.grid(column=6, row=1, sticky=f"w")
		self.main_screen_plus_button.grid(column=7, row=1, sticky=f"w")
		self.main_screen_minus_button.grid(column=7, row=2, sticky=f"w")
		self.main_screen_multiply_button.grid(column=7, row=3, sticky=f"e")
		self.main_screen_divide_button.grid(column=7, row=4, sticky=f"e")
		self.main_screen_equal_button.grid(column=7, row=5, sticky=f"e")

		self.main_screen_number_one_button.place(x=0, y=250)
		self.main_screen_number_two_button.place(x=100, y=250)
		self.main_screen_number_three_button.place(x=200, y=250)
		self.main_screen_number_four_button.place(x=0, y=317.5)
		self.main_screen_number_five_button.place(x=100, y=317.5)
		self.main_screen_number_six_button.place(x=200, y=317.5)
		self.main_screen_number_seven_button.place(x=0, y=385)
		self.main_screen_number_eight_button.place(x=100, y=385)
		self.main_screen_number_nine_button.place(x=200, y=385)

		self.main_screen_number_zero_button.place(x=300, y=250)
		self.main_screen_negative_number_button.place(x=300, y=300.5)
		self.main_screen_comma_button.place(x=300, y=351)
		self.main_screen_mode_button.place(x=300, y=401)

		self.main_screen_sqrt_button.grid_forget()
		self.main_screen_pi_button.grid_forget()
		self.main_screen_e_button.grid_forget()
		self.main_screen_cbrt_button.grid_forget()
		self.main_screen_number_in_third_degree_button.grid_forget()
		self.main_screen_number_module_button.grid_forget()
		self.main_screen_factorial_button.grid_forget()
		self.main_screen_procent_button.grid_forget()
		self.main_screen_clear_button.grid_forget()

		self.main_screen_graphical_calculator_additional_layout: Graphical_claculator_adittional_layout = Graphical_claculator_adittional_layout()

	@typing.override
	def __button_operation__(self: typing.Self, button: str) -> None:
		self.button: str = button
		self.main_screen_expression_entry_data: str = self.main_screen_expression_entry.get()
		match self.main_screen_expression_entry_data:
			case "%":
				self.main_screen_result: str = eval(f"{self.main_screen_expression_entry_data} / 100")

				self.main_screen_result_entry.configure(state=f"normal")
				self.main_screen_result_entry.delete(f"0", tkinter.END)
				self.main_screen_result_entry.insert(f"0", f"result is {self.main_screen_result}")
						
			case _:
				self.main_screen_expression_entry.delete(f"0", tkinter.END)
				self.main_screen_expression_entry.insert(f"0", f"{self.main_screen_expression_entry_data + self.button}")

	@typing.override
	def __equation__(self: typing.Self) -> None:
		self.main_screen_expression_entry_data: str = self.main_screen_expression_entry.get()
		self.main_screen_result: str = eval(f"{self.main_screen_expression_entry_data}")

		self.main_screen_result_entry.configure(state=f"normal")
		self.main_screen_result_entry.delete(f"0", tkinter.END)
		self.main_screen_result_entry.insert(f"0", f"result is {self.main_screen_result}")
			
		self.main_screen_result_entry.configure(state=f"disabled")

	@typing.override
	def __clear_everything__(self: typing.Self) -> None:
		self.main_screen_expression_entry.delete(f"0", tkinter.END)

		self.main_screen_result_entry.configure(state=f"normal")
		self.main_screen_result_entry.delete(f"0", tkinter.END)
		self.main_screen_result_entry.configure(state=f"disabled") 

	@typing.override
	def __mode_option__(self: typing.Self) -> None:
		self.main_screen_mode_option: Menu_Option = Menu_Option()

	@typing.override
	def __change_base__(self: typing.Self, configure: str) -> None:
		self.main_screen_count_system_result: str
		self.main_screen_expression_entry_data: str = self.main_screen_expression_entry.get()
		self.main_screen_base_data: str = self.main_screen_base_option.get()
		match self.main_screen_base_data:
			case "binary-octal": self.main_screen_count_system_result = oct(int(self.main_screen_expression_entry_data, 2))[2:]

			case "binary-decimal": self.main_screen_count_system_result = int(self.main_screen_expression_entry_data, 2)

			case "binary-hexadecimal": self.main_screen_count_system_result = hex(int(self.main_screen_expression_entry_data, 2))[2:]

			case "octal-binary": self.main_screen_count_system_result = bin(int(self.main_screen_expression_entry_data, 8))[2:]

			case "octal-decimal": self.main_screen_count_system_result = int(self.main_screen_expression_entry_data, 8)

			case "octal-hexadecimal": self.main_screen_count_system_result = hex(int(self.main_screen_expression_entry_data, 8))[2:]

			case "decimal-binary": self.main_screen_count_system_result = bin(int(self.main_screen_expression_entry_data))[2:]

			case "decimal-octal": self.main_screen_count_system_result = oct(int(self.main_screen_expression_entry_data))[2:]

			case "decimal-hexadecimal": self.main_screen_count_system_result = hex(int(self.main_screen_expression_entry_data))[2:]

			case "hexadecimal-binary": self.main_screen_count_system_result = bin(int(self.main_screen_expression_entry_data, 16))[2:]

			case "hexadecimal-octal": self.main_screen_count_system_result = oct(int(self.main_screen_expression_entry_data, 16))[2:]

			case _: self.main_screen_count_system_result = int(self.main_screen_expression_entry_data, 16)

		self.main_screen_result_entry.configure(state=f"normal")
		self.main_screen_result_entry.delete(f"0", tkinter.END)
		if locale.getdefaultlocale()[0] == f"sr_RS": self.main_screen_result_entry.insert("0", f"резултат је {self.main_screen_count_system_result}")

		elif locale.getdefaultlocale()[0] == f"ru_RU": self.main_screen_result_entry.insert("0", f"результат {self.main_screen_count_system_result}")

		else: self.main_screen_result_entry.insert("0", f"result is {self.main_screen_count_system_result}")
			
		self.main_screen_result_entry.configure(state=f"disabled")

	@typing.override    
	def __plot__(self: typing.Self) -> None:
		matplotlib.pyplot.style.use(f"_mpl-gallery")
		matplotlib.pyplot.title(f"My Calculus graphical calculator")
		
		self.main_screen_expression_entry_data: str = self.main_screen_expression_entry.get()
		x: numpy.linspace = numpy.linspace(-20, 20, 400)
		y: numpy.array = eval(f"{self.main_screen_expression_entry_data}")

		matplotlib.pyplot.plot(x, y, linewidth=1.0)

		matplotlib.pyplot.show()

	@typing.override
	def __ai_window__(self: typing.Self) -> None:        
		self.main_screen_ai_window: My_Calculus_AI_window = My_Calculus_AI_window()

	@typing.override
	def __settings__(self: typing.Self) -> None:
		import My_Calculus_settings_menu
		
		self.main_screen_settings_window: My_Calculus_settings_menu.Settings_window = My_Calculus_settings_menu.Settings_window()

	@typing.override
	def __copy__(self: typing.Self) -> None:
		self.selected_text: str = self.main_screen_expression_entry.selection_get()
		self.clipboard_clear()
		self.clipboard_append(self.selected_text)

	@typing.override
	def __paste__(self: typing.Self) -> None:
		try:
			self.cursor_position: int = self.main_screen_expression_entry.index(tkinter.INSERT)    
			self.clipboard_text: str = self.clipboard_get()
			self.main_screen_expression_entry.insert(self.cursor_position, self.clipboard_text)
		
		except tkinter.TclError:
			pass

	@typing.override
	def __cut__(self: typing.Self) -> None:
		self.selected_text: str = self.main_screen_expression_entry.selection_get()
		self.main_screen_expression_entry.delete(f"sel.first", f"sel.last")
		self.clipboard_clear()
		self.clipboard_append(self.selected_text)

	@typing.override
	def __copy_result__(self: typing.Self) -> None:
		self.text: str = self.main_screen_result_entry.get()
		self.numbers: list[float] = list(map(float, re.findall(fr"\d+\.\d+", self.text)))
		self.clipboard_clear()
		self.clipboard_append(self.numbers[0])
		
class Menu_Option(customtkinter.CTkToplevel):

	WIDTH: typing.Final[int] = 300
	HEIGHT: typing.Final[int] = 350
	TITLE: typing.Final[str] = f"Menu"
	ICON: typing.Final[str] = f"my calculus icon.ico"

	def __init__(self: typing.Self, *args, **kwargs) -> None:
		customtkinter.CTkToplevel.__init__(self, *args, **kwargs)

		self.minsize(width=self.WIDTH, height=self.HEIGHT)
		self.resizable(False, False)
		self.title(self.TITLE)
		self.after(250, lambda: self.iconbitmap(self.ICON))

		self.main_screen_classical_mode_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"класични", height=50, width=250, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=program.__classical__)
		self.main_screen_classical_mode_button.grid(column=0, row=0)

		self.main_screen_scientific_mode_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"научни", height=50, width=250, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=program.__scientific__)
		self.main_screen_scientific_mode_button.grid(column=0, row=1)

		self.main_screen_programming_mode_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"програмерски", height=50, width=250, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=program.__programming__)
		self.main_screen_programming_mode_button.grid(column=0, row=2)
		
		self.main_screen_graphical_mode_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"графички", height=50, width=250, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=program.__graphical__)
		self.main_screen_graphical_mode_button.grid(column=0, row=3)

		self.main_screen_ai_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"AI", height=50, width=250, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: My_Calculus_AI_window())
		self.main_screen_ai_button.grid(column=0, row=4)
		
		self.main_screen_settings_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"подешавања", height=50, width=250, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=program.__settings__)
		self.main_screen_settings_button.grid(column=0, row=5)

		self.main_screen_classical_mode_button.configure(text=f"classic")
		self.main_screen_scientific_mode_button.configure(text=f"scientific")
		self.main_screen_programming_mode_button.configure(text=f"programming")
		self.main_screen_graphical_mode_button.configure(text=f"graphical")
		self.main_screen_settings_button.configure(text=f"settings")
			

class Scientific_calculator_additional_layout(customtkinter.CTkToplevel):
	 
	WIDTH: typing.Final[int] = 965 
	HEIGHT: typing.Final[int] = 411
	TITLE: typing.Final[str] = f"My Calculus scientific calculator additional layout"
	ICON: typing.Final[str] = f"my calculus icon.ico"

	def __init__(self: typing.Self, *args, **kwargs) -> None:
		customtkinter.CTkToplevel.__init__(self, *args, **kwargs)

		self.minsize(width=self.WIDTH, height=self.HEIGHT)
		self.resizable(False, False)
		self.title(self.TITLE)
		self.after(250, lambda: self.iconbitmap(self.ICON))

		self.main_screen_functions_text: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self, text=f"Функције", text_color=text_color, font=(f"Roboto Bold", 55))
		self.main_screen_functions_text.place(x=2, y=0)

		self.main_screen_logarith_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"logyX", height=50, width=70, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: program.__button_operation__(f"log(x,y)"))
		self.main_screen_logarith_function_button.place(x=2, y=62)
		
		self.main_screen_natural_logarith_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"ln", height=50, width=70, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: program.__button_operation__(f"log()"))
		self.main_screen_natural_logarith_function_button.place(x=78, y=62)

		self.main_screen_e_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"eX", height=50, width=70, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: program.__button_operation__(f"e**"))
		self.main_screen_e_function_button.place(x=148, y=62)

		self.main_screen_root_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=fr"y\/X", height=50, width=70, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: program.__button_operation__(f"xyrt(number, x, y)"))
		self.main_screen_root_function_button.place(x=218, y=62)

		self.main_screen_number_in_y_degree_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"xY", height=50, width=70, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: program.__button_operation__(f"**"))
		self.main_screen_number_in_y_degree_function_button.place(x=288, y=62)

		self.main_screen_two_in_x_degree_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"2X", height=50, width=70, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: program.__button_operation__(f"2**"))
		self.main_screen_two_in_x_degree_function_button.place(x=358, y=62)

		self.main_screen_ten_in_x_degree_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"10X", height=50, width=70, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: program.__button_operation__(f"10**"))
		self.main_screen_ten_in_x_degree_function_button.place(x=428, y=62)

		self.main_screen_trigonomical_functions_text: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self, text=f"Тригонометрические функции", text_color=text_color, font=(f"Roboto Bold", 55))
		self.main_screen_trigonomical_functions_text.place(x=2, y=110)

		self.main_screen_sin_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"sin", height=50, width=70, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: program.__button_operation__(f"sin()"))
		self.main_screen_sin_function_button.place(x=2, y=175)

		self.main_screen_cos_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"cos", height=50, width=70, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: program.__button_operation__(f"cos()"))
		self.main_screen_cos_function_button.place(x=72, y=175)

		self.main_screen_tan_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"tan", height=50, width=70, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: program.__button_operation__(f"tan()"))
		self.main_screen_tan_function_button.place(x=142, y=175)

		self.main_screen_cotan_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"cotan", height=50, width=70, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: program.__button_operation__(f"cotan()"))
		self.main_screen_cotan_function_button.place(x=212, y=175)

		self.main_screen_asin_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"asin", height=50, width=70, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: program.__button_operation__(f"asin()"))
		self.main_screen_asin_function_button.place(x=285, y=175)

		self.main_screen_acos_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"acos", height=50, width=70, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: program.__button_operation__(f"acos()"))
		self.main_screen_acos_function_button.place(x=355, y=175)

		self.main_screen_atan_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"atan", height=50, width=70, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: program.__button_operation__(f"atan()"))
		self.main_screen_atan_function_button.place(x=425, y=175)

		self.main_screen_acotan_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"acotan", height=50, width=70, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: program.__button_operation__(f"acotan()"))
		self.main_screen_acotan_function_button.place(x=2, y=226)

		self.main_screen_sinh_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"sinh", height=50, width=70, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: program.__button_operation__(f"sinh()"))
		self.main_screen_sinh_function_button.place(x=86, y=226)

		self.main_screen_cosh_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"cosh", height=50, width=70, fg_color=button_color, text_color=text_color, font=("Roboto Bold", 25), command=lambda: program.__button_operation__(f"cosh()"))
		self.main_screen_cosh_function_button.place(x=156, y=226)

		self.main_screen_tanh_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"tanh", height=50, width=70, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: program.__button_operation__(f"cosh()"))
		self.main_screen_tanh_function_button.place(x=226, y=226)

		self.main_screen_cotanh_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"cotanh", height=50, width=70, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: program.__button_operation__(f"cosh()"))
		self.main_screen_cotanh_function_button.place(x=296, y=226)

		self.main_screen_asinh_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"asinh", height=50, width=70, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: program.__button_operation__(f"asinh()"))
		self.main_screen_asinh_function_button.place(x=383, y=226)

		self.main_screen_acosh_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"acosh", height=50, width=70, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: program.__button_operation__(f"acosh()"))
		self.main_screen_acosh_function_button.place(x=457, y=226)

		self.main_screen_atanh_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"atanh", height=50, width=70, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: program.__button_operation__(f"atanh()"))
		self.main_screen_atanh_function_button.place(x=2, y=277)

		self.main_screen_atanh_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"acotanh", height=50, width=70, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: program.__button_operation__(f"acotanh()"))
		self.main_screen_atanh_function_button.place(x=75, y=277)

		self.main_screen_degree_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"deg", height=50, width=70, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: program.__button_operation__(f"degrees()"))
		self.main_screen_degree_function_button.place(x=172, y=277)

		self.main_screen_radian_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"rad", height=50, width=70, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: program.__button_operation__(f"radians()"))
		self.main_screen_radian_function_button.place(x=242, y=277)
		
		self.main_screen_functions_text.configure(text=f"Functions")
		self.main_screen_trigonomical_functions_text.configure(text=f"Trigonometric functions")
   
		
class Graphical_claculator_adittional_layout(customtkinter.CTkToplevel):
	WIDTH: typing.Final[int] = 966 
	HEIGHT: typing.Final[int] = 56
	TITLE: typing.Final[str] = f"My Calculus graphical calculator additional layout"
	ICON: typing.Final[str] = f"my calculus icon.ico"

	def __init__(self: typing.Self, *args, **kwargs) -> None:
		customtkinter.CTkToplevel.__init__(self, *args, **kwargs)

		self.minsize(width=self.WIDTH, height=self.HEIGHT)
		self.resizable(False, False)
		self.title(self.TITLE)
		self.after(250, lambda: self.iconbitmap(self.ICON))

		self.main_screen_functions_text: customtkinter.CTkLabel = customtkinter.CTkLabel(master=self, text=f"Функције", text_color=text_color, font=(f"Roboto Bold", 55))
		self.main_screen_functions_text.place(x=2, y=0)
																															  
		self.main_screen_logarith_base_2_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"log2", height=50, width=70, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: program.__button_operation__(f"numpy.log2()"))
		self.main_screen_logarith_base_2_function_button.place(x=0, y=70)

		self.main_screen_ln_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"ln", height=50, width=70, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: program.__button_operation__(f"numpy.log()"))
		self.main_screen_ln_function_button.place(x=72, y=70)
		
		self.main_screen_logarith_base_10_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"log10", height=50, width=70, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: program.__button_operation__(f"numpy.log10()"))
		self.main_screen_logarith_base_10_function_button.place(x=141, y=70)

		self.main_screen_e_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"eX", height=50, width=70, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: program.__button_operation__(f"e**"))
		self.main_screen_e_function_button.place(x=214, y=70)

		self.main_screen_sqrt_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=fr"\/", height=50, width=70, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: program.__button_operation__(f"numpy.sqrt()"))
		self.main_screen_sqrt_function_button.place(x=285, y=70)

		self.main_screen_number_in_y_degree_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"xY", height=50, width=70, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: program.__button_operation__(f"**"))
		self.main_screen_number_in_y_degree_function_button.place(x=355, y=70)

		self.main_screen_two_in_x_degree_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"2X", height=50, width=70, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: program.__button_operation__(f"2**"))
		self.main_screen_two_in_x_degree_function_button.place(x=425, y=70)
																															   
		self.main_screen_ten_in_x_degree_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"10X", height=50, width=70, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: program.__button_operation__(f"10**"))
		self.main_screen_ten_in_x_degree_function_button.place(x=495, y=70)

		self.main_screen_module_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"|X|", height=50, width=70, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: program.__button_operation__(f"numpy.fabs()"))
		self.main_screen_module_function_button.place(x=565, y=70)

		self.main_screen_sin_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"sin", height=50, width=70, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: program.__button_operation__(f"numpy.sin()"))
		self.main_screen_sin_function_button.place(x=635, y=70)

		self.main_screen_cos_function_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, text=f"cos", height=50, width=70, fg_color=button_color, text_color=text_color, font=(f"Roboto Bold", 25), command=lambda: program.__button_operation__(f"numpy.cos()"))
		self.main_screen_cos_function_button.place(x=705, y=70)  
		
		self.main_screen_functions_text.configure(text=f"Functions")

class My_Calculus_AI_window(customtkinter.CTkToplevel, My_Calculus_AI_window_interface.My_Calculus_AI_window_interface):
	
	HEIGHT: typing.Final[int] = 375
	WIDTH: typing.Final[int] = 655
	TITLE: typing.Final[str] = f"My Claculus AI assistant (Copliot+PC edition)"
	ICON: typing.Final[str] = f"my calculus icon.ico"
	COLOR_THEME: typing.Final[str] = f"dark-blue"
	WIDGET_SCALING: typing.Final[float] = 1.251
	THEME: typing.Final[str] = f"system"

	def __init__(self: typing.Self, *args, **kwargs) -> None:
		customtkinter.CTkToplevel.__init__(self, *args, **kwargs)

		customtkinter.set_widget_scaling(self.WIDGET_SCALING)
		customtkinter.set_default_color_theme(self.COLOR_THEME)
		customtkinter.set_appearance_mode(self.THEME)
		customtkinter.deactivate_automatic_dpi_awareness()

		self.title(self.TITLE)
		self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
		self.resizable(False, False)
		self.after(250, lambda: self.iconbitmap(self.ICON))

		self.ai_window_textbox: customtkinter.CTkTextbox = customtkinter.CTkTextbox(master=self, height=265, width=524, corner_radius=0, fg_color=f"transparent", text_color=(f"black", f"white"))
		self.ai_window_textbox.place(x=0, y=0)

		self.ai_window_textbox.configure(state=f"disabled")

		self.ai_window_entry: customtkinter.CTkEntry = customtkinter.CTkEntry(master=self, height=30, width=465, border_width=0, fg_color=f"transparent", placeholder_text=f"...")
		self.ai_window_entry.place(x=0, y=269)

		self.ai_window_microphone_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, height=30, width=30, border_width=0, fg_color=f"transparent", text=f"🎤", command=self.__audio_input__)
		self.ai_window_microphone_button.place(x=465, y=269)

		self.ai_window_send_request_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, height=30, width=30, border_width=0, fg_color=f"transparent", text=f"->", command=self.__response_from_ai__)
		self.ai_window_send_request_button.place(x=495, y=269)

		self.ai_window_entry.bind(f"<Return>", lambda event: self.__response_from_ai__())  

	@typing.override
	def __response_from_ai__(self: typing.Self, event: typing.Optional[tkinter.Event] = None) -> None:
		self.ai_window_entry_data: str = self.ai_window_entry.get()

		def run_model():
			response_text: str = My_Calculus_AI.My_Calculus_LM().__response__(pipe=SLM, query=f"<|system|>You are a helpful AI assistant.<|end|><|user|>{self.ai_window_entry_data}<|end|><|assistant|>")

			def update_gui():
				self.ai_window_textbox.configure(state="normal")
				self.ai_window_textbox.insert(tkinter.END, f"USER:\n{self.ai_window_entry_data}\nLlama:\n{response_text}\n")
				self.ai_window_textbox.configure(state="disabled")
				self.ai_window_entry.delete(0, tkinter.END)

			self.after(0, update_gui)

		threading.Thread(target=run_model).start()

	@typing.override
	def __audio_input__(self: typing.Self) -> None:
		self.recognizer: speech_recognition.Recognizer = speech_recognition.Recognizer()
		with speech_recognition.Microphone() as self.source:
			self.audio_data: speech_recognition.AudioData = self.recognizer.record(self.source, duration=5)
			self.text: str = self.recognizer.recognize_google(self.audio_data)

		self.ai_window_entry.insert(f"0", self.text)

if __name__ == f"__main__":
	program: Program = Program()

	program.mainloop()
