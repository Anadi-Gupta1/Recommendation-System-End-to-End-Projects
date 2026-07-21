# Recommendation System - End-to-End Projects

This repository contains comprehensive end-to-end implementation of various types of recommendation systems, including content-based filtering, collaborative filtering, and hybrid approaches.

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Repository Structure](#repository-structure)
- [Content-Based Recommendation System](#content-based-recommendation-system)
- [Collaborative Filtering](#collaborative-filtering)
- [Hybrid Recommendation Systems](#hybrid-recommendation-systems)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Project Phases](#project-phases)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Project Overview

This repository demonstrates the complete end-to-end development of recommendation systems, from data preprocessing to model implementation. The project covers three major approaches:

1. **Content-Based Filtering**: Recommends items based on feature similarity
2. **Collaborative Filtering**: Recommends items based on user behavior patterns
3. **Hybrid Systems**: Combines multiple approaches for improved recommendations

## 📁 Repository Structure

```
RECOMMENDATION SYSTEM/
├── Content based Recommendation system/
│   ├── PHASE 1/
│   │   ├── README.md                          # Detailed documentation
│   │   ├── notebooks_Movie-recommendation system_movie-recommendation syste.ipynb
│   │   ├── roughnotes.md                      # Implementation notes & debugging
│   │   ├── tmdb_5000_movies.csv              # Movie metadata dataset
│   │   └── tmdb_5000_credits.csv             # Cast and crew dataset
│   └── PHASE 2/
│       ├── Summary and errors.md              # Project summary
│       ├── roughnotes2.md                     # Additional notes
│       ├── handwritten notes.pdf             # Reference materials
│       ├── notebooks_Movie-recommendation system_movie-recommendation syste.ipynb
│       └── validation:corefeature notebook end to end working.ipynb
├── Collaborative filtering based/
│   └── (Placeholder for collaborative filtering implementation)
├── HYBRID/
│   ├── 2.1.1. Hybrid Recommendation Systems.pdf
│   ├── 2.1.2. Lab_ Designing a Hybrid Recommendation Systems.pdf
│   ├── 2.1.3. Lab_ Designing a Hybrid Collaborative Filtering Recommendation Systems.pdf
│   ├── 2.1.4. Lab_ Designing a Hybrid Knowledge-based Recommendation Systems.pdf
│   └── 2.1.6. Lab Solution_ Building a Neural Network Hybrid Recommendation System.pdf
└── README.md
```

## 🎬 Content-Based Recommendation System

### Overview
The content-based recommendation system suggests movies based on their features such as genres, keywords, cast, crew, and plot overview.

### Dataset
- **tmdb_5000_movies.csv**: Contains movie information including budget, genres, keywords, overview, popularity, production companies, release date, revenue, runtime, spoken languages, status, tagline, title, vote average, and vote count
- **tmdb_5000_credits.csv**: Contains cast and crew information for each movie including movie_id, title, cast details, and crew details
- **Dataset Size**: ~4,800 movies

### Features Used
1. **Genres**: Movie categories (Action, Adventure, Fantasy, Science Fiction, etc.)
2. **Keywords**: Plot-relevant terms and themes
3. **Cast**: Top 3 actors from the movie
4. **Crew**: Director of the movie
5. **Overview**: Plot summary and description

### Implementation Details

#### Data Preprocessing
1. **Data Merging**: Combined movies and credits datasets on the title field
2. **Missing Values**: Removed rows with null values in critical fields
3. **Duplicate Removal**: Eliminated duplicate entries
4. **Feature Selection**: Selected relevant columns (movie_id, title, overview, genres, keywords, cast, crew)

#### Text Processing
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

#### Key Functions
- `convert(obj)`: Extracts names from JSON arrays (used for genres and keywords)
- `convert3(obj)`: Extracts top 3 names from JSON arrays (used for cast)
- `fetch_director(obj)`: Extracts director name from crew JSON array

### How to Use

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

## 👥 Collaborative Filtering

This section is currently under development and will contain implementations of:
- User-based collaborative filtering
- Item-based collaborative filtering
- Matrix factorization techniques
- SVD (Singular Value Decomposition)

## 🔄 Hybrid Recommendation Systems

This folder contains educational resources and lab materials for designing and implementing hybrid recommendation systems:

- **2.1.1. Hybrid Recommendation Systems.pdf** - Introduction to hybrid recommendation systems concepts and architectures
- **2.1.2. Lab_ Designing a Hybrid Recommendation Systems.pdf** - Hands-on lab for designing hybrid recommendation systems
- **2.1.3. Lab_ Designing a Hybrid Collaborative Filtering Recommendation Systems.pdf** - Lab focused on hybrid collaborative filtering approaches
- **2.1.4. Lab_ Designing a Hybrid Knowledge-based Recommendation Systems.pdf** - Lab for knowledge-based hybrid recommendation systems
- **2.1.6. Lab Solution_ Building a Neural Network Hybrid Recommendation System.pdf** - Complete solution for building neural network-based hybrid recommendation systems

### Learning Objectives
- Understand different hybrid recommendation system architectures
- Learn to combine multiple recommendation approaches effectively
- Implement collaborative filtering hybrid systems
- Build knowledge-based hybrid recommenders
- Develop neural network-based hybrid recommendation systems

## �️ Installation & Setup

### Prerequisites
- Python 3.x
- Jupyter Notebook/JupyterLab
- Git

### Required Packages
```bash
pip install pandas numpy scikit-learn nltk
```

### Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd RECOMMENDATION\ SYSTEM
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch Jupyter Notebook**:
   ```bash
   jupyter notebook
   ```

4. **Navigate to the desired phase**:
   - For content-based filtering: `Content based Recommendation system/PHASE 1/`
   - For validation and advanced features: `Content based Recommendation system/PHASE 2/`

## 📖 Usage

### Running the Content-Based Recommendation System

1. Open `Content based Recommendation system/PHASE 1/notebooks_Movie-recommendation system_movie-recommendation syste.ipynb`
2. Execute cells sequentially to:
   - Load datasets
   - Preprocess data
   - Extract features
   - Create tags
   - Build recommendation model

### Running Validation Notebook

1. Open `Content based Recommendation system/PHASE 2/validation:corefeature notebook end to end working.ipynb`
2. This notebook contains the validated end-to-end implementation

### Accessing Learning Materials

Navigate to the `HYBRID` folder to access PDF learning materials for hybrid recommendation systems.

## 📊 Project Phases

### PHASE 1: Data Preprocessing & Feature Engineering
- Dataset loading and exploration
- Data cleaning and preprocessing
- Feature extraction from JSON fields
- Text processing and tag creation
- Basic recommendation pipeline setup

### PHASE 2: Validation & Advanced Features
- End-to-end validation of the recommendation system
- Error handling and debugging
- Performance optimization
- Advanced feature engineering
- Comprehensive documentation

## 🔧 Technologies Used

- **Python**: Core programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Scikit-learn**: Machine learning algorithms and metrics
- **Jupyter Notebook**: Interactive development environment
- **NLTK**: Natural language processing (for future enhancements)

## 📈 Future Enhancements

- Implement vectorization (TF-IDF or CountVectorizer)
- Add cosine similarity calculation
- Create a recommendation function that returns similar movies
- Build a user interface for movie recommendations
- Add evaluation metrics to assess recommendation quality
- Implement collaborative filtering algorithms
- Develop hybrid recommendation systems
- Add real-time recommendation capabilities
- Deploy as a web application (Streamlit/Flask)

## 🎓 Methodology

### Content-Based Filtering
Content-based filtering works by:
1. Analyzing the features of items (movies in this case)
2. Creating a profile for each item based on its features
3. Recommending items that are similar to items the user has liked in the past
4. Similarity is typically measured using cosine similarity between feature vectors

### Advantages
- No cold-start problem for new items
- Transparent recommendations (can explain why a movie was recommended)
- User independence (doesn't require other users' data)
- Can recommend niche items to users with specific tastes

### Limitations
- Limited content analysis (only uses provided features)
- No serendipity (recommends only similar items)
- Requires good feature extraction
- Over-specialization (recommends only items similar to what user already knows)

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Credits

- **Dataset**: TMDB (The Movie Database)
- **Implementation**: Based on content-based filtering principles and machine learning best practices
- **Learning Materials**: Hybrid recommendation system labs and tutorials

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Contact

For questions, suggestions, or issues, please open an issue in the repository.

---

**Note**: This repository is designed for educational purposes and demonstrates end-to-end implementation of various recommendation system approaches. The content-based filtering implementation is fully functional, while collaborative filtering and hybrid systems are in development.
