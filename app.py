import pickle
import streamlit as st
import requests
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer


st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide"
)


st.markdown(
    """
    <style>
    .main {
        background-color: #0E1117;
    }

    h1 {
        text-align: center;
        color: white;
        font-size: 50px;
    }

    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #E50914;
        color: white;
        font-size: 18px;
        border: none;
    }

    .stButton>button:hover {
        background-color: #ff2e2e;
        color: white;
    }

    .movie-title {
        text-align: center;
        font-size: 18px;
        font-weight: bold;
        color: white;
        margin-top: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"

    data = requests.get(url).json()

    poster_path = data.get('poster_path')

    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path

    return "https://via.placeholder.com/500x750?text=No+Image"


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]

    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)


cv = CountVectorizer(max_features=5000, stop_words='english')

vectors = cv.fit_transform(movies['tags']).toarray()

similarity = cosine_similarity(vectors)

st.markdown("<h1>🎬 Movie Recommender System</h1>", unsafe_allow_html=True)

st.markdown(
    "<p style='text-align:center; color:gray;'>Find movies similar to your favorite ones 🍿</p>",
    unsafe_allow_html=True
)

movie_list = movies['title'].values

selected_movie = st.selectbox(
    "Choose a movie",
    movie_list
)


if st.button('Recommend Movies'):

    with st.spinner('Finding best recommendations for you...'):
        recommended_movie_names, recommended_movie_posters = recommend(selected_movie)

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.image(recommended_movie_posters[0])
            st.markdown(f"<div class='movie-title'>{recommended_movie_names[0]}</div>", unsafe_allow_html=True)

        with col2:
            st.image(recommended_movie_posters[1])
            st.markdown(f"<div class='movie-title'>{recommended_movie_names[1]}</div>", unsafe_allow_html=True)

        with col3:
            st.image(recommended_movie_posters[2])
            st.markdown(f"<div class='movie-title'>{recommended_movie_names[2]}</div>", unsafe_allow_html=True)

        with col4:
            st.image(recommended_movie_posters[3])
            st.markdown(f"<div class='movie-title'>{recommended_movie_names[3]}</div>", unsafe_allow_html=True)

        with col5:
            st.image(recommended_movie_posters[4])
            st.markdown(f"<div class='movie-title'>{recommended_movie_names[4]}</div>", unsafe_allow_html=True)


st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:gray;'>Built with Streamlit ❤️</p>",
    unsafe_allow_html=True
)
