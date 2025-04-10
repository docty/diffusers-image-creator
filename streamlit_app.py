import streamlit as st
#from diffusers import DiffusionPipeline, DPMSolverMultistepScheduler
import torch
#from PIL import Image


st.title("Image Generation:2")

 
#@st.cache_resource
# def load_pipeline():
#     pipe = DiffusionPipeline.from_pretrained(
#         "CompVis/stable-diffusion-v1-4",
#         torch_dtype=torch.float16,
#     )
#     pipe.to("cuda" if torch.cuda.is_available() else "cpu")

#     pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipeline.scheduler.config)

#     pipe.enable_attention_slicing()
  
#     return pipe

#pipeline = load_pipeline()

prompt = st.text_input("Enter a prompt to generate an image:", value="pipeline under the sea")

# if st.button("Generate Image"):
#     with st.spinner("Generating image..."):
#         image = pipe(prompt).images[0]
#         st.image(image, caption="Generated Image", use_column_width=True)
