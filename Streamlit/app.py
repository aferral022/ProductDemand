import streamlit as st
import pandas as pd 
import numpy as np 


# Define the pages
main_page = st.Page('home.py', title="Home")
page_2 = st.Page('forecast.py', title="Product Demand Forecast")

# Set up navigation
pg = st.navigation([main_page, page_2])

# Run the selected page
pg.run()

