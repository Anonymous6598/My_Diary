import customtkinter, tkinter, My_Diary, typing, My_Diary_command_prompt_interface

class Terminal(customtkinter.CTkToplevel, My_Diary_command_prompt_interface.My_Diary_command_prompt_interface):

	HEIGHT: typing.Final[int] = 375
	WIDTH: typing.Final[int] = 650
	WINDOW: typing.Final[str] = "-toolwindow"
	TITLE: typing.Final[str] = "My Diary command prompt"

	def __init__(self, *args, **kwargs) -> None:
		customtkinter.CTkToplevel.__init__(self, *args, **kwargs)

		self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
		self.attributes(self.WINDOW, True)
		self.resizable(False, False)
		self.title(self.TITLE)

		self.terminal_frame: customtkinter.CTkFrame = customtkinter.CTkFrame(master=self, height=300, width=520, fg_color="black", border_width=0)
		self.terminal_frame.place(x=0, y=0)

		self.terminal_textbox: customtkinter.CTkTextbox = customtkinter.CTkTextbox(master=self.terminal_frame, height=264, width=517, fg_color="transparent", text_color="green", font=("Ubuntu", 22))
		self.terminal_textbox.place(x=1.5, y=1)

		self.terminal_textbox.insert("0.0", ">>>")
		self.terminal_textbox.configure(state="disabled")

		self.terminal_entry: customtkinter.CTkEntry = customtkinter.CTkEntry(master=self.terminal_frame, height=30, width=517, border_width=0, fg_color="transparent", placeholder_text="...", placeholder_text_color="green", text_color="green", font=("Ubuntu", 22))
		self.terminal_entry.place(x=1.5, y=267)

		self.terminal_entry.bind("<Return>", self.__terminal_action__)

	def __terminal_action__(self, event: str) -> None:
		self.terminal_entry_data = self.terminal_entry.get()

		self.terminal_textbox.configure(state="normal")
		if self.terminal_entry_data == "сачувај текст као ..." or self.terminal_entry_data == "save text as ..." or self.terminal_entry_data == "сохранить текст как ...":
			program.__save_text_as__(event)

			self.terminal_textbox.configure(state="normal")
			self.terminal_textbox.insert(tkinter.END, self.terminal_entry_data + "\n", "-1.0")
			self.terminal_textbox.insert(tkinter.END, ">>>", "-1.0")
			self.terminal_textbox.configure(state="disabled")
			self.terminal_entry.delete("-1", tkinter.END)

		elif self.terminal_entry_data == "сачувај текст као docx" or self.terminal_entry_data == "save text as docx" or self.terminal_entry_data == "сохранить текст как ворд":
			program.__save_text_as_docx__()

			self.terminal_textbox.configure(state="normal")
			self.terminal_textbox.insert(tkinter.END, self.terminal_entry_data + "\n", "-1.0")
			self.terminal_textbox.insert(tkinter.END, ">>>", "-1.0")
			self.terminal_textbox.configure(state="disabled")
			self.terminal_entry.delete("-1", tkinter.END)

		elif self.terminal_entry_data == "обриши текст" or self.terminal_entry_data == "clear text" or self.terminal_entry_data == "удалить текст":
			program.__clear_text__()

			self.terminal_textbox.configure(state="normal")
			self.terminal_textbox.insert(tkinter.END, self.terminal_entry_data + "\n", "-1.0")
			self.terminal_textbox.insert(tkinter.END, ">>>", "-1.0")
			self.terminal_textbox.configure(state="disabled")
			self.terminal_entry.delete("-1", tkinter.END)

		elif self.terminal_entry_data == "отвори ... фајл" or self.terminal_entry_data == "open ... file" or self.terminal_entry_data == "открыть ... файл":
			program.__open_file__(event)

			self.terminal_textbox.configure(state="normal")
			self.terminal_textbox.insert(tkinter.END, self.terminal_entry_data + "\n", "-1.0")
			self.terminal_textbox.insert(tkinter.END, ">>>", "-1.0")
			self.terminal_textbox.configure(state="disabled")
			self.terminal_entry.delete("-1", tkinter.END)

		elif self.terminal_entry_data == "отвори docx фајл" or self.terminal_entry_data == "open docx file" or self.terminal_entry_data == "открыть ворд файл":
			program.__open_file_docx__()

			self.terminal_textbox.configure(state="normal")
			self.terminal_textbox.insert(tkinter.END, self.terminal_entry_data + "\n", "-1.0")
			self.terminal_textbox.insert(tkinter.END, ">>>", "-1.0")
			self.terminal_textbox.configure(state="disabled")
			self.terminal_entry.delete("-1", tkinter.END)

		elif self.terminal_entry_data == "претвори из pdf у docx" or self.terminal_entry_data == "convert pdf to docx" or self.terminal_entry_data == "превратить из пдф в ворд":
			program.__pdf_to_docx__()

			self.terminal_textbox.configure(state="normal")
			self.terminal_textbox.insert(tkinter.END, self.terminal_entry_data + "\n", "-1.0")
			self.terminal_textbox.insert(tkinter.END, ">>>", "-1.0")
			self.terminal_textbox.configure(state="disabled")
			self.terminal_entry.delete("-1", tkinter.END)

		elif self.terminal_entry_data == "претвори из docx у pdf" or self.terminal_entry_data == "convert docx to pdf" or self.terminal_entry_data == "превратить из ворд в пдф":
			program.__docx_to_pdf__()

			self.terminal_textbox.configure(state="normal")
			self.terminal_textbox.insert(tkinter.END, self.terminal_entry_data + "\n", "-1.0")
			self.terminal_textbox.insert(tkinter.END, ">>>", "-1.0")
			self.terminal_textbox.configure(state="disabled")
			self.terminal_entry.delete("-1", tkinter.END)

		elif self.terminal_entry_data == "претвори из pdf у txt" or self.terminal_entry_data == "convert pdf to txt" or self.terminal_entry_data == "превратить из пдф в текст":
			program.__pdf_to_txt__()

			self.terminal_textbox.configure(state="normal")
			self.terminal_textbox.insert(tkinter.END, self.terminal_entry_data + "\n", "-1.0")
			self.terminal_textbox.insert(tkinter.END, ">>>", "-1.0")
			self.terminal_textbox.configure(state="disabled")
			self.terminal_entry.delete("-1", tkinter.END)

		elif self.terminal_entry_data == "претвори из txt у pdf" or self.terminal_entry_data == "convert txt to pdf" or self.terminal_entry_data == "превратить из текст в пдф":
			program.__txt_to_pdf__()

			self.terminal_textbox.configure(state="normal")
			self.terminal_textbox.insert(tkinter.END, self.terminal_entry_data + "\n", "-1.0")
			self.terminal_textbox.insert(tkinter.END, ">>>", "-1.0")
			self.terminal_textbox.configure(state="disabled")
			self.terminal_entry.delete("-1", tkinter.END)

		elif self.terminal_entry_data == "претвори из docx у txt" or self.terminal_entry_data == "convert docx to txt" or self.terminal_entry_data == "превратить из ворд в текст":
			program.__docx_to_txt__()

			self.terminal_textbox.configure(state="normal")
			self.terminal_textbox.insert(tkinter.END, self.terminal_entry_data + "\n", "-1.0")
			self.terminal_textbox.insert(tkinter.END, ">>>", "-1.0")
			self.terminal_textbox.configure(state="disabled")
			self.terminal_entry.delete("-1", tkinter.END)

		elif self.terminal_entry_data == "претвори из txt у docx" or self.terminal_entry_data == "convert txt to docx" or self.terminal_entry_data == "превратить из ворд в текст":
			program.__txt_to_docx__()
			
			self.terminal_textbox.configure(state="normal")
			self.terminal_textbox.insert(tkinter.END, self.terminal_entry_data + "\n", "-1.0")
			self.terminal_textbox.insert(tkinter.END, ">>>", "-1.0")
			self.terminal_textbox.configure(state="disabled")
			self.terminal_entry.delete("-1", tkinter.END)

		elif self.terminal_entry_data == "отвори конзолу" or self.terminal_entry_data == "open shell" or self.terminal_entry_data == "открыть консоль":
			program.__open_shell__()
			
			self.terminal_textbox.configure(state="normal")
			self.terminal_textbox.insert(tkinter.END, self.terminal_entry_data + "\n", "-1.0")
			self.terminal_textbox.insert(tkinter.END, ">>>", "-1.0")
			self.terminal_textbox.configure(state="disabled")
			self.terminal_entry.delete("-1", tkinter.END)

		elif self.terminal_entry_data == "отвори powershell" or self.terminal_entry_data == "open powershell" or self.terminal_entry_data == "открыть powershell":
			program.__open_powershell__()
			
			self.terminal_textbox.configure(state="normal")
			self.terminal_textbox.insert(tkinter.END, self.terminal_entry_data + "\n", "-1.0")
			self.terminal_textbox.insert(tkinter.END, ">>>", "-1.0")
			self.terminal_textbox.configure(state="disabled")
			self.terminal_entry.delete("-1", tkinter.END)

		elif self.terminal_entry_data == "сачувај код као" or self.terminal_entry_data == "save code as" or self.terminal_entry_data == "сохранить код как":
			program.__save_code_as__(event)
			
			self.terminal_textbox.configure(state="normal")
			self.terminal_textbox.insert(tkinter.END, self.terminal_entry_data + "\n", "-1.0")
			self.terminal_textbox.insert(tkinter.END, ">>>", "-1.0")
			self.terminal_textbox.configure(state="disabled")
			self.terminal_entry.delete("-1", tkinter.END)

		elif self.terminal_entry_data == "отвори код" or self.terminal_entry_data == "open code" or self.terminal_entry_data == "открыть код":
			program.__open_code__()
			
			self.terminal_textbox.configure(state="normal")
			self.terminal_textbox.insert(tkinter.END, self.terminal_entry_data + "\n", "-1.0")
			self.terminal_textbox.insert(tkinter.END, ">>>", "-1.0")
			self.terminal_textbox.configure(state="disabled")
			self.terminal_entry.delete("-1", tkinter.END)
			
		elif self.terminal_entry_data == "боја текста 1" or self.terminal_entry_data == "text color 1" or self.terminal_entry_data == "цвет текста 1":
			self.terminal_entry.configure(text_color="red")
			self.terminal_textbox.configure(text_color="red")

			self.terminal_textbox.configure(state="normal")
			self.terminal_textbox.insert(tkinter.END, self.terminal_entry_data + "\n", "-1.0")
			self.terminal_textbox.insert(tkinter.END, ">>>", "-1.0")
			self.terminal_textbox.configure(state="disabled")
			self.terminal_entry.delete("-1", tkinter.END)
			
		elif self.terminal_entry_data == "боја текста 2" or self.terminal_entry_data == "text color 2" or self.terminal_entry_data == "цвет текста 2":
			self.terminal_entry.configure(text_color="green")
			self.terminal_textbox.configure(text_color="green")

			self.terminal_textbox.configure(state="normal")
			self.terminal_textbox.insert(tkinter.END, self.terminal_entry_data + "\n", "-1.0")
			self.terminal_textbox.insert(tkinter.END, ">>>", "-1.0")
			self.terminal_textbox.configure(state="disabled")
			self.terminal_entry.delete("-1", tkinter.END)
		
		elif self.terminal_entry_data == "боја текста 3" or self.terminal_entry_data == "text color 3" or self.terminal_entry_data == "цвет текста 3":
			self.terminal_entry.configure(text_color="blue")
			self.terminal_textbox.configure(text_color="blue")

			self.terminal_textbox.configure(state="normal")
			self.terminal_textbox.insert(tkinter.END, self.terminal_entry_data + "\n", "-1.0")
			self.terminal_textbox.insert(tkinter.END, ">>>", "-1.0")
			self.terminal_textbox.configure(state="disabled")
			self.terminal_entry.delete("-1", tkinter.END)
			
		elif self.terminal_entry_data == "боја текста 4" or self.terminal_entry_data == "text color 4" or self.terminal_entry_data == "цвет текста 4":
			self.terminal_entry.configure(text_color="white")
			self.terminal_textbox.configure(text_color="white")

			self.terminal_textbox.configure(state="normal")
			self.terminal_textbox.insert(tkinter.END, self.terminal_entry_data + "\n", "-1.0")
			self.terminal_textbox.insert(tkinter.END, ">>>", "-1.0")
			self.terminal_textbox.configure(state="disabled")
			self.terminal_entry.delete("-1", tkinter.END)
		
		elif self.terminal_entry_data == "боја текста 5" or self.terminal_entry_data == "text color 5" or self.terminal_entry_data == "цвет текста 5":
			self.terminal_entry.configure(text_color="purple")
			self.terminal_textbox.configure(text_color="purple")

			self.terminal_textbox.configure(state="normal")
			self.terminal_textbox.insert(tkinter.END, self.terminal_entry_data + "\n", "-1.0")
			self.terminal_textbox.insert(tkinter.END, ">>>", "-1.0")
			self.terminal_textbox.configure(state="disabled")
			self.terminal_entry.delete("-1", tkinter.END)
			
		elif self.terminal_entry_data == "боја текста 6" or self.terminal_entry_data == "text color 6" or self.terminal_entry_data == "цвет текста 6":
			self.terminal_entry.configure(text_color="yellow")
			self.terminal_textbox.configure(text_color="yellow")

			self.terminal_textbox.configure(state="normal")
			self.terminal_textbox.insert(tkinter.END, self.terminal_entry_data + "\n", "-1.0")
			self.terminal_textbox.insert(tkinter.END, ">>>", "-1.0")
			self.terminal_textbox.configure(state="disabled")
			self.terminal_entry.delete("-1", tkinter.END)
			
		elif self.terminal_entry_data == "помоћ":
			self.terminal_textbox.configure(state="normal")
			self.terminal_textbox.insert(tkinter.END, f"commands: \n 1) сачувај текст / код као ... \n 2) отвори ... фајл / код / конзолу / powershell \n 3) конвертирај из ... у ... \n 4) изађи из програма / терминала \n 5) боја текста(1-6) \n", "-1.0")
			self.terminal_textbox.insert(tkinter.END, ">>>", "-1.0")
			self.terminal_textbox.configure(state="disabled")
			self.terminal_entry.delete("-1", tkinter.END)

		elif self.terminal_entry_data == "help":
			self.terminal_textbox.configure(state="normal")
			self.terminal_textbox.insert(tkinter.END, f"commands: \n 1) save text / code as ... \n 2) open ... file / code / shell / powershell \n 3) convert ... to ... \n 4) exit program / terminal \n 5) text color(1-6) \n", "-1.0")
			self.terminal_textbox.insert(tkinter.END, ">>>", "-1.0")
			self.terminal_textbox.configure(state="disabled")
			self.terminal_entry.delete("-1", tkinter.END)
			
		elif self.terminal_entry_data == "помощь":
			self.terminal_textbox.configure(state="normal")
			self.terminal_textbox.insert(tkinter.END, f"commands: \n 1) сохранить текст / код как ... \n 2) открыть ... файл / код / консоль / powershell \n 3) превратить из ... в ... \n 4) выйти из программы / терминала \n 5) цвет текста(1-6) \n", "-1.0")
			self.terminal_textbox.insert(tkinter.END, ">>>", "-1.0")
			self.terminal_textbox.configure(state="disabled")
			self.terminal_entry.delete("-1", tkinter.END)

		elif self.terminal_entry_data == "изађи из терминала" or self.terminal_entry_data == "exit terminal" or self.terminal_entry_data == "выйти из терминала":
			self.destroy()

		elif self.terminal_entry_data == "изађи из програма" or self.terminal_entry_data == "exit program" or self.terminal_entry_data == "выйти из программы":
			program.__exit__()
		
		else:
			self.terminal_textbox.configure(state="normal")
			self.terminal_textbox.insert(tkinter.END, self.terminal_entry_data + " - команда не постоји / command doesn't exist / команда не существует" + "\n", "-1.0")
			self.terminal_textbox.insert(tkinter.END, ">>>", "-1.0")
			self.terminal_textbox.configure(state="disabled")
			self.terminal_entry.delete("-1", tkinter.END)

program: My_Diary.Program = My_Diary.Program()