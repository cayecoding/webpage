import base64
import streamlit as st
import plotly.express as px
from PIL import Image

def app():
  # ---- LOAD ASSETS ----
  img_contact_form2 = Image.open("siargao.jpg")
  # ---- PROJECTS ----
  with st.container():
    st.write("---")
    st.header("ABOUT THIS PAGE")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
      st.image(img_contact_form2)
    with text_column:
      st.subheader("WELCOME TO SIARGAO")
      st.write(
            """
            Etymology. The name originates from Visayan siargaw or saliargaw (Premna odorata),
            a mangrove species that grows on the islands. Siargao Island is a tropical paradise
            located in the Surigao del Norte province of the Philippines. This teardrop-shaped
            island has grown steadily in popularity over the past few years and is often known
            as the country's surfing capital. Siargao is an island of nine municipalities in the
            province of Surigao del Norte. Known as the “Surfing Capital of the Philippines”,
            Siargao is mainly responsible for introducing surfing to the country. 48 islands,
            Siargao Island is composed of 48 islands and islets-politically divided into nine
            municipalities: Burgos, Dapa, Del Carmen, General Luna, Pilar, San Benito, San Isidro,
            Santa Monica, and Socorro. Beyond its physical beauty, Siargao Island is enriched by
            its warm-hearted locals and vibrant island culture. The locals, known as “Surigaonons,”
            are known for their welcoming nature, making visitors feel at home. The island's culture
            is deeply rooted in surfing, fishing, and a laid-back way of life.
            """
            )
      st.markdown("[Watch Video...](https://www.youtube.com/watch?v=fo1BPRKD2Bg)")

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
  img5 = get_img_as_base64("p6.jpg")
  img6 = get_img_as_base64("p7.jpg")
    
  page_bg_img = f"""
  <style>
  [data-testid="stAppViewContainer"] > .main {{
  background-image: url("data:image/png;base64,{img4}");
  background-position: center; 
  background-repeat: no-repeat;
  background-size: 110%;
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
