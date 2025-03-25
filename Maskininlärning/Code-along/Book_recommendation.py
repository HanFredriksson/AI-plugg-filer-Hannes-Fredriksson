import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler


def load_data():
    books = pd.read_csv("../data/Books.csv")
    ratings = pd.read_csv("../data/Ratings.csv")

    books.drop_duplicates("Book-Title", inplace=True)
    merged = ratings.merge(books, on="ISBN")
    merged.drop(["ISBN", "Image-URL-S", "Image-URL-M", "Image-URL-L", "Publisher"], axis=1, inplace=True)
    merged.dropna(inplace=True)

    return merged, books


def extract_features(raw_tabel):
    x = raw_tabel.groupby("User-ID").count()["Book-Rating"] > 100
    expert_users = x[x].index
    filtered_users = raw_tabel[raw_tabel["User-ID"].isin(expert_users)]

    y = filtered_users.groupby("Book-Title").count()["Book-Rating"] >= 50
    famous_books = y[y].index
    user_ratings = filtered_users[filtered_users["Book-Title"].isin(famous_books)]

    design_matrix = user_ratings.pivot_table(index="Book-Title", columns= "User-ID", values="Book-Rating")
    design_matrix.fillna(0, inplace=True)

    return design_matrix

def make_model(matrix):
    scaler = StandardScaler(with_mean=True, with_std=True)
    sceled = scaler.fit_transform(matrix)
    sim_score = cosine_similarity(sceled)

    return sim_score


def recommend (book_name, tabel, design_matrix, similarity_score):
    index = np.where(design_matrix.index==book_name)[0][0]
    similar_books = sorted(list(enumerate(similarity_score[index])), key=lambda x: x[1], reverse=True)[1:6]

    data = []

    for index, _ in similar_books:
        item = []
        temp_df = tabel[tabel["Book-Title"] == design_matrix.index[index]]
        item.extend(temp_df["Book-Title"].values)
        item.extend(temp_df["Book-Author"].values)
        data.append(item)

    return data

def main():
    table, books = load_data()
    matrix = extract_features(table)
    model = make_model(matrix)
    name = "1984"
    print(recommend(name, books, matrix, model))


    if __name__ == "main":
        main()