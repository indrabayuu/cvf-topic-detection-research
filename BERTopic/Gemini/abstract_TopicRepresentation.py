"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

import os
import google.generativeai as genai
import time

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

generation_config = {
    "temperature": 0.8,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 20,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    system_instruction="Based on these [KEYWORDS], determine a concise and relevant label that accurately represents the overall topic in 5 words or fewer",
)

# List of BERTopic-Abstract Keywords
data = [
    ["blur", "image", "noise", "kernel", "denoising", "patch", "deblurring", "method", "quality", "deconvolution"],
    ["image", "blur", "deblurring", "method", "denoising", "algorithm", "gradient", "result", "proposed", "problem"],
    ["saliency", "salient", "dataset", "fixation", "object", "image", "visual", "region", "gaze", "data"],
    ["question", "image", "visual", "dataset", "video", "language", "sentence", "description", "text", "answer"],
    ["object", "segmentation", "semantic", "detection", "network", "approach", "instance", "task", "image", "model"],
    ["image", "network", "method", "rain", "quality", "resolution", "end", "based", "proposed", "state"],
    ["image", "method", "blur", "network", "resolution", "real", "super", "model", "deep", "result"],
    ["reflection", "image", "scene", "mirror", "light", "transparent", "method", "surface", "illuminant", "normal"],
    ["forgetting", "learning", "incremental", "task", "continual", "class", "new", "catastrophic", "data", "old"],
    ["client", "federated", "fl", "local", "model", "data", "learning", "gradient", "privacy", "global"],
    ["client", "federated", "fl", "data", "learning", "model", "local", "global", "privacy", "server"],
    ["saliency", "gaze", "salient", "region", "model", "eye", "image", "method", "object", "detection"],
    ["video", "concept", "image", "description", "visual", "sentence", "language", "phrase", "word", "text"],
    ["person", "tracking", "object", "feature", "identification", "video", "method", "tracker", "id", "frame"],
    ["face", "facial", "landmark", "expression", "image", "structure", "method", "model", "identity", "loss"],
    ["search", "quantization", "architecture", "nas", "neural", "precision", "bit", "space", "network", "accuracy"],
    ["matrix", "solver", "camera", "problem", "bundle", "flag", "point", "fundamental", "adjustment", "minimal"],
    ["image", "model", "face", "gan", "method", "network", "approach", "training", "generative", "propose"],
    ["point", "method", "object", "camera", "depth", "network", "map", "cloud", "visual", "estimation"],
    ["detection", "based", "stereo", "method", "object", "image", "map", "view", "lane", "fusion"],
    ["attack", "adversarial", "defense", "certified", "based", "perturbation", "domain", "sample", "model", "training"]
]

def process_keywords(keywords):
    input_text = "[ " + ", ".join(keywords) + "]"
    print(f"Processing keywords: {input_text}")
    response = model.generate(input_text, stream=True)
    print(f"Response: {response}")

for keywords in data:
    process_keywords(keywords)
    time.sleep(30)  # Wait for 30 seconds before processing the next set, due to limit per minutes in GEMINI API
