import g4f, locale

class My_Diary_AI:
    def response(prompt: str) -> str:
        try:
            response = g4f.ChatCompletion.create(model=f"", provider=g4f.Provider.DeepInfra, messages=[{f"role": f"user", f"content": prompt}])
        
            return response
        
        except Exception:
            if locale.getdefaultlocale()[0] == "sr_RS":
                return f"покушајте поново касније"
            
            elif locale.getdefaultlocale()[0] == "ru_RU":
                return f"попробуете попозже"
            
            else:
                return f"try again later"