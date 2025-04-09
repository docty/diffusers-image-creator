import streamlit as st
from diffusers import DiffusionPipeline, DPMSolverMultistepScheduler
import torch
from PIL import Image


st.title("Image Generation")

 
@st.cache_resource
def load_pipeline():
    pipe = DiffusionPipeline.from_pretrained(
        "stable-diffusion-v1-5/stable-diffusion-v1-5",
        torch_dtype=torch.float16,
    )
    pipe.to("cuda" if torch.cuda.is_available() else "cpu")

    pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipeline.scheduler.config)

    pipe.enable_attention_slicing()
  
    return pipe

pipeline = load_pipeline()
