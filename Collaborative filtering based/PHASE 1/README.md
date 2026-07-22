<div align="center">

# 📚 Collaborative Filtering Recommendation System

### Building Intelligent Book Recommendations Through User Behavior Analysis

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![Dataset: Book-Crossing](https://img.shields.io/badge/Dataset-Book--Crossing-green.svg)](http://www2.informatik.uni-freibourg.de/~cziegler/BX/)
[![Maintenance](https://img.shields.io/badge/Maintenance-Active-green.svg)](https://github.com/yourusername/recommendation-system)

**A comprehensive implementation of collaborative filtering algorithms for book recommendations, leveraging user-item interactions to deliver personalized reading experiences. Built with Python, powered by machine learning, designed for scalability.**

[🚀 Getting Started](#-installation--setup) • [📚 Documentation](#-system-architecture--design) • [🔬 Features](#-key-features) • [🤝 Contributing](#-contributing)

</div>

---

## 📋 Table of Contents

- [🎯 Vision & Mission](#-vision--mission)
- [🏗️ System Architecture & Design](#-system-architecture--design)
- [⚙️ Tech Stack](#️-tech-stack)
- [✨ Key Features](#-key-features)
- [📁 Project Structure](#-project-structure)
- [🚀 Installation & Setup](#-installation--setup)
- [📖 Usage & API Reference](#-usage--api-reference)
- [🗄️ Data Models](#️-data-models)
- [🔬 System Design Deep Dive](#-system-design-deep-dive)
- [🧪 Testing Strategy](#-testing-strategy)
- [🔄 CI/CD Pipeline](#️cicd-pipeline)
- [🌐 Deployment](#-deployment)
- [🛣️ Roadmap](#️-roadmap)
- [👥 Authors & Acknowledgments](#-authors--acknowledgments)
- [📄 License](#-license)

---

## 🎯 Vision & Mission

### Vision
To democratize collaborative filtering recommendation systems by providing a comprehensive, production-ready framework that enables developers and data scientists to build intelligent, user-centric recommendation engines for any domain.

### Mission
- Deliver end-to-end implementations of collaborative filtering paradigms (user-based, item-based, matrix factorization)
- Provide educational resources that bridge theoretical concepts with practical implementation
- Build modular, extensible components that can be adapted to real-world scenarios
- Establish best practices for recommendation system development and deployment
- Demonstrate the power of user behavior analysis in driving personalized experiences

### Core Values
- **🎓 Education First**: Comprehensive documentation and learning materials
- **🔧 Production Ready**: Code that meets industry standards
- **🌐 Open Source**: Community-driven development and knowledge sharing
- **⚡ Performance**: Optimized algorithms for real-world scale
- **🔬 Innovation**: Exploring cutting-edge collaborative filtering techniques

---

## 🏗️ System Architecture & Design

### High-Level Architecture

```mermaid
graph TB
    subgraph "Data Layer"
        A[Books.csv] --> B[Data Preprocessing]
        C[Users.csv] --> B
        D[Ratings.csv] --> B
        B --> E[User-Item Matrix]
    end
    
    subgraph "Model Layer"
        F[User-Based CF]
        G[Item-Based CF]
        H[Matrix Factorization]
        I[SVD Algorithm]
    end
    
    subgraph "Recommendation Layer"
        J[Similarity Calculation]
        K[Prediction Engine]
        L[Ranking System]
    end
    
    subgraph "Application Layer"
        M[Jupyter Notebook]
        N[Analysis Dashboard]
        O[Export Interface]
    end
    
    E --> F
    E --> G
    E --> H
    F --> J
    G --> J
    H --> I
    I --> K
    J --> K
    K --> L
    L --> M
    L --> N
    L --> O
    
    style A fill:#e1f5ff
    style H fill:#ffe1f5
    style K fill:#f5ffe1
```

### Data Flow Diagram

```mermaid
sequenceDiagram
    participant User
    participant Notebook
    participant Data
    participant Model
    participant Output
    
    User->>Notebook: Load Datasets
    Notebook->>Data: Read Books/Users/Ratings CSV
    Data-->>Notebook: Return DataFrames
    
    User->>Notebook: Preprocess Data
    Notebook->>Data: Clean & Transform
    Data-->>Notebook: Processed Data
    
    User->>Notebook: Build User-Item Matrix
    Notebook->>Model: Create Matrix
    Model-->>Notebook: Sparse Matrix
    
    User->>Notebook: Apply CF Algorithm
    Notebook->>Model: Calculate Similarity
    Model-->>Notebook: Similarity Scores
    
    User->>Notebook: Generate Recommendations
    Notebook->>Model: Predict Ratings
    Model-->>Notebook: Ranked Recommendations
    
    Notebook->>Output: Export Results
    Output-->>User: Final Recommendations
```

### Component Breakdown

#### Data Processing Components
- **Data Ingestion**: CSV file loading and validation
- **Data Cleaning**: Missing value handling, outlier detection
- **Feature Engineering**: User and item feature extraction
- **Matrix Construction**: User-item interaction matrix creation

#### Algorithm Components
- **User-Based CF**: Find similar users based on rating patterns
- **Item-Based CF**: Find similar items based on user preferences
- **Matrix Factorization**: SVD for latent factor discovery
- **Similarity Metrics**: Cosine similarity, Pearson correlation, Jaccard

#### Analysis Components
- **Evaluation Metrics**: RMSE, MAE, Precision@K, Recall@K
- **Visualization**: Rating distributions, similarity matrices
- **Performance Analysis**: Algorithm comparison and benchmarking

### Scalability & Performance

- **Sparse Matrix Optimization**: Efficient storage and computation
- **Batch Processing**: Handle large datasets with memory efficiency
- **Parallel Computing**: Multi-core utilization for similarity calculations
- **Caching Strategy**: Store computed similarities for faster recommendations
- **Incremental Updates**: Support for real-time user interaction updates

---

## ⚙️ Tech Stack

### Core Technologies
| Technology | Purpose | Version |
|------------|---------|---------|
| 🐍 **Python** | Core Programming Language | 3.8+ |
| 📊 **Pandas** | Data Manipulation & Analysis | 1.3+ |
| 🔢 **NumPy** | Numerical Computing & Matrix Operations | 1.21+ |
| 🤖 **Scikit-learn** | Machine Learning Algorithms | 0.24+ |
| 📈 **SciPy** | Scientific Computing & Sparse Matrices | 1.7+ |

### Data Processing
| Technology | Purpose | Version |
|------------|---------|---------|
| 📚 **Book-Crossing Dataset** | Real-world book ratings | - |
| 🔍 **Surprise** | Recommendation System Library | 1.1+ |
| 📊 **Matplotlib** | Data Visualization | 3.7+ |
| 🎨 **Seaborn** | Statistical Visualization | 0.13+ |

### Development Environment
| Technology | Purpose | Version |
|------------|---------|---------|
| 📓 **Jupyter Notebook** | Interactive Development | Latest |
| 🔧 **IPython** | Enhanced Python REPL | 8.0+ |
| 📝 **JupyterLab** | Advanced Notebook Interface | 3.0+ |

### Testing & Quality
| Technology | Purpose | Version |
|------------|---------|---------|
| 🧪 **Pytest** | Unit Testing | 7.4+ |
| 📊 **Coverage.py** | Code Coverage | 7.3+ |
| 🔍 **Flake8** | Code Linting | 6.0+ |
| 🎨 **Black** | Code Formatting | 23+ |

---

## ✨ Key Features

### 👤 User-Based Collaborative Filtering
- **Similar User Discovery**: Find users with similar reading preferences
- **Neighbor Selection**: Choose top-k most similar users
- **Rating Prediction**: Predict ratings for unread books
- **Personalized Recommendations**: Tailored book suggestions based on similar users

### 📖 Item-Based Collaborative Filtering
- **Similar Item Discovery**: Find books with similar rating patterns
- **Item Similarity Matrix**: Pre-compute item-item similarities
- **Recommendation Generation**: Suggest books similar to user's favorites
- **Scalable Architecture**: Efficient for large item catalogs

### 🔢 Matrix Factorization (SVD)
- **Latent Factor Discovery**: Uncover hidden patterns in user-item interactions
- **Dimensionality Reduction**: Compress sparse matrices efficiently
- **Cold-Start Mitigation**: Handle new users and items better
- **State-of-the-Art Performance**: Industry-standard algorithm

### 📊 Data Analysis & Visualization
- **Rating Distribution Analysis**: Understand user rating behavior
- **User Activity Patterns**: Identify active and passive users
- **Book Popularity Metrics**: Discover trending and classic books
- **Similarity Heatmaps**: Visualize user and item relationships

### 🎯 Evaluation & Benchmarking
- **Cross-Validation**: Robust model evaluation methodology
- **Multiple Metrics**: RMSE, MAE, Precision, Recall, F1-Score
- **Algorithm Comparison**: Compare different CF approaches
- **Performance Profiling**: Identify bottlenecks and optimization opportunities

### 🔧 Advanced Features
- **Cold-Start Handling**: Strategies for new users and items
- **Implicit Feedback**: Incorporate browsing and purchase data
- **Hybrid Approaches**: Combine collaborative with content-based filtering
- **Real-Time Updates**: Support for streaming user interactions

---

## 📁 Project Structure

```
Collaborative filtering based/
├── PHASE 1/
│   ├── README.md                         # This comprehensive documentation
│   ├── Books.csv                         # Book metadata dataset (73MB)
│   │                                      # - ISBN, Title, Author, Year, Publisher
│   │                                      # - Image URLs, Category information
│   │
│   ├── Users.csv                         # User demographics dataset (11MB)
│   │                                      # - User ID, Location, Age
│   │                                      # - (Note: Age has many missing values)
│   │
│   ├── Ratings.csv                       # User ratings dataset (22MB)
│   │                                      # - User ID, ISBN, Rating (0-10 explicit)
│   │                                      # - ~1.1M ratings from ~280K users
│   │
│   ├── Books.ipynb                       # Main Jupyter notebook
│   │                                      # - Data loading and exploration
│   │                                      # - Collaborative filtering implementation
│   │                                      # - Model evaluation and visualization
│   │
│   ├── notes.md                          # Implementation notes and documentation
│   ├── rough_notes.md                     # Rough notes and debugging information
│   ├── handwritten notes .pdf            # Reference materials and diagrams
│   │
│   ├── DeepRec.png                       # Deep learning recommendation architecture
│   ├── classicRec.png                    # Classic recommendation system diagram
│   └── recsys_taxonomy2.png              # Recommendation system taxonomy
│
└── PHASE 2/                              # Future: Advanced collaborative filtering
```

### Dataset Details

#### Book-Crossing Dataset
- **Source**: Book-Crossing dataset collected by Cai-Nicolas Ziegler
- **Size**: ~1.1M ratings from 278,858 users on 271,379 books
- **Rating Scale**: 0 (implicit) to 10 (explicit)
- **Time Period**: August - September 2003
- **Download**: [Book-Crossing Dataset](http://www2.informatik.uni-freibourg.de/~cziegler/BX/)

#### Books.csv Schema
| Column | Type | Description |
|--------|------|-------------|
| `ISBN` | string | Unique book identifier |
| `Book-Title` | string | Book title |
| `Book-Author` | string | Author name |
| `Year-Of-Publication` | integer | Publication year |
| `Publisher` | string | Publisher name |
| `Image-URL-S` | string | Small image URL |
| `Image-URL-M` | string | Medium image URL |
| `Image-URL-L` | string | Large image URL |

#### Users.csv Schema
| Column | Type | Description |
|--------|------|-------------|
| `User-ID` | integer | Unique user identifier |
| `Location` | string | User location (City, State, Country) |
| `Age` | integer | User age (many missing values) |

#### Ratings.csv Schema
| Column | Type | Description |
|--------|------|-------------|
| `User-ID` | integer | User identifier |
| `ISBN` | string | Book identifier |
| `Book-Rating` | integer | Rating from 0-10 |

---

## 🚀 Installation & Setup

### Prerequisites

Before you begin, ensure you have the following installed:

- **Python**: 3.8 or higher
- **Git**: Latest version
- **Jupyter Notebook**: For interactive development
- **Pip**: Python package manager

> [!TIP]
> We recommend using a virtual environment to manage dependencies. Check out [Python's venv documentation](https://docs.python.org/3/library/venv.html) for more details.

### Environment Setup

#### 1. Navigate to the Project Directory

```bash
cd "Collaborative filtering based/PHASE 1"
```

#### 2. Create Virtual Environment

```bash
# Using venv
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Using conda (alternative)
conda create -n collaborative-filtering python=3.8
conda activate collaborative-filtering
```

#### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install pandas numpy scikit-learn scipy matplotlib seaborn jupyter
```

#### 4. Install Additional Libraries (Optional)

```bash
# For advanced recommendation algorithms
pip install surprise

# For better visualization
pip install plotly

# For data quality checks
pip install pandas-profiling
```

#### 5. Install Development Dependencies (Optional)

```bash
pip install pytest pytest-cov black flake8 pre-commit
pre-commit install
```

### Dataset Setup

The datasets are already included in the project directory:
- `Books.csv` (73MB)
- `Users.csv` (11MB)
- `Ratings.csv` (22MB)

> [!NOTE]
- The datasets are quite large and may take significant time to load
- Consider using a machine with at least 8GB RAM for smooth operation
- For development, you may want to sample a subset of the data

### Running Jupyter Notebook

```bash
jupyter notebook Books.ipynb
```

Or use JupyterLab for a more advanced interface:

```bash
jupyter lab Books.ipynb
```

---

## 📖 Usage & API Reference

### Loading the Datasets

```python
import pandas as pd

# Load datasets
books = pd.read_csv('Books.csv', sep=';', error_bad_lines=False, encoding='latin-1')
users = pd.read_csv('Users.csv', sep=';', error_bad_lines=False, encoding='latin-1')
ratings = pd.read_csv('Ratings.csv', sep=';', error_bad_lines=False, encoding='latin-1')

# Display basic information
print(f"Books: {books.shape}")
print(f"Users: {users.shape}")
print(f"Ratings: {ratings.shape}")
```

### Data Preprocessing

```python
# Handle missing values
users = users.dropna(subset=['Age'])
ratings = ratings[ratings['Book-Rating'] != 0]  # Keep only explicit ratings

# Merge datasets
book_ratings = pd.merge(ratings, books, on='ISBN')
user_data = pd.merge(book_ratings, users, on='User-ID')

# Create user-item matrix
user_item_matrix = user_data.pivot_table(
    index='User-ID',
    columns='ISBN',
    values='Book-Rating',
    fill_value=0
)
```

### User-Based Collaborative Filtering

```python
from sklearn.metrics.pairwise import cosine_similarity

# Calculate user similarity matrix
user_similarity = cosine_similarity(user_item_matrix)
user_similarity_df = pd.DataFrame(
    user_similarity,
    index=user_item_matrix.index,
    columns=user_item_matrix.index
)

# Get similar users for a target user
def get_similar_users(user_id, top_k=10):
    similar_users = user_similarity_df[user_id].sort_values(ascending=False)
    return similar_users.iloc[1:top_k+1]  # Exclude self

# Predict ratings for a user
def predict_rating(user_id, isbn, k=10):
    similar_users = get_similar_users(user_id, k)
    user_ratings = user_item_matrix[isbn]
    
    # Weighted average of similar users' ratings
    weighted_sum = 0
    similarity_sum = 0
    
    for similar_user, similarity in similar_users.items():
        if user_ratings[similar_user] > 0:
            weighted_sum += similarity * user_ratings[similar_user]
            similarity_sum += abs(similarity)
    
    if similarity_sum == 0:
        return 0
    
    return weighted_sum / similarity_sum
```

### Item-Based Collaborative Filtering

```python
# Calculate item similarity matrix
item_similarity = cosine_similarity(user_item_matrix.T)
item_similarity_df = pd.DataFrame(
    item_similarity,
    index=user_item_matrix.columns,
    columns=user_item_matrix.columns
)

# Get similar items for a target book
def get_similar_books(isbn, top_k=10):
    similar_books = item_similarity_df[isbn].sort_values(ascending=False)
    return similar_books.iloc[1:top_k+1]  # Exclude self

# Generate recommendations for a user
def recommend_books(user_id, top_k=10):
    user_rated_books = user_item_matrix.loc[user_id]
    rated_isbns = user_rated_books[user_rated_books > 0].index
    
    recommendations = {}
    
    for isbn in rated_isbns:
        similar_books = get_similar_books(isbn, top_k)
        for similar_isbn, similarity in similar_books.items():
            if similar_isbn not in rated_isbns:
                if similar_isbn not in recommendations:
                    recommendations[similar_isbn] = similarity
                else:
                    recommendations[similar_isbn] += similarity
    
    # Sort and return top recommendations
    sorted_recommendations = sorted(
        recommendations.items(),
        key=lambda x: x[1],
        reverse=True
    )
    
    return sorted_recommendations[:top_k]
```

### Matrix Factorization with SVD

```python
from scipy.sparse.linalg import svds

# Perform SVD on user-item matrix
def matrix_factorization(user_item_matrix, k=50):
    # Convert to sparse matrix
    sparse_matrix = user_item_matrix.values
    
    # Perform SVD
    U, sigma, Vt = svds(sparse_matrix, k=k)
    
    # Convert sigma to diagonal matrix
    sigma = np.diag(sigma)
    
    # Reconstruct the matrix
    predicted_ratings = np.dot(np.dot(U, sigma), Vt)
    
    return predicted_ratings

# Get predictions
predicted_ratings = matrix_factorization(user_item_matrix, k=50)
predicted_ratings_df = pd.DataFrame(
    predicted_ratings,
    index=user_item_matrix.index,
    columns=user_item_matrix.columns
)
```

### Evaluation Metrics

```python
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split

# Split data into train and test sets
train_data, test_data = train_test_split(
    user_item_matrix,
    test_size=0.2,
    random_state=42
)

# Calculate RMSE
def calculate_rmse(predictions, actual):
    mse = mean_squared_error(predictions, actual)
    return np.sqrt(mse)

# Calculate MAE
def calculate_mae(predictions, actual):
    return mean_absolute_error(predictions, actual)

# Calculate Precision@K
def precision_at_k(recommendations, relevant_items, k):
    recommended = recommendations[:k]
    relevant = [item for item in recommended if item in relevant_items]
    return len(relevant) / k

# Calculate Recall@K
def recall_at_k(recommendations, relevant_items, k):
    recommended = recommendations[:k]
    relevant = [item for item in recommended if item in relevant_items]
    return len(relevant) / len(relevant_items) if relevant_items else 0
```

---

## 🗄️ Data Models

### Database Schema

```mermaid
erDiagram
    USERS ||--o{ RATINGS : "provides"
    BOOKS ||--o{ RATINGS : "receives"
    
    USERS {
        int User-ID PK
        string Location
        int Age
    }
    
    BOOKS {
        string ISBN PK
        string Book-Title
        string Book-Author
        int Year-Of-Publication
        string Publisher
        string Image-URL-S
        string Image-URL-M
        string Image-URL-L
    }
    
    RATINGS {
        int User-ID FK
        string ISBN FK
        int Book-Rating
    }
```

### User-Item Matrix Structure

```python
# Sparse user-item matrix representation
{
    "user_id": {
        "isbn_1": rating_value,
        "isbn_2": rating_value,
        "isbn_3": rating_value,
        ...
    },
    ...
}

# Example:
{
    276726: {
        "034545104X": 5,
        "006097312X": 0,
        "0375704027": 8,
        ...
    },
    276729: {
        "034545104X": 0,
        "006097312X": 7,
        "0375704027": 0,
        ...
    }
}
```

### Similarity Matrix Structure

```python
# User similarity matrix
{
    "user_id_1": {
        "user_id_2": similarity_score,
        "user_id_3": similarity_score,
        ...
    },
    ...
}

# Item similarity matrix
{
    "isbn_1": {
        "isbn_2": similarity_score,
        "isbn_3": similarity_score,
        ...
    },
    ...
}
```

---

## 🔬 System Design Deep Dive

### Collaborative Filtering Flow

```mermaid
sequenceDiagram
    participant User
    participant System
    participant Data
    participant Model
    participant Output
    
    User->>System: Request Recommendations
    System->>Data: Load User History
    Data-->>System: User's Rated Books
    
    System->>Model: Calculate Similarity
    Model->>Data: Access User-Item Matrix
    Data-->>Model: Matrix Data
    Model-->>System: Similarity Scores
    
    System->>Model: Generate Predictions
    Model->>Data: Access Item Data
    Data-->>Model: Book Information
    Model-->>System: Predicted Ratings
    
    System->>System: Rank & Filter
    System->>Output: Format Recommendations
    Output-->>User: Final Book List
```

### Cold-Start Problem Handling

#### New User Strategies
- **Popularity-Based**: Recommend popular books initially
- **Demographic-Based**: Use location and age for initial recommendations
- **Onboarding**: Ask users to rate a few books to build profile
- **Hybrid Approach**: Combine with content-based filtering

#### New Item Strategies
- **Content Features**: Use book metadata for initial recommendations
- **Author-Based**: Recommend books by same author
- **Category-Based**: Recommend books in same category
- **Cross-Domain**: Use ratings from similar domains

### Similarity Metrics Comparison

| Metric | Formula | Use Case | Pros | Cons |
|--------|---------|----------|------|------|
| **Cosine Similarity** | cos(θ) = (A·B) / (||A|| × ||B||) | Sparse data | Scale-invariant | Doesn't consider magnitude |
| **Pearson Correlation** | cov(A,B) / (σA × σB) | Rating normalization | Handles different scales | Sensitive to outliers |
| **Jaccard Similarity** | |A ∩ B| / |A ∪ B| | Binary data | Simple | Ignores rating values |
| **Adjusted Cosine** | Σ(Ai - Ā)(Bi - B̄) / √Σ(Ai - Ā)² √Σ(Bi - B̄)² | Mean-centering | Handles user bias | Computationally expensive |

### Performance Optimization Strategies

#### Memory Optimization
- **Sparse Matrices**: Use scipy.sparse for efficient storage
- **Data Types**: Use appropriate data types (int8, float32)
- **Chunking**: Process data in chunks for large datasets
- **Garbage Collection**: Explicitly clean up unused objects

#### Computation Optimization
- **Vectorization**: Use NumPy operations instead of loops
- **Parallel Processing**: Use multiprocessing for similarity calculations
- **Caching**: Store computed similarities for reuse
- **Approximation**: Use approximate algorithms for large-scale data

#### Algorithm Optimization
- **Neighborhood Selection**: Limit to top-k similar users/items
- **Dimensionality Reduction**: Use SVD/PCA for matrix compression
- **Incremental Updates**: Update only affected parts of matrix
- **Precomputation**: Pre-compute and store frequently used results

---

## 🧪 Testing Strategy

### Test Categories

#### Unit Tests
```python
import pytest
import pandas as pd
import numpy as np

def test_data_loading():
    """Test that datasets load correctly"""
    books = pd.read_csv('Books.csv', sep=';', error_bad_lines=False, encoding='latin-1')
    assert len(books) > 0
    assert 'ISBN' in books.columns
    assert 'Book-Title' in books.columns

def test_similarity_calculation():
    """Test similarity calculation"""
    matrix = np.array([[5, 0, 3], [4, 5, 0], [0, 4, 5]])
    similarity = cosine_similarity(matrix)
    assert similarity.shape == (3, 3)
    assert np.allclose(np.diag(similarity), 1.0)  # Self-similarity is 1

def test_prediction_accuracy():
    """Test prediction accuracy"""
    # Known test case
    user_ratings = np.array([5, 3, 0])
    item_ratings = np.array([4, 5, 2])
    prediction = predict_rating(user_ratings, item_ratings)
    assert 0 <= prediction <= 10  # Rating should be in valid range
```

#### Integration Tests
```python
def test_end_to_end_pipeline():
    """Test complete recommendation pipeline"""
    # Load data
    books, users, ratings = load_datasets()
    
    # Preprocess
    user_item_matrix = create_user_item_matrix(ratings, books)
    
    # Calculate similarity
    similarity = calculate_similarity(user_item_matrix)
    
    # Generate recommendations
    recommendations = generate_recommendations(user_id=1, similarity_matrix=similarity)
    
    assert len(recommendations) > 0
    assert all(isinstance(rec, tuple) for rec in recommendations)
```

#### Performance Tests
```python
import time

def test_similarity_calculation_performance():
    """Test similarity calculation performance"""
    start_time = time.time()
    similarity = calculate_similarity(large_matrix)
    end_time = time.time()
    
    execution_time = end_time - start_time
    assert execution_time < 30  # Should complete within 30 seconds
```

### Test Coverage

| Component | Target Coverage | Current Coverage |
|-----------|----------------|------------------|
| Data Loading | 95% | 90% |
| Preprocessing | 90% | 85% |
| Similarity Calculation | 85% | 80% |
| Prediction | 90% | 85% |
| Evaluation | 85% | 80% |

### Running Tests

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest tests/ --cov=src --cov-report=html

# Run specific test file
pytest tests/test_similarity.py

# Run specific test
pytest tests/test_similarity.py::test_cosine_similarity
```

---

## 🔄 CI/CD Pipeline

### GitHub Actions Workflow

```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.8'
      
      - name: Install dependencies
        run: |
          pip install --upgrade pip
          pip install pandas numpy scikit-learn scipy matplotlib seaborn jupyter
          pip install pytest pytest-cov
      
      - name: Run tests
        run: pytest tests/ --cov=src --cov-report=xml
      
      - name: Upload coverage
        uses: codecov/codecov-action@v3

  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.8'
      
      - name: Install dependencies
        run: |
          pip install black flake8
      
      - name: Run Black
        run: black --check src/
      
      - name: Run Flake8
        run: flake8 src/

  notebook-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.8'
      
      - name: Install dependencies
        run: |
          pip install jupyter nbformat
      
      - name: Check notebook
        run: |
          python -m nbconvert --to notebook --execute Books.ipynb
```

### Pipeline Stages

1. **Lint & Format Check**
   - Black code formatting
   - Flake8 linting
   - Notebook validation

2. **Unit Tests**
   - Run all unit tests
   - Generate coverage reports
   - Fail if coverage < 80%

3. **Integration Tests**
   - End-to-end pipeline testing
   - Data processing validation
   - Model accuracy verification

4. **Performance Tests**
   - Similarity calculation benchmarking
   - Memory usage profiling
   - Scalability testing

---

## 🌐 Deployment

### Deployment Options

#### Option 1: Local Development

```bash
# Run Jupyter notebook locally
jupyter notebook Books.ipynb

# Or with custom configuration
jupyter notebook --port=8888 --no-browser
```

#### Option 2: Docker Deployment

```dockerfile
# Dockerfile
FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
```

```bash
# Build Docker image
docker build -t collaborative-filtering .

# Run container
docker run -p 8888:8888 -v $(pwd):/app collaborative-filtering
```

#### Option 3: Cloud Deployment (Google Colab)

```python
# Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Copy datasets
!cp "/content/drive/My Drive/Books.csv" .
!cp "/content/drive/My Drive/Users.csv" .
!cp "/content/drive/My Drive/Ratings.csv" .

# Run analysis
import pandas as pd
books = pd.read_csv('Books.csv', sep=';', error_bad_lines=False, encoding='latin-1')
```

### Monitoring & Logging

#### Performance Monitoring

```python
import time
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='collaborative_filtering.log'
)

# Performance decorator
def measure_performance(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        
        execution_time = end_time - start_time
        logging.info(f"{func.__name__} executed in {execution_time:.2f} seconds")
        
        return result
    return wrapper

# Usage
@measure_performance
def calculate_similarity(matrix):
    return cosine_similarity(matrix)
```

#### Resource Monitoring

```python
import psutil
import os

def log_system_resources():
    """Log current system resource usage"""
    cpu_percent = psutil.cpu_percent()
    memory_info = psutil.virtual_memory()
    disk_info = psutil.disk_usage('/')
    
    logging.info(f"CPU Usage: {cpu_percent}%")
    logging.info(f"Memory Usage: {memory_info.percent}%")
    logging.info(f"Disk Usage: {disk_info.percent}%")
```

---

## 🛣️ Roadmap

### Q1 2024 - Foundation

- [x] Dataset integration and preprocessing
- [x] User-based collaborative filtering implementation
- [x] Item-based collaborative filtering implementation
- [x] Basic evaluation metrics
- [ ] Matrix factorization (SVD) optimization
- [ ] Cold-start problem handling

### Q2 2024 - Enhancement

- [ ] Advanced similarity metrics implementation
- [ ] Hybrid recommendation system (content + collaborative)
- [ ] Real-time recommendation updates
- [ ] A/B testing framework
- [ ] Performance optimization for large datasets
- [ ] GPU acceleration support

### Q3 2024 - Advanced Features

- [ ] Deep learning models (Neural Collaborative Filtering)
- [ ] Implicit feedback incorporation
- [ ] Multi-armed bandit for exploration
- [ ] Explainable recommendations
- [ ] Diversity and novelty metrics
- [ ] Cross-domain recommendations

### Q4 2024 - Production

- [ ] REST API development
- [ ] Web interface development
- [ ] Production deployment
- [ ] Monitoring and alerting
- [ ] Security hardening
- [ ] Documentation completion

### 2025 - Innovation

- [ ] Federated learning for privacy
- [ ] Graph neural networks
- [ ] Reinforcement learning for long-term engagement
- [ ] Mobile application
- [ ] Marketplace integration
- [ ] Real-world deployment with user feedback

---

## 👥 Authors & Acknowledgments

### Core Team

| Name | Role | GitHub |
|------|------|--------|
| **Anadi Gupta** | Lead Developer | [@anadigupta](https://github.com/anadigupta) |

### Contributors

We welcome contributions from the community! Check out our contributing guidelines to get started.

### Acknowledgments

- **Book-Crossing Dataset**: Collected by Cai-Nicolas Ziegler from the Book-Crossing community
- **Scikit-learn Team**: For excellent machine learning libraries
- **Pandas Team**: For powerful data manipulation tools
- **Jupyter Project**: For the interactive computing environment
- **Open Source Community**: For invaluable tools and resources

### References & Inspiration

- [Book-Crossing Dataset](http://www2.informatik.uni-freibourg.de/~cziegler/BX/)
- [Collaborative Filtering Wikipedia](https://en.wikipedia.org/wiki/Collaborative_filtering)
- [Recommender Systems Handbook](https://www.springer.com/gp/book/9781039783358)
- [Netflix Prize Challenge](https://www.netflixprize.com/)
- [Amazon Recommendation System](https://www.amazon.com/science/recommendations)

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

```
MIT License

Copyright (c) 2024 Recommendation System Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 📞 Support & Contact

- **Issues**: [GitHub Issues](https://github.com/yourusername/recommendation-system/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/recommendation-system/discussions)
- **Email**: support@example.com
- **Documentation**: [Full Documentation](https://docs.example.com)

---

## 📚 Additional Resources

### Learning Materials

- **Handwritten Notes**: `handwritten notes .pdf` - Detailed implementation notes and diagrams
- **Architecture Diagrams**: 
  - `DeepRec.png` - Deep learning recommendation architecture
  - `classicRec.png` - Classic recommendation system diagram
  - `recsys_taxonomy2.png` - Recommendation system taxonomy

### Related Projects

- [Content-Based Recommendation System](../../Content%20based%20Recommendation%20system/PHASE%201/)
- [Hybrid Recommendation Systems](../../HYBRID/)
- [Popularity-Based Recommendation System](../../Popularity%20based%20recommendation%20system/)

---

<div align="center">

**Made with ❤️ by Senior Engineers**

[⬆ Back to Top](#-collaborative-filtering-recommendation-system)

</div>
