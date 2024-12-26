# 方法1：使用 rembg (推荐，最简单)
from rembg import remove
from PIL import Image

def remove_bg_rembg(input_path, output_path):
    # 读取图片
    input_image = Image.open(input_path)
    # 移除背景
    output_image = remove(input_image)
    # 保存图片
    output_image.save(output_path)
    

remove_bg_rembg("jy.gif", "jy_bg_removed.gif")
    
    