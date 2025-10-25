import abc, typing

class My_Diary_AI_interface(abc.ABC):

    @abc.abstractmethod
    def __response__(self: typing.Self, prompt: str) -> str:
        pass
