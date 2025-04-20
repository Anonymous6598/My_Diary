import customtkinter, CTkPDFViewer, typing, My_Diary_PDF_viewer_interface

class My_Diary_PDF_viewer(customtkinter.CTkToplevel, My_Diary_PDF_viewer_interface.My_Diary_PDF_reader_interface):
    
    TITLE: typing.Final[str] = f"My Diary PDF reader"

    def __init__(self: typing.Self, *args: typing.Any, **kwargs: typing.Any) -> None:
        customtkinter.CTkToplevel.__init__(self, *args, **kwargs)
        
        self.title(self.TITLE)

    @typing.override    
    def __show_pdf__(self: typing.Self, pdf_file: str) -> None:
        self.pdf_frame: CTkPDFViewer.CTkPDFViewerNavigate = CTkPDFViewer.CTkPDFViewerNavigate(self, file=pdf_file)
        self.pdf_frame.pack(fill="both", expand=True)
        