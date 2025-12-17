import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout='wide',page_title='startUp Analysis')

df = pd.read_csv('startup_funding_clean.csv')

df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['year'] = df['date'].dt.year

df['month']=df['date'].dt.month

temp_df=df.groupby(['year','month'])['amount'].sum().reset_index()
temp_df['X-axis']=temp_df['month'].astype('str')+'-'+temp_df['year'].astype('str')  






def load_investor_details(investor):
    st.title(investor)

    filtered_df = df[df['investors'].str.contains(investor, na=False)]

    last5_df = filtered_df.sort_values(
        'date', ascending=False
    )[['date','startup','vertical','city','round','amount']].head()

    st.subheader('Recent Investments')
    st.dataframe(last5_df)

    big_series = (
        filtered_df
        .groupby('startup')['amount']
        .sum()
        .sort_values(ascending=False)
    )


    st.dataframe(big_series)



    col1,col2=st.columns(2)

    with col1:
        fig, ax = plt.subplots()
        ax.bar(big_series.index, big_series.values)
        st.subheader('Biggest Investments')
        st.pyplot(fig)

    with col2:
        vertical_series=df[df['investors'].str.contains(investor,na=False)].groupby('vertical')['amount'].sum()
        fig1,ax1=plt.subplots()
        st.subheader('sectors Invested') 
        ax1.pie(vertical_series,labels=vertical_series.index,autopct='%0.01f%%')

        st.pyplot(fig1)

    col3,col4=st.columns(2)
    with col3:
       city_series= df[df['investors'].str.contains(investor,na=False)].groupby('city')['amount'].sum()
       fig3,ax3=plt.subplots()
       st.subheader('city Invested') 
       ax3.pie(city_series,labels=city_series.index,autopct='%0.01f%%')
       st.pyplot(fig3)

    with col4:
       year_series= df[df['investors'].str.contains(investor,na=False)].groupby('year')['amount'].sum()
       fig4,ax4=plt.subplots()
       st.subheader('YoY Investment') 
       ax4.plot(year_series.index,year_series.values)
       st.pyplot(fig4)

    



def load_Overall_Analysis():
    total= round(df['amount'].sum())
    col1,col2,col3,col4=st.columns(4)
    with col1:
     st.metric('Total',str(total)+' Crores')
    maxV=df.groupby('startup')['amount'].max().sort_values(ascending=False).head(1).values[0]
    with col2:
     st.metric('Max',str(maxV)+' Crores')
    avg=round(df.groupby('startup')['amount'].sum().mean())
    with col3:
       st.metric('Avg',str(avg)+ ' Crores')
    cnt=round(df['startup'].nunique())
    with col4:
       st.metric('Funded StartUps',str(cnt))


    st.header('MoM Graph')
    fig5,ax5=plt.subplots()
    st.subheader('Mom Investment') 
    ax5.plot(temp_df['X-axis'],temp_df['amount'])
    st.pyplot(fig5)
    
    



st.sidebar.title('Startup Funding Analysis')

option = st.sidebar.selectbox(
    'Select One',
    ['Overall Analysis','Startups','Investor']
)

if option == 'Overall Analysis':
    st.title('Overall Analysis')
    btn0=st.sidebar.button('Show Overall Analysis')
    if btn0:
        load_Overall_Analysis()


elif option == 'Startups':
    st.title('Startup Analysis')
    st.sidebar.selectbox(
        'Select Startup',
        sorted(df['startup'].dropna().unique().tolist())
    )

else:
    st.title('Investor Analysis')

    selected_investor = st.sidebar.selectbox(
        'Select Investor',
        sorted(
            set(
                df['investors']
                .dropna()
                .str.split(',')
                .sum()
            )
        )
    )

    if st.sidebar.button('Find Investor Details'):
        load_investor_details(selected_investor)
