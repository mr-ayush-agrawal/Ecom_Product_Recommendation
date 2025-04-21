# Making a streamlit app

import streamlit as st
from src.NewUser import new_user_recommendation
from src.ExistingUser import existing_user_recomendation
from src.Utils import display_grid, get_products_list

st.title('Product Recommendation')

user_type = st.selectbox('Select User Type', ['New User', 'Existing User'])
num_recommendation = st.slider('Select Number of products to recommend', 5, 20)

if user_type == 'New User':
    if st.button("Recommend"):
        
        result = new_user_recommendation(n = num_recommendation)    
        st.header ('Recomendation Resutls')

        st.subheader("Top Rated : ")
        columns = st.columns(3)
        display_grid(result['top_rated'].values.tolist(), columns) 
        st.subheader("Most Rated : ")
        columns = st.columns(3)
        display_grid(result['most_rated'].values.tolist(), columns) 

elif user_type == 'Existing User':
    
    all_products = get_products_list()

    # Initialize session state to store selected products and ratings
    if 'product_ratings' not in st.session_state:
        st.session_state.product_ratings = {}
    if 'temp_product' not in st.session_state:
        st.session_state.temp_product = all_products[0]
    if 'temp_rating' not in st.session_state:
        st.session_state.temp_rating = 5  # default rating

    st.header("Rate Products")

    # Layout: 60% for product dropdown, 40% for rating
    col1, col2 = st.columns([3, 2])
    with col1:
        st.session_state.temp_product = st.selectbox(
            "Select a product",
            [p for p in all_products if p not in st.session_state.product_ratings],
            key="product_selector"
        )
    with col2:
        st.session_state.temp_rating = st.slider(
            "Rating (1-5)",
            min_value=1,
            max_value=5,
            key="rating_slider"
        )

    # Add button to save the selection
    if st.button("Add Rating"):
        product = st.session_state.temp_product
        rating = st.session_state.temp_rating
        st.session_state.product_ratings[product] = rating

    # Show current selections
    UserSelection = dict()
    if st.session_state.product_ratings:
        st.subheader("Your Ratings")
        for product, rating in st.session_state.product_ratings.items():
            st.write(f"**{product}**: {rating} ⭐")
            UserSelection[product] = rating


    if len(UserSelection) >= 1:
        if st.button('Recommend'):
            result= existing_user_recomendation(UserSelection, num_recommendation) 
            st.header ('Recomendation Resutls')

            columns = st.columns(3)
            display_grid(result, columns)

            # Clear the temp selections after recommendation
            st.session_state.temp_selections = []
            st.session_state.product_ratings = {}
    else :
        st.warning("Please rate at least one product before proceeding.")

