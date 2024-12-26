import streamlit as st

st.set_page_config(layout="wide")

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
dev_app_page = st.Page("apps/dev_app.py", title="HuggingFace", icon=":material/code:")
cheatsheet_app_page = st.Page("apps/cheatsheets/streamlit_cheatsheet_app.py", title="Streamlit Cheatsheet", icon=":material/code:")
swift_cheatshee_app_page = st.Page("apps/cheatsheets/swift_cheatsheet_app.py",  title="Swift Cheatsheet", icon=":material/code:")
bootstrap_app_page = st.Page("apps/dev/bootstrap_app.py", title="Bootstrap Playground", icon=":material/code:")
chat_bot_app_page = st.Page("apps/dev/chat_bot.py", title="Chat Bot", icon=":material/code:")
api_debugger_app_page = st.Page("apps/dev/api_debugger.py", title="API Debugger", icon=":material/code:")
awesome_app_page = st.Page("apps/awesome_app.py", title="Awesome Websites", icon=":material/code:")
nextjs_cheatsheet_app_page = st.Page("apps/cheatsheets/nextjs_cheatsheet_app.py", title="Next.js Cheatsheet", icon=":material/code:")
vue3_cheatsheet_app_page = st.Page("apps/cheatsheets/vue3_cheatsheet_app.py", title="Vue 3 Cheatsheet", icon=":material/code:")

gif_remove_bg_app_page = st.Page("apps/dev/gif_remove_bg_app.py", title="GIF Remove BG", icon=":material/code:")

if st.session_state.logged_in:
    pg = st.navigation(
        
        {
            "Dev": [dev_app_page, cheatsheet_app_page, swift_cheatshee_app_page, 
                    nextjs_cheatsheet_app_page, vue3_cheatsheet_app_page, bootstrap_app_page, chat_bot_app_page, 
                    api_debugger_app_page],
            "Tools": [data_analysis_app_page, graphviz_app_page, doc_viewer_app_page, gif_remove_bg_app_page],
            "Explore": [camera_app_page, fractal_app_page, awesome_app_page],
            "Account": [logout_page],
        }
    )
else:
    pg = st.navigation(
        {
            "Dev": [dev_app_page, cheatsheet_app_page, swift_cheatshee_app_page, 
                    nextjs_cheatsheet_app_page, vue3_cheatsheet_app_page, bootstrap_app_page, chat_bot_app_page, 
                    api_debugger_app_page],
            "Tools": [data_analysis_app_page, graphviz_app_page, doc_viewer_app_page, gif_remove_bg_app_page],
            "Explore": [camera_app_page, fractal_app_page, awesome_app_page],
            "Account": [login_page],
        })

st.logo("static/logo.png", size='large')
with st.sidebar:
    # st.title("Streamlit App")
    pass


pg.run()