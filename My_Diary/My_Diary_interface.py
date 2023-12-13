import abc

class My_Diary_interface(abc.ABC):
    
    @abc.abstractmethod
    def __undo__() -> None:
        pass
    
    @abc.abstractmethod
    def __redo__() -> None:
        pass
    
    @abc.abstractmethod
    def __save_text__() -> None:
        pass
    
    @abc.abstractmethod
    def __edit_text__() -> None:
        pass
    
    @abc.abstractmethod
    def __edit_text_font__() -> None:
        pass
    
    @abc.abstractmethod
    def __open_file__() -> None:
        pass
    
    @abc.abstractmethod
    def __convert__() -> None:
        pass
    
    @abc.abstractmethod
    def __pdf_to_docx__() -> None:
        pass
    
    @abc.abstractmethod
    def __docx_to_pdf__() -> None:
        pass
    
    @abc.abstractmethod
    def __pdf_to_txt__() -> None:
        pass
    
    @abc.abstractmethod
    def __txt_to_pdf__() -> None:
        pass
    
    @abc.abstractmethod
    def __txt_to_docx__() -> None:
        pass

    @abc.abstractmethod
    def __docx_to_txt__() -> None:
        pass
    
    @abc.abstractmethod
    def __code_editor__() -> None:
        pass
    
    @abc.abstractmethod
    def __open_powershell__() -> None:
        pass

    @abc.abstractmethod
    def __open_shell__() -> None:
        pass
    
    @abc.abstractmethod
    def __save_code__() -> None:
        pass
    
    @abc.abstractmethod
    def __open_code__() -> None:
        pass

    @abc.abstractmethod
    def __settings__() -> None:
        pass
    
    @abc.abstractmethod
    def __language_settings__() -> None:
        pass
    
    @abc.abstractmethod
    def __autosave_settings__() -> None:
        pass
    
    @abc.abstractmethod
    def __text_autosave__() -> None:
        pass
    
    @abc.abstractmethod
    def __theme_settings__() -> None:
        pass
    
    @abc.abstractmethod
    def __change_text_color__() -> None:
        pass
    
    @abc.abstractmethod
    def __change_text_field_color__() -> None:
        pass
    
    @abc.abstractmethod
    def __change_text_field_text_height__() -> None:
        pass
    
    @abc.abstractmethod
    def __change_button_color__() -> None:
        pass