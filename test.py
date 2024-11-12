import streamlit as st
st.set_page_config(layout="wide")
from datetime import time, datetime
import numpy as np
from datetime import datetime, time, timedelta
import os
url_data = ''

from PIL import Image
import io

header_footer_css = """
    <style>
    .header {
      position: fixed;
        top: 0;
        left: 0;
        right: 0;
        background-color: #f1f1f1;
        color: black;
        text-align: center;
        padding: 10px;
        font-size: 20px;
        z-index: 10;
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f1f1f1;
        color: black;
        text-align: center;
        padding: 10px;
        font-size: 12px;
        z-index: 10;
    }
    .main-content {
        padding-top: 0px;  /* Space for header */
        padding-bottom: 40px; /* Space for footer */
    }
    </style>
"""

########################################################################### HEADER ##########################################################################################################

st.markdown(header_footer_css, unsafe_allow_html=True)
#st.markdown('<div class="header">Welcome to My Streamlit App</div>', unsafe_allow_html=True)


########################################################################### CONTENT ##########################################################################################################

st.sidebar.title("Menu")
page = st.sidebar.radio("Go to", ["Home", "Architecture" ,"Nowcast Portal", "Contact us"])

# Content for Page 1
if page == "Home":
    st.title("Convective Storm Nowcasting Using Machine Learning")

    st.header("Project Abstract")
    abstract = """
    This study investigates convective storm nowcasting using a CNN-based deep learning architecture, designed to predict storm occurrence probabilities. 
    The model utilizes a tabular dataset extracted from satellite observations between 2004 and 2022, in collaboration with the UK Centre for Ecology and Hydrology (UKCEH). 
    Key input features include time of observation, latitude, longitude, intensity, size, and the distance to the five nearest storms. 
    This research aims to provide timely storm predictions for urban areas in Africa, with a focus on improving public safety and disaster management. 
    Furthermore, a 2D wavelet transform is employed to enhance feature extraction, enabling the model to capture complex spatial and temporal relationships. 
    Future work will expand the model's capabilities by integrating additional data sources such as wind shear and soil moisture and exploring advanced architectures like Convolutional LSTM (ConvLSTM) networks. 
    This research contributes to the ongoing efforts in the field of storm nowcasting and aims to advance the accuracy and reliability of storm predictions.
    """
    st.success(abstract)

    st.image("./images/new-region.png", caption="Convective Storm Nowcasting Project", use_column_width=False)

    st.info(
        """
        **Goal**: To leverage information about the five nearest storms 
        (time of observation, latitude, longitude, size, distance) 
        to predict storm occurrences at different lead times using a CNN-based deep learning architecture.
        """)

    st.markdown('<div class="footer">&copy; 2024 Mendrika Rakotomanga. All Rights Reserved.</div>', unsafe_allow_html=True)

elif page == "Architecture":

    st.title("Convective Storm Nowcasting Using Machine Learning")
    st.header("Model Architecture")

    st.image("./images/lstm.png", caption="Convective Storm Nowcasting Project", use_column_width=False)

    st.markdown('<div class="footer">&copy; 2024 Mendrika Rakotomanga. All Rights Reserved.</div>', unsafe_allow_html=True)

elif page == "Nowcast Portal":
    st.title("Convective Storm Nowcasting Using Machine Learning")
    st.write("**Author**: Mendrika Rakotomanga, Douglas Parker, Nadhir B. Rached, Seonaid Anderson, Cornelia Klein")
    st.empty()

    observation, spacer, nowcast = st.columns([1, 0.5, 1])  # Adjust the width ratios as needed

    with observation:

        selected_date = st.date_input("Choose a date", datetime.today())
        current_time = datetime.now().time()
        selected_time = st.time_input("Choose a time")
        # Display selected time
        #st.write(f"Selected time: {selected_time.strftime('%H:%M')}")

        formatted_date = selected_date.strftime('%Y%m%d')
        formatted_time = selected_time.strftime('%H%M')

        input_t0 = f"Hist_cores_{formatted_date}{formatted_time}.nc"
        file_name_t0 = f"Hist_cores_{formatted_date}{formatted_time}.nc"

        #st.write(formatted_time)

        st.subheader("Latest Observation")
        slider1 = st.select_slider( "Select a time", options=[-120, -90, -60, -30, 0],  value=0 )
        st.write(f"Observation: t_0 - {slider1} min")

        image = Image.open("./images/full-input-202007011830(t0).png")
        st.image(image, caption=f"Observation at {slider1} minutes")

        img_buffer = io.BytesIO()
        image.save(img_buffer, format="PNG")
        img_buffer.seek(0)  # Reset buffer position to the beginning

        st.download_button(
        label="Download Image",  # Button label
        data=img_buffer,  # Image data
        file_name="downloaded_image.png",  # File name for the downloaded file
        mime="image/png"  # MIME type
)        

    with spacer:
        st.write("") 


    # Add a title and slider in the second column
    with nowcast:
        st.subheader("Nowcast")

        lead_time = st.select_slider( "Select a lead time", options=[1, 3],  value=1)
        st.write(f"Lead time: {lead_time} h")

        if lead_time == 1:            
            image = Image.open("./images/pred-202007011930(lt1).png")
            st.image(image, caption=f"{lead_time} hour lead time", width=370)

            img_buffer = io.BytesIO()
            image.save(img_buffer, format="PNG")
            img_buffer.seek(0)  # Reset buffer position to the beginning

            st.download_button(
                label="Download Image",  # Button label
                data=img_buffer,        # Image data
                file_name=f"nowcast-{lead_time}h-lead-time.png",  # File name for the downloaded file
                mime="image/png"  # MIME type
            )
        elif lead_time == 3:
            
            image = Image.open(f"./images/pred-202007012130(lt3).png")
            st.image(image, caption=f"{lead_time} hour lead time", width=370)

            img_buffer = io.BytesIO()
            image.save(img_buffer, format="PNG")
            img_buffer.seek(0)  # Reset buffer position to the beginning

            st.download_button(
                label="Download Image",  # Button label
                data=img_buffer,  # Image data
                file_name=f"nowcast-{lead_time}h-lead-time.png",  # File name for the downloaded file
                mime="image/png"  # MIME type
            )
    st.empty()  
    st.markdown('<div class="footer">&copy; 2024 Mendrika Rakotomanga. All Rights Reserved.</div>', unsafe_allow_html=True)
    
    
    st.warning("This is just an example from 2020-07-11 at 18:30 UTC.")

elif page == "Contact us":

    # Add a description or introduction
    st.write("Have questions or want to get in touch? Fill out the form below and we’ll get back to you as soon as possible.")

    # Create a form for the "Contact Us" page
    with st.form(key="contact_form"):
        # Input fields for name, email, and message
        name = st.text_input("Name", placeholder="Your full name")
        email = st.text_input("Email", placeholder="yourname@example.com")
        message = st.text_area("Message", placeholder="Type your message here")

        # Submit and Clear buttons
        submit_button = st.form_submit_button(label="Submit")
        clear_button = st.form_submit_button(label="Clear")

    # Handle form submission
    if submit_button:
        if name and email and message:
            st.success(f"Thank you for reaching out, {name}! We'll get back to you at {email} soon.")
        else:
            st.error("Please fill out all fields before submitting the form.")

    # Optional: Display a footer or additional information
    st.markdown("---")
    st.write("You can also reach us at [contact@example.com](mailto:contact@example.com) or call us at +123 456 7890.")

    st.empty()  
    st.markdown('<div class="footer">&copy; 2024 Mendrika Rakotomanga. All Rights Reserved.</div>', unsafe_allow_html=True)    
