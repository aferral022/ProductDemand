import streamlit as st
import pandas as pd 
import numpy as np 


# Define the pages
main_page = st.Page('home.py', title="Home")
page_2 = st.Page('forecast.py', title="Product Demand Forecast")
page_3 = st.Page('resume.py', title="Resume")
page_4 = st.Page('projects.py', title='Projects')

# Set up navigation
pg = st.navigation([main_page, page_2, page_3, page_4])

# Run the selected page
pg.run()

