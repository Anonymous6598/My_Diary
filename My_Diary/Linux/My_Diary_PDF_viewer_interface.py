import abc, typing

class My_Diary_PDF_reader_interface(abc.ABC):
    def __show_pdf__(self: typing.Self, pdf_file: str) -> None:
        pass
