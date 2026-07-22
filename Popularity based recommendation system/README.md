# Popularity-Based Recommendation System

This project implements a popularity-based book recommendation system using the Book-Crossing dataset.

## Overview

The popularity-based recommender suggests books based on:
- Number of ratings (popularity)
- Average rating score

## Dataset

- **Books.csv**: Contains book information (ISBN, title, author, publisher, etc.)
- **Users.csv**: Contains user demographic information
- **Ratings.csv**: Contains user-book ratings

## Approach

1. Load and merge datasets
2. Calculate number of ratings per book
3. Calculate average rating per book
4. Filter books based on minimum rating threshold
5. Recommend top-rated books

## Usage

Run the Jupyter notebook or Python script to generate recommendations.
