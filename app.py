import streamlit as st
import pandas as pd

df=pd.read_csv('startup_funding.csv')
df['Investors Name']=df['Investors Name'].fillna('undisclosed')

st.sidebar.title('Startups Funding  Analysis')

option=st.sidebar.selectbox('Select One',['Overall Analysis','Startups','Investor'])


if(option=='Overall Analysis'):
    st.title('Overall Analysis')
elif(option=='Startups'):
    st.sidebar.selectbox('Select Startups',sorted(df['Startup Name'].unique().tolist()))
    btn1=st.sidebar.button('Find Startups Details')
    st.title('Startup Analysis')
else:
    st.sidebar.selectbox('select Startups',sorted(df['Investors Name'].unique().tolist()))
    btn2=st.sidebar.button('Find Startups Details')
    st.title('Investor Analysis')






