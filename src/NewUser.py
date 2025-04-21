from typing import Dict
import pandas as pd
import os

def new_user_recommendation(n : int) -> Dict:
    '''
    Input :
        n : int -> Number of the products to be returned
    Return : 
        Dictonary of products in 2 category
        top_rated and most_rated : each with list of n products
    '''

    path = os.path.join(os.getcwd(), 'Data/Ranked_result.csv')
    df = pd.read_csv(path, index_col=0)
    
    # Already the data set is sorted according to Mean rating
    top_rated = df.head(n).index

    # Sorting accroding to most rated
    df = df.sort_values(['RatingCount', 'MeanRating'], ascending=[False, False])
    most_rated = df.head(n).index

    return {
        'top_rated' : top_rated,
        'most_rated' : most_rated
    }