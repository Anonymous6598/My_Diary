import transformers, torch, typing, My_Diary_AI_interface

class My_Diary_LM(My_Diary_AI_interface.My_Diary_AI_interface):
    
    LANGUAGE_MODEL: typing.Final[str] = f"arcee-ai/Llama-3.1-SuperNova-Lite" 
    
    def __init__(self: typing.Self) -> None:
        self.tokenizer_for_lm: transformers.PreTrainedTokenizer = transformers.AutoTokenizer.from_pretrained(self.LANGUAGE_MODEL)
        self.pipeline_for_lm: transformers.Pipeline = transformers.pipeline(f"text-generation", model=self.LANGUAGE_MODEL, torch_dtype=torch.float16, device_map=f"auto", max_length=100, pad_token_id=self.tokenizer_for_lm.eos_token_id, eos_token_id=self.tokenizer_for_lm.eos_token_id)

    @typing.override
    async def __response__(self: typing.Self, prompt: str) -> str:
        self.user_query: list[dict[str, str]] = [{"role": "user", "content": prompt}]

        return self.pipeline(self.user_query)[0].get("generated_text")[1].get("content")