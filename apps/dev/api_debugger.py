import streamlit as st
import requests


def get_data(url):
    response = requests.get(url)
    try:    
        return True, response.json()
    except:
        st.write(response.status_code)
        return False, response.text




col1, col2 = st.columns(2)

# url = col1.text_input("输入API地址", value="https://test-statuscenter.xmov.ai/pingpong/")
url = col1.text_input("输入API地址", value="https://test-open.xmov.ai/")
if col1.button("获取数据"):
    is_json, data = get_data(url)
    if is_json:
        st.json(data)
    else:
        st.code(data)