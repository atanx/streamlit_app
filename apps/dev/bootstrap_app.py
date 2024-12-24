import streamlit as st

st.title("Bootstrap Playground")

col1, col2 = st.columns(2)

with col1:
    code = """<!DOCTYPE html>
<html>
<head>
  <title>Bootstrap5 实例</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link href="https://cdn.staticfile.net/twitter-bootstrap/5.1.1/css/bootstrap.min.css" rel="stylesheet">
  <script src="https://cdn.staticfile.net/twitter-bootstrap/5.1.1/js/bootstrap.bundle.min.js"></script>
</head>
<body>

<div class="container mt-3">
  <h3>模态框实例</h3>
  <p>点击按钮打开模态框</p>
  
  <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#myModal">
    打开模态框
  </button>
</div>

<!-- 模态框 -->
<div class="modal" id="myModal">
  <div class="modal-dialog">
    <div class="modal-content">

      <!-- 模态框头部 -->
      <div class="modal-header">
        <h4 class="modal-title">模态框标题</h4>
        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
      </div>

      <!-- 模态框内容 -->
      <div class="modal-body">
        模态框内容..
      </div>

      <!-- 模态框底部 -->
      <div class="modal-footer">
        <button type="button" class="btn btn-danger" data-bs-dismiss="modal">关闭</button>
      </div>

    </div>
  </div>
</div>

</body>
</html>   """
    code_input = st.text_area("")

@st.dialog("Cast your vote")
def vote(item):
    st.write(f"Why is {item} your favorite?")
    reason = st.text_input("Because...")
    if st.button("Submit"):
        st.session_state.vote = {"item": item, "reason": reason}
        st.rerun()
 
btn = st.button("show dialog")
if btn:
    vote("Python")

if 'vote' in st.session_state:
    st.write(f"You voted for {st.session_state.vote['item']} because {st.session_state.vote['reason']}")
     
with col2:
    if code:            
        st.html(code)
        pass
    else:
        st.write("No code provided")
