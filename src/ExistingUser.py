import os
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from typing import Dict
import numpy as np

path = os.path.join(os.getcwd(), 'Data/Processed_matrix.csv')
matrix = pd.read_csv(path, index_col='UserId')

def __recommend_products(ratings_filled : pd.DataFrame, new_user_ratings, top_k=5, similar_users_n=5):
    """
    ratings_df: pd.DataFrame with UserID as index and ProductIDs as columns.
    new_user_ratings: dict, e.g., {'P1': 5, 'P3': 2}
    top_k: Number of products to recommend
    similar_users_n: Number of most similar users to consider
    """

    # Step 2: Create new user row
    new_user_vector = pd.Series(0, index=ratings_filled.columns)
    for product, rating in new_user_ratings.items():
        if product in new_user_vector:
            new_user_vector[product] = rating
    new_user_df = pd.DataFrame([new_user_vector], index=["new_user"])

    # Step 3: Compute cosine similarity
    all_users = pd.concat([ratings_filled, new_user_df])
    similarity = cosine_similarity(all_users)
    similarity_df = pd.DataFrame(similarity, index=all_users.index, columns=all_users.index)

    # Step 4: Get top N similar users to the new user
    similar_users = similarity_df["new_user"].drop("new_user").nlargest(similar_users_n)

    print(similar_users)

    # Step 5: Predict ratings
    weighted_ratings = np.dot(similar_users.values, ratings_filled.loc[similar_users.index])
    sim_sum = similar_users.sum()
    predicted_ratings = weighted_ratings / sim_sum

    # Step 6: Filter out already rated items
    predicted_ratings_series = pd.Series(predicted_ratings, index=ratings_filled.columns)
    for product in new_user_ratings.keys():
        predicted_ratings_series[product] = 0  # exclude already rated

    # Step 7: Return top K recommendations
    recommended = predicted_ratings_series.sort_values(ascending=False).head(top_k)
    return recommended.index.tolist()

def existing_user_recomendation(user_ratings : Dict, n : int):
    
    result = __recommend_products(
        ratings_filled=matrix, 
        new_user_ratings = user_ratings,
        top_k= n,
        similar_users_n=5
    )
    return result
