from collections import deque

#movie names stored
MOVIES = {
    "Inception":        {"genre": ["Sci-Fi", "Thriller"], "rating": 8.8, "director": "Christopher Nolan", "year": 2010},
    "The Dark Knight":  {"genre": ["Action", "Crime"],    "rating": 9.0, "director": "Christopher Nolan", "year": 2008},
    "Interstellar":     {"genre": ["Sci-Fi", "Drama"],    "rating": 8.6, "director": "Christopher Nolan", "year": 2014},
    "The Matrix":       {"genre": ["Sci-Fi", "Action"],   "rating": 8.7, "director": "Wachowski",         "year": 1999},
    "Avengers: Endgame":{"genre": ["Action", "Sci-Fi"],   "rating": 8.4, "director": "Russo Brothers",    "year": 2019},
    "Parasite":         {"genre": ["Thriller", "Drama"],  "rating": 8.6, "director": "Bong Joon-ho",      "year": 2019},
    "Pulp Fiction":     {"genre": ["Crime", "Drama"],     "rating": 8.9, "director": "Tarantino",         "year": 1994},
    "The Godfather":    {"genre": ["Crime", "Drama"],     "rating": 9.2, "director": "Coppola",           "year": 1972},
    "Forrest Gump":     {"genre": ["Drama", "Romance"],   "rating": 8.8, "director": "Robert Zemeckis",  "year": 1994},
    "Titanic":          {"genre": ["Drama", "Romance"],   "rating": 7.9, "director": "James Cameron",     "year": 1997},
    "Gladiator":        {"genre": ["Action", "Drama"],    "rating": 8.5, "director": "Ridley Scott",      "year": 2000},
    "The Shawshank Redemption": {"genre": ["Drama"],      "rating": 9.3, "director": "Frank Darabont",   "year": 1994},
    "Joker":            {"genre": ["Crime", "Thriller"],  "rating": 8.4, "director": "Todd Phillips",     "year": 2019},
    "Get Out":          {"genre": ["Thriller", "Horror"], "rating": 7.7, "director": "Jordan Peele",     "year": 2017},
    "Mad Max: Fury Road":{"genre": ["Action", "Sci-Fi"],  "rating": 8.1, "director": "George Miller",    "year": 2015},
}


#  (genre recommendation to movie )
def build_genre_graph(movie_db):
    """Make a quick genre → movie list mapping"""
    graph = {}
    for title, info in movie_db.items():
        for g in info["genre"]:
            if g not in graph:
                graph[g] = []      # human-ish: explicit check instead of setdefault
            graph[g].append(title)
    return graph

#bfs is used here
def bfs_recommendations(start, movie_db, max_hops=2):
    """BFS: find movies connected by shared genres"""
    if start not in movie_db:
        return []

    visited = {start}
    queue = deque([(start, 0, "")])   # (movie, hops, via_genre)
    results = []

    genre_graph = build_genre_graph(movie_db)  # human tendency: build once outside loop

    while queue:
        curr, hops, via_genre = queue.popleft()

        if hops > max_hops:
            continue  # gone too far

        for genre in movie_db[curr]["genre"]:
            for neighbour in genre_graph.get(genre, []):
                if neighbour not in visited:
                    visited.add(neighbour)
                    if hops + 1 <= max_hops:
                        queue.append((neighbour, hops + 1, genre))
                    results.append((neighbour, hops + 1, genre))  # maybe redundant but human-like

    # sort by rating, high first
    results.sort(key=lambda x: movie_db[x[0]]["rating"], reverse=True)
    return results

#dfs is used here

def dfs_recommendations(start, movie_db, preferred_genre=None, visited=None, depth=0, max_depth=3):
    """DFS: explore deeply, optionally biasing a genre"""
    if visited is None:
        visited = set()

    if start not in movie_db or depth > max_depth:
        return []

    visited.add(start)
    results = []

    genre_graph = build_genre_graph(movie_db)  # might be recomputed multiple times (oops, human)

    genres_to_check = movie_db[start]["genre"]
    if preferred_genre and preferred_genre in genres_to_check:
        genres_to_check = [preferred_genre] + [g for g in genres_to_check if g != preferred_genre]

    for g in genres_to_check:
        for neighbour in genre_graph.get(g, []):
            if neighbour not in visited:
                results.append((neighbour, depth + 1, g))
                # human: recursive call with extend, could be more efficient
                results.extend(dfs_recommendations(neighbour, movie_db, preferred_genre, visited, depth + 1, max_depth))

    return results

