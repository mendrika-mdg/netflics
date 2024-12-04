import streamlit as st
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

st.set_page_config(
    page_title="Object-based Nowcasting",  # Set the title of the page
    page_icon="🌧️",               # Optional: Set an icon for the page
    layout="wide"                 # Optional: Choose layout ("centered" or "wide")
)



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

    Convective storm nowcasting plays a crucial role in early warning and mitigating the impact of severe weather. This study introduces a fast, simple, yet effective object-based approach using machine learning. 
    Storm objects are identified via a 2D wavelet transform on cloud-top temperature satellite data. Features such as time of observation ($t_0$), latitude, longitude, size, distance, and wavelet power of the five nearest storms to a given location are used to predict storm occurrence 1 to 6 hours ahead. 
    Initial results for Dakar outperformed an operational conditional climatology model for 1-, 3-, and 6-hour lead times. 
    Explainable AI techniques, such as Shapley values, were used to ensure the model’s predictions are meteorologically consistent. 
    The model was expanded to cover a larger region while maintaining the input structure. Additionally, modifications were made to include LSTMs for sequential storm information and convolutional layers for gridded nowcasting. 
    Performance, evaluated using the Fractions Skill Score (FSS), showed skill for 1- and 3-hour lead times.
    
    """
    st.success(abstract)

    st.image("./images/new-region.png", caption="Object-Based Approach to Convective Storm Nowcasting", use_column_width=False)

    st.info(
        """
        **Goal**: To use information about the five nearest storms 
        (time of observation, latitude, longitude, size, distance) 
        to predict storm occurrences at different lead times using a hybrid LSTM-CNN-based deep learning architecture.
        """)

    st.markdown('<div class="footer">&copy; 2024 Mendrika Rakotomanga. All Rights Reserved.</div>', unsafe_allow_html=True)

elif page == "Architecture":

    st.title("Convective Storm Nowcasting Using Machine Learning")
    st.header("Model Architecture")

    st.image("./images/lstm.png", caption="Model Architecture", use_column_width=False)

    st.markdown('<div class="footer">&copy; 2024 Mendrika Rakotomanga. All Rights Reserved.</div>', unsafe_allow_html=True)

elif page == "Nowcast Portal":
    st.title("Convective Storm Nowcasting Using Machine Learning")
    st.write("**Author**: Mendrika Rakotomanga, Douglas Parker, Nadhir B. Rached, Seonaid Anderson, Cornelia Klein")
    st.empty()

    observation, spacer, nowcast = st.columns([1, 0.5, 1])  # Adjust the width ratios as needed

    with observation:
        date_object = datetime(2020, 7, 11)
        selected_date = st.date_input("Choose a date", date_object)

        time_object = time(18, 30)
        current_time = datetime.now().time()
        selected_time = st.time_input("Choose a time", time_object)
        # Display selected time
        #st.write(f"Selected time: {selected_time.strftime('%H:%M')}")

        formatted_date = selected_date.strftime('%Y%m%d')
        formatted_time = selected_time.strftime('%H%M')

        input_t0 = f"Hist_cores_{formatted_date}{formatted_time}.nc"
        file_name_t0 = f"Hist_cores_{formatted_date}{formatted_time}.nc"

        #st.write(formatted_time)

        st.subheader("Latest Observation")
        slider1 = st.select_slider( "Select a time", options=[-120, -90, -60, -30, 0],  value=0 )
        #st.write(f"Observation: t_0 - {slider1} min")

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
    st.write("You can also reach us at [mmmhr@leeds.ac.uk](mailto:mmmhr@leeds.ac.uk)")

    st.empty()  
    st.markdown('<div class="footer">&copy; 2024 Mendrika Rakotomanga. All Rights Reserved.</div>', unsafe_allow_html=True)    
