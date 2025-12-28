import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    try:

        response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.
                            format(movie_id),timeout=5)
        data=response.json()
        if data.get('poster_path'):
            return "https://image.tmdb.org/t/p/w500/"+data['poster_path']

        else:
            return None
    except:
        return None
    
def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]
    movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies=[]
    recommended_movies_poster=[]
    for i in movie_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster

movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')
option=st.selectbox('Search Movie...',movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(option)

    cols = st.columns(5)
    for col, name, poster in zip(cols, names, posters):
        with col:
            st.text(name)
            if poster:
                st.image(poster)
            else:
                st.write("No poster available")
