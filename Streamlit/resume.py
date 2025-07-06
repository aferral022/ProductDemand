import streamlit as st
from PIL import Image

image = Image.open('photo.jpg')


st.image(image)
st.title('Andrea Ferral')



st.markdown(' ### Work Experience')
st.markdown(''' ##### **Lampire Biological Laboratories**''')
st.markdown(''' 
	 $~~~$ **March 2025 - Present**  
	   $~~~~~~$ **Laboratory Manager:**  Manage the laboratory and personnel at the Coopersburg, PA location.''')
st.markdown(''' ##### **Arista Biologicals, Inc.**  ''')
st.markdown('''	$~~~$ **April 2009 - December 2024**  
	$~~~~~~$ **Laboratory Manager:** Managed the QC and order fulfillment departments. ''')
st.markdown('### Education')
st.markdown(''' ##### Eastern University''')
st.markdown(''' $~~~$ **August 2023 - Present**  
	$~~~~~~$ **MS in Data Science**''')
st.markdown(''' ##### University of North Carolina-Pembroke ''')
st.markdown(''' $~~~$ **August 2006 - December 2007**  
	$~~~~~~$ **BS in Chemistry**''')
st.markdown(''' ##### Cedar Crest College''')
st.markdown(''' $~~~$ **August 2004 - May 2006**''')


st.markdown('''### Skills''')
col_1, col_2, col_3 = st.columns(3)

with col_1:
	st.markdown('''
	- Multitasking
	- Problem-solving
	- Attention to Detail''')
with col_2: 
	st.markdown(''' 
	- Protein Purifications  
	- Lateral Flow Assays  
	- Colloidal Gold Conjugation''')
with col_3: 
	st.markdown(''' 
	- Python  
	- Data Analysis  
	- Machine Learning''')