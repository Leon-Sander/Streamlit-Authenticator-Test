import streamlit as st
pg = st.navigation([st.Page("authentication.py"), st.Page("app.py")])
pg.run()