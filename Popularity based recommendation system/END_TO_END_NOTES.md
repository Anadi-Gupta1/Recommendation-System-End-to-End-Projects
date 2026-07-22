# Popularity-Based Recommendation System - End-to-End Notes

## 1. Introduction

A popularity-based recommendation system is the simplest form of recommender system that suggests items based on their overall popularity among all users. Unlike collaborative filtering or content-based systems, it doesn't personalize recommendations but instead shows what's trending or highly rated by the general population.

### Key Characteristics
- **No personalization**: Same recommendations for all users
- **Cold-start resistant**: Works well even with new users/items
- **Simple to implement**: Basic statistical calculations
- **Scalable**: Computationally efficient

## 2. Dataset Overview

The book recommendation system uses three main datasets:

### Books.csv
- **ISBN**: Unique identifier for each book
- **Book-Title**: Name of the book
- **Book-Author**: Author name
- **Year-Of-Publication**: Publication year
- **Publisher**: Publishing company
- **Image-URL-S/M/L**: Small, medium, and large cover images

### Users.csv
- **User-ID**: Unique user identifier
- **Location**: User's geographical location
- **Age**: User's age (contains missing values)

### Ratings.csv
- **User-ID**: User who provided the rating
- **ISBN**: Book being rated
- **Book-Rating**: Rating value (0-10 scale)

## 3. Data Loading and Initial Exploration

```python
import pandas as pd
import numpy as np

# Load datasets
books = pd.read_csv('Books.csv')
users = pd.read_csv('Users.csv')
ratings = pd.read_csv('Ratings.csv')
```

### Dataset Statistics
- **Books**: 271,360 books
- **Ratings**: 1,149,780 ratings
- **Users**: User data with location and age information

## 4. Data Quality Assessment

### Missing Values Analysis
```python
# Check for null values
books.isnull().sum()
# Results: Book-Author (2), Publisher (2), Image-URL-L (3)

users.isnull().sum()
# Results: Age (110,762 missing values)

ratings.isnull().sum()
# Results: No missing values
```

### Duplicate Records Check
```python
books.duplicated().sum()    # 0 duplicates
ratings.duplicated().sum()  # 0 duplicates
users.duplicated().sum()    # 0 duplicates
```

## 5. Data Preprocessing

### Handling Data Type Warnings
The `Year-Of-Publication` column has mixed types, which triggers a DtypeWarning. This can be resolved by:
- Specifying dtype during import
- Setting `low_memory=False`
- Converting the column to appropriate type after loading

### Missing Values Strategy
- **Books**: Minimal missing values (2-3 records) - can be dropped or imputed
- **Users**: High missing values in Age column (110K+ records) - may need imputation or exclusion from analysis
- **Ratings**: No missing values - clean dataset

## 6. Building the Recommendation System

