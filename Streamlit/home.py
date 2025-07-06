import streamlit as st 


st.title("Andrea Ferral's DTSC 691  Capstone Project")

st.subheader('Introduction')

st.write('''Welcome to my page for my DTSC 691 Capstone project!''')
st.write('''My name is Andrea Ferral and I am completing my final course in Eastern University's MS in Data Science program. 
	I have a BS in Chemistry, but have always had a strong interest in math and data.''')  
st.write('''I have a seven year old son who keeps me very busy. When I am able to get a few minutes of free time, I enjoy crocheting and reading.
	My current crochet work-in-progress is a Minecraft blanket for my son.''')

st.subheader('Background')

st.write('''I earned my BS in Chemistry in December of 2007. In 2009, I started working as a purification technician for a biological laboratory in Allentown, PA.
	Over 15 years with the company, I worked up to Laboratory Manager.  Unfortunately, at the end of 2024, the site was closed, and operations were transferred to a
	site in Texas.  Luckily, a local supplier (and sometimes competitor) needed a laboratory manager for their Coopersburg, PA site. My previous employer
	recommended me for the position, and Lampire Biological Laboratories has employed me since late March 2025. I hope to utilize the skills I have learned 
	in the Data Science program to assist in identifying growth areas for both my site and the company.''')

st.subheader('Project Details')
st.write('''My project aims to construct a machine learning model for predicting customer-purchased products at Lampire Biological Laboratories’ 
	Coopersburg, PA, laboratory site. The current accounting and sales tracking software is Traverse, and, historically, it has proven difficult to gain 
	insights into order or product trends quickly. The project's goal is to predict product demand three months, six months, nine months, and twelve months 
	in the future.''')
st.write(''' On the Project Demand page, the user can select a specific product by using various drop-down boxes. Once a complete product description has been
	chosen, the user can choose the time period for the demand forecast. Following all selections, the forecasted demand, in liters, will be shown along with
	additional metrics for the selected product, broken down by fiscal year. Finally, a line plot will show the total volume sold per quarter. If there is more than
	one product code for the selected product description, both products will be separately shown on the graph.''')