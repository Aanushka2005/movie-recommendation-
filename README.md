# Movie Recommender System

### Using BFS & DFS Graph Algorithms

**Author:** Anushka Sahu | **Reg. No.:** 25BAI11314
**Course:** B.Tech CSE (AI/ML) | **Session:** 2025–2026


## Overview

This project is a simple and interactive Python-based movie recommendation system that uses graph traversal algorithms to suggest movies.

Each movie is treated as a node in a graph, and movies are connected if they share similar genres. When a user selects a movie, the system explores these connections using BFS (Breadth-First Search) or DFS (Depth-First Search) to find related films.

The recommendations are then sorted by rating so that users get both relevant and high-quality suggestions.


## Features

|
Feature              What it does                                                 
 
 1)BFS Recommendations -Suggests a variety of movies by exploring nearby connections 
 2)DFS Recommendations -Goes deep into a specific genre for focused suggestions      
 3)Search by Genre - Finds all movies in a selected genre                         
 4)Top Rated - Displays highest-rated movies                                
 5)List All Movies - Shows the complete movie collection                          


## Getting Started

### Requirements

* Python 3.x
* No external libraries required

### How to Run

```bash
python movie_recommender.py
```

After running the file, the program will display a menu for interaction.

## Menu Options

```
MENU
1. BFS Recommendations
2. DFS Recommendations
3. Search by Genre
4. Top-Rated Movies
5. List All Movies
6. Exit
```

---

### Option 1 — BFS Recommendations

Enter a movie name and optionally the number of hops.

BFS explores the graph step by step:

* First finds closely related movies
* Then moves to slightly distant ones

This produces diverse and balanced recommendations.

Example:

```
Movie: Inception | Max Hops: 2

BFS Recommendations for: Inception
1. The Shawshank Redemption (1994) | 9.3
2. The Godfather (1972) | 9.2
3. The Dark Knight (2008) | 9.0
...
```

### Option 2 — DFS Recommendations

Enter a movie name and optionally a preferred genre.

DFS explores deeply into one genre before backtracking.

This produces more focused recommendations.

Example:

```
Movie: The Dark Knight | Preferred Genre: Crime

DFS Recommendations for: The Dark Knight
1. Pulp Fiction (1994) | 8.9
2. The Godfather (1972) | 9.2
3. Joker (2019) | 8.4
...
```

### Option 3 — Search by Genre

Enter a genre such as:
Action, Drama, Sci-Fi, Thriller, Romance, Crime, Horror

The system will display all matching movies sorted by rating.


### Option 4 — Top-Rated Movies

Enter how many movies to display. The system will return the top-rated ones.


### Option 5 — List All Movies

Displays all 15 movies in alphabetical order.


### Option 6 — Exit

Closes the program.


## Movie Database

The system includes 15 well-known movies across different genres and years. All data is stored locally.

Examples include:

* The Shawshank Redemption (Drama)
* The Godfather (Crime, Drama)
* Inception (Sci-Fi, Thriller)
* Interstellar (Sci-Fi, Drama)
* Titanic (Drama, Romance)
* Get Out (Thriller, Horror)

## How It Works

### Graph Structure

The system builds a structure like:

```
"Sci-Fi" → ["Inception", "The Matrix", "Interstellar"]
"Drama" → ["Titanic", "Forrest Gump", ...]
```

Movies are connected through shared genres.


### BFS (Breadth-First Search)

* Uses a queue
* Explores level by level
* Controlled by max_hops

Best for variety and exploration.


### DFS (Depth-First Search)

* Uses recursion
* Explores one path deeply
* Can prioritize a genre

Best for focused recommendations.


## Project Structure

```
movie_recommender.py
├── MOVIES
├── build_genre_graph()
├── bfs_recommendations()
├── dfs_recommendations()
├── search_by_genre()
├── top_rated()
├── display functions
└── main()
```

---

## Notes

* Movie names are case-sensitive
* DFS rebuilds the graph multiple times (can be optimized)
* Output is limited to top 8 recommendations


## Conclusion

This project demonstrates how BFS and DFS can be applied to a real-world problem like movie recommendation.

BFS is useful for exploring a wide range of options, while DFS is better for diving deep into a specific genre. The project is simple, easy to run, and a good example of combining graph algorithms with practical applications.
