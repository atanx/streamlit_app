import streamlit as st
import dataclasses

@dataclasses.dataclass
class Website:
    name: str
    url: str
    description: str
    image: str


def awesome_app():
    st.title("Some Awesome Websites")

    websites = [ Website(name="DB Diagram", 
                         url="https://dbdiagram.io/d", 
                         description="Draw database diagrams.", 
                         image="./static/diagram.png"),
                Website(name="Remove Background", 
                         url="https://www.remove.bg/", 
                         description="Remove background from any image.", 
                         image="./static/remove_bg.png")
    ]
    for idx, website in enumerate(websites):
        with st.expander(f"#{idx+1}. {website.name}"):
            st.write(website.url)
            st.info(website.description)
            st.image(website.image, caption=website.name, width=400)
        
awesome_app()
