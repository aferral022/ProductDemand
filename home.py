import streamlit as st 


st.title("Andrea Ferral's DTSC 691  Capstone Project")

st.subheader('Introduction')

st.write('''Welcome to my page for my DTSC 691 Capstone project!''')
st.write('''My name is Andrea Ferral and I am completing my final course in Eastern University's MS in Data Science program. 
	I have a BS in Chemistry, but have always had a strong interest in math and data.''')  
st.write('''I have a seven year old son who keeps me very busy. When I am able to get a few minutes of free time, I enjoy crocheting and reading.
	My current crochet work-in-progress is a Minecraft blanket for my son.''')

st.subheader('Project Details')
st.write('''My project aims to construct a machine learning model for predicting customer-purchased products at Lampire Biological Laboratories’ 
	Coopersburg, PA, laboratory site. The current accounting and sales tracking software is Traverse, and, historically, it has proven difficult to gain 
	insights into order or product trends quickly. The project's goal is to predict product demand three months, six months, nine months, and twelve months 
	in the future.''')
st.write(''' On the Project Demand page, the user can select a specific product by using various drop-down boxes. Once a complete product description has been
	chosen, the user can choose the time period for the demand forecast. Following all selections, the forecasted demand, in liters, will be shown along with
	additional metrics for the selected product, broken down by fiscal year. Finally, a line plot will show the total volume sold per quarter. If there is more than
	one product code for the selected product description, both products will be separately shown on the graph.''')
