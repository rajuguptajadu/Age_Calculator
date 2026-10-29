import streamlit as st
st.image("logo-du.png", caption="LOGO of DU")
st.title("Welcome to the Delhi University")
st.title("Office of Procurement and Store")
st.text_input("Enter your Name")
st.text_input("Please Enter your email id")
st.file_uploader("Upload your file/folder here")
option = st.selectbox("How would you like to be contacted:?",("Email", "Home Phone","Mobile Phone"),)
st.write("you selected :", option)
st.link_button("Go to DU Website","https://du.ac.in")
st.title("My unique video")
st.video("https://youtu.be/7qWiLzxkJVU")
st.video("https://youtu.be/UzGhZKoHuyg")
st.video("https://youtu.be/7knTvH3pXxY")
st.video("https://youtu.be/S9C6l3a1SMU")
with st.sidebar:
    st.title("General Branch-II/सामान्य शाखा-2")
    st.markdown("Use these settings to update the main page dashboard views.")
    
    # User Input Widgets
    user_name = st.text_input("Enter your name:", placeholder="Raju Kumar Gupta")
    selected_metric = st.selectbox("Select Display Metric", ["Procurement", "Services", "Grievances"])
    chart_rows = st.slider("Number of Data Points", min_value=10, max_value=100, value=50)
    
    st.divider()
    st.caption("Room No. 209, General Branch-II,/n, New Administrative Block, University of Delhi")