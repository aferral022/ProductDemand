import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


#Load Forecast DF
@st.cache_data
def load_csv ():
    df = pd.read_csv('forecast_final.csv')
    return df 
df = load_csv() 

@st.cache_data
def load_csv2 ():
    df2 = pd.read_csv('orders_per_fiscal.csv')
    return df2
df2 = load_csv2()

@st.cache_data
def load_csv3():
    df3 = pd.read_csv('volume_per_fiscal.csv')
    return df3
df3 = load_csv3()

def load_name():
    prod_name = pd.read_csv('prod_name.csv')
    return prod_name
prod_name = load_name()

def load_chart():
    chart_df = pd.read_csv('chart_df.csv')
    return chart_df
chart_df = load_chart()




#Product choices for Product Selectbox
st.title('Product Demand Forecast')

product = st.selectbox('Choose a product',
    options = df['Product'].drop_duplicates(),
    index=None,
    placeholder='Product')

#Product Type Select Box

product_filtered = df[df['Product'] == product]

if product:
    product_type = st.selectbox('Choose a product type',
    options = product_filtered['Product Type'].drop_duplicates(),
    index = None,
    placeholder = 'Product Type')

    type_filtered = product_filtered[product_filtered['Product Type']==product_type]

    if product_type:
        species = st.selectbox('Choose a species',
            options = type_filtered['Species'].drop_duplicates(),
            index = None, 
            placeholder = 'Species')

        species_filtered = type_filtered[type_filtered['Species']== species]

        if species:
            anticoag = st.selectbox('Choose an anticoagulant',
                options = species_filtered['Anticoagulant'].drop_duplicates(),
                index = None,
                placeholder = 'Anticoagulant')

            anticoag_filtered = species_filtered[species_filtered['Anticoagulant']==anticoag]

            if anticoag:     
                period = st.selectbox('Choose a future demand period',
                    options = ['3 MONTHS', '6 MONTHS', '9 MONTHS', '12 MONTHS'],
                    index = None)

                if period == '3 MONTHS':
                    demand = round(anticoag_filtered.loc[anticoag_filtered['Month']<'2025-08-01', 'Forecast'].sum(),3)
                elif period == '6 MONTHS':
                    demand = round(anticoag_filtered.loc[anticoag_filtered['Month']<'2025-10-01', 'Forecast'].sum(),3)
                elif period == '9 MONTHS':
                    demand = round(anticoag_filtered.loc[anticoag_filtered['Month']<'2026-01-01', 'Forecast'].sum(),3)
                else:
                    demand = round(anticoag_filtered['Forecast'].sum(),3)

                y = anticoag_filtered['Item ID'].unique()
                x= pd.Series(y)

                name = prod_name.loc[(prod_name['Item ID']==x.values[0]), 'Product Name'].iloc[0]

                if period:
                    st.write(f'The forecasted demand of {name} for the next {period} is {demand} liters.')

                    

                    fy2022 = (df2.loc[(df2['Item ID'].isin(x)) & (df2['Fiscal Year']== 2022)]['Number of Orders'].sum())
                    fy2023 = (df2.loc[(df2['Item ID'].isin(x)) & (df2['Fiscal Year']== 2023)]['Number of Orders'].sum())
                    fy2024 = (df2.loc[(df2['Item ID'].isin(x)) & (df2['Fiscal Year']== 2024)]['Number of Orders'].sum())
                    
                    fy2022 = int(fy2022)
                    fy2023 = int(fy2023)
                    fy2024 = int(fy2024)

                    delta_22_23 = (fy2023-fy2022)
                    delta_23_24 = (fy2024-fy2023)

                    st.subheader('Number of Orders')

                    col_fy22, col_fy23, col_fy24 = st.columns(3)

                    col_fy22.metric('Fiscal Year 2022', fy2022)
                    col_fy23.metric('Fiscal Year 2023', fy2023, delta=delta_22_23)
                    col_fy24.metric('Fiscal Year 2024', fy2024, delta=delta_23_24)

                    st.subheader('Total Volume (L)')

                    vol_22 = df3.loc[(df3['Item ID'].isin(x)) & (df3['Fiscal Year']==2022)]['Total Volume (L)'].sum()
                    vol_23 = df3.loc[(df3['Item ID'].isin(x)) & (df3['Fiscal Year']==2023)]['Total Volume (L)'].sum()
                    vol_24 = df3.loc[(df3['Item ID'].isin(x)) & (df3['Fiscal Year']==2024)]['Total Volume (L)'].sum()

                    vol_22 = round(float(vol_22),2)
                    vol_23 = round(float(vol_23),2)
                    vol_24 = round(float(vol_24),2)

                    vol_delta_22_23 = round(vol_23 - vol_22,2)
                    vol_delta_23_24 = round(vol_24 - vol_23,2)

                    col_vol_22, col_vol_23, col_vol_24 = st.columns(3)

                    col_vol_22.metric('Fiscal Year 2022', vol_22)
                    col_vol_23.metric('Fiscal Year 2023', vol_23, delta=vol_delta_22_23)
                    col_vol_24.metric('Fiscal Year 2024', vol_24, delta=vol_delta_23_24)


                    #Line graph for Volume sold per quarter for chosen product

                    z = chart_df[chart_df['Item ID'].isin(y)].sort_values('Quarter')

                    fig = px.line(z, x='Quarter', y='Volume (L)', color='Item ID')
                    fig.update_yaxes(rangemode='tozero')
                    
                    st.plotly_chart(fig)





