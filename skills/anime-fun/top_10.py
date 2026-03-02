import requests
import sys
import os

def get_top_anime(limit=10):
    url = f"https://api.jikan.moe/v4/top/anime?limit={limit}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        print(f"🏆 Top {limit} Anime (Live)\n")
        for i, anime in enumerate(data['data'], 1):
            title = anime['title_english'] or anime['title']
            score = anime['score']
            genres = ", ".join([g['name'] for g in anime['genres']])
            rank = anime['rank']
            print(f"{i}. {title} (Rank: {rank}, Score: {score})")
            print(f"   📂 Genres: {genres}")
            print(f"   🔗 URL: {anime['url']}\n")
            
    except Exception as e:
        print(f"Error fetching top anime: {e}")

if __name__ == "__main__":
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    get_top_anime(limit)
