import streamlit
from PIL import Image

with streamlit.expander("Start"):  #rozszerza okienko
    cameraimage=streamlit.camera_input("Camera")

if cameraimage:
    img=Image.open(cameraimage)
    grayImg=img.convert("L")
    streamlit.image(grayImg)