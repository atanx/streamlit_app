
import streamlit as st
import graphviz

def plot_graph():
    # Create a graphlib graph object
    graph = graphviz.Digraph(node_attr={"shape": "box"})
    graph.edge("run", "intr")
    graph.edge("intr", "runbl")
    graph.edge("runbl", "run")
    graph.edge("run", "kernel")
    graph.edge("kernel", "zombie")
    graph.edge("kernel", "sleep")
    graph.edge("kernel", "runmem")
    graph.edge("sleep", "swap")
    graph.edge("swap", "runswap")
    graph.edge("runswap", "new")
    graph.edge("runswap", "runmem")
    graph.edge("new", "runmem")
    graph.edge("sleep", "runmem")

    st.graphviz_chart(graph)

def plot_graph_from_content(content):
    graph = graphviz.Digraph()
    for line in content.split("\n"):
        if line.strip():
            parts = line.split(" ") # 分割成两部分
            if len(parts) == 2:
                graph.edge(parts[0], parts[1])
    st.graphviz_chart(graph)



col1, col2 = st.columns(2)
with col1:
    st.write("输入内容")
    content = st.text_area("输入内容", """
run intr
intr runbl
runbl run
run kernel
kernel zombie
kernel sleep
sleep swap
swap runswap
runswap new
runswap runmem
new runmem
sleep runmem
kernel runmem
""", height=500)
with col2:
    st.write("绘制图表")
    plot_graph_from_content(content)

plot_graph()