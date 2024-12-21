import streamlit as st
import cv2
import numpy as np
from PIL import Image

def main():
    st.title("摄像头实时显示")

    # 创建一个选择框，选择使用哪个摄像头
    camera_index = st.selectbox("选择摄像头", [0, 1, 2], 0)

    # 添加一个按钮来开启/关闭摄像头
    run = st.checkbox('开启摄像头')

    # 创建一个占位符来显示视频帧
    FRAME_WINDOW = st.image([])
    
    # 添加一些图像处理选项
    with st.sidebar:
        st.header("图像处理选项")
        apply_gray = st.checkbox("灰度图")
        apply_blur = st.checkbox("模糊")
        apply_canny = st.checkbox("边缘检测")
        
        if apply_blur:
            blur_value = st.slider("模糊程度", 1, 30, 5)
        
        if apply_canny:
            canny_low = st.slider("Canny 低阈值", 0, 255, 100)
            canny_high = st.slider("Canny 高阈值", 0, 255, 200)

    # 打开摄像头
    camera = cv2.VideoCapture(camera_index)

    while run:
        _, frame = camera.read()
        
        # 图像处理
        if frame is not None:
            # 转换颜色空间从 BGR 到 RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # 应用选择的图像处理
            if apply_gray:
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
                frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)
            
            if apply_blur:
                frame = cv2.GaussianBlur(frame, (blur_value*2+1, blur_value*2+1), 0)
            
            if apply_canny:
                frame = cv2.Canny(cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY), 
                                canny_low, canny_high)
                frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)
            
            # 显示帧
            FRAME_WINDOW.image(frame)
        else:
            st.error("无法获取摄像头画面")
            break

    # 关闭摄像头
    camera.release()

    # 添加截图功能
    if st.button('截图'):
        if 'frame' in locals():
            # 保存图片
            img = Image.fromarray(frame)
            img.save('screenshot.png')
            st.success('截图已保存为 screenshot.png')
            
            # 显示保存的图片
            st.image('screenshot.png')

if __name__ == '__main__':
    main()