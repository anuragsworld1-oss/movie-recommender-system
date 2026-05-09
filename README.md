# 🎬 CineMatch AI — Movie Recommender System

A **Content-Based Movie Recommendation System** powered by Machine Learning and NLP that suggests movies similar to a selected title using text vectorization and cosine similarity.

Built with **Streamlit**, integrated with **TMDB API**, and designed with a Netflix-style UI for an interactive user experience.

---

# 🚀 Live Demo

👉  https://movie-recommender-system-69gsmwwnx4xrrt73guqyff.streamlit.app/#cine-match-ai

---

# 📸 Project Preview

### 🏠 Home Interface
![Home Interface](assets/homepage.png)

### 🎯 Recommendations Output
![Recommendations Output](assets/recommendation.png)

---

# 💡 Problem Statement

With thousands of movies available on streaming platforms, users often struggle to find relevant content.

This project solves this by building a **smart recommendation engine** that suggests movies based on content similarity.

---

# ⚙️ How It Works (Simple Explanation)

Each movie is transformed into a **text-based feature vector** using metadata like:

- Genres  
- Keywords  
- Cast  
- Crew  
- Overview  

These are combined into a single **"tag" representation**.

Then similarity is calculated as:

:contentReference[oaicite:0]{index=0}

The system computes similarity between movies and recommends the closest matches.

---

# 🧠 Machine Learning Pipeline

- Data Collection (TMDB dataset)  
- Data Cleaning & Preprocessing  
- Feature Engineering (tags creation)  
- Text Vectorization (CountVectorizer)  
- Similarity Calculation (Cosine Similarity)  
- Recommendation Engine  
- Streamlit Deployment  

---

# 🛠️ Tech Stack

## 🧑‍💻 Frontend
- Streamlit  

## 🧠 Machine Learning
- Scikit-learn  
- NLP (Text Processing)  
- CountVectorizer  
- Cosine Similarity  

## 🌐 API Integration
- TMDB API (movie posters & metadata)  

## 📦 Libraries
- pandas  
- numpy  
- requests  
- pickle  
- sklearn  

---

# 📁 Project Structure

```text
movie-recommender-system/
│
├── app.py
├── movie_dict.pkl
├── movies.pkl
│
├── assets/
│   ├── homepage.png
│   ├── recommendation.png
│
├── requirements.txt
├── .gitignore
└── README.md

👨‍💻 Author

Anurag

GitHub: https://github.com/anuragsworld1-oss
Project: CineMatch AI 
