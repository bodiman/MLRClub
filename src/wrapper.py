from llama_cpp import Llama

from model import LinearModel


"""
Members
-------

Methods
-------

forward: context: str ->

"""
class Wrapper:
    def init(self, path) -> None:
        self.path = path
        self.llm = Llama(
            model_path=self.path,
            n_gpu_layers=-1, # Uncomment to use GPU acceleration
            embedding=True,
            # seed=1337, # Uncomment to set a specific seed
            # n_ctx=2048, # Uncomment to increase the context window
        )

        self.head = LinearModel(
            input_size=4096,
            output_size=4096
        )

        self.max_steps = 500

    def initialize(self, prompt: str, args = {}) -> None:
        tokens = self.llm.tokenize(str.encode(f"Instruct: {prompt}\nOutput:"))

        self.gen = self.model.generate(
            tokens=tokens,
            **args
        )


    def generate_label(self):
        output_tokens = []
        for i, token in enumerate(self.gen):
            output_tokens.append(token)
            if i >= self.max_steps:
                break
            
            output_tokens.append(token)
            
        return output_tokens
