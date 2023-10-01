import customtkinter, tkinter
from My_Diary_6 import Program

class Terminal(customtkinter.CTkToplevel):

	HEIGHT: int = 375
	WIDTH: int = 650
	WINDOW: str = "-toolwindow"
	TITLE: str = "My Diary command prompt"

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

		self.terminal_entry: customtkinter.CTkEntry = customtkinter.CTkEntry(master=self.terminal_frame, height=30, width=517, border_width=0, fg_color="transparent", placeholder_text="type here", placeholder_text_color="green", text_color="green", font=("Ubuntu", 22))
		self.terminal_entry.place(x=1.5, y=267)

		self.terminal_entry.bind("<Return>", self.__terminal_action__)

	def __terminal_action__(self, event: str) -> None:
		self.terminal_entry_data = self.terminal_entry.get()

		self.terminal_textbox.configure(state="normal")
		if self.terminal_entry_data == "clear text":
			program.__clear_text__()

			self.terminal_textbox.configure(state="normal")
			self.terminal_textbox.insert(tkinter.END, self.terminal_entry_data + "\n", "-1.0")
			self.terminal_textbox.insert(tkinter.END, ">>>", "-1.0")
			self.terminal_textbox.configure(state="disabled")
			self.terminal_entry.delete("-1", tkinter.END)

		elif self.terminal_entry_data == "open taskbar":
			program.__open_taskbar__()

			self.terminal_textbox.configure(state="normal")
			self.terminal_textbox.insert(tkinter.END, self.terminal_entry_data + "\n", "-1.0")
			self.terminal_textbox.insert(tkinter.END, ">>>", "-1.0")
			self.terminal_textbox.configure(state="disabled")
			self.terminal_entry.delete("-1", tkinter.END)

		elif self.terminal_entry_data == "close taskbar":
			program.__close_taskbar__()

			self.terminal_textbox.configure(state="normal")
			self.terminal_textbox.insert(tkinter.END, self.terminal_entry_data + "\n", "-1.0")
			self.terminal_textbox.insert(tkinter.END, ">>>", "-1.0")
			self.terminal_textbox.configure(state="disabled")
			self.terminal_entry.delete("-1", tkinter.END)

		elif self.terminal_entry_data == "quit operation":
			program.__quit_operation__()

			self.terminal_textbox.configure(state="normal")
			self.terminal_textbox.insert(tkinter.END, self.terminal_entry_data + "\n", "-1.0")
			self.terminal_textbox.insert(tkinter.END, ">>>", "-1.0")
			self.terminal_textbox.configure(state="disabled")
			self.terminal_entry.delete("-1", tkinter.END)
		
		elif self.terminal_entry_data == "save text as ...":
			program.__save_text_as__(event)

			self.terminal_textbox.configure(state="normal")
			self.terminal_textbox.insert(tkinter.END, self.terminal_entry_data + "\n", "-1.0")
			self.terminal_textbox.insert(tkinter.END, ">>>", "-1.0")
			self.terminal_textbox.configure(state="disabled")
			self.terminal_entry.delete("-1", tkinter.END)

		elif self.terminal_entry_data == "save text as docx":
			program.__save_text_as_docx__()

			self.terminal_textbox.configure(state="normal")
			self.terminal_textbox.insert(tkinter.END, self.terminal_entry_data + "\n", "-1.0")
			self.terminal_textbox.insert(tkinter.END, ">>>", "-1.0")
			self.terminal_textbox.configure(state="disabled")
			self.terminal_entry.delete("-1", tkinter.END)

		elif self.terminal_entry_data == "clear text":
			program.__clear_text__()

			self.terminal_textbox.configure(state="normal")
			self.terminal_textbox.insert(tkinter.END, self.terminal_entry_data + "\n", "-1.0")
			self.terminal_textbox.insert(tkinter.END, ">>>", "-1.0")
			self.terminal_textbox.configure(state="disabled")
			self.terminal_entry.delete("-1", tkinter.END)

		elif self.terminal_entry_data == "open ... file":
			program.__open_file__(event)

			self.terminal_textbox.configure(state="normal")
			self.terminal_textbox.insert(tkinter.END, self.terminal_entry_data + "\n", "-1.0")
			self.terminal_textbox.insert(tkinter.END, ">>>", "-1.0")
			self.terminal_textbox.configure(state="disabled")
			self.terminal_entry.delete("-1", tkinter.END)

		elif self.terminal_entry_data == "open docx file":
			program.__open_file_docx__()

			self.terminal_textbox.configure(state="normal")
			self.terminal_textbox.insert(tkinter.END, self.terminal_entry_data + "\n", "-1.0")
			self.terminal_textbox.insert(tkinter.END, ">>>", "-1.0")
			self.terminal_textbox.configure(state="disabled")
			self.terminal_entry.delete("-1", tkinter.END)

		elif self.terminal_entry_data == "convert pdf to docx":
			program.__pdf_to_docx__()

			self.terminal_textbox.configure(state="normal")
			self.terminal_textbox.insert(tkinter.END, self.terminal_entry_data + "\n", "-1.0")
			self.terminal_textbox.insert(tkinter.END, ">>>", "-1.0")
			self.terminal_textbox.configure(state="disabled")
			self.terminal_entry.delete("-1", tkinter.END)

		elif self.terminal_entry_data == "convert docx to pdf":
			program.__docx_to_pdf__()

			self.terminal_textbox.configure(state="normal")
			self.terminal_textbox.insert(tkinter.END, self.terminal_entry_data + "\n", "-1.0")
			self.terminal_textbox.insert(tkinter.END, ">>>", "-1.0")
			self.terminal_textbox.configure(state="disabled")
			self.terminal_entry.delete("-1", tkinter.END)

		elif self.terminal_entry_data == "convert pdf to txt":
			program.__pdf_to_txt__()

			self.terminal_textbox.configure(state="normal")
			self.terminal_textbox.insert(tkinter.END, self.terminal_entry_data + "\n", "-1.0")
			self.terminal_textbox.insert(tkinter.END, ">>>", "-1.0")
			self.terminal_textbox.configure(state="disabled")
			self.terminal_entry.delete("-1", tkinter.END)

		elif self.terminal_entry_data == "convert txt to pdf":
			program.__txt_to_pdf__()

			self.terminal_textbox.configure(state="normal")
			self.terminal_textbox.insert(tkinter.END, self.terminal_entry_data + "\n", "-1.0")
			self.terminal_textbox.insert(tkinter.END, ">>>", "-1.0")
			self.terminal_textbox.configure(state="disabled")
			self.terminal_entry.delete("-1", tkinter.END)

		elif self.terminal_entry_data == "convert docx to txt":
			program.__docx_to_txt__()

			self.terminal_textbox.configure(state="normal")
			self.terminal_textbox.insert(tkinter.END, self.terminal_entry_data + "\n", "-1.0")
			self.terminal_textbox.insert(tkinter.END, ">>>", "-1.0")
			self.terminal_textbox.configure(state="disabled")
			self.terminal_entry.delete("-1", tkinter.END)

		elif self.terminal_entry_data == "convert txt to docx":
			program.__txt_to_docx__()
			
			self.terminal_textbox.configure(state="normal")
			self.terminal_textbox.insert(tkinter.END, self.terminal_entry_data + "\n", "-1.0")
			self.terminal_textbox.insert(tkinter.END, ">>>", "-1.0")
			self.terminal_textbox.configure(state="disabled")
			self.terminal_entry.delete("-1", tkinter.END)

		elif self.terminal_entry_data == "open shell":
			program.__open_shell__()
			
			self.terminal_textbox.configure(state="normal")
			self.terminal_textbox.insert(tkinter.END, self.terminal_entry_data + "\n", "-1.0")
			self.terminal_textbox.insert(tkinter.END, ">>>", "-1.0")
			self.terminal_textbox.configure(state="disabled")
			self.terminal_entry.delete("-1", tkinter.END)

		elif self.terminal_entry_data == "open powershell":
			program.__open_powershell__()
			
			self.terminal_textbox.configure(state="normal")
			self.terminal_textbox.insert(tkinter.END, self.terminal_entry_data + "\n", "-1.0")
			self.terminal_textbox.insert(tkinter.END, ">>>", "-1.0")
			self.terminal_textbox.configure(state="disabled")
			self.terminal_entry.delete("-1", tkinter.END)

		elif self.terminal_entry_data == "save code as":
			program.__save_code_as__(event)
			
			self.terminal_textbox.configure(state="normal")
			self.terminal_textbox.insert(tkinter.END, self.terminal_entry_data + "\n", "-1.0")
			self.terminal_textbox.insert(tkinter.END, ">>>", "-1.0")
			self.terminal_textbox.configure(state="disabled")
			self.terminal_entry.delete("-1", tkinter.END)

		elif self.terminal_entry_data == "open code":
			program.__open_code__()
			
			self.terminal_textbox.configure(state="normal")
			self.terminal_textbox.insert(tkinter.END, self.terminal_entry_data + "\n", "-1.0")
			self.terminal_textbox.insert(tkinter.END, ">>>", "-1.0")
			self.terminal_textbox.configure(state="disabled")
			self.terminal_entry.delete("-1", tkinter.END)
			
		elif self.terminal_entry_data == "text color 1":
			self.terminal_entry.configure(text_color="red")
			self.terminal_textbox.configure(text_color="red")

			self.terminal_textbox.configure(state="normal")
			self.terminal_textbox.insert(tkinter.END, self.terminal_entry_data + "\n", "-1.0")
			self.terminal_textbox.insert(tkinter.END, ">>>", "-1.0")
			self.terminal_textbox.configure(state="disabled")
			self.terminal_entry.delete("-1", tkinter.END)
			
		elif self.terminal_entry_data == "text color 2":
			self.terminal_entry.configure(text_color="green")
			self.terminal_textbox.configure(text_color="green")

			self.terminal_textbox.configure(state="normal")
			self.terminal_textbox.insert(tkinter.END, self.terminal_entry_data + "\n", "-1.0")
			self.terminal_textbox.insert(tkinter.END, ">>>", "-1.0")
			self.terminal_textbox.configure(state="disabled")
			self.terminal_entry.delete("-1", tkinter.END)
		
		elif self.terminal_entry_data == "text color 3":
			self.terminal_entry.configure(text_color="blue")
			self.terminal_textbox.configure(text_color="blue")

			self.terminal_textbox.configure(state="normal")
			self.terminal_textbox.insert(tkinter.END, self.terminal_entry_data + "\n", "-1.0")
			self.terminal_textbox.insert(tkinter.END, ">>>", "-1.0")
			self.terminal_textbox.configure(state="disabled")
			self.terminal_entry.delete("-1", tkinter.END)
			
		elif self.terminal_entry_data == "text color 4":
			self.terminal_entry.configure(text_color="white")
			self.terminal_textbox.configure(text_color="white")

			self.terminal_textbox.configure(state="normal")
			self.terminal_textbox.insert(tkinter.END, self.terminal_entry_data + "\n", "-1.0")
			self.terminal_textbox.insert(tkinter.END, ">>>", "-1.0")
			self.terminal_textbox.configure(state="disabled")
			self.terminal_entry.delete("-1", tkinter.END)
		
		elif self.terminal_entry_data == "text color 5":
			self.terminal_entry.configure(text_color="purple")
			self.terminal_textbox.configure(text_color="purple")

			self.terminal_textbox.configure(state="normal")
			self.terminal_textbox.insert(tkinter.END, self.terminal_entry_data + "\n", "-1.0")
			self.terminal_textbox.insert(tkinter.END, ">>>", "-1.0")
			self.terminal_textbox.configure(state="disabled")
			self.terminal_entry.delete("-1", tkinter.END)
			
		elif self.terminal_entry_data == "text color 6":
			self.terminal_entry.configure(text_color="yellow")
			self.terminal_textbox.configure(text_color="yellow")

			self.terminal_textbox.configure(state="normal")
			self.terminal_textbox.insert(tkinter.END, self.terminal_entry_data + "\n", "-1.0")
			self.terminal_textbox.insert(tkinter.END, ">>>", "-1.0")
			self.terminal_textbox.configure(state="disabled")
			self.terminal_entry.delete("-1", tkinter.END)

		elif self.terminal_entry_data == "help":
			self.terminal_textbox.configure(state="normal")
			self.terminal_textbox.insert(tkinter.END, f"commands: \n 1) save text / code as ... \n 2) open ... file / code / shell / powershell \n 3) clear text \n 4) convert ... to ... \n 5) exit program / terminal \n 6) open/close taskbar \n 7) quit operation \n 8) text color(1-6) \n", "-1.0")
			self.terminal_textbox.insert(tkinter.END, ">>>", "-1.0")
			self.terminal_textbox.configure(state="disabled")
			self.terminal_entry.delete("-1", tkinter.END)

		elif self.terminal_entry_data == "exit terminal":
			self.destroy()

		elif self.terminal_entry_data == "exit program":
			program.__exit__()
		
		else:
			self.terminal_textbox.configure(state="normal")
			self.terminal_textbox.insert(tkinter.END, self.terminal_entry_data + " - command doesn't exist" + "\n", "-1.0")
			self.terminal_textbox.insert(tkinter.END, ">>>", "-1.0")
			self.terminal_textbox.configure(state="disabled")
			self.terminal_entry.delete("-1", tkinter.END)

program: Program = Program()