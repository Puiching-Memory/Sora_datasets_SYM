from share4v.model.builder import load_pretrained_model
from share4v.mm_utils import get_model_name_from_path
from share4v.eval.run_share4v import eval_model

model_path = "pth/ShareGPT4V-7B"

"""
tokenizer, model, image_processor, context_len = load_pretrained_model(
    model_path=model_path,
    model_base=None,
    model_name=get_model_name_from_path(model_path)
)
"""
prompt = "Describe the whole picture"
image_file = r"./fe9f31c57fe7c5bd7d3cc27434cd4bba.jpg"

args = type('Args', (), {
    "model_path": model_path,
    "model_base": None,
    "model_name": get_model_name_from_path(model_path),
    "query": prompt,
    "conv_mode": None,
    "image_file": image_file,
    "sep": ",",
    "temperature": 0,
    "top_p": None,
    "num_beams": 1,
    "max_new_tokens": 512,
    "offload_folder":"./cache"
})()

eval_model(args)