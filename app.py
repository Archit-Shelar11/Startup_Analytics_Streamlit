import streamlit as st
import pandas as pd
import time

st.title("StartUp Dashboard")
st.header("Case study on Indian Starup Funds")

st.write("This is the paragraph")

st.markdown(""" 
### Land Of startups 'The India'
""")

st.code(""" 
def fun():
        print("Hello World")
""")

st.latex(" x^2 +y +c=0")

df = pd.DataFrame({
    'Name': ['Archit','Shrwan','Siddesh','Yuvraj'],
    'IQ': [100, 99, 99, 100],
    'Branch': ['RAI','RAI','Manu','Ele']
})


st.dataframe(df)

st.metric('Revenue','Rs 3L','3%')

st.image("demeo.webp")

st.sidebar.title("Title of SideBar")

col1,col2= st.columns(2)

with col1:
    st.write("This is the column 1")

with col2:
    st.write('This is the column 2')


st.error('Login Failed')
st.success('Login Succesfull')
st.info('Please check Profile')
st.warning('This is the warning')

# bar=st.progress(0)

# for i in range(1,101):
#     time.sleep(0.1)
#     bar.progress(i)



email=st.text_input('Enter Your Email')
number=st.number_input('Enter Age')
gender=st.selectbox('Select the gender',['Male','Female'])

btn=st.button("Do Login")

if btn:
    if email=='archit@gmail.com' and number==18:
        st.balloons()
    else :
        st.error('Login Failed')


file =st.file_uploader('Upload Csv File')

if file is not None:
    df=pd.read_csv(file)
    st.dataframe(df.describe())
