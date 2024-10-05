import customtkinter, CTkPDFViewer, typing, My_Diary_PDF_viewer_interface

class My_Diary_PDF_viewer(customtkinter.CTkToplevel, My_Diary_PDF_viewer_interface.My_Diary_PDF_reader_interface):
    
    TITLE: typing.Final[str] = f"My Diary PDF reader (beta)"

    def __init__(self: typing.Self, *args: typing.Any, **kwargs: typing.Any) -> None:
        customtkinter.CTkToplevel.__init__(self, *args, **kwargs)
        
        self.title(f"My Diary PDF reader (beta)")

    @typing.override    
    def __show_pdf__(self: typing.Self, pdf_file: str) -> None:
        self.pdf_frame: CTkPDFViewer.CTkPDFViewer = CTkPDFViewer.CTkPDFViewer(self, file=pdf_file)
        self.pdf_frame.pack(fill="both", expand=True)
        