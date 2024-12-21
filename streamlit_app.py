import streamlit as st

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    st.title("Log in")
    st.write("Please enter your username and password to log in.")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Log in"):
        if username == "admin" and password == "password":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Invalid username or password. Please try again.")

def logout():
    if st.button("Log out"):
        st.session_state.logged_in = False
        st.rerun()

login_page = st.Page(login, title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
data_analysis_app_page = st.Page("apps/da_demo_app.py", title="Data Analysis", icon=":material/dashboard:", default=True)
graphviz_app_page = st.Page("apps/graphviz_app.py", title="Graphviz", icon=":material/bug_report:")
doc_viewer_app_page = st.Page( "apps/doc_viewer_app.py", title="Doc Viewer", icon=":material/notification_important:")
camera_app_page = st.Page("apps/cam_app.py", title="Camera", icon=":material/search:")
fractal_app_page = st.Page("apps/fractal_app.py", title="Fractal", icon=":material/history:")

if st.session_state.logged_in:
    pg = st.navigation(
        {
            "Tools": [data_analysis_app_page, graphviz_app_page, doc_viewer_app_page],
            "Explore": [camera_app_page, fractal_app_page],
            "Account": [logout_page],
        }
    )
else:
    pg = st.navigation(
        {
            "Tools": [data_analysis_app_page, graphviz_app_page, doc_viewer_app_page],
            # "Explore": [camera_app_page, fractal_app_page],
            "Account": [login_page],
        })

st.logo("static/logo.png", size='large')
with st.sidebar:
    st.title("Streamlit App")
pg.run()