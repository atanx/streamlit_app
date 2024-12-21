import streamlit as st
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from io import BytesIO
import time

def mandelbrot(h, w, max_iter, x_min, x_max, y_min, y_max):
    """计算曼德勃罗特集"""
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

def julia(h, w, max_iter, x_min, x_max, y_min, y_max, c):
    """计算朱利亚集"""
    y, x = np.ogrid[y_min:y_max:h*1j, x_min:x_max:w*1j]
    z = x + y*1j
    divtime = max_iter + np.zeros(z.shape, dtype=int)

    for i in range(max_iter):
        z = z**2 + c
        diverge = z*np.conj(z) > 2**2
        div_now = diverge & (divtime == max_iter)
        divtime[div_now] = i
        z[diverge] = 2

    return divtime

def main():
    st.title("分形图探索工具")
    
    # 侧边栏控制
    with st.sidebar:
        st.header("参数设置")
        
        # 选择分形类型
        fractal_type = st.selectbox(
            "选择分形类型",
            ["曼德勃罗特集", "朱利亚集"],
            key="fractal_type"
        )
        
        # 图像尺寸
        resolution = st.slider(
            "分辨率",
            min_value=100,
            max_value=1000,
            value=500,
            step=100,
            key="resolution"
        )
        
        # 迭代次数
        max_iter = st.slider(
            "最大迭代次数",
            min_value=20,
            max_value=200,
            value=100,
            key="max_iter"
        )
        
        # 颜色方案
        color_scheme = st.selectbox(
            "颜色方案",
            ["热力图", "彩虹", "蓝黑", "自定义"],
            key="color_scheme"
        )
        
        # 坐标范围
        st.subheader("坐标范围")
        x_min = st.number_input("X最小值", value=-2.0, format="%.2f", key="x_min")
        x_max = st.number_input("X最大值", value=1.0, format="%.2f", key="x_max")
        y_min = st.number_input("Y最小值", value=-1.5, format="%.2f", key="y_min")
        y_max = st.number_input("Y最大值", value=1.5, format="%.2f", key="y_max")
        
        # 朱利亚集参数
        if fractal_type == "朱利亚集":
            st.subheader("朱利亚集参数")
            c_real = st.number_input("C实部", value=-0.4, format="%.3f", key="c_real")
            c_imag = st.number_input("C虚部", value=0.6, format="%.3f", key="c_imag")
            c = complex(c_real, c_imag)
        
        # 生成按钮
        generate = st.button("生成分形", key="generate")

    # 主页面显示
    if generate:
        with st.spinner("正在生成分形图..."):
            # 创建图像
            if fractal_type == "曼德勃罗特集":
                fractal = mandelbrot(resolution, resolution, max_iter, 
                                   x_min, x_max, y_min, y_max)
            else:
                fractal = julia(resolution, resolution, max_iter, 
                              x_min, x_max, y_min, y_max, c)
            
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
            
            # 创建图像
            fig, ax = plt.subplots(figsize=(10, 10))
            im = ax.imshow(fractal, cmap=cmap, extent=[x_min, x_max, y_min, y_max])
            plt.colorbar(im)
            ax.set_title(f"{fractal_type} - {max_iter}次迭代")
            
            # 显示图像
            st.pyplot(fig)
            
            # 下载选项
            buf = BytesIO()
            plt.savefig(buf, format="png", dpi=300, bbox_inches="tight")
            buf.seek(0)
            st.download_button(
                label="下载图像",
                data=buf,
                file_name=f"fractal_{int(time.time())}.png",
                mime="image/png"
            )
    
    # 添加说明
    with st.expander("使用说明"):
        st.markdown("""
        ### 参数说明
        - **分辨率**: 图像的像素大小
        - **最大迭代次数**: 决定图像的精细程度
        - **坐标范围**: 复平面上显示的区域
        - **颜色方案**: 不同的配色方案
        
        ### 操作提示
        1. 调整参数以获得不同的效果
        2. 可以通过坐标范围来放大感兴趣的区域
        3. 增加迭代次数可以获得更精细的细节
        4. 朱利亚集可以通过改变C值获得不同的图案
        """)

if __name__ == "__main__":
    main()
