import os
import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']  # Mac OS的中文字体
# 或者使用
# plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows的中文字体
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


def load_data(file):
    """加载数据文件"""
    try:
        if file.name.endswith('.csv'):
            df = pd.read_csv(file)
        elif file.name.endswith(('.xls', '.xlsx')):
            df = pd.read_excel(file)
        return df
    except Exception as e:
        st.error(f"错误: {str(e)}")
        return None

def main():
    st.title("数据分析工具")
    # 文件上传
    col1, col2 = st.columns([1, 2])
    uploaded_file = col1.file_uploader("上传数据文件", type=['csv', 'xlsx', 'xls'])
    if os.path.exists("doc.md"):
        with open("doc.md", "r", encoding="utf-8") as f:
            col2.code(f.read())
    else:
        col2.code("doc.md 文件不存在")

    df = None
    if uploaded_file is not None:
        df = load_data(uploaded_file)
    else:
        default_file = os.path.expanduser("~/Downloads/学生成绩.xlsx")
        if os.path.exists(default_file):
            df = pd.read_excel(default_file)
        else:
            st.error(f"Error: {default_file} not found")
    if df is not None:
        # 显示基本信息
        st.header("数据概览")
        st.write("数据形状:", df.shape)
        
        # 数据预览
        st.subheader("数据预览")
        st.dataframe(df.head())
        
        # 数据类型信息
        st.subheader("数据类型信息")
        st.write(df.dtypes)
        
        # 基本统计信息
        st.subheader("基本统计信息")
        st.write(df.describe())
        
        # 缺失值分析
        st.subheader("缺失值分析")
        missing_data = df.isnull().sum()
        st.write(missing_data[missing_data > 0])
        
        # 可视化部分
        st.header("数据可视化")
        
        # 选择要可视化的列
        numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
        categorical_columns = df.select_dtypes(include=['object']).columns
        
        # 直方图
        st.subheader("直方图")
        hist_column = st.selectbox("选择要显示直方图的列", numeric_columns)
        fig = px.histogram(df, x=hist_column)
        st.plotly_chart(fig)
        
        # 箱型图
        st.subheader("箱型图")
        box_column = st.selectbox("选择要显示箱型图的列", numeric_columns)
        fig = px.box(df, y=box_column)
        st.plotly_chart(fig)
        
        # 散点图
        if len(numeric_columns) >= 2:
            st.subheader("散点图")
            col1, col2 = st.columns(2)
            with col1:
                x_column = st.selectbox("选择X轴", numeric_columns)
            with col2:
                y_column = st.selectbox("选择Y轴", numeric_columns)
            
            color_column = st.selectbox("选择颜色分类列（可选）", 
                                        ['None'] + list(categorical_columns))
            
            if color_column == 'None':
                fig = px.scatter(df, x=x_column, y=y_column)
            else:
                fig = px.scatter(df, x=x_column, y=y_column, color=color_column)
            st.plotly_chart(fig)
        
        # 相关性分析
        st.subheader("相关性分析")
        corr = df[numeric_columns].corr()
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
        st.pyplot(fig)
        
        # 数据导出
        st.header("数据导出")
        if st.button("导出处理后的数据"):
            df.to_csv('processed_data.csv', index=False)
            st.success("数据已导出到 processed_data.csv")

main()
