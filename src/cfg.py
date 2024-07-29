import json
import os

import timm
import torch

def load_model():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(base_dir, "baseline_classifier.pt")
    idx2label = os.path.join(base_dir, "idx2label.json")
    global MODEL, IDX2LABEL
    
    with open(idx2label, "r") as f:
        IDX2LABEL = json.load(f)
    IDX2LABEL = {int(i):label for i,label in IDX2LABEL.items()}
        
    MODEL = timm.create_model("efficientnet_b3", num_classes=20)
    MODEL.load_state_dict(torch.load(model_path, map_location=torch.device("cpu")))
    MODEL.eval()

load_model()