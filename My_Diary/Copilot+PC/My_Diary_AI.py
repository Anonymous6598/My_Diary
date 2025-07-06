import typing, My_Diary_AI_interface, openvino_genai

class My_Diary_LM(My_Diary_AI_interface.My_Diary_AI_interface):
    
    LANGUAGE_MODEL: typing.Final[str] = f"Llama-3.2-1B-Instruct" 
    DEVICE: typing.Final[str] = f"NPU"
    
    def __init__(self: typing.Self) -> None:
        self.language_model = self.LANGUAGE_MODEL
        self.device = self.DEVICE 

    def __initialize_model__(self: typing.Self) -> openvino_genai.LLMPipeline:
        pipeline_config: dict(str, str) = {f"GENERATE_HINT": f"BEST_PERF"}
        pipe: openvino_genai.LLMPipeline = openvino_genai.LLMPipeline(self.language_model, self.device, pipeline_config)
        return pipe

    @typing.override
    def __response__(self: typing.Self, pipe: openvino_genai.LLMPipeline = None, query: str = None) -> str:
        self.config: openvino_genai.GenerationConfig = openvino_genai.GenerationConfig()
        self.config.max_new_tokens = 1024
        self.config.temperature = 0.3
        self.config.top_p = 0.5
        self.config.top_k = 1
        self.config.repetition_penalty = 1.0
        self.config.num_return_sequences = 1
        self.config.num_beams = 1
        self.config.num_return_sequences = 1
        self.config.do_sample = False
        self.config.eos_token_id = -1

        self.result: str = pipe.generate(query, self.config)
        return self.result