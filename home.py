import streamlit as st
from stable_diffusion import show_stable_diffusion_page
from ad_Template_generator import show_ad_Template_generator_page

st.set_page_config(page_title="Multi-Page App", layout="wide")

#the navigation structure
PAGES = {
   "Home": lambda: st.markdown("""
   # Welcome to the Ad Teamplate Generator App 👋 !

   This application allows you to generate ad templates with customizable elements such as headlines, button texts, and images.
   You can create your ad template with an image created with stable diffusion or with an image you upload yourself.

   To get started,my suggestion is to first go to the Stable Diffusion page and create your image. Afterward, navigate to the Ad Template Generator page to prepare your template.

   Enjoy creating your own ad templates!
   """),
   "Stable Diffusion": show_stable_diffusion_page,
   "Ad Template Generator": show_ad_Template_generator_page
}


st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

page = PAGES[selection]
page()
