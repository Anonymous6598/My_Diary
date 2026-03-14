import abc, typing

class My_Calculus_settings_window_interface(abc.ABC):
     
     @abc.abstractmethod
     def __change_text_color__(self: typing.Self, pickle_serializer: pickle) -> None:
         pass
     
     @abc.abstractmethod
     def __change_expression_entry_color__(self: typing.Self, pickle_serializer: pickle) -> None:
         pass
     
     @abc.abstractmethod
     def __change_expression_entry_text_color__(self: typing.Self, pickle_serializer: pickle) -> None:
         pass
     
     @abc.abstractmethod
     def __change_button_color__(self: typing.Self, pickle_serializer: pickle) -> None:
         pass
