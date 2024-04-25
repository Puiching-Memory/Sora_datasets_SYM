from llama_cpp import Llama
model = Llama("/data/hf/Llama3-8B-Chinese-Chat.q4_k_m.GGUF", verbose=False, n_gpu_layers=-1)
messages = [
    {"role": "system", "content": "你是一个疯狂的科学家大卫，你总是为了毁灭宇宙而努力。"},
    {"role": "user", "content": "你是谁？"},
]

output = model.create_chat_completion(messages, stop=["<|eot_id|>", "<|end_of_text|>"], max_tokens=300)["choices"][0]["message"]["content"]

print(output)