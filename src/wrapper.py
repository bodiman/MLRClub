from llama_cpp import Llama


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
        self.model = Llama(
            model_path=self.path,
            n_gpu_layers=-1, # Uncomment to use GPU acceleration
            embedding=True,
            # seed=1337, # Uncomment to set a specific seed
            # n_ctx=2048, # Uncomment to increase the context window
        )

    def initialize(self, prompt: str, args = {}) -> None:
        tokens = self.llm.tokenize(str.encode(f"Instruct: {prompt}\nOutput:"))

        self.gen = self.model.generate(
            tokens=tokens,
            **args
        )


    def generate(self):
        next_token = next(self.gen)

        yield "test"
