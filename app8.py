import streamlit as st
import plotly.graph_objects as go
import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.font_manager


def mandelbrot(h, w, x_min, x_max, y_min, y_max, max_iter):
    """
    计算曼德勃罗特集合
    :param h: 高度
    :param w: 宽度
    :param x_min: x的最小值
    :param x_max: x的最大值
    :param y_min: y的最小值
    :param y_max: y的最大值
    :param max_iter: 最大迭代次数
    :return: 曼德勃罗特集合
    """
    y, x = np.ogrid[y_min:y_max:h*1j, x_min:x_max:w*1j]
    c = x + y*1j
    z = c
    divtime = max_iter + np.zeros(z.shape, dtype=int)

    for i in range(max_iter):
        z = z**2 + c
        diverge = z*np.conj(z) > 2**2
        div_now = diverge & (divtime == max_iter)
        divtime[div_now] = i
        z[diverge] = 2

    return divtime

st.title("数据可视化")
state = st.session_state
state.x_center = 0.27
state.y_center = 0.0

# 控制参数
with st.sidebar:
    resolution = st.slider("分辨率", 100, 1000, 500)
    max_iter = st.slider("最大迭代次数", 20, 100, 50)
    colorscale = st.selectbox(
        "选择颜色方案",
        ['Viridis', 'Plasma', 'Inferno', 'Magma', 'Hot', 'Electric']
    )
     
    is_animating = st.checkbox("开始动画", False)

    # x_min = st.slider("x的最小值", -2.0, 2.0, -1.4 + 0.2)
    # x_max = st.slider("x的最大值", -2.0, 2.0, 1.4 + 0.2)
    # y_min = st.slider("y的最小值", -2.0, 2.0, -1.4)
    # y_max = st.slider("y的最大值", -2.0, 2.0, 1.4)
    x_center = st.slider("x的中心值", -2.0, 2.0, state.x_center)
    y_center = st.slider("y的中心值", -2.0, 2.0, state.y_center)
    x_min = x_center - 1.4
    x_max = x_center + 1.4
    y_min = y_center - 1.4
    y_max = y_center + 1.4

plot_placeholder = st.empty()

# 计算分形
fractal = mandelbrot(resolution, resolution, x_min, x_max, y_min, y_max, max_iter)

# 创建图表
fig = go.Figure(data=go.Heatmap(
    z=fractal,
    colorscale=colorscale,
    showscale=False
))

# 更新布局
fig.update_layout(
    width=800,
    height=800,
    xaxis=dict(showticklabels=False),
    yaxis=dict(showticklabels=False),
    plot_bgcolor='black',
    paper_bgcolor='black'
)

# 显示图表
plot_placeholder.plotly_chart(fig)

# 创建一个空的placeholder用于显示坐标值
coords_placeholder = st.empty()

if is_animating:
    steps = list(range(150))
    steps.reverse()
    for i in steps:
        
        x_min = x_center - i * 0.01
        x_max = x_center + i * 0.01
        y_min = y_center - i * 0.01
        y_max = y_center + i * 0.01
        
        fractal = mandelbrot(resolution, resolution, x_min, x_max, y_min, y_max, max_iter)
        fig = go.Figure(data=go.Heatmap(
            z=fractal,
            colorscale=colorscale,
            showscale=False
        ))
        
        fig.update_layout(
            width=800,
            height=800,
            xaxis=dict(showticklabels=False),
            yaxis=dict(showticklabels=False),
            plot_bgcolor='black',
            paper_bgcolor='black'
        )
        
        # 使用columns更新坐标值
        cols = coords_placeholder.columns(2)
        with cols[0]:
            st.write("x_min: ", round(x_min, 2))
            st.write("x_max: ", round(x_max, 2))
        with cols[1]:
            st.write("y_min: ", round(y_min, 2))
            st.write("y_max: ", round(y_max, 2))
            
        plot_placeholder.plotly_chart(fig, key=f"plot_{i}")
        
        time.sleep(0.1)

with st.sidebar:
    st.write("x_min: ", x_min)
    st.write("x_max: ", x_max)
    st.write("y_min: ", y_min)
    st.write("y_max: ", y_max)
