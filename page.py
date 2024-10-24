import streamlit as st

# Sidebar menu for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Page 1", "Page 2"])

# Content for Page 1
if page == "Page 1":
    st.title("Welcome to Page 1")
    st.write("This is the content of Page 1.")
    st.write("Here, you can include text, widgets, and more.")
    
    # Add widgets to Page 1
    slider_value = st.slider("Page 1 Slider", min_value=0, max_value=100, value=50)
    st.write(f"Slider value: {slider_value}")

# Content for Page 2
elif page == "Page 2":
    st.title("Welcome to Page 2")
    st.write("This is the content of Page 2.")
    st.write("Feel free to add any additional content for this page.")

    # Add widgets to Page 2
    text_input = st.text_input("Enter some text for Page 2:")
    st.write(f"You entered: {text_input}")
