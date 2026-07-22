import pandas as pd
import numpy as np


books = pd.read_csv('Books.csv')
users = pd.read_csv('Users.csv')
ratings = pd.read_csv('Ratings.csv')

book.head(1)

users.head(1)

ratings.head(1)

books

ratings

print(ratings.shape)






book.isnull().sum()

users.isnull().sum()

ratings.isnull().sum()


book.duplicated().sum()

ratings.duplicated().sum()

users.duplicated().sum()

# # popularity based recommendation system
# 

ratings.merge(books,on = 'ISBN')

rating_with_name = ratings.merge(books,on = 'ISBN')|

rating_with_name

num_rating_df = rating_with_name.groupby('Book-Title').count()['Book-Rating'].reset_index()

num_rating_df.rename(columns={'Book-Rating':'num_ratings'}, inplace=True)

num_rating_df

avg_rating_df = (
    rating_with_name
    .groupby('Book-Title')['Book-Rating']
    .mean()
    .reset_index()
)

avg_rating_df


avg_rating_df.rename(columns={'Book-Rating': 'avg_rating'}, inplace=True)

avg_rating_df

popular_df = num_rating_df.merge(avg_rating_df,on='Book-Title')
popular_df

popular_df[popular_df['num_ratings']>=250]

popular_df = popular_df[popular_df['num_ratings']>=250].sort_values('avg_rating',ascending = False).head(50)

popular_df = (
    popular_df
    .merge(books, on='Book-Title')
    .drop_duplicates('Book-Title')
    [['Book-Title', 'Book-Author', 'Publisher', 'Image-URL-M', 'num_ratings', 'avg_rating']]
)

popular_df

