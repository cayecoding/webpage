import base64
import streamlit as st
import plotly.express as px
from PIL import Image

def app():
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
    background-image: url("data:image/png;base64,{img3}");
    background-position: left; 
    background-repeat: repeat;
    background-size: 90%;
    background-attachment: fixed;
    }}
    [data-testid="stSidebar"] > div:first-child {{
    background-image: url("data:image/png;base64,{img}");
    background-position: left; 
    background-repeat: no-repeat;
    background-size: 120%;
    background-attachment: fixed;
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

    st.title("About the Author")

    # ---- LOAD ASSETS ----
    img_contact_form = Image.open("p3.jpg")


    # ---- AUTHOR'S BACKGROUND ----
    with st.container():
        st.write("---")
        left_column, right_column = st.columns([1,2])
        
        with right_column:
            st.header("AUTHOR'S PROFILE")
            st.write(
                """
                PERSONAL INFORMATION
                Hellow everything, my name is Caye Guadalou L. Ruaya, just call me Caye for short.
                I am 19 years old and a Pink Lover.
                My Dream School is Cebu Institute of Technology-University. However, I landed in the most prestigious
                university in Surigao City, namely Surigao del Norte State University.
                I am a current Computer Engineering Student in the above mentioned universitity.
                """
            )
            
        with left_column:
            st.image(img_contact_form)

