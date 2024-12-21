import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from plotly.graph_objects import Figure, Scatter
import streamlit.components.v1 as components
import time
import altair as alt


st.title("函数探索工具")
st.write("这是一个用于探索三角函数的工具。你可以通过调整参数来观察sin(x)、cos(x)和sin(x)+cos(x)的变化。")
st.html(
    "<p><span style='text-decoration: line-through double red;'>Oops</span>!</p>"
)
st.markdown("""
- [altair_chart](https://docs.streamlit.io/develop/api-reference/charts/st.altair_chart)
- [plotly_chart](https://docs.streamlit.io/develop/api-reference/charts/st.plotly_chart)
- [graphviz_chart](https://docs.streamlit.io/develop/api-reference/charts/st.graphviz_chart)

"""
)
# st.help(st.altair_chart)

# embed streamlit docs in a streamlit app
# components.iframe("https://www.baidu.com", height=500)

def my_generator():
    for i in range(10):
        yield str(i)
        time.sleep(0.1)


offset = 5
with st.sidebar:
    st.title("函数选择")
    offset_slider = st.slider("sin(x)的偏移量", 0, 10, offset, key="offset")
    is_animating = st.checkbox("开始动画", False)
    st.write_stream(my_generator)
    with st.echo():
        st.write('This code will be printed')
        
    mode = st.radio("选择模式", ["area", "line"])
    e = RuntimeError("This is an exception of type RuntimeError")
    st.exception(e)


x = np.linspace(0, 10, 100)
y1 = np.sin(x+offset_slider)
y2 = np.cos(x)
y3 = y1 + y2


st.latex(r'''
f(x) = sin(x+t) + cos(x-t)
''')
fig = Figure()
fig.add_trace(Scatter(x=x, y=y1, name='sin(x)', line=dict(color='red')))
fig.add_trace(Scatter(x=x, y=y2, name='cos(x)', line=dict(color='blue')))
fig.add_trace(Scatter(x=x, y=y3, name='sin(x) + cos(x)', line=dict(color='green')))
plot_placeholder = st.empty()
st.plotly_chart(fig, key="fig")

fig = Figure()
fig.add_trace(Scatter(x=x, y=y1, name='sin(x)', line=dict(color='red')))
fig.add_trace(Scatter(x=x, y=y2, name='cos(x)', line=dict(color='blue')))
fig.add_trace(Scatter(x=x, y=y3, name='sin(x) + cos(x)', line=dict(color='green')))
fig.update_layout(
    xaxis=dict(
        range=[0, 10],  # 设置x轴范围
        fixedrange=True,  # 锁定x轴范围
        showgrid=True,
    ),
    yaxis=dict(
        range=[-2.5, 2.5],  # 设置y轴范围
        fixedrange=True,  # 锁定y轴范围
        showgrid=True,
    ),
    title='Trigonometric Functions',
    showlegend=True,
    plot_bgcolor='black',     # 绘图区背景色
    # paper_bgcolor='black',    # 整个图表背景色
    
)
plot_placeholder.plotly_chart(fig)

while is_animating:
    offset += 0.1
    y1 = np.sin(x+offset)
    y2 = np.cos(x-offset)
    y3 = y1 + y2
    
    if mode == "line":
        fig.data[0].y = y1
        fig.data[1].y = y2
        fig.data[2].y = y3
        plot_placeholder.plotly_chart(fig)
    else:
        fig = Figure()
        fig.add_trace(Scatter(
            x=x, y=y1, name='sin(x)', 
            fill='tonexty',  # 添加填充
            line=dict(color='red')
        ))
        fig.add_trace(Scatter(
            x=x, y=y2, name='cos(x)', 
            fill='tonexty',
            line=dict(color='blue')
        ))
        fig.add_trace(Scatter(
            x=x, y=y3, name='sin(x) + cos(x)', 
            fill='tonexty',
            line=dict(color='green')
        ))
        
        fig.update_layout(
            xaxis=dict(
                range=[0, 10],
                fixedrange=True,
                showgrid=True,
            ),
            yaxis=dict(
                range=[-2.5, 2.5],
                fixedrange=True,
                showgrid=True,
            ),
            title='Trigonometric Functions',
            showlegend=True,
            plot_bgcolor='black',
        )
        plot_placeholder.plotly_chart(fig)
    time.sleep(0.1)

