import base64
import streamlit as st
from PIL import Image
import plotly.express as px

def app():   
  # ---- HEADER SECTION ----
  with st.container():
    st.title("MAIN PAGE")
    st.subheader("THIS IS SIARGAO")
    st.title("Also known as the SURFING CAPITAL OF THE PHILIPPINES")
    st.write(
            "Arat na sa Siargao!"
            )
    
  df = px.data.iris()

  @st.cache_data
  def get_img_as_base64(file):
    with open(file, "rb") as f:
            data = f.read()
    return base64.b64encode(data).decode()


  
  img = get_img_as_base64("p1.jpg")
  img1 = get_img_as_base64("p2.jpg")
  img2 = get_img_as_base64("p3.jpg")
  img3 = get_img_as_base64("p4.jpg")
  img4 = get_img_as_base64("p5.jpg")
  
  page_bg_img = f"""
  <style>
  [data-testid="stAppViewContainer"] > .main {{
  background-image: url("data:image/png;base64,{img1}");
  background-position: center; 
  background-repeat: no-repeat;
  background-size: 100%;
  background-attachment: local;
   }}
  [data-testid="stSidebar"] > div:first-child {{
  background-image: url("data:image/png;base64,{img}");
  background-position: left; 
  background-repeat: no-repeat;
  background-size: 150%;
  background-attachment: local;
  }}

  [data-testid="stHeader"] {{
  background: rgba(0,0,0,0);
  }}

  [data-testid="stToolbar"] {{
  right: 2rem;
  }}
  </style>
  """

  st.markdown(page_bg_img, unsafe_allow_html=True)
