from Recommender import Recommender
import os

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def run_recommender():
    get_recommendations = Recommender()

    while True:
        clear_terminal()
        input_title = input("Pick a movie: ")

        get_recommendations.input_movie = input_title

        try:
            recommendations = get_recommendations.recommander()
        except Exception as e:
            print(f"\nCould not find or process movie '{input_title}'. Error: {e}")
            input("\nPress Enter to try again...")
            continue

        clear_terminal()
        print(get_recommendations.input_movie)
        selected = get_recommendations.input_movie.iloc[0]  # only one row
        print(f"You picked the movie: {selected['title']}, From {selected['year']}, Genres: {selected['genres']}\n")
        print("----------------------------")
        for _, movie in recommendations.iterrows():
            print(f"{movie['title']}, From: {movie['year']}, Genres: {movie['genres']}")
        print("----------------------------\n")

        again = input("Do you want to pick another movie? (y/n): ").lower()
        if again != "y":
            print("Goodbye!")
            break

if __name__ == "__main__":
    run_recommender()
