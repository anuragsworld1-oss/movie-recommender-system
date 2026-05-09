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
        font-size: 55px;
        margin-bottom: 0;
    }

    .subtitle {
        text-align: center;
        color: #AAAAAA;
        font-size: 18px;
        margin-bottom: 30px;
    }

    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3.2em;
        background: linear-gradient(to right, #E50914, #ff4b2b);
        color: white;
        font-size: 18px;
        font-weight: bold;
        border: none;
    }

    .stButton>button:hover {
        background: linear-gradient(to right, #ff4b2b, #E50914);
        color: white;
    }

    .movie-title {
        text-align: center;
        font-size: 17px;
        font-weight: bold;
        color: white;
        margin-top: 10px;
        margin-bottom: 5px;
    }

    .rating {
        text-align: center;
        color: gold;
        font-size: 15px;
    }

    .overview {
        color: #CCCCCC;
        font-size: 13px;
        text-align: center;
    }

    </style>
    """,
    unsafe_allow_html=True
)


def fetch_movie_details(movie_id):

    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"

    data = requests.get(url).json()

    poster_path = data.get('poster_path')

    if poster_path:
        poster = "https://image.tmdb.org/t/p/w500/" + poster_path
    else:
        poster = "https://via.placeholder.com/500x750?text=No+Image"

    rating = data.get('vote_average', 'N/A')
    release_date = data.get('release_date', 'Unknown')
    overview = data.get('overview', 'No description available.')

    return poster, rating, release_date, overview


def recommend(movie):

    index = movies[movies['title'] == movie].index[0]

    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_movies = []

    for i in distances[1:6]:

        movie_id = movies.iloc[i[0]].movie_id

        poster, rating, release_date, overview = fetch_movie_details(movie_id)

        recommended_movies.append({
            'title': movies.iloc[i[0]].title,
            'poster': poster,
            'rating': rating,
            'release_date': release_date,
            'overview': overview
        })

    return recommended_movies


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)


cv = CountVectorizer(max_features=5000, stop_words='english')

vectors = cv.fit_transform(movies['tags']).toarray()

similarity = cosine_similarity(vectors)


st.markdown("<h1>🎬 CineMatch AI</h1>", unsafe_allow_html=True)

st.markdown(
    "<div class='subtitle'>Discover movies similar to your favorites 🍿</div>",
    unsafe_allow_html=True
)


st.sidebar.title("⚙️ About")

st.sidebar.info(
    "This Movie Recommender uses NLP, CountVectorizer, and Cosine Similarity to recommend similar movies."
)

st.sidebar.markdown("---")
st.sidebar.write("Built using:")
st.sidebar.write("✅ Python")
st.sidebar.write("✅ Streamlit")
st.sidebar.write("✅ Scikit-Learn")
st.sidebar.write("✅ TMDB API")


movie_list = movies['title'].values

selected_movie = st.selectbox(
    "🎥 Search your favorite movie",
    movie_list
)


if st.button('🚀 Show Recommendations'):

    with st.spinner('Analyzing movie patterns...'):

        recommended_movies = recommend(selected_movie)

        st.markdown("## Recommended Movies")

        cols = st.columns(5)

        for idx, movie in enumerate(recommended_movies):

            with cols[idx]:
                st.image(movie['poster'])

                st.markdown(
                    f"<div class='movie-title'>{movie['title']}</div>",
                    unsafe_allow_html=True
                )

                st.markdown(
                    f"<div class='rating'>⭐ {movie['rating']}</div>",
                    unsafe_allow_html=True
                )

                st.caption(f"📅 {movie['release_date']}")

                st.markdown(
                    f"<div class='overview'>{movie['overview'][:120]}...</div>",
                    unsafe_allow_html=True
                )


st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:gray;'>Made with ❤️ by Anurag</p>",
    unsafe_allow_html=True
)
