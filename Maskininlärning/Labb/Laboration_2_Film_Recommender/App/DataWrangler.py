"""
**Data Wrangler** - Tänker att vi gör ett medelvärde på ranking för varje film, mer än att hålla kol på alla röstningar och skalan. Den bör var i någon form av skalering eller normalisering, för att ge ett mer objektivt värde. Lägga till en column med medlet. 

Sedan bör gener kolumnen göras om till ett set. För att gör filtrering enklare i den kolumnen mot input filmen.  Standardized rating direct i datasetet så det är färdigt att kör, tänk på bara om jag behöver ratings senare i modellen.

*Komponenter*
- Ladda data - Kan behövas flera sätt att ladda olika data set till modellen. 
- Lägga ihop set med varandra med den datan som behövs. Som tags, tids data, ranking data, movieid, namn och bag of words 
- Förädla - Sandardisera eller nomarlisera. Två metoder för detta. Kommer behövas flera kolumner med olika behandlade värden. 
- Bag of words för geners för att förenkla för modellen att hitta i första gallring, läggg till det som en column för gener istället.
- Tf-idf vector för tags and geners. Behöver en kolumn med både gener och tags i den.    
- Beräkning/Agrregering av tids data för att ge ett möjligt värde för hur nyligen den var engagerad.
    * Medel på tiden som det varit engegemang i filmen
    * Senast det var någon post
    * Dom senaste 6 månderna eller året
    * Spannet från första till sista post

- Beräkning/Aggregering av ranking data för att ge ett standardizerat värde på ranking
    * Lägga till alla typer av ranking värde 0.5 till 5.0 och antelet för varje ranking.
    * En stadrizerad värde för medlet på av alla raningar. 
"""


import pandas as pd
import numpy as np
import os 
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

class MovieData():
    self.movie_data = data
    self.movie_data_Tfidf = vector

    # Kör automatikst när instansierar klassen

    def load_compile_data():
        general_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), "..", "Data")) # Taget från stackoverflow (https://stackoverflow.com/questions/9856683/using-pythons-os-path-how-do-i-go-up-one-directory)

        movie_data = pd.read_csv(general_path + "\\movies.csv")
        ratings_data = pd.read_csv(general_path + "\\ratings.csv")
        tags_data = pd.read_csv(general_path + "\\tags.csv")

        movie_data.insert(2, "year",  movie_data["title"].str.extract(r"\((\d{4})\)"))
        movie_data["title"] = movie_data["title"].str.replace(r"(\s*\(\d{4})\)", "", regex=True)

        return movie_data
    

    def compiler(self):
        tags_data["tag"] = tags_data["tag"].astype(str) 
        tags = tags_data.groupby(["movieId"], as_index=False).aggregate({"tag" : " ".join})
        tags["tag"] = tags["tag"].str.replace(" ", "|")

        movies_data = movies_data.merge(tags, on="movieId", how="left")
        movies_data["tag"] = movies_data["tag"].fillna("")
        movies_data["tf_idf_input"] = movies_data["genres"] + " " + movies_data["tag"]

        movies_data = movies_data.drop("tag", axis=1)
        pass


    def tfidf_vectorizer(self, tags_gener):
        pass


    def rating_aggrigator(self, rating_data):
        pass

    def time_aggrigator(self, rating_data, tag_data):
        # def movie_timestamp(self): if this code gets to big 
        # Need to know the timestamp in seconds since midnight Coordinated Universal Time (UTC) of January 1, 1970 the movie relesed
        # Droppa filmer med minder än två posts 
        pass

    
    def bow_vectorizer(self):
        genres = ["Action", "Adventure", "Animation", "Children", "Comedy", 
          "Crime", "Documentary", "Drama", "Fantasy", "Film-Noir", 
          "Horror", "Musical", "Mystery", "Romance", "Sci-Fi", "Thriller", 
          "War", "Western", "(no genres listed)"]
        
        vectorizer = CountVectorizer()
        vectorizer.fit(genres)
        df["BoW_input"] = df["genres"].apply( lambda row: vectorizer.transform([row]).toarray())
        pass