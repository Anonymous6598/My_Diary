import customtkinter, tkinter, tkinter.filedialog, tkinter.messagebox, pickle, os, sys, docx, typing, My_Diary_interface, My_Diary_window, CTkMenuBar, locale, My_Diary_converterer, My_Diary_PDF_viewer, My_Diary_AI_window, g4f, CTkToolTip, tkinterdnd2, warnings, CTkScrollableDropdown

with open(f"my_diary_saved_text.pickle", f"rb+") as text_data: autosaved_text: str = pickle.load(text_data)

warnings.filterwarnings(f"ignore")
                                   
class Program(My_Diary_window.My_Diary_window, My_Diary_interface.My_Diary_interface):

    TITLE: typing.Final[str] = f"My Diary"
    COLOR_THEME: typing.Final[str] = f"dark-blue"
    WIDGET_SCALING: typing.Final[float] = 1.251
    ICON: typing.Final[str] = f"my_diary_icon.ico"

    def __init__(self: typing.Self, *args, **kwargs) -> None:
        My_Diary_window.My_Diary_window.__init__(self, *args, **kwargs)

        customtkinter.set_widget_scaling(self.WIDGET_SCALING)
        customtkinter.set_default_color_theme(self.COLOR_THEME)
        customtkinter.deactivate_automatic_dpi_awareness()

        self.title(self.TITLE)
        self.iconbitmap(self.ICON)
  
        self.bind(f"<Alt_L>" + f"<F4>", self.__exit__)
        self.bind(f"<Control_L>" + f"<s>", self.__save_text__)
        self.bind(f"<Control_L>" + f"<o>", self.__open_file__)
        self.bind(f"<Button-3>", self.__open_right_click_menu__)
        self.protocol(f"WM_DELETE_WINDOW", self.__exit__)

        self.main_screen_title_menu: CTkMenuBar.CTkTitleMenu = CTkMenuBar.CTkTitleMenu(master=self, title_bar_color=f"default")

        self.main_screen_title_menu_menu_button: customtkinter.CTkButton = self.main_screen_title_menu.add_cascade(text=f"☰")

        self.main_screen_title_menu_undo_button: customtkinter.CTkButton = self.main_screen_title_menu.add_cascade(text=f"⟲", command=self.__undo__)

        self.main_screen_title_menu_redo_button: customtkinter.CTkButton = self.main_screen_title_menu.add_cascade(text=f"⟳", command=self.__redo__)

        self.main_screen_frame_texbox_font: customtkinter.CTkFont = customtkinter.CTkFont(family=f"Ubuntu", size=22, weight=f"normal", slant=f"roman", underline=False, overstrike=False)

        self.main_screen_frame_textbox: customtkinter.CTkTextbox = customtkinter.CTkTextbox(master=self, height=795, width=1536, corner_radius=0, undo=True, fg_color=f"transparent", font=self.main_screen_frame_texbox_font, text_color=(f"black", f"white"))
        self.main_screen_frame_textbox.pack(expand=True, fill=f"both")

        self.main_screen_frame_textbox.drop_target_register(tkinterdnd2.DND_ALL)
        self.main_screen_frame_textbox.dnd_bind(f"<<Drop>>", self.__drop_file_into_textbox__)

        self.main_screen_frame_textbox.bind(f"<KeyRelease>", self.__word_count__)
        self.main_screen_frame_textbox.bind(f"<F1>", self.__html_script__)
        
        self.main_screen_edit_text_window: customtkinter.CTkToplevel = customtkinter.CTkToplevel()
        
        self.main_screen_edit_text_window.protocol(f"WM_DELETE_WINDOW", lambda: self.main_screen_edit_text_window.withdraw())
        self.main_screen_edit_text_window.title(f"My Diary font chooser window")
        self.main_screen_edit_text_window.after(250, lambda: self.main_screen_edit_text_window.iconbitmap(self.ICON))
        self.main_screen_edit_text_window.resizable(False, False)
        
        self.main_screen_edit_text_window.withdraw()
        
        self.main_screen_edit_font_button: customtkinter.CTkComboBox = customtkinter.CTkComboBox(master=self.main_screen_edit_text_window, height=20, width=75, corner_radius=0, values=[f"System", f"Terminal", f"Ubuntu", f"Script", f"Roman", f"Modern", f"MS Serif"], command=self.__edit_text_font__)

        self.main_screen_edit_size_button: customtkinter.CTkComboBox = customtkinter.CTkComboBox(master=self.main_screen_edit_text_window, height=20, width=75, corner_radius=0, values=[f"1", f"2", f"4", f"5", f"6", f"8", f"11", f"12", f"13", f"14", f"16", f"18", f"20", f"22", f"24", f"26", f"28", f"30", f"32", f"34", f"36", f"38", f"40", f"42", f"44", f"46", f"48", f"50", f"60", f"70", f"80", f"90", f"100"], command=self.__edit_text_font__)

        self.main_screen_edit_size_scrollable_button: CTkScrollableDropdown.CTkScrollableDropdown = CTkScrollableDropdown.CTkScrollableDropdown(self.main_screen_edit_size_button, values=[f"1", f"2", f"4", f"5", f"6", f"8", f"11", f"12", f"13", f"14", f"16", f"18", f"20", f"22", f"24", f"26", f"28", f"30", f"32", f"34", f"36", f"38", f"40", f"42", f"44", f"46", f"48", f"50", f"60", f"70", f"80", f"90", f"100"])

        self.main_screen_edit_color_button: customtkinter.CTkComboBox = customtkinter.CTkComboBox(master=self.main_screen_edit_text_window, height=20, width=75, corner_radius=0, values=[f"black", f"white", f"red", f"green", f"blue"], command=self.__edit_text_font__)

        self.main_screen_edit_slant_button: customtkinter.CTkComboBox = customtkinter.CTkComboBox(master=self.main_screen_edit_text_window, height=20, width=75, corner_radius=0, values=[f"roman", f"italic"], command=self.__edit_text_font__)

        self.main_screen_edit_weight_button: customtkinter.CTkComboBox = customtkinter.CTkComboBox(master=self.main_screen_edit_text_window, height=20, width=75, corner_radius=0, values=[f"normal", f"bold"], command=self.__edit_text_font__)

        self.main_screen_edit_underline_button: customtkinter.CTkComboBox = customtkinter.CTkComboBox(master=self.main_screen_edit_text_window, height=20, width=75, corner_radius=0, values=[f"not underlined", f"underlined"], command=self.__edit_text_font__)

        self.main_screen_edit_overstrike_button: customtkinter.CTkComboBox = customtkinter.CTkComboBox(master=self.main_screen_edit_text_window, height=20, width=75, corner_radius=0, values=[f"not overstriked", f"overstriked"], command=self.__edit_text_font__)

        self.main_screen_right_click_menu: tkinter.Menu = tkinter.Menu(self, tearoff=0)

        self.main_screen_title_menu_submenu: CTkMenuBar.CustomDropdownMenu = CTkMenuBar.CustomDropdownMenu(widget=self.main_screen_title_menu_menu_button, fg_color=f"transparent")

        if locale.getdefaultlocale()[0] == f"sr_RS":

            self.main_screen_save_button: customtkinter.CTkButton = self.main_screen_title_menu_submenu.add_option(option=f"сачувај текст", command=self.__save_text__)

            self.main_screen_open_button: customtkinter.CTkButton = self.main_screen_title_menu_submenu.add_option(option=f"отвори фајл", command=self.__open_file__)
        
            self.main_screen_clear_button: customtkinter.CTkButton = self.main_screen_title_menu_submenu.add_option(option=f"обриши текст", command=self.__clear_text__)
        
            self.main_screen_edit_text_button: customtkinter.CTkButton = self.main_screen_title_menu_submenu.add_option(option=f"уреди текст", command=self.__edit_text__)
        
            self.main_screen_converter_button: CTkMenuBar.CustomDropdownMenu = self.main_screen_title_menu_submenu.add_submenu(f"претварач")
        
            self.main_screen_pdf_to_word_converter_button: customtkinter.CTkButton  = self.main_screen_converter_button.add_option(f"из PDF у docx", command=My_Diary_converterer.My_Diary_converterer.pdf_to_docx)

            self.main_screen_word_to_pdf_converter_button: customtkinter.CTkButton  = self.main_screen_converter_button.add_option(f"из docx у PDF", command=My_Diary_converterer.My_Diary_converterer.docx_to_pdf)
        
            self.main_screen_pdf_to_txt_converter_button: customtkinter.CTkButton  = self.main_screen_converter_button.add_option(f"из PDF у txt", command=My_Diary_converterer.My_Diary_converterer.pdf_to_txt)

            self.main_screen_txt_to_pdf_converter_button: customtkinter.CTkButton  = self.main_screen_converter_button.add_option(f"из txt у PDF", command=My_Diary_converterer.My_Diary_converterer.txt_to_pdf)
        
            self.main_screen_txt_to_word_converter_button: customtkinter.CTkButton  = self.main_screen_converter_button.add_option(f"из txt у docx", command=My_Diary_converterer.My_Diary_converterer.txt_to_docx)

            self.main_screen_word_to_txt_converter_button: customtkinter.CTkButton  = self.main_screen_converter_button.add_option(f"из docx у txt", command=My_Diary_converterer.My_Diary_converterer.docx_to_txt)

            self.main_screen_ai_button: customtkinter.CTkButton = self.main_screen_title_menu_submenu.add_option(option=f"AI", command=lambda: My_Diary_AI_window.AI_Window())

            self.main_screen_right_click_menu.add_command(label=f"копирај", command=self.__copy__)
            self.main_screen_right_click_menu.add_command(label=f"налепи", command=self.__paste__)
            self.main_screen_right_click_menu.add_command(label=f"исеци", command=self.__cut__)

            self.main_screen_right_click_menu.add_separator()

            self.main_screen_right_click_menu.add_command(label=f"сачувај", command=self.__save_text__)
            self.main_screen_right_click_menu.add_command(label=f"отвори", command=self.__open_file__)

            self.main_screen_right_click_menu.add_separator()
            
            self.main_screen_right_click_menu.add_command(label=f"из docx у pdf", command=My_Diary_converterer.My_Diary_converterer.docx_to_pdf)
            self.main_screen_right_click_menu.add_command(label=f"из pdf у docx", command=My_Diary_converterer.My_Diary_converterer.pdf_to_docx)
            self.main_screen_right_click_menu.add_command(label=f"из txt у pdf", command=My_Diary_converterer.My_Diary_converterer.txt_to_pdf)
            self.main_screen_right_click_menu.add_command(label=f"из pdf у txt", command=My_Diary_converterer.My_Diary_converterer.pdf_to_txt)
            self.main_screen_right_click_menu.add_command(label=f"из txt у docx", command=My_Diary_converterer.My_Diary_converterer.txt_to_docx)
            self.main_screen_right_click_menu.add_command(label=f"из docx у txt", command=My_Diary_converterer.My_Diary_converterer.docx_to_txt)

            self.main_screen_right_click_menu.add_separator()

            self.main_screen_right_click_menu.add_command(label=f"изађи", command=self.__exit__)

        elif locale.getdefaultlocale()[0] == f"ru_RU":
            self.main_screen_save_button: customtkinter.CTkButton = self.main_screen_title_menu_submenu.add_option(option=f"сохранить текст", command=self.__save_text__)

            self.main_screen_open_button: customtkinter.CTkButton = self.main_screen_title_menu_submenu.add_option(option=f"открыть текст", command=self.__open_file__)
        
            self.main_screen_clear_button: customtkinter.CTkButton = self.main_screen_title_menu_submenu.add_option(option=f"удалить текст", command=self.__clear_text__)
        
            self.main_screen_edit_text_button: customtkinter.CTkButton = self.main_screen_title_menu_submenu.add_option(option=f"отредактировать текст", command=self.__edit_text__)
        
            self.main_screen_converter_button: CTkMenuBar.CustomDropdownMenu = self.main_screen_title_menu_submenu.add_submenu(f"конвертер")
        
            self.main_screen_pdf_to_word_converter_button: customtkinter.CTkButton  = self.main_screen_converter_button.add_option(f"из PDF в docx", command=My_Diary_converterer.My_Diary_converterer.pdf_to_docx)

            self.main_screen_word_to_pdf_converter_button: customtkinter.CTkButton  = self.main_screen_converter_button.add_option(f"из docx в PDF", command=My_Diary_converterer.My_Diary_converterer.docx_to_pdf)
        
            self.main_screen_pdf_to_txt_converter_button: customtkinter.CTkButton  = self.main_screen_converter_button.add_option(f"из PDF в txt", command=My_Diary_converterer.My_Diary_converterer.pdf_to_txt)

            self.main_screen_txt_to_pdf_converter_button: customtkinter.CTkButton  = self.main_screen_converter_button.add_option(f"из txt в PDF", command=My_Diary_converterer.My_Diary_converterer.txt_to_pdf)
        
            self.main_screen_txt_to_word_converter_button: customtkinter.CTkButton  = self.main_screen_converter_button.add_option(f"из txt в docx", command=My_Diary_converterer.My_Diary_converterer.txt_to_docx)

            self.main_screen_word_to_txt_converter_button: customtkinter.CTkButton  = self.main_screen_converter_button.add_option(f"из docx в txt", command=My_Diary_converterer.My_Diary_converterer.docx_to_txt)

            self.main_screen_ai_button: customtkinter.CTkButton = self.main_screen_title_menu_submenu.add_option(option=f"Нейро Сеть", command=lambda: My_Diary_AI_window.AI_Window())

            self.main_screen_right_click_menu.add_command(label=f"копировать", command=self.__copy__)
            self.main_screen_right_click_menu.add_command(label=f"вставить", command=self.__paste__)
            self.main_screen_right_click_menu.add_command(label=f"вырезать", command=self.__cut__)

            self.main_screen_right_click_menu.add_separator()

            self.main_screen_right_click_menu.add_command(label=f"сохранить", command=self.__save_text__)
            self.main_screen_right_click_menu.add_command(label=f"открыть", command=self.__open_file__)

            self.main_screen_right_click_menu.add_separator()
            
            self.main_screen_right_click_menu.add_command(label=f"из docx в pdf", command=My_Diary_converterer.My_Diary_converterer.docx_to_pdf)
            self.main_screen_right_click_menu.add_command(label=f"из pdf в docx", command=My_Diary_converterer.My_Diary_converterer.pdf_to_docx)
            self.main_screen_right_click_menu.add_command(label=f"из txt в pdf", command=My_Diary_converterer.My_Diary_converterer.txt_to_pdf)
            self.main_screen_right_click_menu.add_command(label=f"из pdf в txt", command=My_Diary_converterer.My_Diary_converterer.pdf_to_txt)
            self.main_screen_right_click_menu.add_command(label=f"из txt в docx", command=My_Diary_converterer.My_Diary_converterer.txt_to_docx)
            self.main_screen_right_click_menu.add_command(label=f"из docx в txt", command=My_Diary_converterer.My_Diary_converterer.docx_to_txt)

            self.main_screen_right_click_menu.add_separator()

            self.main_screen_right_click_menu.add_command(label=f"выйти", command=self.__exit__)

        else:
            self.main_screen_save_button: customtkinter.CTkButton = self.main_screen_title_menu_submenu.add_option(option=f"save", command=self.__save_text__)

            self.main_screen_open_button: customtkinter.CTkButton = self.main_screen_title_menu_submenu.add_option(option=f"open", command=self.__open_file__)
        
            self.main_screen_clear_button: customtkinter.CTkButton = self.main_screen_title_menu_submenu.add_option(option=f"clear", command=self.__clear_text__)
        
            self.main_screen_edit_text_button: customtkinter.CTkButton = self.main_screen_title_menu_submenu.add_option(option=f"edit", command=self.__edit_text__)
        
            self.main_screen_converter_button: CTkMenuBar.CustomDropdownMenu = self.main_screen_title_menu_submenu.add_submenu(f"converter")
        
            self.main_screen_pdf_to_word_converter_button: customtkinter.CTkButton  = self.main_screen_converter_button.add_option(f"from PDF to docx", command=My_Diary_converterer.My_Diary_converterer.pdf_to_docx)

            self.main_screen_word_to_pdf_converter_button: customtkinter.CTkButton  = self.main_screen_converter_button.add_option(f"from docx to PDF", command=My_Diary_converterer.My_Diary_converterer.docx_to_pdf)
        
            self.main_screen_pdf_to_txt_converter_button: customtkinter.CTkButton  = self.main_screen_converter_button.add_option(f"from PDF to txt", command=My_Diary_converterer.My_Diary_converterer.pdf_to_txt)

            self.main_screen_txt_to_pdf_converter_button: customtkinter.CTkButton  = self.main_screen_converter_button.add_option(f"from txt to PDF", command=My_Diary_converterer.My_Diary_converterer.txt_to_pdf)
        
            self.main_screen_txt_to_word_converter_button: customtkinter.CTkButton  = self.main_screen_converter_button.add_option(f"from txt to docx", command=My_Diary_converterer.My_Diary_converterer.txt_to_docx)

            self.main_screen_word_to_txt_converter_button: customtkinter.CTkButton  = self.main_screen_converter_button.add_option(f"from docx to txt", command=My_Diary_converterer.My_Diary_converterer.docx_to_txt)

            self.main_screen_ai_button: customtkinter.CTkButton = self.main_screen_title_menu_submenu.add_option(option=f"AI", command=lambda: My_Diary_AI_window.AI_Window())

            self.main_screen_right_click_menu.add_command(label=f"copy", command=self.__copy__)
            self.main_screen_right_click_menu.add_command(label=f"paste", command=self.__paste__)
            self.main_screen_right_click_menu.add_command(label=f"cut", command=self.__cut__)

            self.main_screen_right_click_menu.add_separator()

            self.main_screen_right_click_menu.add_command(label=f"save", command=self.__save_text__)
            self.main_screen_right_click_menu.add_command(label=f"open", command=self.__open_file__)

            self.main_screen_right_click_menu.add_separator()
            
            self.main_screen_right_click_menu.add_command(label=f"from docx into pdf", command=My_Diary_converterer.My_Diary_converterer.docx_to_pdf)
            self.main_screen_right_click_menu.add_command(label=f"from pdf into docx", command=My_Diary_converterer.My_Diary_converterer.pdf_to_docx)
            self.main_screen_right_click_menu.add_command(label=f"from txt into pdf", command=My_Diary_converterer.My_Diary_converterer.txt_to_pdf)
            self.main_screen_right_click_menu.add_command(label=f"from pdf into txt", command=My_Diary_converterer.My_Diary_converterer.pdf_to_txt)
            self.main_screen_right_click_menu.add_command(label=f"from txt into docx", command=My_Diary_converterer.My_Diary_converterer.txt_to_docx)
            self.main_screen_right_click_menu.add_command(label=f"from docx into txt", command=My_Diary_converterer.My_Diary_converterer.docx_to_txt)

            self.main_screen_right_click_menu.add_separator()

            self.main_screen_right_click_menu.add_command(label=f"exit", command=self.__exit__)

        self.bind(f"<KeyRelease>", self.__text_autosave__)
        self.main_screen_frame_textbox.bind(f"<F2>", self.__enter_text_autosave__)

        self.main_screen_title_menu_summary_button: customtkinter.CTkButton = self.main_screen_title_menu_submenu.add_option(option=f"long story short", command=self.__text_summary__)

        self.main_screen_title_menu_creativity_button: customtkinter.CTkButton = self.main_screen_title_menu_submenu.add_option(option=f"my shakespeare", command=self.__create_text__)

        self.main_screen_word_counter_variable: int = 0

        self.main_screen_word_counter_data_variable: tkinter.IntVar = tkinter.IntVar(value=self.main_screen_word_counter_variable)

        self.main_screen_title_menu_word_count: customtkinter.CTkButton = self.main_screen_title_menu.add_cascade(textvariable=self.main_screen_word_counter_data_variable, command=self.__word_count_show__)

        if locale.getdefaultlocale()[0] == f"sr_RS":
            self.main_screen_title_menu_creativity_button_tooltip: CTkToolTip.CTkToolTip = CTkToolTip.CTkToolTip(self.main_screen_title_menu_creativity_button, message=f"направи текст уз помоћ вештачке интелигенције")
            self.main_screen_title_menu_menu_button_tooltip: CTkToolTip.CTkToolTip = CTkToolTip.CTkToolTip(self.main_screen_title_menu_menu_button, message=f"мени")
            self.main_screen_title_menu_summary_button_tooltip: CTkToolTip.CTkToolTip = CTkToolTip.CTkToolTip(self.main_screen_title_menu_summary_button, message=f"кратак опис текста")

        elif locale.getdefaultlocale()[0] == f"ru_RU":
            self.main_screen_title_menu_creativity_button_tooltip: CTkToolTip.CTkToolTip = CTkToolTip.CTkToolTip(self.main_screen_title_menu_creativity_button, message=f"сделай текст с помощью нейросети")
            self.main_screen_title_menu_menu_button_tooltip: CTkToolTip.CTkToolTip = CTkToolTip.CTkToolTip(self.main_screen_title_menu_menu_button, message=f"меню")
            self.main_screen_title_menu_summary_button_tooltip: CTkToolTip.CTkToolTip = CTkToolTip.CTkToolTip(self.main_screen_title_menu_summary_button, message=f"краткое описание текста")
    
        else:
            self.main_screen_title_menu_creativity_button_tooltip: CTkToolTip.CTkToolTip = CTkToolTip.CTkToolTip(self.main_screen_title_menu_creativity_button, message=f"make text with AI")
            self.main_screen_title_menu_menu_button_tooltip: CTkToolTip.CTkToolTip = CTkToolTip.CTkToolTip(self.main_screen_title_menu_menu_button, message=f"menu")
            self.main_screen_title_menu_summary_button_tooltip: CTkToolTip.CTkToolTip = CTkToolTip.CTkToolTip(self.main_screen_title_menu_summary_button, message=f"short story of text")

    @typing.override
    def __undo__(self: typing.Self) -> None:
        try: self.main_screen_frame_textbox.edit_undo()

        except tkinter.TclError: pass

    @typing.override		
    def __redo__(self: typing.Self) -> None:
        try: self.main_screen_frame_textbox.edit_redo()

        except tkinter.TclError: pass

    @typing.override
    def __save_text__(self: typing.Self, event: str | None = None) -> None:
        try:
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
                        self.file_data: str = self.main_screen_frame_textbox.get("1.0", tkinter.END)
                        pickle.dump(self.file_data, self.file)
                        
                case _:
                    with open(self.file_name, f"w+", encoding=f"UTF-8") as self.file:
                        self.file_data: str = self.main_screen_frame_textbox.get("1.0", tkinter.END)
                        self.file.write(self.file_data)

        except FileNotFoundError: pass

    @typing.override
    def __clear_text__(self: typing.Self) -> None:
        self.main_screen_frame_textbox.delete(f"1.0", tkinter.END)
    
    @typing.override
    def __edit_text__(self: typing.Self) -> None:
        self.main_screen_edit_text_window.deiconify()

        self.main_screen_edit_font_button.grid(column=1, row=0)
        self.main_screen_edit_size_button.grid(column=2, row=0)
        self.main_screen_edit_color_button.grid(column=3, row=0)
        self.main_screen_edit_slant_button.grid(column=4, row=0)
        self.main_screen_edit_weight_button.grid(column=5, row=0)
        self.main_screen_edit_underline_button.grid(column=6, row=0)
        self.main_screen_edit_overstrike_button.grid(column=7, row=0)

    @typing.override
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

    @typing.override
    def __open_file__(self: typing.Self, event: str | None = None) -> None:
        try:
            self.opened_name_file: tkinter.filedialog = tkinter.filedialog.askopenfilename(title=f"open file", filetypes=[(f"All Files (*.*)", f"*.*"), (f"Word file (*.docx)", f"*.docx"), (f"Text file (*.txt)", f"*.txt"), (f"PDF file (*.pdf)", f"*.pdf"), (f"Python file (*.py)", f"*.py"), (f"Java file (*.java)", f"*.java"), (f"C# file (*.cs)", f"*.cs"), (f"HTML file (*.html)", f"*.html"), (f"CSS file (*.css)", f"*.css"), (f"JavaScript file (*.js)", f"*.js"), (f"C++ file (*.cpp)", f"*.cpp"), (f"Pickle file (*.pickle)", f"*.pickle")], defaultextension=[(f"All Files (*.*)", f"*.*"), (f"Text file (*.txt)", f"*.txt"), (f"Word file (*.docx)", f"*.docx"), (f"PDF file (*.pdf)", f"*.pdf"), (f"Python file (*.py)", f"*.py"), (f"Java file (*.java)", f"*.java"), (f"C# file (*.cs)", f"*.cs"), (f"HTML file (*.html)", f"*.html"), (f"CSS file (*.css)", f"*.css"), (f"JavaScript file (*.js)", f"*.js"), (f"C++ file (*.cpp)", f"*.cpp"), (f"Pickle file (*.pickle)", f"*.pickle")])
            match os.path.splitext(self.opened_name_file)[1]:
                case ".docx":
                    self.openned_file: docx.Document = docx.Document(self.opened_name_file)
                    self.openned_file_data: list[str] = []
                    for self.paragraphs in self.openned_file.paragraphs: self.openned_file_data.append(self.paragraphs.text)

                    self.main_screen_frame_textbox.insert(f"1.0", f"\n".join(self.openned_file_data))
                
                case ".pickle":
                    with open(self.opened_name_file, f"rb+") as self.openned_file: self.main_screen_frame_textbox.insert(f"1.0", pickle.load(self.openned_file))
                    
                case ".pdf":
                    self.my_diary_pdf_view: My_Diary_PDF_viewer.My_Diary_PDF_viewer = My_Diary_PDF_viewer.My_Diary_PDF_viewer().__show_pdf__(self.opened_name_file)
                
                case _: 
                    with open(self.opened_name_file, f"r+", encoding=f"UTF-8") as self.openned_file: self.main_screen_frame_textbox.insert(f"1.0", self.openned_file.read())

        except FileNotFoundError: pass

        except docx.opc.exceptions.PackageNotFoundError: pass
    
    @typing.override		
    def __text_autosave__(self: typing.Self, event: str | None = None) -> None: 
        with open(f"my_diary_saved_text.pickle", f"wb+") as self.text_data: pickle.dump(self.main_screen_frame_textbox.get(f"1.0", tkinter.END), self.text_data)

    @typing.override
    def __enter_text_autosave__(self: typing.Self, event: str | None = None) -> None:
        self.main_screen_frame_textbox.insert(f"1.0", autosaved_text)

    @typing.override
    def __word_count__(self: typing.Self, event: str | None = None) -> None:
        self.main_screen_frame_textbox_data: str = self.main_screen_frame_textbox.get(f"0.0", tkinter.END)
        self.main_screen_word_counter_data_variable.set(value=len(self.main_screen_frame_textbox_data.split()))

    @typing.override
    def __word_count_show__(self: typing.Self) -> None:
        if locale.getdefaultlocale()[0] == f"sr_RS":
            tkinter.messagebox.showinfo(title=f"речи", message=f"речи: {len(self.main_screen_frame_textbox.get(f'1.0', tkinter.END).split())}")
            
        elif locale.getdefaultlocale()[0] == f"ru_RU":
            tkinter.messagebox.showinfo(title=f"слов", message=f"слов: {len(self.main_screen_frame_textbox.get(f'1.0', tkinter.END).split())}")
            
        else:
            tkinter.messagebox.showinfo(title=f"words", message=f"words: {len(self.main_screen_frame_textbox.get(f'1.0', tkinter.END).split())}")

    @typing.override
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
            
        elif event.data.endswith(f".pdf"):
            try: self.my_diary_pdf_view: My_Diary_PDF_viewer.My_Diary_PDF_viewer = My_Diary_PDF_viewer.My_Diary_PDF_viewer().__show_pdf__(event.data)

            except FileNotFoundError: pass

        elif os.path.isfile(event.data):
            try:
                with open(event.data, f"r+", encoding=f"UTF-8") as self.openned_file: self.main_screen_frame_textbox.insert(f"1.0", self.openned_file.read())

            except FileNotFoundError: pass

        else:
            self.main_screen_frame_textbox.insert(f"1.0", event.data)

    @typing.override
    def __html_script__(self: typing.Self, event: str | None = None) -> None:
        self.main_screen_frame_textbox.insert(f"0.0", f"<!DOCTYPE html> \n  \n  <html lang='en'> \n <head> \n <meta charset='utf-8' /> \n <title></title> \n </head> \n <body> \n \n </body> \n </html>")	  																																			   

    @typing.override
    def __open_right_click_menu__(self: typing.Self, event: str | None = None) -> None:
        self.main_screen_right_click_menu.post(event.x_root, event.y_root)

    @typing.override
    def __cut__(self: typing.Self) -> None:
        self.selected_text: str = self.main_screen_frame_textbox.selection_get()
        self.main_screen_frame_textbox.delete(f"sel.first", f"sel.last")
        self.clipboard_clear()
        self.clipboard_append(self.selected_text)

    @typing.override
    def __copy__(self: typing.Self) -> None:
        self.selected_text: str = self.main_screen_frame_textbox.selection_get()
        self.clipboard_clear()
        self.clipboard_append(self.selected_text)

    @typing.override
    def __paste__(self: typing.Self) -> None:
        try:
            self.cursor_position: int = self.main_screen_frame_textbox.index(tkinter.INSERT)
            self.clipboard_text: str = self.clipboard_get()
            self.main_screen_frame_textbox.insert(self.cursor_position, self.clipboard_text)
        
        except tkinter.TclError:
            pass

    @typing.override
    def __text_summary__(self: typing.Self) -> None:
        self.summary: str = g4f.ChatCompletion.create(model=f"gpt-4o", messages=[{f"role": f"system", f"content": f"Summarize the following text:"}, {f"role": f"user", f"content": self.main_screen_frame_textbox.get(f"1.0", tkinter.END)}])
        if locale.getdefaultlocale()[0] == f"sr_RS":
            tkinter.messagebox.showinfo(title=f"long story short", message=f"Резиме: {self.summary}")
        
        elif locale.getdefaultlocale()[0] == f"ru_RU":
            tkinter.messagebox.showinfo(title=f"long story short", message=f"Сводка: {self.summary}")
        
        else:
            tkinter.messagebox.showinfo(title=f"long story short", message=f"Summary: {self.summary}")

    @typing.override
    def __create_text__(self: typing.Self) -> None:
        if locale.getdefaultlocale()[0] == f"sr_RS":
            self.text_topic_input: customtkinter.CTkInputDialog = customtkinter.CTkInputDialog(title=f"нови текст", text=f"унесите текст тему")
            self.text_topic_input.after(250, lambda: self.text_topic_input.iconbitmap(self.ICON))

        elif locale.getdefaultlocale()[0] == f"ru_RU":
            self.text_topic_input: customtkinter.CTkInputDialog = customtkinter.CTkInputDialog(title=f"новый текст", text=f"введите текст тему")
            self.text_topic_input.after(250, lambda: self.text_topic_input.iconbitmap(self.ICON))

        else:
            self.text_topic_input: customtkinter.CTkInputDialog = customtkinter.CTkInputDialog(title=f"new text", text=f"enter text topic")
            self.text_topic_input.after(250, lambda: self.text_topic_input.iconbitmap(self.ICON))

        self.create_text: str = g4f.ChatCompletion.create(model=f"gpt-4o", messages=[{f"role": f"system", f"content": f"Create text based on user prompt:"}, {f"role": f"user", f"content": self.text_topic_input.get_input()}])
        self.main_screen_frame_textbox.insert(f"1.0", self.create_text)

    @typing.override
    def __exit__(self: typing.Self) -> None:
        if locale.getdefaultlocale()[0] == f"sr_RS":
            self.main_screen_exit: tkinter.messagebox = tkinter.messagebox.askyesno(title=f"излаз", message=f"желите да изађете?")
            if self.main_screen_exit: sys.exit()

        elif locale.getdefaultlocale()[0] == f"ru_RU":
            self.main_screen_exit: tkinter.messagebox = tkinter.messagebox.askyesno(title=f"выход", message=f"желайте выйти?")
            if self.main_screen_exit: sys.exit()
            
        else:
            self.main_screen_exit: tkinter.messagebox = tkinter.messagebox.askyesno(title=f"exit", message=f"would you like to exit?")
            if self.main_screen_exit: sys.exit()

if __name__ == f"__main__":
    program: Program = Program()
    program.mainloop()

