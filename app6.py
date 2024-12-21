import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

def mandelbrot(h, w, max_iter, x_min, x_max, y_min, y_max):
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

def create_clean_figure(fractal, cmap, extent):
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111)
    
    # 移除所有轴和边框
    # ax.set_axis_off()
    
    # 设置图像填充整个图形
    ax.set_position([0, 0, 1, 1])
    
    # 显示分形图
    ax.imshow(fractal, cmap=cmap, extent=extent, interpolation='nearest')
    
    return fig

def main():
    st.title("动态分形图探索")
    
    # 创建一个空的占位符
    plot_placeholder = st.empty()
    
    # 控制面板
    with st.sidebar:
        st.header("实时控制")
        
        # 动态参数
        max_iter = st.slider("迭代次数", 20, 200, 100)
        zoom_speed = st.slider("缩放速度", 0.1, 2.0, 1.0)
        rotation_speed = st.slider("旋转速度", 0.0, 2.0, 1.0)
        
        # 颜色方案
        color_scheme = st.selectbox(
            "颜色方案",
            ["热力图", "彩虹", "蓝黑", "自定义"]
        )
        
        # 动画控制
        is_animating = st.checkbox("开始动画", True)

    # 设置颜色方案
    if color_scheme == "热力图":
        cmap = "hot"
    elif color_scheme == "彩虹":
        cmap = "rainbow"
    elif color_scheme == "蓝黑":
        cmap = "Blues"
    else:
        colors = [(0, 0, 0), (0, 0, 1), (1, 0, 0)]
        cmap = LinearSegmentedColormap.from_list("custom", colors)

    # 动画循环
    t = 0
    while is_animating:
        # 计算动态边界
        scale = 2 * np.exp(-zoom_speed * t/50)
        angle = rotation_speed * t/50
        
        # 计算旋转后的边界
        x_center = 0.5 * np.cos(angle) - 0.5
        y_center = 0.5 * np.sin(angle)
        
        x_min = x_center - scale
        x_max = x_center + scale
        y_min = y_center - scale
        y_max = y_center + scale
        
        # 生成分形
        fractal = mandelbrot(500, 500, max_iter, x_min, x_max, y_min, y_max)
        
        # 创建和显示图像
        fig = create_clean_figure(fractal, cmap, [x_min, x_max, y_min, y_max])
        plot_placeholder.pyplot(fig)
        plt.close(fig)  # 清理内存
        
        t += 1
        
        # 控制动画速度
        plt.pause(0.05)

if __name__ == "__main__":
    main()