### Step 1: Merge Ratings with Book Information
```python
rating_with_name = ratings.merge(books, on='ISBN')
```
- **Purpose**: Add book details (title, author, etc.) to each rating
- **Join Key**: ISBN (common identifier)
- **Result**: 1,031,136 merged records (some ratings don't match books)

### Step 2: Calculate Number of Ratings per Book
```python
num_rating_df = rating_with_name.groupby('Book-Title').count()['Book-Rating'].reset_index()
num_rating_df.rename(columns={'Book-Rating': 'num_ratings'}, inplace=True)
```
- **Logic**: Count how many users rated each book
- **Grouping**: By Book-Title
- **Metric**: Total number of ratings per book
- **Result**: 241,071 unique books with rating counts

### Step 3: Calculate Average Rating per Book
```python
avg_rating_df = rating_with_name.groupby('Book-Title')['Book-Rating'].mean().reset_index()
avg_rating_df.rename(columns={'Book-Rating': 'avg_rating'}, inplace=True)
```
- **Logic**: Calculate mean rating for each book
- **Grouping**: By Book-Title
- **Metric**: Average rating (0-10 scale)
- **Result**: 241,071 unique books with average ratings

### Step 4: Combine Metrics
```python
popular_df = num_rating_df.merge(avg_rating_df, on='Book-Title')
```
- **Purpose**: Create single dataframe with both popularity metrics
- **Columns**: Book-Title, num_ratings, avg_rating
- **Result**: Combined dataset for filtering

## 7. Filtering Strategy

### Minimum Rating Threshold
```python
popular_df = popular_df[popular_df['num_ratings'] >= 250]
```
- **Rationale**: Filter out books with insufficient ratings
- **Threshold**: 250+ ratings (ensures statistical significance)
- **Result**: 186 books qualify
- **Why 250?**: Balances popularity with diversity - high enough to be meaningful but low enough to include popular books

### Sorting by Average Rating
```python
popular_df = popular_df.sort_values('avg_rating', ascending=False).head(50)
```
- **Logic**: Sort highest-rated books first
- **Limit**: Top 50 books
- **Result**: Most popular highly-rated books

## 8. Final Recommendation Preparation

### Add Book Details and Clean
```python
popular_df = popular_df.merge(books, on='Book-Title') \
    .drop_duplicates('Book-Title') \
    [['Book-Title', 'Book-Author', 'Publisher', 'Image-URL-M', 'num_ratings', 'avg_rating']]
```
- **Merge**: Add author, publisher, and image information
- **Drop Duplicates**: Remove duplicate book entries
- **Select Columns**: Keep only relevant display columns
- **Final Columns**: Title, Author, Publisher, Image, Rating Count, Average Rating

## 9. Top Recommendations

The system identifies popular books like:
1. **Harry Potter series** (multiple books in top 50)
2. **The Lord of the Rings** trilogy
3. **Classic literature**: To Kill a Mockingbird, 1984, The Catcher in the Rye
4. **Modern bestsellers**: The Da Vinci Code, The Lovely Bones
5. **Non-fiction**: Tuesdays with Morrie, Nickel and Dimed

## 10. Algorithm Summary

### Popularity Score Formula
```
Popularity = f(num_ratings, avg_rating)
```
Where:
- `num_ratings` ≥ 250 (minimum threshold)
- Sorted by `avg_rating` descending
- Top 50 books selected

### Advantages
- Simple and interpretable
- No cold-start problem
- Fast computation
- Works with sparse data

### Limitations
- No personalization
- Bias toward older books (more time to accumulate ratings)
- May not reflect current trends
- Doesn't account for user preferences

## 11. Implementation Best Practices

### Data Quality
- Always check for missing values and duplicates
- Handle data type warnings appropriately
- Validate merge operations

### Threshold Selection
- Choose rating threshold based on dataset size
- Too low: includes obscure books
- Too high: excludes good but less-rated books
- 250 is reasonable for this dataset (1M+ ratings)

### Performance Optimization
- Use groupby efficiently
- Merge on indexed columns for large datasets
- Consider sampling for exploratory analysis

## 12. Potential Improvements

### Weighted Rating System
Instead of simple average, use weighted rating:
```
Weighted Rating = (v/(v+m)) * R + (m/(v+m)) * C
```
Where:
- v = number of ratings
- m = minimum ratings required
- R = average rating
- C = mean rating across all books

### Time-Based Decay
Give more weight to recent ratings:
```
Decay Factor = e^(-λ * days_since_rating)
```

### Category-Based Popularity
Show popular books within specific genres or categories.

### Hybrid Approach
Combine popularity with collaborative filtering for personalized recommendations.

## 13. Deployment Considerations

### Real-Time Updates
- Precompute popularity scores periodically
- Update recommendations daily/weekly
- Cache results for fast serving

### Scalability
- For large datasets, use distributed computing (Spark)
- Implement batch processing for metric calculation
- Use database indexing for fast lookups

### User Interface
- Display book covers, ratings, and review counts
- Allow filtering by genre/author
- Show "Why recommended" explanation

## 14. Code Structure

```python
# Complete implementation
def build_popularity_recommender(ratings_path, books_path, min_ratings=250, top_n=50):
    """
    Build a popularity-based book recommendation system.
    
    Args:
        ratings_path: Path to ratings CSV
        books_path: Path to books CSV
        min_ratings: Minimum number of ratings to qualify
        top_n: Number of top recommendations to return
    
    Returns:
        DataFrame with top N popular books
    """
    # Load data
    ratings = pd.read_csv(ratings_path)
    books = pd.read_csv(books_path)
    
    # Merge ratings with book info
    rating_with_name = ratings.merge(books, on='ISBN')
    
    # Calculate metrics
    num_rating_df = rating_with_name.groupby('Book-Title').count()['Book-Rating'].reset_index()
    num_rating_df.rename(columns={'Book-Rating': 'num_ratings'}, inplace=True)
    
    avg_rating_df = rating_with_name.groupby('Book-Title')['Book-Rating'].mean().reset_index()
    avg_rating_df.rename(columns={'Book-Rating': 'avg_rating'}, inplace=True)
    
    # Combine and filter
    popular_df = num_rating_df.merge(avg_rating_df, on='Book-Title')
    popular_df = popular_df[popular_df['num_ratings'] >= min_ratings]
    popular_df = popular_df.sort_values('avg_rating', ascending=False).head(top_n)
    
    # Add book details
    popular_df = popular_df.merge(books, on='Book-Title') \
        .drop_duplicates('Book-Title') \
        [['Book-Title', 'Book-Author', 'Publisher', 'Image-URL-M', 'num_ratings', 'avg_rating']]
    
    return popular_df
```

## 15. Evaluation Metrics

### Offline Metrics
- **Coverage**: Percentage of books that can be recommended
- **Diversity**: Variety in recommendations
- **Novelty**: How new/discoverable the recommendations are

### Online Metrics
- **Click-through rate**: Users clicking on recommendations
- **Conversion rate**: Users purchasing/borrowing recommended books
- **User satisfaction**: Explicit feedback or ratings

## 16. Conclusion

The popularity-based recommendation system serves as an excellent baseline and fallback mechanism. While it lacks personalization, it's reliable, easy to implement, and provides value especially for new users. The key to success is choosing appropriate thresholds and continuously updating the popularity metrics to reflect current trends.

### Key Takeaways
1. Start with data quality assessment
2. Use meaningful thresholds for filtering
3. Combine multiple metrics (count + average)
4. Consider weighted scoring for better results
5. Update recommendations regularly
6. Use as baseline for more complex systems
