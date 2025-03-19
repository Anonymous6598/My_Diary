import g4f, g4f.Provider, typing, My_Diary_AI_interface

class My_Diary_LM(My_Diary_AI_interface.My_Diary_AI_interface):
    
    LANGUAGE_MODEL: typing.Final[str] = f"gpt-4o-mini" 
    PROVIDER: typing.Final[g4f.Provider] = g4f.Provider.DDG
    
    def __init__(self: typing.Self) -> None:
       self.language_model: str = self.LANGUAGE_MODEL
       self.provider: g4f.Provider = self.PROVIDER 

    @typing.override
    def __response__(self: typing.Self, prompt: str) -> str:
        self.user_query: list[dict[str, str]] = [{f"role": f"user", f"content": prompt}]
        
        self.response: str = g4f.ChatCompletion.create(model=self.language_model, provider=self.provider, messages=self.user_query)

        return self.response