import abc, typing

class My_Diary_interface(abc.ABC):
    
    @abc.abstractmethod
    def __undo__(self: typing.Self) -> None:
        pass
    
    @abc.abstractmethod
    def __redo__(self: typing.Self) -> None:
        pass
    
    @abc.abstractmethod
    def __save_text__(self: typing.Self) -> None:
        pass
    
    @abc.abstractmethod
    def __edit_text__(self: typing.Self) -> None:
        pass
    
    @abc.abstractmethod
    def __edit_text_font__(self: typing.Self) -> None:
        pass
    
    @abc.abstractmethod
    def __open_file__(self: typing.Self) -> None:
        pass
    
    @abc.abstractmethod
    def __text_autosave__(self: typing.Self, event: str | None = None) -> None:
        pass

    @abc.abstractmethod
    def __clear_text__(self: typing.Self) -> None:
        pass

    @abc.abstractmethod
    def __enter_text_autosave__(self: typing.Self, event: str | None = None) -> None:
        pass

    @abc.abstractmethod
    def __word_count__(self: typing.Self, event: str | None = None) -> None:
        pass

    @abc.abstractmethod
    def __word_count_show__(self: typing.Self) -> None:
        pass

    @abc.abstractmethod
    def __drop_file_into_textbox__(self: typing.Self, event: str | None = None) -> None:
        pass

    @abc.abstractmethod
    def __html_script__(self: typing.Self, event: str | None = None) -> None:
        pass

    @abc.abstractmethod
    def __open_right_click_menu__(self: typing.Self, event: str | None = None) -> None:
        pass

    @abc.abstractmethod
    def __cut__(self: typing.Self) -> None:
        pass

    @abc.abstractmethod
    def __copy__(self: typing.Self) -> None:
        pass

    @abc.abstractmethod
    def __paste__(self: typing.Self) -> None:
        pass

    @abc.abstractmethod
    def __text_summary__(self: typing.Self) -> None:
        pass

    @abc.abstractmethod
    def __create_text__(self: typing.Self) -> None:
        pass

    @abc.abstractmethod
    def __exit__(self: typing.Self) -> None:
        pass

    @abc.abstractmethod
    def __fullscreen__(self: typing.Self) -> None:
        pass
