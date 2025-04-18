from sklearn.metrics.pairwise import cosine_similarity
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from DataWrangler import MovieData


class Recomander():
    
    def __init__(self):
        
        get_profiles_matrix = MovieData()

        self.recomandations = None
        self.movie_profiles = get_profiles_matrix.movie_profiles
        self.tf_idf_matrix = get_profiles_matrix.tfidf_matrix
        self.input_movie = None


    def find_input_movie(self, input_movie):
            # Find the movie profile based on title
            movie_profile = self.movie_profiles[self.movie_profiles["title"] == input_movie]
            self.input_movie = movie_profile


    def candidates_model(self):  
        bow_columns = self.movie_profiles.columns[15:]
        input_vector = self.input_movie[bow_columns].values
        similar_movies = self.movie_profiles[self.movie_profiles["movieId"] != self.input_movie["movieId"].values[0]]

        sims = cosine_similarity(input_vector, similar_movies[bow_columns].values)[0]
        similar_movies = similar_movies.copy()
        similar_movies["similarity"] = sims        
        
        candidates = similar_movies.sort_values("similarity", ascending=False).head(60)  
        
        return candidates

    
    def scoring(self):
        candidates = self.candidates_model()
        
        input_tfidf = self.tf_idf_matrix[self.input_movie.index[0]]
        candidates_tfidf = self.tf_idf_matrix[candidates.index]

        sims = cosine_similarity(input_tfidf, candidates_tfidf)[0]
        candidates = candidates.copy()
        candidates["similarity"] = sims

        scoring_set = candidates.sort_values("similarity", ascending=False).head(20)
        
        return scoring_set
        

    def pred_engagement_level(self):        
            feature_list = ["mean_time", "std_time", "last_engagement", 
                        "total_engagement", "release_year_unix", 
                        "since_release_to_mean", "engagement_span"]
            
            X_train, y_train = self.movie_profiles[feature_list], self.movie_profiles["engagement_level"]
            random_forest = RandomForestClassifier(n_estimators=10)
            random_forest.fit(X_train, y_train)

            return random_forest, feature_list


    def recommander(self):
        scoring_set= self.scoring()
        model, feature_list = self.pred_engagement_level()

        pred = model.predict(scoring_set[feature_list])

        scoring_set["pred_engagement_level"] = pred
        classes = ['Very High', 'High', 'Medium', 'Low', 'Very Low']

        scoring_set["pred_engagement_level"] = scoring_set["pred_engagement_level"].astype('category')


        order = list(set(scoring_set["pred_engagement_level"]) - set(classes)) + classes
        scoring_set["pred_engagement_level"] = scoring_set["pred_engagement_level"].cat.reorder_categories(order)

        high_engamnate = scoring_set.sort_values(by="pred_engagement_level", ascending=True).head(3)
        scoring_set.drop(high_engamnate.index, inplace=True)

        recent_realesed = scoring_set.sort_values(by="year", ascending=False).head(2)
        recommendations = pd.concat([high_engamnate, recent_realesed])
        recommendations.reset_index(drop=True, inplace=True)

        return recommendations
        