import streamlit as st
import torch
from PIL import Image

from diffusers import StableDiffusionImg2ImgPipeline

def show_stable_diffusion_page():
    st.title("Generate Image Using Stable Diffusion Img2Img")

    # Initialize the stable diffusion pipeline
    model_id_or_path = "runwayml/stable-diffusion-v1-5"
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    pipe = StableDiffusionImg2ImgPipeline.from_pretrained(model_id_or_path, torch_dtype=torch.float32)
    pipe.to(device)


    uploaded_main_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_main_image is not None:
        main_image = Image.open(uploaded_main_image).convert("RGB")
        main_image = main_image.resize((768, 512))


        prompt = st.text_input("Enter a prompt:")
        #st.write(f"User entered prompt: {prompt}")


        if st.button("Generate Image"):
            result_images = pipe(prompt=prompt, image=main_image, strength=0.75, guidance_scale=7.5).images
            st.session_state['generated_image'] = result_images[0]
            st.image(result_images[0], caption="Generated Image", use_column_width=True)
