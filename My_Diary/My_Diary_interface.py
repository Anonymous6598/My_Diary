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