#display to help the user

def display_movie_info(title, movie_db):
    m = movie_db[title]
    print(f"   {title} ({m['year']}) |  {m['rating']} | "
          f" {', '.join(m['genre'])} |  {m['director']}")

def display_recommendations(title, recs, movie_db, method):
    print("\n" + "="*60)
    print(f"  {method} Recommendations for: {title}")
    print("="*60)
    if not recs:
        print("  No recommendations found.")
        return

    seen = set()
    rank = 1
    for movie, hop_or_depth, genre in recs:
        if movie not in seen:
            seen.add(movie)
            print(f"  {rank:>2}. [via {genre:<8}] ", end="")
            display_movie_info(movie, movie_db)
            rank += 1
            if rank > 8:  # human: cap display at 8, arbitrary
                break

#search helping agent

def search_by_genre(genre, movie_db):
    """Return movies matching genre, sorted by rating"""
    hits = [(t, info) for t, info in movie_db.items() if genre in info["genre"]]
    hits.sort(key=lambda x: x[1]["rating"], reverse=True)
    return hits

def top_rated(movie_db, n=5):
    """Top-N rated movies"""
    return sorted(movie_db.items(), key=lambda x: x[1]["rating"], reverse=True)[:n]


def list_movies(movie_db):
    print("\n  Available movies:")
    for i, title in enumerate(sorted(movie_db.keys()), 1):
        print(f"  {i:>2}. {title}")

def main():
    print("\n" + "="*60)
    print("   MOVIE RECOMMENDER  ")
    print("      Using BFS & DFS Algorithms")
    print("="*60)

    while True:
        print("\n  MENU")
        print("  1. BFS Recommendations")
        print("  2. DFS Recommendations")
        print("  3. Search by Genre")
        print("  4. Top-Rated Movies")
        print("  5. List All Movies")
        print("  6. Exit")

        choice = input("\n  Enter choice (1-6): ").strip()

        if choice == "1":
            list_movies(MOVIES)
            title = input("\n  Enter movie name exactly: ").strip()
            if title not in MOVIES:
                print(" Movie not found")
                continue
            hops = input("  Max hops (default 2): ").strip()
            hops = int(hops) if hops.isdigit() else 2
            recs = bfs_recommendations(title, MOVIES, max_hops=hops)
            display_recommendations(title, recs, MOVIES, "BFS")

        elif choice == "2":
            list_movies(MOVIES)
            title = input("\n  Enter movie name exactly: ").strip()
            if title not in MOVIES:
                print(" Movie not found")
                continue
            pref = input(f"  Preferred genre (optional)\n  Genres: {', '.join(MOVIES[title]['genre'])}\n> ").strip()
            recs = dfs_recommendations(title, MOVIES, preferred_genre=pref or None)
            display_recommendations(title, recs, MOVIES, "DFS")

        elif choice == "3":
            genres = sorted({g for m in MOVIES.values() for g in m["genre"]})
            print(f"\n  Genres: {', '.join(genres)}")
            genre = input("  Enter genre: ").strip()
            hits = search_by_genre(genre, MOVIES)
            if not hits:
                print("  No movies found for that genre.")
            else:
                print(f"\n  Movies in '{genre}':")
                for t, info in hits:
                    display_movie_info(t, MOVIES)

        elif choice == "4":
            n = input("  How many top movies to show? (default 5): ").strip()
            n = int(n) if n.isdigit() else 5
            print(f"\n  Top {n} Rated Movies:")
            for t, info in top_rated(MOVIES, n):
                display_movie_info(t, MOVIES)

        elif choice == "5":
            list_movies(MOVIES)

        elif choice == "6":
            print("\n  Thanks for using Movie Recommender! \n")
            break

        else:
            print("  Invalid choice. Enter 1-6.")


if __name__ == "__main__":
    main()