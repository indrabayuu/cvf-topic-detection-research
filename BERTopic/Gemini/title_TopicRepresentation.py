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
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    system_instruction="Based on these [KEYWORDS], determine a concise and relevant label that accurately represents the overall topic in 5 words or fewer",
)

# List of BERTopic-Title Keywords
data = [
    ["tracking", "object", "visual", "multiple", "target", "multi", "pursuit", "latent", "pose", "real"],
    ["tracking", "online", "target", "object", "visual", "multi", "occlusion", "robust", "multiple", "motion"],
    ["tracking", "target", "tracker", "multi", "correlation", "adaptive", "foreground", "reliable", "object", "multiple"],
    ["network", "neural", "convolutional", "deep", "architecture", "using", "learning", "pooling", "vision", "random"],
    ["flow", "optical", "stereo", "camera", "based", "slow", "fast", "interpolation", "correspondence", "accurate"],
    ["visual", "question", "answering", "attention", "language", "reasoning", "generation", "dialog", "learning", "grounding"],
    ["navigation", "language", "path", "trajectory", "vision", "imitation", "prediction", "agent", "lstm", "visual"],
    ["reinforcement", "learning", "driving", "simulation", "embodied", "environment", "agent", "meta", "interactive", "free"],
    ["action", "temporal", "recognition", "activity", "supervised", "localization", "weakly", "video", "spatio", "actor"],
    ["federated", "learning", "heterogeneous", "privacy", "data", "client", "iid", "heterogeneity", "local", "personalized"],
    ["stereo", "view", "depth", "multi", "estimation", "disparity", "ray", "consistent", "using", "gated"],
    ["action", "recognition", "event", "video", "complex", "activity", "detection", "learning", "interaction", "feature"],
    ["tracking", "visual", "online", "multiple", "filter", "object", "learning", "multi", "weighted", "spatially"],
    ["pose", "estimation", "human", "hand", "monocular", "rgb", "object", "real", "learning", "robust"],
    ["architecture", "search", "distillation", "neural", "network", "knowledge", "training", "sequential", "data", "product"],
    ["pose", "human", "estimation", "hand", "mesh", "shape", "motion", "body", "regression", "using"],
    ["federated", "learning", "communication", "global", "personalized", "vertical", "client", "personalization", "iid", "overlapping"],
    ["retrieval", "image", "answering", "question", "content", "text", "exploring", "search", "modal", "visual"],
    ["retrieval", "text", "visual", "image", "graph", "identification", "learning", "teacher", "student", "table"],
    ["video", "action", "temporal", "supervised", "recognition", "segmentation", "self", "multi", "audio", "learning"],
    ["action", "temporal", "recognition", "transformer", "skeleton", "network", "spatio", "contrastive", "based", "multi"]
]

def process_keywords(keywords):
    input_text = "[ " + ", ".join(keywords) + "]"
    print(f"Processing keywords: {input_text}")
    response = model.generate_content(input_text, stream=True)
    print(f"Response: {response}")

for keywords in data:
    process_keywords(keywords)
    time.sleep(30)  # Wait for 30 seconds before processing the next set, due to limit per minutes in GEMINI API
