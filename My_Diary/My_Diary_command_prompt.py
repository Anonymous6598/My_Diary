import customtkinter, tkinter, My_Diary, typing, My_Diary_command_prompt_interface

class Terminal(customtkinter.CTkToplevel, My_Diary_command_prompt_interface.My_Diary_command_prompt_interface):

	HEIGHT: typing.Final[int] = 375
	WIDTH: typing.Final[int] = 650
	WINDOW: typing.Final[str] = f"-toolwindow"
	TITLE: typing.Final[str] = f"My Diary command prompt"

	def __init__(self: typing.Self, *args, **kwargs) -> None:
		customtkinter.CTkToplevel.__init__(self, *args, **kwargs)

		self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
		self.attributes(self.WINDOW, True)
		self.resizable(False, False)
		self.title(self.TITLE)

		self.terminal_frame: customtkinter.CTkFrame = customtkinter.CTkFrame(master=self, height=300, width=520, fg_color=f"black", border_width=0)
		self.terminal_frame.place(x=0, y=0)

		self.terminal_textbox: customtkinter.CTkTextbox = customtkinter.CTkTextbox(master=self.terminal_frame, height=264, width=517, fg_color=f"transparent", text_color=f"green", font=(f"Ubuntu", 22))
		self.terminal_textbox.place(x=1.5, y=1)

		self.terminal_textbox.insert(f"0.0", f">>>")
		self.terminal_textbox.configure(state=f"disabled")

		self.terminal_entry: customtkinter.CTkEntry = customtkinter.CTkEntry(master=self.terminal_frame, height=30, width=517, border_width=0, fg_color=f"transparent", placeholder_text=f"...", placeholder_text_color=f"green", text_color=f"green", font=(f"Ubuntu", 22))
		self.terminal_entry.place(x=1.5, y=267)

		self.terminal_entry.bind(f"<Return>", self.__terminal_action__)

	def __terminal_action__(self: typing.Self, event: str | None = None) -> None:
		self.terminal_entry_data = self.terminal_entry.get()

		self.terminal_textbox.configure(state=f"normal")
		match self.terminal_entry_data: 
			case "сачувај текст" | "save text" | "сохранить текст":
				program.__save_text__(event)

				self.terminal_textbox.configure(state=f"normal")
				self.terminal_textbox.insert(tkinter.END, f"{self.terminal_entry_data}\n", f"-1.0")
				self.terminal_textbox.insert(tkinter.END, f">>>", f"-1.0")
				self.terminal_textbox.configure(state=f"disabled")
				self.terminal_entry.delete(f"-1", tkinter.END)

			case "обриши текст" | "clear text" | "удалить текст":
				program.__clear_text__()

				self.terminal_textbox.configure(state=f"normal")
				self.terminal_textbox.insert(tkinter.END, f"{self.terminal_entry_data}\n", f"-1.0")
				self.terminal_textbox.insert(tkinter.END, f">>>", f"-1.0")
				self.terminal_textbox.configure(state=f"disabled")
				self.terminal_entry.delete(f"-1", tkinter.END)

			case "отвори фајл" | "open file" | "открыть файл":
				program.__open_file__(event)

				self.terminal_textbox.configure(state=f"normal")
				self.terminal_textbox.insert(tkinter.END, f"{self.terminal_entry_data}\n", f"-1.0")
				self.terminal_textbox.insert(tkinter.END, f">>>", f"-1.0")
				self.terminal_textbox.configure(state=f"disabled")
				self.terminal_entry.delete(f"-1", tkinter.END)

			case "претвори из pdf у docx" | "convert pdf to docx" | "превратить из пдф в ворд":
				program.__pdf_to_docx__()

				self.terminal_textbox.configure(state=f"normal")
				self.terminal_textbox.insert(tkinter.END, f"{self.terminal_entry_data}\n", f"-1.0")
				self.terminal_textbox.insert(tkinter.END, f">>>", f"-1.0")
				self.terminal_textbox.configure(state=f"disabled")
				self.terminal_entry.delete(f"-1", tkinter.END)

			case "претвори из docx у pdf" | "convert docx to pdf" | "превратить из ворд в пдф":
				program.__docx_to_pdf__()

				self.terminal_textbox.configure(state=f"normal")
				self.terminal_textbox.insert(tkinter.END, f"{self.terminal_entry_data}\n", f"-1.0")
				self.terminal_textbox.insert(tkinter.END, f">>>", f"-1.0")
				self.terminal_textbox.configure(state=f"disabled")
				self.terminal_entry.delete(f"-1", tkinter.END)

			case "претвори из pdf у txt" | "convert pdf to txt" | "превратить из пдф в текст":
				program.__pdf_to_txt__()

				self.terminal_textbox.configure(state=f"normal")
				self.terminal_textbox.insert(tkinter.END, f"{self.terminal_entry_data}\n", f"-1.0")
				self.terminal_textbox.insert(tkinter.END, f">>>", f"-1.0")
				self.terminal_textbox.configure(state=f"disabled")
				self.terminal_entry.delete(f"-1", tkinter.END)

			case "претвори из txt у pdf" | "convert txt to pdf" | "превратить из текст в пдф":
				program.__txt_to_pdf__()

				self.terminal_textbox.configure(state=f"normal")
				self.terminal_textbox.insert(tkinter.END, f"{self.terminal_entry_data}\n", f"-1.0")
				self.terminal_textbox.insert(tkinter.END, f">>>", f"-1.0")
				self.terminal_textbox.configure(state=f"disabled")
				self.terminal_entry.delete(f"-1", tkinter.END)

			case "претвори из docx у txt" | "convert docx to txt" | "превратить из ворд в текст":
				program.__docx_to_txt__()

				self.terminal_textbox.configure(state=f"normal")
				self.terminal_textbox.insert(tkinter.END, f"{self.terminal_entry_data}\n", f"-1.0")
				self.terminal_textbox.insert(tkinter.END, f">>>", f"-1.0")
				self.terminal_textbox.configure(state=f"disabled")
				self.terminal_entry.delete(f"-1", tkinter.END)

			case "претвори из txt у docx" | "convert txt to docx" | "превратить из ворд в текст":
				program.__txt_to_docx__()
			
				self.terminal_textbox.configure(state=f"normal")
				self.terminal_textbox.insert(tkinter.END, f"{self.terminal_entry_data}\n", f"-1.0")
				self.terminal_textbox.insert(tkinter.END, f">>>", f"-1.0")
				self.terminal_textbox.configure(state=f"disabled")
				self.terminal_entry.delete(f"-1", tkinter.END)

			case "отвори конзолу" | "open shell" | "открыть консоль":
				program.__open_shell__()
			
				self.terminal_textbox.configure(state=f"normal")
				self.terminal_textbox.insert(tkinter.END, f"{self.terminal_entry_data}\n", f"-1.0")
				self.terminal_textbox.insert(tkinter.END, f">>>", f"-1.0")
				self.terminal_textbox.configure(state=f"disabled")
				self.terminal_entry.delete(f"-1", tkinter.END)

			case "отвори powershell" | "open powershell" | "открыть powershell":
				program.__open_powershell__()
			
				self.terminal_textbox.configure(state=f"normal")
				self.terminal_textbox.insert(tkinter.END, f"{self.terminal_entry_data}\n", f"-1.0")
				self.terminal_textbox.insert(tkinter.END, f">>>", f"-1.0")
				self.terminal_textbox.configure(state=f"disabled")
				self.terminal_entry.delete(f"-1", tkinter.END)

			case "сачувај код" | "save code" | "сохранить код":
				program.__save_code__(event)
			
				self.terminal_textbox.configure(state=f"normal")
				self.terminal_textbox.insert(tkinter.END, f"{self.terminal_entry_data}\n", f"-1.0")
				self.terminal_textbox.insert(tkinter.END, f">>>", f"-1.0")
				self.terminal_textbox.configure(state=f"disabled")
				self.terminal_entry.delete(f"-1", tkinter.END)

			case "отвори код" | "open code" | "открыть код":
				program.__open_code__()
			
				self.terminal_textbox.configure(state=f"normal")
				self.terminal_textbox.insert(tkinter.END, f"{self.terminal_entry_data}\n", f"-1.0")
				self.terminal_textbox.insert(tkinter.END, f">>>", f"-1.0")
				self.terminal_textbox.configure(state=f"disabled")
				self.terminal_entry.delete(f"-1", tkinter.END)
			
			case "боја текста 1" | "text color 1" | "цвет текста 1":
				self.terminal_entry.configure(text_color="red")
				self.terminal_textbox.configure(text_color="red")

				self.terminal_textbox.configure(state=f"normal")
				self.terminal_textbox.insert(tkinter.END, f"{self.terminal_entry_data}\n", f"-1.0")
				self.terminal_textbox.insert(tkinter.END, f">>>", f"-1.0")
				self.terminal_textbox.configure(state=f"disabled")
				self.terminal_entry.delete(f"-1", tkinter.END)
			
			case "боја текста 2" | "text color 2" | "цвет текста 2":
				self.terminal_entry.configure(text_color="green")
				self.terminal_textbox.configure(text_color="green")

				self.terminal_textbox.configure(state=f"normal")
				self.terminal_textbox.insert(tkinter.END, f"{self.terminal_entry_data}\n", f"-1.0")
				self.terminal_textbox.insert(tkinter.END, f">>>", f"-1.0")
				self.terminal_textbox.configure(state=f"disabled")
				self.terminal_entry.delete(f"-1", tkinter.END)
		
			case "боја текста 3" | "text color 3" | "цвет текста 3":
				self.terminal_entry.configure(text_color="blue")
				self.terminal_textbox.configure(text_color="blue")

				self.terminal_textbox.configure(state=f"normal")
				self.terminal_textbox.insert(tkinter.END, f"{self.terminal_entry_data}\n", f"-1.0")
				self.terminal_textbox.insert(tkinter.END, f">>>", f"-1.0")
				self.terminal_textbox.configure(state=f"disabled")
				self.terminal_entry.delete(f"-1", tkinter.END)
			
			case "боја текста 4" | "text color 4" | "цвет текста 4":
				self.terminal_entry.configure(text_color="white")
				self.terminal_textbox.configure(text_color="white")

				self.terminal_textbox.configure(state=f"normal")
				self.terminal_textbox.insert(tkinter.END, f"{self.terminal_entry_data}\n", f"-1.0")
				self.terminal_textbox.insert(tkinter.END, f">>>", f"-1.0")
				self.terminal_textbox.configure(state=f"disabled")
				self.terminal_entry.delete(f"-1", tkinter.END)
		
			case "боја текста 5" | "text color 5" | "цвет текста 5":
				self.terminal_entry.configure(text_color="purple")
				self.terminal_textbox.configure(text_color="purple")

				self.terminal_textbox.configure(state=f"normal")
				self.terminal_textbox.insert(tkinter.END, f"{self.terminal_entry_data}\n", f"-1.0")
				self.terminal_textbox.insert(tkinter.END, f">>>", f"-1.0")
				self.terminal_textbox.configure(state=f"disabled")
				self.terminal_entry.delete(f"-1", tkinter.END)
			
			case "боја текста 6" | "text color 6" | "цвет текста 6":
				self.terminal_entry.configure(text_color="yellow")
				self.terminal_textbox.configure(text_color="yellow")

				self.terminal_textbox.configure(state=f"normal")
				self.terminal_textbox.insert(tkinter.END, f"{self.terminal_entry_data}\n", f"-1.0")
				self.terminal_textbox.insert(tkinter.END, f">>>", f"-1.0")
				self.terminal_textbox.configure(state=f"disabled")
				self.terminal_entry.delete(f"-1", tkinter.END)
			
			case "помоћ":
				self.terminal_textbox.configure(state=f"normal")
				self.terminal_textbox.insert(tkinter.END, f"commands: \n 1) сачувај текст / код \n 2) отвори фајл / код / конзолу / powershell \n 3) конвертирај из ... у ... \n 4) изађи из програма / терминала \n 5) боја текста(1-6) \n", "-1.0")
				self.terminal_textbox.insert(tkinter.END, f">>>", f"-1.0")
				self.terminal_textbox.configure(state=f"disabled")
				self.terminal_entry.delete(f"-1", tkinter.END)

			case "help":
				self.terminal_textbox.configure(state=f"normal")
				self.terminal_textbox.insert(tkinter.END, f"commands: \n 1) save text / code \n 2) open file / code / shell / powershell \n 3) convert ... to ... \n 4) exit program / terminal \n 5) text color(1-6) \n", "-1.0")
				self.terminal_textbox.insert(tkinter.END, f">>>", f"-1.0")
				self.terminal_textbox.configure(state=f"disabled")
				self.terminal_entry.delete("-1", tkinter.END)
			
			case "помощь":
				self.terminal_textbox.configure(state=f"normal")
				self.terminal_textbox.insert(tkinter.END, f"commands: \n 1) сохранить текст / код \n 2) открыть файл / код / консоль / powershell \n 3) превратить из ... в ... \n 4) выйти из программы / терминала \n 5) цвет текста(1-6) \n", "-1.0")
				self.terminal_textbox.insert(tkinter.END, f">>>", f"-1.0")
				self.terminal_textbox.configure(state=f"disabled")
				self.terminal_entry.delete(f"-1", tkinter.END)

			case "изађи из терминала" | "exit terminal" | "выйти из терминала":
				self.destroy()

			case "изађи из програма" | "exit program" | "выйти из программы":
				program.__exit__()
		
			case _:
				self.terminal_textbox.configure(state=f"normal")
				self.terminal_textbox.insert(tkinter.END, f"{self.terminal_entry_data} - команда не постоји / command doesn't exist / команда не существует \n", "-1.0")
				self.terminal_textbox.insert(tkinter.END, f">>>", f"-1.0")
				self.terminal_textbox.configure(state=f"disabled")
				self.terminal_entry.delete(f"-1", tkinter.END)

program: My_Diary.Program = My_Diary.Program()