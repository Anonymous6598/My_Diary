import abc

class My_Diary_command_prompt_interface(abc.ABC):
    
    @abc.abstractmethod
    def __terminal_action__() -> None:
        pass