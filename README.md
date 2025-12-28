# 🎬 Movie Recommendation System

## 📌 Summary
A content-based Movie Recommendation System that suggests similar movies to users based on movie metadata using cosine similarity and natural language processing techniques.

---

## 📖 Overview
With the rapid growth of online streaming platforms, users often struggle to decide what to watch next.  
This project aims to solve that problem by building a **content-based movie recommender system** that analyzes movie information and recommends similar movies when a user selects a movie.

The system is built using **Python, Machine Learning, and Streamlit**, providing an interactive and user-friendly web interface.

---

## ❓ Problem Statement
Users are overwhelmed by the vast number of movies available on streaming platforms.  
Manually searching for similar or relevant movies is time-consuming and inefficient.

**Objective:**  
To design a system that automatically recommends movies similar to a selected movie using data-driven techniques.

---

## 📊 Dataset
The project uses the **TMDB 5000 Movies Dataset**, which includes:
- Movie titles
- Genres
- Overview
- Cast and crew
- Movie IDs

**Source:**  
TMDB (The Movie Database)

---

## 🛠️ Tools & Technologies
- **Python**
- **Pandas & NumPy** – Data manipulation
- **Scikit-learn** – Vectorization and similarity calculation
- **NLTK** – Text preprocessing
- **Streamlit** – Web application
- **Pickle** – Model serialization
- **Git & GitHub** – Version control
- **TMDB API** – Movie posters

---

## 🔍 Methods (Data Preprocessing)
The following preprocessing steps were applied:

- Merging multiple datasets
- Handling missing values
- Text cleaning and normalization
- Feature extraction using:
  - Genres
  - Keywords
  - Cast
  - Crew
  - Movie overview
- Text vectorization using **CountVectorizer**
- Similarity computation using **Cosine Similarity**

These steps ensure raw real-world data is converted into a structured format suitable for machine learning.

---

## 👤 End-User Interface (Streamlit)
The application provides:
- A dropdown to select a movie
- A **Recommend** button
- Top 5 similar movie recommendations
- Movie posters fetched dynamically using TMDB API

The interface is simple, interactive, and beginner-friendly.

---

## ▶️ How to Run This Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/s-saqlain/movie-recommender-system.git
cd movie-recommender-system
