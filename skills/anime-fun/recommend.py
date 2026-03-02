import requests
import sys
import random

def get_recommendations(genres_input="", min_score=8.0):
    """
    Suggests anime based on user genres and a minimum score.
    Uses Jikan API v4.
    """
    # Map of common genre names to Jikan IDs (based on MAL)
    genre_map = {
        "action": 1, "adventure": 2, "comedy": 4, "drama": 8, "fantasy": 10,
        "horror": 14, "mystery": 7, "romance": 22, "sci-fi": 24, "slice of life": 36,
        "sports": 30, "supernatural": 37, "suspense": 41
    }
    
    url = "https://api.jikan.moe/v4/anime"
    params = {
        "order_by": "score",
        "sort": "desc",
        "min_score": min_score,
        "sfw": True
    }
    
    if genres_input:
        selected_genres = [g.strip().lower() for g in genres_input.split(",")]
        genre_ids = [str(genre_map[g]) for g in selected_genres if g in genre_map]
        if genre_ids:
            params["genres"] = ",".join(genre_ids)
            print(f"🔍 Searching for highly-rated {genres_input} anime...")
    else:
        print(f"🔍 Searching for top-rated anime across all categories (Score > {min_score})...")

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        anime_list = data.get('data', [])
        
        if not anime_list:
            print("No high-rated anime found for those categories. Try expanding your genres!")
            return

        # Pick 3 random gems from the top results
        sample_size = min(len(anime_list), 5)
        recommendations = random.sample(anime_list[:15], sample_size)
        
        print(f"\n✨ My Top Recommendations for You:\n")
        for anime in recommendations:
            title = anime['title_english'] or anime['title']
            score = anime['score']
            genres = ", ".join([g['name'] for g in anime['genres']])
            synopsis = anime['synopsis'][:150] + "..." if anime['synopsis'] else "No synopsis available."
            
            print(f"⭐ {title} (Score: {score})")
            print(f"   📂 Genres: {genres}")
            print(f"   📝 {synopsis}")
            print(f"   🔗 {anime['url']}\n")
            
    except Exception as e:
        print(f"Error fetching recommendations: {e}")

if __name__ == "__main__":
    genres = sys.argv[1] if len(sys.argv) > 1 else ""
    get_recommendations(genres)
