import abc, typing

class My_Diary_AI_window_interface(abc.ABC):

    def __response__(self: typing.Self, configure: str | None = None) -> None:
        pass

    def __audio_input__(self: typing.Self) -> None:
        pass