import tkinter, tkinter.filedialog, pickle, os, sys, docx, docx.shared, aspose.words, typing, My_Diary_interface, My_Diary_window, CTkMenuBar, CTkPDFViewer, locale, CTkMessagebox, tempfile
from tkinterdnd2 import *
from customtkinter import *

with open(f"my_diary_saved_text.pickle", f"rb+") as text_data: autosaved_text: str = pickle.load(text_data)

class Program(My_Diary_window.Tk, My_Diary_interface.My_Diary_interface):

	TITLE: typing.Final[str] = f"My Diary"
	COLOR_THEME: typing.Final[str] = f"dark-blue"
	WIDGET_SCALING: typing.Final[float] = 1.251
	THEME: typing.Final[str] = f"system"

	def __init__(self: typing.Self, *args, **kwargs) -> None:
		My_Diary_window.Tk.__init__(self, *args, **kwargs)

		set_widget_scaling(self.WIDGET_SCALING)
		set_default_color_theme(self.COLOR_THEME)
		set_appearance_mode(self.THEME)
		deactivate_automatic_dpi_awareness()

		self.icon = (b"\x00\x00\x01\x00\x01\x00\x10\x10\x00\x00\x01\x00\x08\x00h\x05\x00\x00"b"\x16\x00\x00\x00(\x00\x00\x00\x10\x00\x00\x00 \x00\x00\x00\x01\x00"b"\x08\x00\x00\x00\x00\x00@\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"b"\x00\x01\x00\x00\x00\x01") + b"\x00"*1282 + b"\xff"*64

		_, self.icon_path = tempfile.mkstemp()
		with open(self.icon_path, f"wb+") as icon_file: icon_file.write(self.icon)

		self.title(self.TITLE)
		self.iconbitmap(self.icon_path)
  
		self.bind(f"<Alt_L>" + f"<F4>", self.__exit__)
		self.bind(f"<Control_L>" + f"<s>", self.__save_text__)
		self.bind(f"<Control_L>" + f"<o>", self.__open_file__)
		self.protocol(f"WM_DELETE_WINDOW", self.__exit__)

		self.main_screen_title_menu: CTkMenuBar.CTkTitleMenu = CTkMenuBar.CTkTitleMenu(master=self, title_bar_color=f"default")

		self.main_screen_tiltle_menu_menu_button: CTkButton = self.main_screen_title_menu.add_cascade(text=f"☰")

		self.main_screen_tiltle_menu_undo_button: CTkButton = self.main_screen_title_menu.add_cascade(text=f"⟲", command=self.__undo__)

		self.main_screen_tiltle_menu_redo_button: CTkButton = self.main_screen_title_menu.add_cascade(text=f"⟳", command=self.__redo__)

		self.main_screen_frame_texbox_font: CTkFont = CTkFont(family=f"Ubuntu", size=22, weight=f"normal", slant=f"roman", underline=False, overstrike=False)

		self.main_screen_frame_textbox: CTkTextbox = CTkTextbox(master=self, height=795, width=1536, corner_radius=0, undo=True, fg_color=f"transparent", font=self.main_screen_frame_texbox_font, text_color=(f"black", f"white"))
		self.main_screen_frame_textbox.pack(expand=True, fill=f"both")

		self.main_screen_frame_textbox.drop_target_register(DND_ALL)
		self.main_screen_frame_textbox.dnd_bind(f"<<Drop>>", self.__drop_file_into_textbox__)

		self.main_screen_frame_textbox.bind(f"<KeyRelease>", self.__word_count__)
		self.main_screen_frame_textbox.bind(f"<F1>", self.__html_script__)
		
		self.main_screen_edit_text_window: CTkToplevel = CTkToplevel()
		
		self.main_screen_edit_text_window.protocol(f"WM_DELETE_WINDOW", lambda: self.main_screen_edit_text_window.withdraw())
		self.main_screen_edit_text_window.title(f"My Diary edit text font window")
		self.main_screen_edit_text_window.after(250, lambda: self.main_screen_edit_text_window.iconbitmap(self.icon_path))
		self.main_screen_edit_text_window.resizable(False, False)
		
		self.main_screen_edit_text_window.withdraw()
		
		self.main_screen_edit_font_button: CTkComboBox = CTkComboBox(master=self.main_screen_edit_text_window, height=20, width=75, corner_radius=0, values=[f"System", f"Terminal", f"Ubuntu", f"Script", f"Roman", f"Modern", f"MS Serif"], fg_color=f"green", border_color=f"green", button_color=f"green", button_hover_color=f"green", dropdown_fg_color=f"green", command=self.__edit_text_font__)

		self.main_screen_edit_size_button: CTkComboBox = CTkComboBox(master=self.main_screen_edit_text_window, height=20, width=75, corner_radius=0, values=[f"1", f"2", f"4", f"5", f"6", f"8", f"11", f"12", f"13", f"14", f"16", f"18", f"20", f"22", f"24", f"26", f"28", f"30", f"32", f"34", f"36", f"38", f"40", f"42", f"44", f"46", f"48", f"50", f"60", f"70", f"80", f"90", f"100"], fg_color=f"green", border_color=f"green", button_color=f"green", button_hover_color=f"green", dropdown_fg_color=f"green", command=self.__edit_text_font__)

		self.main_screen_edit_color_button: CTkComboBox = CTkComboBox(master=self.main_screen_edit_text_window, height=20, width=75, corner_radius=0, values=[f"black", f"white", f"red", f"green", f"blue"], fg_color=f"green", border_color=f"green", button_color=f"green", button_hover_color=f"green", dropdown_fg_color=f"green", command=self.__edit_text_font__)

		self.main_screen_edit_slant_button: CTkComboBox = CTkComboBox(master=self.main_screen_edit_text_window, height=20, width=75, corner_radius=0, values=[f"roman", f"italic"], fg_color=f"green", border_color=f"green", button_color=f"green", button_hover_color=f"green", dropdown_fg_color=f"green", command=self.__edit_text_font__)

		self.main_screen_edit_weight_button: CTkComboBox = CTkComboBox(master=self.main_screen_edit_text_window, height=20, width=75, corner_radius=0, values=[f"normal", f"bold"], fg_color=f"green", border_color=f"green", button_color=f"green", button_hover_color=f"green", dropdown_fg_color=f"green", command=self.__edit_text_font__)

		self.main_screen_edit_underline_button: CTkComboBox = CTkComboBox(master=self.main_screen_edit_text_window, height=20, width=75, corner_radius=0, values=[f"not underlined", f"underlined"], fg_color=f"green", border_color=f"green", button_color=f"green", button_hover_color=f"green", dropdown_fg_color=f"green", command=self.__edit_text_font__)

		self.main_screen_edit_overstrike_button: CTkComboBox = CTkComboBox(master=self.main_screen_edit_text_window, height=20, width=75, corner_radius=0, values=[f"not overstriked", f"overstriked"], fg_color=f"green", border_color=f"green", button_color=f"green", button_hover_color=f"green", dropdown_fg_color=f"green", command=self.__edit_text_font__)


		if locale.getdefaultlocale()[0] == f"sr_RS":
			self.main_screen_title_menu_submenu: CTkMenuBar.CustomDropdownMenu = CTkMenuBar.CustomDropdownMenu(widget=self.main_screen_tiltle_menu_menu_button, fg_color=f"transparent")

			self.main_screen_save_button: CTkButton = self.main_screen_title_menu_submenu.add_option(option=f"сачувај текст", command=self.__save_text__)

			self.main_screen_open_button: CTkButton = self.main_screen_title_menu_submenu.add_option(option=f"отвори фајл", command=self.__open_file__)
		
			self.main_screen_clear_button: CTkButton = self.main_screen_title_menu_submenu.add_option(option=f"обриши текст", command=self.__clear_text__)
		
			self.main_screen_edit_text_button: CTkButton = self.main_screen_title_menu_submenu.add_option(option=f"уреди текст", command=self.__edit_text__)
		
			self.main_screen_converter_button: CTkMenuBar.CustomDropdownMenu = self.main_screen_title_menu_submenu.add_submenu(f"претварач")
		
			self.main_screen_pdf_to_word_converter_button: CTkButton  = self.main_screen_converter_button.add_option(f"из PDF у docx", command=self.__pdf_to_docx__)

			self.main_screen_word_to_pdf_converter_button: CTkButton  = self.main_screen_converter_button.add_option(f"из docx у PDF", command=self.__docx_to_pdf__)
		
			self.main_screen_pdf_to_txt_converter_button: CTkButton  = self.main_screen_converter_button.add_option(f"из PDF у txt", command=self.__pdf_to_txt__)

			self.main_screen_txt_to_pdf_converter_button: CTkButton  = self.main_screen_converter_button.add_option(f"из txt у PDF", command=self.__txt_to_pdf__)
		
			self.main_screen_txt_to_word_converter_button: CTkButton  = self.main_screen_converter_button.add_option(f"из txt у docx", command=self.__txt_to_docx__)

			self.main_screen_word_to_txt_converter_button: CTkButton  = self.main_screen_converter_button.add_option(f"из docx у txt", command=self.__docx_to_txt__)

		elif locale.getdefaultlocale()[0] == f"ru_RU":
			self.main_screen_title_menu_submenu: CTkMenuBar.CustomDropdownMenu = CTkMenuBar.CustomDropdownMenu(widget=self.main_screen_tiltle_menu_menu_button, fg_color=f"transparent")

			self.main_screen_save_button: CTkButton = self.main_screen_title_menu_submenu.add_option(option=f"сохранить текст", command=self.__save_text__)

			self.main_screen_open_button: CTkButton = self.main_screen_title_menu_submenu.add_option(option=f"открыть текст", command=self.__open_file__)
		
			self.main_screen_clear_button: CTkButton = self.main_screen_title_menu_submenu.add_option(option=f"удалить текст", command=self.__clear_text__)
		
			self.main_screen_edit_text_button: CTkButton = self.main_screen_title_menu_submenu.add_option(option=f"отредактировать текст", command=self.__edit_text__)
		
			self.main_screen_converter_button: CTkMenuBar.CustomDropdownMenu = self.main_screen_title_menu_submenu.add_submenu(f"конвертер")
		
			self.main_screen_pdf_to_word_converter_button: CTkButton  = self.main_screen_converter_button.add_option(f"из PDF в docx", command=self.__pdf_to_docx__)

			self.main_screen_word_to_pdf_converter_button: CTkButton  = self.main_screen_converter_button.add_option(f"из docx в PDF", command=self.__docx_to_pdf__)
		
			self.main_screen_pdf_to_txt_converter_button: CTkButton  = self.main_screen_converter_button.add_option(f"из PDF в txt", command=self.__pdf_to_txt__)

			self.main_screen_txt_to_pdf_converter_button: CTkButton  = self.main_screen_converter_button.add_option(f"из txt в PDF", command=self.__txt_to_pdf__)
		
			self.main_screen_txt_to_word_converter_button: CTkButton  = self.main_screen_converter_button.add_option(f"из txt в docx", command=self.__txt_to_docx__)

			self.main_screen_word_to_txt_converter_button: CTkButton  = self.main_screen_converter_button.add_option(f"из docx в txt", command=self.__docx_to_txt__)

		else:
			self.main_screen_title_menu_submenu: CTkMenuBar.CustomDropdownMenu = CTkMenuBar.CustomDropdownMenu(widget=self.main_screen_tiltle_menu_menu_button, fg_color=f"transparent")

			self.main_screen_save_button: CTkButton = self.main_screen_title_menu_submenu.add_option(option=f"save", command=self.__save_text__)

			self.main_screen_open_button: CTkButton = self.main_screen_title_menu_submenu.add_option(option=f"open", command=self.__open_file__)
		
			self.main_screen_clear_button: CTkButton = self.main_screen_title_menu_submenu.add_option(option=f"clear", command=self.__clear_text__)
		
			self.main_screen_edit_text_button: CTkButton = self.main_screen_title_menu_submenu.add_option(option=f"edit", command=self.__edit_text__)
		
			self.main_screen_converter_button: CTkMenuBar.CustomDropdownMenu = self.main_screen_title_menu_submenu.add_submenu(f"converter")
		
			self.main_screen_pdf_to_word_converter_button: CTkButton  = self.main_screen_converter_button.add_option(f"from PDF to docx", command=self.__pdf_to_docx__)

			self.main_screen_word_to_pdf_converter_button: CTkButton  = self.main_screen_converter_button.add_option(f"from docx to PDF", command=self.__docx_to_pdf__)
		
			self.main_screen_pdf_to_txt_converter_button: CTkButton  = self.main_screen_converter_button.add_option(f"from PDF to txt", command=self.__pdf_to_txt__)

			self.main_screen_txt_to_pdf_converter_button: CTkButton  = self.main_screen_converter_button.add_option(f"from txt to PDF", command=self.__txt_to_pdf__)
		
			self.main_screen_txt_to_word_converter_button: CTkButton  = self.main_screen_converter_button.add_option(f"from txt to docx", command=self.__txt_to_docx__)

			self.main_screen_word_to_txt_converter_button: CTkButton  = self.main_screen_converter_button.add_option(f"from docx to txt", command=self.__docx_to_txt__)

		self.bind(f"<KeyRelease>", self.__text_autosave__)
		self.main_screen_frame_textbox.bind(f"<F2>", self.__enter_text_autosave__)

		self.main_screen_word_counter_variable: int = 0

		self.main_screen_word_counter_data_variable: tkinter.IntVar = tkinter.IntVar(value=self.main_screen_word_counter_variable)

		self.main_screen_tiltle_menu_word_count: CTkButton = self.main_screen_title_menu.add_cascade(textvariable=self.main_screen_word_counter_data_variable, command=self.__word_count_show__)

	def __undo__(self: typing.Self) -> None:
		try: self.main_screen_frame_textbox.edit_undo()

		except tkinter.TclError: pass

	def __redo__(self: typing.Self) -> None:
		try: self.main_screen_frame_textbox.edit_redo()

		except tkinter.TclError: pass

	def __save_text__(self: typing.Self, event: str | None = None) -> None:
		self.file_name: tkinter.filedialog.asksaveasfilename = tkinter.filedialog.asksaveasfilename(filetypes=[(f"All Files (*.*)", f"*.*"), (f"Text file (*.txt)", f"*.txt"), (f"Docx file (*.docx)", f"*.docx"), (f"Python file (*.py)", f"*.py"), (f"Java file (*.java)", f"*.java"), (f"C# file (*.cs)", f"*.cs"), (f"HTML file (*.html)", f"*.html"), (f"CSS file (*.css)", f"*.css"), (f"JavaScript file (*.js)", f"*.js"), (f"C++ file (*.cpp)", f"*.cpp"), (f"Pickle file (*.pickle)", f"*.pickle")], defaultextension=[(f"All Files (*.*)", f"*.*"), (f"Text file (*.txt)", f"*.txt"), (f"Docx file (*.docx)", f"*.docx"), (f"Python file (*.py)", f"*.py"), (f"Java file (*.java)", f"*.java"), (f"C# file (*.cs)", f"*.cs"), (f"HTML file (*.html)", f"*.html"), (f"CSS file (*.css)", f"*.css"), (f"JavaScript file (*.js)", f"*.js"), (f"C++ file (*.cpp)", f"*.cpp"), (f"Pickle file (*.pickle)", f"*.pickle")])
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
					self.file: docx.Document = docx.Document()
					self.file_data: str = self.main_screen_frame_textbox.get(f"1.0", tkinter.END)
					self.file_run: docx.Document = self.file.add_paragraph().add_run(self.file_data)
					self.font: docx.Document = self.file_run.font
					self.font.size: docx.shared.Pt = docx.shared.Pt(14)
					self.font.color.rgb: docx.shared.RGBColor = docx.shared.RGBColor(0, 0, 0)
					self.file_run.italic: bool = False
					self.file_run.bold: bool = False
					self.file_run.underline: bool = False
					self.font.strike: bool = False
					self.file.save(self.file_name)

			case ".pickle":
				with open(self.file_name, f"wb+") as self.file:
					try:
						self.file_data: str = self.main_screen_frame_textbox.get("1.0", tkinter.END)
						pickle.dump(self.file_data, self.file)
					
					except FileNotFoundError: pass
					
			case _:
				with open(self.file_name, f"w+", encoding=f"UTF-8") as self.file:
					try:
						self.file_data: str = self.main_screen_frame_textbox.get("1.0", tkinter.END)
						self.file.write(self.file_data)
					
					except FileNotFoundError: pass
			
	def __clear_text__(self: typing.Self) -> None:
		self.main_screen_frame_textbox.delete(f"1.0", tkinter.END)

	def __edit_text__(self: typing.Self) -> None:
		self.main_screen_edit_text_window.deiconify()

		self.main_screen_edit_font_button.grid(column=1, row=0)
		self.main_screen_edit_size_button.grid(column=2, row=0)
		self.main_screen_edit_color_button.grid(column=3, row=0)
		self.main_screen_edit_slant_button.grid(column=4, row=0)
		self.main_screen_edit_weight_button.grid(column=5, row=0)
		self.main_screen_edit_underline_button.grid(column=6, row=0)
		self.main_screen_edit_overstrike_button.grid(column=7, row=0)

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

	def __open_file__(self: typing.Self, event: str | None = None) -> None:
		self.opened_name_file: tkinter.filedialog = tkinter.filedialog.askopenfilename(title=f"open file", filetypes=[(f"All Files (*.*)", f"*.*"), (f"Word file (*.docx)", f"*.docx"), (f"Text file (*.txt)", f"*.txt"), (f"PDF file (*.pdf)", f"*.pdf"), (f"Python file (*.py)", f"*.py"), (f"Java file (*.java)", f"*.java"), (f"C# file (*.cs)", f"*.cs"), (f"HTML file (*.html)", f"*.html"), (f"CSS file (*.css)", f"*.css"), (f"JavaScript file (*.js)", f"*.js"), (f"C++ file (*.cpp)", f"*.cpp"), (f"Pickle file (*.pickle)", f"*.pickle")], defaultextension=[(f"All Files (*.*)", f"*.*"), (f"Text file (*.txt)", f"*.txt"), (f"Word file (*.docx)", f"*.docx"), (f"PDF file (*.pdf)", f"*.pdf"), (f"Python file (*.py)", f"*.py"), (f"Java file (*.java)", f"*.java"), (f"C# file (*.cs)", f"*.cs"), (f"HTML file (*.html)", f"*.html"), (f"CSS file (*.css)", f"*.css"), (f"JavaScript file (*.js)", f"*.js"), (f"C++ file (*.cpp)", f"*.cpp"), (f"Pickle file (*.pickle)", f"*.pickle")])
		match os.path.splitext(self.opened_name_file)[1]:
			case ".docx":
				try:
					self.openned_file: docx.Document = docx.Document(self.opened_name_file)
					self.openned_file_data: list[str] = []
					for self.paragraphs in self.openned_file.paragraphs: self.openned_file_data.append(self.paragraphs.text)

					self.main_screen_frame_textbox.insert(f"1.0", f"\n".join(self.openned_file_data))

				except docx.opc.exceptions.PackageNotFoundError: pass
			
			case ".pickle":
				try:
					with open(self.opened_name_file, f"rb+") as self.openned_file:
						self.main_screen_frame_textbox.insert(f"1.0", pickle.load(self.openned_file))

				except FileNotFoundError: pass
				
			case ".pdf":
				self.main_screen_pdf_view: CTkToplevel = CTkToplevel()
				self.main_screen_pdf_view.title(f"My Diary PDF reader (beta)")
				self.main_screen_pdf_view.after(250, lambda: self.main_screen_pdf_view.iconbitmap(self.icon_path))

				self.pdf_frame: CTkPDFViewer.CTkPDFViewer = CTkPDFViewer.CTkPDFViewer(self.main_screen_pdf_view, file=self.opened_name_file)
				self.pdf_frame.pack(fill="both", expand=True)

			case _:
				try:
					with open(self.opened_name_file, f"r+", encoding=f"UTF-8") as self.openned_file:
						self.main_screen_frame_textbox.insert(f"1.0", self.openned_file.read())

				except FileNotFoundError: pass

	def __pdf_to_docx__(self: typing.Self) -> None:
		try:
			self.file: tkinter.filedialog.askopenfilename = tkinter.filedialog.askopenfilename(title=f"convert pdf file", filetypes=[(f"Pdf file (*.pdf)", f"*.pdf")], defaultextension=[(f"Pdf file (*.pdf)", f"*.pdf")])
			self.converted_file: aspose.words.Document = aspose.words.Document(self.file)
			self.converted_file.save(f"{self.file}.docx")

		except RuntimeError: pass
	
	def __docx_to_pdf__(self: typing.Self) -> None:
		try:
			self.file: tkinter.filedialog.askopenfilename = tkinter.filedialog.askopenfilename(title=f"convert docx file", filetypes=[(f"Word file (*.docx)", f"*.docx")], defaultextension=[(f"Word file (*.docx)", f"*.docx")])
			self.converted_file: aspose.words.Document = aspose.words.Document(self.file)
			self.converted_file.save(f"{self.file}.pdf")

		except RuntimeError: pass

	def __pdf_to_txt__(self: typing.Self) -> None:
		try:
			self.file: tkinter.filedialog.askopenfilename = tkinter.filedialog.askopenfilename(title=f"convert pdf file", filetypes=[(f"Pdf file (*.pdf)", f"*.pdf")], defaultextension=[(f"Pdf file (*.pdf)", f"*.pdf")])
			self.converted_file: aspose.words.Document = aspose.words.Document(self.file)
			self.converted_file.save(f"{self.file}.txt")

		except RuntimeError: pass
		
	def __txt_to_pdf__(self: typing.Self) -> None:
		try:
			self.file: tkinter.filedialog.askopenfilename = tkinter.filedialog.askopenfilename(title=f"convert txt file", filetypes=[(f"Text file (*.txt)", f"*.txt")], defaultextension=[(f"Text file (*.txt)", f"*.txt")])
			self.converted_file: aspose.words.Document = aspose.words.Document(self.file)
			self.converted_file.save(f"{self.file}.pdf")

		except RuntimeError: pass
	
	def __docx_to_txt__(self: typing.Self) -> None:
		try:
			self.file: tkinter.filedialog.askopenfilename = tkinter.filedialog.askopenfilename(title=f"convert docx file", filetypes=[(f"Word file (*.docx)", f"*.docx")], defaultextension=[(f"Word file (*.docx)", f"*.docx")])
			self.converted_file: aspose.words.Document = aspose.words.Document(self.file)
			self.converted_file.save(f"{self.file}.txt")
		
		except RuntimeError: pass

	def __txt_to_docx__(self: typing.Self) -> None:
		try:
			self.file: tkinter.filedialog.askopenfilename = tkinter.filedialog.askopenfilename(title=f"convert txt file", filetypes=[(f"Text file (*.txt)", "*.txt")], defaultextension=[(f"Text file (*.txt)", f"*.txt")])
			self.converted_file: aspose.words.Document = aspose.words.Document(self.file)
			self.converted_file.save(f"{self.file}.docx")

		except RuntimeError: pass
		
	def __text_autosave__(self: typing.Self, event: str | None = None) -> None: 
		with open(f"my_diary_saved_text.pickle", f"wb+") as self.text_data: pickle.dump(self.main_screen_frame_textbox.get(f"1.0", tkinter.END), self.text_data)
		
	def __enter_text_autosave__(self: typing.Self, event: str | None = None) -> None:
		self.main_screen_frame_textbox.insert(f"1.0", autosaved_text)

	def __word_count__(self: typing.Self, event: str | None = None) -> None:
		self.main_screen_frame_textbox_data: str = self.main_screen_frame_textbox.get(f"0.0", tkinter.END)
		self.main_screen_word_counter_data_variable.set(value=len(self.main_screen_frame_textbox_data.split()))
		
	def __word_count_show__(self: typing.Self) -> None:
		if locale.getdefaultlocale()[0] == f"sr_RS":
			CTkMessagebox.CTkMessagebox(icon=f"info", title=f"речи", message=f"речи: {len(self.main_screen_frame_textbox.get(f'1.0', tkinter.END).split())}", button_color=f"green")
			
		elif locale.getdefaultlocale()[0] == f"ru_RU":
			CTkMessagebox.CTkMessagebox(icon=f"info", title=f"слова", message=f"слов: {len(self.main_screen_frame_textbox.get(f'1.0', tkinter.END).split())}", button_color=f"green")
			
		else:
			CTkMessagebox.CTkMessagebox(icon=f"info", title=f"words", message=f"words: {len(self.main_screen_frame_textbox.get(f'1.0', tkinter.END).split())}", button_color=f"green")
		
	def __drop_file_into_textbox__(self: typing.Self, event: str | None = None) -> None:
		self.main_screen_frame_textbox.delete(f"1.0", tkinter.END)
		if event.data.endswith(f".docx"):
			try:
				self.openned_file: docx.Document = docx.Document(event.data)
				self.openned_file_data: list[str] = []
				for self.paragraphs in self.openned_file.paragraphs: self.openned_file_data.append(self.paragraphs.text)

				self.main_screen_frame_textbox.insert(f"1.0", f"\n".join(self.openned_file_data))

			except docx.opc.exceptions.PackageNotFoundError: pass

		elif event.data.endswith(f".pickle"):
			try:
				with open(event.data, f"rb+") as self.openned_file: self.main_screen_frame_textbox.insert(f"1.0", pickle.load(self.openned_file))

			except FileNotFoundError: pass
			
		elif event.data.endswith(".pdf"):
			self.main_screen_pdf_view: CTkToplevel = CTkToplevel()
			self.main_screen_pdf_view.title(f"My Diary PDF reader (beta)")
			self.main_screen_pdf_view.after(250, lambda: self.main_screen_pdf_view.iconbitmap(self.icon_path))
				
			pdf_frame: CTkPDFViewer.CTkPDFViewer = CTkPDFViewer.CTkPDFViewer(self.main_screen_pdf_view, file=event.data)
			pdf_frame.pack(fill="both", expand=True)

		else:
			try:
				with open(event.data, f"r+", encoding=f"UTF-8") as self.openned_file: self.main_screen_frame_textbox.insert(f"1.0", self.openned_file.read())

			except FileNotFoundError: pass

	def __html_script__(self: typing.Self, event: str | None = None) -> None:
		self.main_screen_frame_textbox.insert(f"0.0", f"<!DOCTYPE html> \n  \n  <html lang='en'> \n <head> \n <meta charset='utf-8' /> \n <title></title> \n </head> \n <body> \n \n </body> \n </html>")	  																																			   

	def __exit__(self: typing.Self) -> None:
		if locale.getdefaultlocale()[0] == f"sr_RS":
			self.main_screen_exit: CTkMessagebox.CTkMessagebox = CTkMessagebox.CTkMessagebox(title=f"излаз", message=f"желите да изађете?", icon=f"question", option_2=f"да", option_1=f"не", button_color=f"green")
			if self.main_screen_exit.get() == f"да": sys.exit()
			else: pass

		elif locale.getdefaultlocale()[0] == f"ru_RU":
			self.main_screen_exit: CTkMessagebox.CTkMessagebox = CTkMessagebox.CTkMessagebox(title=f"выход", message=f"желайте выйти?", icon=f"question", option_2=f"да", option_1=f"нет", button_color=f"green")
			if self.main_screen_exit.get() == f"да": sys.exit()
			else: pass
			
		else:
			self.main_screen_exit: CTkMessagebox.CTkMessagebox = CTkMessagebox.CTkMessagebox(title=f"exit", message=f"would you like to exit?", icon=f"question", option_2=f"yes", option_1=f"no", button_color=f"green")
			if self.main_screen_exit.get() == f"yes": sys.exit()
			else: pass

if __name__ == f"__main__":
    program: Program = Program().mainloop()