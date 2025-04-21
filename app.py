# Making a streamlit app

import streamlit as st
from src.NewUser import new_user_recommendation
from src.Utils import display_grid

# print(new_user_recommendation(n = 5))

st.title('Product Recommendation')

user_type = st.selectbox('Select User Type', ['New User', 'Existing User'])
num_recommendation = st.slider('Select Number of products to recommend', 5, 20)

st.header ('Recomendation Resutls')
if user_type == 'New User':
    result = new_user_recommendation(n = num_recommendation)    
    st.subheader("Top Rated : ")
    columns = st.columns(3)
    display_grid(result['top_rated'].values.tolist(), columns) 
    st.subheader("Most Rated : ")
    columns = st.columns(3)
    display_grid(result['most_rated'].values.tolist(), columns) 

elif user_type == 'Existing User':
    st.write(f"You selected Existing User. {num_recommendation}")