# Content-Based Movie Recommendation System

A content-based recommendation system that suggests movies based on their features such as genres, keywords, cast, crew, and plot overview.

## Overview

This project implements a content-based filtering approach to recommend movies similar to a given movie. The system analyzes movie attributes and uses text processing techniques to create feature vectors that capture the essence of each film.

## Dataset

The system uses the TMDB (The Movie Database) dataset containing:

- **tmdb_5000_movies.csv**: Contains movie information including budget, genres, keywords, overview, popularity, production companies, release date, revenue, runtime, spoken languages, status, tagline, title, vote average, and vote count.
- **tmdb_5000_credits.csv**: Contains cast and crew information for each movie including movie_id, title, cast details, and crew details.

**Dataset Size**: ~4,800 movies

## Features Used

The recommendation system analyzes the following movie features:

1. **Genres**: Movie categories (Action, Adventure, Fantasy, Science Fiction, etc.)
2. **Keywords**: Plot-relevant terms and themes
3. **Cast**: Top 3 actors from the movie
4. **Crew**: Director of the movie
5. **Overview**: Plot summary and description

## Implementation Details

### Data Preprocessing

1. **Data Merging**: Combined movies and credits datasets on the title field
2. **Missing Values**: Removed rows with null values in critical fields
3. **Duplicate Removal**: Eliminated duplicate entries
4. **Feature Selection**: Selected relevant columns (movie_id, title, overview, genres, keywords, cast, crew)

### Text Processing

1. **JSON Parsing**: Converted JSON strings in genres, keywords, cast, and crew to Python lists
2. **Feature Extraction**:
   - Extracted genre names from genre objects
   - Extracted keyword names from keyword objects
   - Extracted top 3 actor names from cast objects
   - Extracted director name from crew objects
3. **Text Cleaning**:
   - Removed spaces from multi-word names (e.g., "Science Fiction" → "ScienceFiction")
   - Split overview text into individual words
   - Converted all text to lowercase
4. **Tag Creation**: Combined all processed features into a single "tags" column for each movie

### Key Functions

- `convert(obj)`: Extracts names from JSON arrays (used for genres and keywords)
- `convert3(obj)`: Extracts top 3 names from JSON arrays (used for cast)
- `fetch_director(obj)`: Extracts director name from crew JSON array

## Files Structure

```
Content based Recommendation system/
├── tmdb_5000_movies.csv              # Movie metadata dataset
├── tmdb_5000_credits.csv             # Cast and crew dataset
├── notebooks_Movie-recommendation system_movie-recommendation syste.ipynb  # Jupyter notebook with implementation
├── roughnotes.md                     # Project notes and documentation
└── README.md                         # This file
```

## How to Use

1. **Load the Datasets**:
   ```python
   import pandas as pd
   movies = pd.read_csv('tmdb_5000_movies.csv')
   credits = pd.read_csv('tmdb_5000_credits.csv')
   ```

2. **Merge and Preprocess**:
   ```python
   movies = movies.merge(credits, on='title')
   movies = movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]
   ```

3. **Apply Text Processing Functions**:
   ```python
   movies['genres'] = movies['genres'].apply(convert)
   movies['keywords'] = movies['keywords'].apply(convert)
   movies['cast'] = movies['cast'].apply(convert3)
   movies['crew'] = movies['crew'].apply(fetch_director)
   ```

4. **Create Tags**:
   ```python
   movies['tags'] = movies['overview'] + movies['keywords'] + movies['genres'] + movies['cast'] + movies['crew']
   new_df = movies[['movie_id', 'title', 'tags']]
   new_df['tags'] = new_df['tags'].apply(lambda x: " ".join(x)).apply(lambda x: x.lower())
   ```

## Requirements

- Python 3.x
- pandas
- numpy
- Jupyter Notebook (for running the notebook)

## Future Enhancements

- Implement vectorization (TF-IDF or CountVectorizer)
- Add cosine similarity calculation
- Create a recommendation function that returns similar movies
- Build a user interface for movie recommendations
- Add evaluation metrics to assess recommendation quality

## Methodology

Content-based filtering works by:
1. Analyzing the features of items (movies in this case)
2. Creating a profile for each item based on its features
3. Recommending items that are similar to items the user has liked in the past
4. Similarity is typically measured using cosine similarity between feature vectors

## Advantages

- No cold-start problem for new items
- Transparent recommendations (can explain why a movie was recommended)
- User independence (doesn't require other users' data)
- Can recommend niche items to users with specific tastes

## Limitations

- Limited content analysis (only uses provided features)
- No serendipity (recommends only similar items)
- Requires good feature extraction
- Over-specialization (recommends only items similar to what user already knows)

## Credits

- Dataset: TMDB (The Movie Database)
- Implementation based on content-based filtering principles
