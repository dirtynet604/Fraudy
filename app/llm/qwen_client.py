from transformers import AutoTokenizer
from transformers import AutoModelForCausalLM
import torch


class QwenClient:

    def __init__(self):

        model_name = "Qwen/Qwen2.5-7B-Instruct"

        self.tokenizer = AutoTokenizer.from_pretrained(
            model_name
        )

        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float16,
            device_map="auto"
        )

    def analyze(self, prompt):

        messages = [
            {
                "role": "user",
                "content": prompt
            }
        ]

        text = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )

        inputs = self.tokenizer(
            text,
            return_tensors="pt"
        ).to(self.model.device)

        outputs = self.model.generate(
            **inputs,
            max_new_tokens=1024,
            temperature=0.1
        )

        return self.tokenizer.decode(
            outputs[0],
            skip_special_tokens=True
        )