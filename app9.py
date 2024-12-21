import os
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(layout="wide")

def get_file_list(path, file_type):
    return [each for each in os.listdir(path) if each.endswith(file_type)]


with st.sidebar:
    file_list = get_file_list(".", ".py")
    file_list += [st.__file__]
    selected_file = st.selectbox("选择文件", file_list)
    
    st_file = st.__file__
    
    doc_dict = {
        "streamlit": st,
        # "os": os,
        "pandas": pd,
        "pandas.DataFrame": pd.DataFrame,
        "numpy": np,
        "plotly": px,
    }
    doc_selected = st.selectbox("选择文档", doc_dict.keys())
    with st.container(height=700):
        st.help(doc_dict[doc_selected])



if selected_file:
    with open(selected_file, "r", encoding="utf-8") as f:
        with st.container(height=800):
            data = f.read()
            st.header(f"当前文件: {selected_file}")
            st.code(data, language="python", line_numbers=True)




