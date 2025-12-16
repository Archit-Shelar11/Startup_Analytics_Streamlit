# Import required libraries
import streamlit as st
import pandas as pd
import time

# App title
st.title("StartUp Dashboard")

# App header
st.header("Case Study on Indian Startup Funds")

# Simple text
st.write("This is the paragraph")

# Markdown heading
st.markdown("### Land of Startups — *India*")

# Display code block
st.code("""
def fun():
    print("Hello World")
""")

# Display LaTeX equation
st.latex("x^2 + y + c = 0")

# Sample DataFrame
df = pd.DataFrame({
    'Name': ['Archit', 'Shrwan', 'Siddesh', 'Yuvraj'],
    'IQ': [100, 99, 99, 100],
    'Branch': ['RAI', 'RAI', 'Manu', 'Ele']
})

# Show DataFrame
st.dataframe(df)

# Display metric
st.metric("Revenue", "₹3L", "3%")

# Display image
st.image("demo.webp")

# Sidebar title
st.sidebar.title("Title of Sidebar")

# Create two columns
col1, col2 = st.columns(2)

# Column 1 content
with col1:
    st.write("This is column 1")

# Column 2 content
with col2:
    st.write("This is column 2")

# Alert messages
st.error("Login Failed")
st.success("Login Successful")
st.info("Please check profile")
st.warning("This is a warning")

# User input fields
email = st.text_input("Enter your email")
age = st.number_input("Enter age", min_value=0, step=1)
gender = st.selectbox("Select gender", ["Male", "Female"])

# Login button
btn = st.button("Do Login")

# Login validation
if btn:
    if email == "archit@gmail.com" and age == 18:
        st.balloons()
    else:
        st.error("Invalid credentials")

# CSV file uploader
file = st.file_uploader("📁 Upload CSV File", type=["csv"])

# Process uploaded CSV
if file is not None:
    uploaded_df = pd.read_csv(file)
    st.subheader("Uploaded Data")
    st.dataframe(uploaded_df)
    st.subheader("Statistics")
    st.dataframe(uploaded_df.describe(include="all"))
