import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Sample dataset of books and user ratings
books = pd.DataFrame({
    'book_id': [1, 2, 3, 4, 5],
    'title': ["To Kill a Mockingbird", "Pride and Prejudice", "The Great Gatsby", "1984", "The Catcher in the Rye"],
    'genre': ["Fiction", "Fiction", "Fiction", "Science Fiction", "Fiction"]
})

ratings = pd.DataFrame({
    'user_id': [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],
    'book_id': [1, 2, 2, 3, 3, 4, 4, 5, 1, 5],
    'rating': [5, 4, 4, 3, 5, 2, 3, 4, 5, 3]
})

# Create a user-book rating matrix
rating_matrix = ratings.pivot(index='user_id', columns='book_id', values='rating').fillna(0)

# Calculate cosine similarity between users
user_similarity = cosine_similarity(rating_matrix)
np.fill_diagonal(user_similarity, 0)  # Remove self-similarity
user_similarity_df = pd.DataFrame(user_similarity, index=rating_matrix.index, columns=rating_matrix.index)


# Function to get book recommendations for a user based on similar users
def user_based_recommendations(user_id, n_recommendations=3):
    similar_users = user_similarity_df[user_id].nlargest(n_recommendations).index
    recommended_books = ratings[ratings['user_id'].isin(similar_users)]
    book_scores = recommended_books.groupby('book_id')['rating'].mean()
    book_scores = book_scores.sort_values(ascending=False).head(n_recommendations)

    recommended_book_titles = books[books['book_id'].isin(book_scores.index)]['title']
    return recommended_book_titles.tolist()


# Function to get book recommendations based on content similarity
def content_based_recommendations(user_id, n_recommendations=3):
    user_ratings = ratings[ratings['user_id'] == user_id]
    user_books = user_ratings.merge(books, on='book_id')
    favorite_genre = user_books['genre'].mode()[0]

    similar_books = books[books['genre'] == favorite_genre]
    recommended_books = similar_books[~similar_books['book_id'].isin(user_ratings['book_id'])]

    return recommended_books.head(n_recommendations)['title'].tolist()


def main():
    try:
        user_id = int(input("Enter your user ID (1-5): "))
        if user_id not in ratings['user_id'].unique():
            print("User ID not found. Please enter a valid user ID.")
            return

        print(f"Getting recommendations for User {user_id}...\n")

        # User-based recommendations
        user_recommendations = user_based_recommendations(user_id)
        print("User-based Recommendations:")
        for i, book in enumerate(user_recommendations, start=1):
            print(f"{i}. {book}")

        print("\n")

        # Content-based recommendations
        content_recommendations = content_based_recommendations(user_id)
        print("Content-based Recommendations:")
        for i, book in enumerate(content_recommendations, start=1):
            print(f"{i}. {book}")

    except ValueError:
        print("Invalid input. Please enter a valid user ID (integer).")


if __name__ == "__main__":
    main()

