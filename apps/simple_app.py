import streamlit as st
import time

# 1. 基本布局元素
# 标题和文本
st.title("应用标题")
st.header("一级标题")
st.subheader("二级标题")
st.text("普通文本")
st.markdown("**Markdown** 文本")
st.write("万能显示函数")

# 2. 侧边栏
with st.sidebar:
    st.title("侧边栏")
    option = st.selectbox("选择一个选项", ["A", "B", "C"], key="sidebar_select")

# 3. 数据展示
import pandas as pd
import numpy as np

# 显示数据表格
x = np.linspace(0, 10, 100)
y = np.sin(x)
df = pd.DataFrame({
    'first column': x,
    'second column': y
})
st.dataframe(df.head())  # 交互式表格
st.table(df.head())      # 静态表格

# 4. 图表
import plotly.express as px

# Plotly 图表
fig = px.line(df, x='first column', y='second column')
st.plotly_chart(fig)

# 5. 输入组件
# 文本输入
text_input = st.text_input("输入文本")
number = st.number_input("输入数字", min_value=0, max_value=100)

# 选择框
option = st.selectbox("选择一个选项", ["A", "B", "C"], key="select1")

# 多选框
options = st.multiselect("多选", ["A", "B", "C"])

# 滑块
slider_val = st.slider("选择范围", 0, 100)

# 文件上传
uploaded_file = st.file_uploader("上传文件", type=['csv', 'xlsx'])

# 6. 列布局
col1, col2, col3 = st.columns(3)  # 平均分成3列
# 或者指定比例
col1, col2 = st.columns([2, 1])  # 2:1 的比例

with col1:
    st.header("第一列")
    st.write("这是第一列的内容")
with col2:
    st.header("第二列")
    st.write("这是第二列的内容")

# 7. 容器 (container)
with st.container():
    st.write("这是一个容器")
    st.write("容器内的所有元素都会被组合在一起")

# 8. 进度和状态
# 进度条
progress_bar = st.progress(0)
for i in range(100):
    progress_bar.progress(i + 1)

# 状态消息
st.success("成功消息")
st.error("错误消息")
st.warning("警告消息")
st.info("提示消息")

# 9. 缓存数据
@st.cache_data
def load_data():
    # 这个函数的结果会被缓存
    return pd.read_csv("large_file.csv")

# 10. Session State
if 'count' not in st.session_state:
    st.session_state.count = 0

if st.button('计数器'):
    st.session_state.count += 1

st.write('计数:', st.session_state.count)

# 11. 选项卡
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])
with tab1:
    st.header("Tab 1")
    st.image("image.png")
with tab2:
    st.header("Tab 2")
    st.image("image.png")

# 12. 展开/折叠区域
with st.expander("点击展开详情"):
    st.write("这里是详细内容")
    st.image("image.png")

# 13. 表单提交
with st.form("my_form"):
    st.write("表单")
    cols = st.columns([1, 1, 1])  # 在表单内部创建列
    with cols[0]:
        name = st.text_input("姓名")
    with cols[1]:
        age = st.number_input("年龄", min_value=0, max_value=100)
    with cols[2]:
        gender = st.selectbox("性别", ["男", "女"])
    submitted = st.form_submit_button("提交")

# 或者方法2：使用表单内的其他布局方式
with st.form("my_form2"):
    st.write("表单")
    # 使用两行布局
    name = st.text_input("姓名")
    age = st.number_input("年龄", min_value=0, max_value=100)
    submitted = st.form_submit_button("提交")
    
    # 注意：这部分逻辑最好放在表单外部
    if submitted:
        # 验证输入
        if not name:
            st.error("请输入姓名")
        else:
            # 处理表单数据
            st.success(f"表单已提交！姓名：{name}，年龄：{age}")
            
            # 可以在这里添加数据处理逻辑
            # 例如：保存到数据库
            save_data = {
                "name": name,
                "age": age,
                "timestamp": time.time()
            }
            
            # 显示结果
            st.write("提交的数据：", save_data)
            
            # 可以清除表单（通过session_state）
            if 'name' in st.session_state:
                del st.session_state.name

# 14. 空白区域 (empty)
placeholder = st.empty()
# 稍后可以替换内容
placeholder.text("这是新内容")

# 15. 分栏布局示例
st.title("分栏布局示例")

# 创建三列
left_col, middle_col, right_col = st.columns(3)

# 左列内容
with left_col:
    st.header("左侧")
    st.write("左侧内容")
    st.button("左侧按钮")

# 中间列内容
with middle_col:
    st.header("中间")
    st.write("中间内容")
    st.select_slider("滑块", options=["1", "2", "3"])

# 右列内容
with right_col:
    st.header("右侧")
    st.write("右侧内容")
    st.metric(label="温度", value="24°C", delta="-1.2°C")

# 16. 嵌套布局示例
st.title("嵌套布局示例")

# 外层列
col1, col2 = st.columns([2, 1])

with col1:
    st.header("主要内容区")
    # 内层列
    subcol1, subcol2 = st.columns(2)
    with subcol1:
        st.write("子列1")
    with subcol2:
        st.write("子列2")

with col2:
    st.header("侧边内容")
    st.write("辅助信息")