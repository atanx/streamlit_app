import streamlit as st
from rembg import remove
from PIL import Image
import os
from pathlib import Path
import tempfile

def process_image(input_path, output_path):
    """处理普通图片"""
    try:
        st.info(f"正在处理图片: {input_path}")
        
        # 创建进度条
        progress_bar = st.progress(0)
        progress_text = st.empty()
        
        # 读取图片
        progress_text.text("1. 读取图片中...")
        input_image = Image.open(input_path)
        progress_bar.progress(0.3)
        
        # 移除背景
        progress_text.text("2. 正在移除背景...")
        output_image = remove(input_image)
        progress_bar.progress(0.7)
        
        # 保存图片前处理格式
        output_suffix = Path(output_path).suffix.lower()
        if output_suffix == '.jpg' or output_suffix == '.jpeg':
            # JPEG 不支持透明度，需要用白色背景
            background = Image.new('RGBA', output_image.size, (255, 255, 255, 255))
            background.paste(output_image, mask=output_image.split()[3])  # 使用alpha通道作为mask
            output_image = background.convert('RGB')
        
        # 保存图片
        progress_text.text("3. 保存处理后的图片...")
        output_image.save(output_path)
        progress_bar.progress(1.0)
        
        progress_text.text("处理完成！")
        st.success(f"背景移除成功！已保存至: {output_path}")
        
        # 显示处理前后的图片对比
        col1, col2 = st.columns(2)
        with col1:
            st.image(input_path, caption="原图")
        with col2:
            st.image(output_image, caption="处理后")
            
        return True
        
    except Exception as e:
        st.error(f"处理过程中出现错误: {str(e)}")
        return False

def process_gif(input_path, output_path):
    """处理GIF图片"""
    try:
        # 打开GIF文件
        st.info(f"正在处理GIF: {input_path}")
        gif = Image.open(input_path)
        
        # 获取GIF的所有帧
        frames = []
        frame_durations = []
        
        # 创建进度条
        progress_bar = st.progress(0)
        progress_text = st.empty()
        
        try:
            # 遍历所有帧
            i = 0
            while True:
                gif.seek(i)
                # 获取当前帧的持续时间
                frame_durations.append(gif.info.get('duration', 100))
                
                # 处理当前帧
                progress_text.text(f"正在处理第 {i+1} 帧...")
                frame = Image.new('RGBA', gif.size, (0, 0, 0, 0))
                frame.paste(gif)
                # 移除背景
                processed_frame = remove(frame)
                frames.append(processed_frame)
                
                # 更新进度条
                progress = min((i + 1) / 100, 1.0)  # 假设最��100帧，可以根据需要调整
                progress_bar.progress(progress)
                
                i += 1
                
        except EOFError:
            pass  # 到达GIF末尾
        
        # 保存处理后的GIF
        progress_text.text("正在保存处理后的GIF...")
        frames[0].save(
            output_path,
            save_all=True,
            append_images=frames[1:],
            duration=frame_durations,
            loop=0,
            optimize=False,
            disposal=2,  # 重要：确保每帧都完全替换前一帧
            transparency=0  # 设置透明色
        )
        
        progress_bar.progress(1.0)
        progress_text.text("处理完成！")
        st.success(f"GIF处理成功！已保存至: {output_path}")
        
        col1, col2 = st.columns(2)
        with col1:
            st.image(input_path, caption="原始GIF")
        with col2:
            st.image(output_path, caption="处理后的GIF")
            
        return True
        
    except Exception as e:
        st.error(f"处理过程中出现错误: {str(e)}")
        return False

# Streamlit界面
st.title("图片背景移除工具")

# 选择处理类型
file_type = st.radio(
    "选择要处理的文件类型",
    ["普通图片", "GIF动图"],
    horizontal=True
)

# 根据选择显示不同的文件上传器
if file_type == "普通图片":
    uploaded_file = st.file_uploader("选择要处理的图片", type=['png', 'jpg', 'jpeg'])
    file_processor = process_image
else:
    uploaded_file = st.file_uploader("选择要处理的GIF", type=['gif'])
    file_processor = process_gif

if uploaded_file is not None:
    # 创建临时目录存放文件
    with tempfile.TemporaryDirectory() as temp_dir:
        # 保存上传的文件
        input_path = Path(temp_dir) / uploaded_file.name
        with open(input_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # 设置输出路径，对于普通图片统一使用 PNG 格式
        if file_type == "普通图片":
            output_path = Path(temp_dir) / f"bg_removed_{input_path.stem}.png"
        else:
            output_path = Path(temp_dir) / f"bg_removed_{uploaded_file.name}"
        
        # 处理图片
        if st.button("开始移除背景"):
            if file_processor(str(input_path), str(output_path)):
                # 如果处理成功，提供下载链接
                if output_path.exists():
                    with open(output_path, 'rb') as f:
                        st.download_button(
                            label="下载处理后的图片",
                            data=f.read(),
                            file_name=f"bg_removed_{uploaded_file.name}",
                            mime=f"image/{output_path.suffix[1:]}"
                        )

# 添加说明信息
with st.expander("使用说明"):
    st.markdown("""
    ### 使用说明
    1. 选择要处理的文件类型（普通图片或GIF动图）
    2. 上传需要处理的图片文件
    3. 点击"开始移除背景"按钮
    4. 等待处理完成后下载处理后的图片
    
    ### 支持的格式
    - 普通图片：PNG, JPG, JPEG
    - 动图：GIF
    
    ### 注意事项
    - GIF处理可能需要较长时间，请耐心等待
    - 建议上传的图片大小不要超过10MB
    - 处理后的图片将保留原始格式
    """)
