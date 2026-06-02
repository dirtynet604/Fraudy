from llm.qwen_client import QwenClient
from llm.llama_client import LlamaClient

class LLMEnsemble:

    def __init__(self):

        self.qwen = QwenClient()
        self.llama = LlamaClient()

    def analyze(self, prompt):

        qwen_result = self.qwen.analyze(prompt)

        llama_result = self.llama.analyze(prompt)

        return {
            "qwen": qwen_result,
            "llama": llama_result
        }