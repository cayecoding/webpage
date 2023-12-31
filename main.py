import streamlit as st
from streamlit_option_menu import option_menu
import Home, AuthorsProfile, Contacts, Content
from PIL import Image

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func): 

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
    # app = st.sidebar(
            
        with st.sidebar:
            app = option_menu (
               
                menu_title=None, 
                options=["Home", "AuthorsProfile", "Content", 'Contacts'], 
                icons=['house-fill', 'person-circle', "pencil", 'phone'], 
                menu_icon="cast",
                default_index=0,
                orientation="horizontal",
                styles={
                        "container": {"padding": "5!important","background-color":'blue'},
                        "icon": {"color": "white", "font-size": "23px"}, 
                        "nav-link": {"color":"white","font-size": "20px", "text-align": "", "margin":"0px", "--hover-color": "blue"},
                        "nav-link-selected": {"background-color": "#DB6551"},
                        }     
            )
    
        if app == 'Home':
            Home.app() 
        if app == 'AuthorsProfile':
            AuthorsProfile.app()            
        if app == 'Content':
            Content.app()
        if app == 'Contacts':
            Contacts.app()       
                
    run()     

