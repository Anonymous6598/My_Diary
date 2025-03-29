import customtkinter, tkinter, typing, My_Diary_AI, speech_recognition, My_Diary_AI_window_interface

class AI_Window(customtkinter.CTkToplevel, My_Diary_AI_window_interface.My_Diary_AI_window_interface):

	TITLE: typing.Final[str] = f"My Diary AI assistant"
	HEIGHT: typing.Final[int] = 375
	WIDTH: typing.Final[int] = 655
	COLOR_THEME: typing.Final[str] = f"dark-blue"
	WIDGET_SCALING: typing.Final[float] = 1.251

	def __init__(self: typing.Self, *args, **kwargs) -> None:
		customtkinter.CTkToplevel.__init__(self, *args, **kwargs)

		customtkinter.set_widget_scaling(self.WIDGET_SCALING)
		customtkinter.set_default_color_theme(self.COLOR_THEME)
		customtkinter.deactivate_automatic_dpi_awareness()

		self.title(self.TITLE)
		self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
		self.resizable(False, False)

		self.ai_window_textbox: customtkinter.CTkTextbox = customtkinter.CTkTextbox(master=self, height=265, width=524, corner_radius=0, fg_color=f"transparent", text_color=(f"black", f"white"))
		self.ai_window_textbox.place(x=0, y=0)

		self.ai_window_textbox.configure(state=f"disabled")

		self.ai_window_entry: customtkinter.CTkEntry = customtkinter.CTkEntry(master=self, height=30, width=465, border_width=0, fg_color=f"transparent", placeholder_text=f"...")
		self.ai_window_entry.place(x=0, y=269)

		self.ai_window_microphone_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, height=30, width=30, border_width=0, fg_color=f"transparent", text=f"🎤", command=self.__audio_input__)
		self.ai_window_microphone_button.place(x=465, y=269)

		self.ai_window_send_request_button: customtkinter.CTkButton = customtkinter.CTkButton(master=self, height=30, width=30, border_width=0, fg_color=f"transparent", text=f"->", command=self.__response__)
		self.ai_window_send_request_button.place(x=495, y=269)

		self.ai_window_entry.bind(f"<Return>", self.__response__)

	@typing.override
	def __response__(self: typing.Self, configure: str | None = None) -> None:
		self.ai_window_entry_data: str = self.ai_window_entry.get()

		self.ai_window_textbox.configure(state=f"normal")
		self.query: str = My_Diary_AI.My_Diary_LM().__response__(self.ai_window_entry_data)

		self.ai_window_textbox.insert(tkinter.END, f"USER:\n{self.ai_window_entry_data}\nGPT-4o:\n{self.query}\n", f"-1.0")
		self.ai_window_textbox.configure(state=f"disabled")
		self.ai_window_entry.delete(f"-1", tkinter.END)

	def __audio_input__(self: typing.Self) -> None:
		try:
			self.recognizer: speech_recognition.Recognizer = speech_recognition.Recognizer()
			with speech_recognition.Microphone() as self.source:
				self.audio_data: speech_recognition.AudioData = self.recognizer.record(self.source, duration=5)
				self.text: str = self.recognizer.recognize_google(self.audio_data)

			self.ai_window_entry.insert(f"0", self.text)
		
		except speech_recognition.UnknownValueError: pass
