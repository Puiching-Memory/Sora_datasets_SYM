import torch
import clip
from PIL import Image

device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

image = preprocess(Image.open(r"C:\Users\YiYu\Pictures\Saved Pictures\微信图片_20240606202924.jpg")).unsqueeze(0).to(device)
text = clip.tokenize(["The image captures a breathtaking view of a mountainous landscape. The mountains, majestic and towering, are blanketed in a lush layer of green vegetation. The sky above is a clear blue, dotted with fluffy white clouds that add a sense of depth and scale to the scene. The perspective of the image is from a high vantage point, looking down upon the mountains, giving a sense of their grandeur and vastness. The colors in the image are vibrant, with the green of the vegetation contrasting beautifully with the blue of the sky. The image does not provide any specific details that could be used to identify the landmark as 'sa_15439'."]).to(device)

with torch.no_grad():
    image_features = model.encode_image(image)
    text_features = model.encode_text(text)

    logits_per_image, logits_per_text = model(image, text)
    probs = logits_per_image.softmax(dim=-1).cpu().numpy()

print("Label probs:", probs)  # prints: [[0.9927937  0.00421068 0.00299572]]