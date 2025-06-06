import typing, My_Diary_AI_interface, transformers, torch, intel_npu_acceleration_library

class My_Diary_LM(My_Diary_AI_interface.My_Diary_AI_interface):
    
    LANGUAGE_MODEL: typing.Final[str] = f"microsoft/Phi-3-mini-4k-instruct" 
    
    def __init__(self: typing.Self) -> None:
       self.language_model: str = self.LANGUAGE_MODEL 

    def __initialize_model__(self: typing.Self) -> transformers.Pipeline:
        self.model_id: str = self.language_model
        self.model: transformers.AutoModelForCausalLM = transformers.AutoModelForCausalLM.from_pretrained(self.model_id, torch_dtype=torch.float16, use_cache=True).eval()
        self.tokenizer: transformers.PreTrainedTokenizer = transformers.AutoTokenizer.from_pretrained(self.model_id)
        self.model = intel_npu_acceleration_library.compile(self.model, dtype=torch.float16)
        self.pipe: transformers.Pipeline = transformers.pipeline(f"text-generation", model=self.model, tokenizer=self.tokenizer)
        return self.pipe

    @typing.override
    def __response__(self: typing.Self, pipe: transformers.Pipeline = None, query: str = None) -> str:
        generation_args: dict[f"max_new_tokens": int, f"return_full_text": bool, f"temperature": float, f"do_sample": bool] = {f"max_new_tokens": 1024, f"return_full_text": False, f"temperature": 0.3, f"do_sample": False}
        self.query: str = query
        self.output: str = pipe(self.query, **generation_args)
        return self.output[0][f"generated_text"]
