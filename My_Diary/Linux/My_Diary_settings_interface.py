import abc, typing, pickle

class My_Diary_setting_window_interface(abc.ABC):

    @abc.abstractmethod
    def __language_settings__(self: typing.Self, pickle_serializer: pickle) -> None:
        pass

    @abc.abstractmethod
    def __theme_settings__(self: typing.Self, pickle_serializer: pickle) -> None:
        pass
