import abc, typing

class My_Calculus_AI_window_interface(abc.ABC):
    
    @abc.abstractmethod
    def __response_from_ai__(self: typing.Self, configure: str | None = None) -> None:
        pass

    @abc.abstractmethod
    def __audio_input__(self: typing.Self) -> None:
        pass
