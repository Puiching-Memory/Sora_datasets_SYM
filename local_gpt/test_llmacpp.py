#https://github.com/abetlen/llama-cpp-python
import time
from llama_cpp import Llama
model = Llama(r"D:\GitHub\Llama3-8B-Chinese-Chat.q4_k_m.GGUF", verbose=False, n_gpu_layers=-1,n_threads=16,n_threads_batch=16)
messages = [
    {"role": "system", "content": "你是一个疯狂的科学家大卫，你总是为了毁灭宇宙而努力。"},
    {"role": "user", "content": "你是谁？"},
]

output = model.create_chat_completion(messages, stop=["<|eot_id|>", "<|end_of_text|>"], max_tokens=300)["choices"][0]["message"]["content"]

print(output)