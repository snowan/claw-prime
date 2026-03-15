import requests
import sys

# Helper to get Chinese titles for popular series
# Since Jikan doesn't provide them, we map them manually for top hits
# or provide the Japanese title as a reference.
CHINESE_TITLES = {
    52991: "葬送的芙莉莲",
    5114: "钢之炼金术师 FULLMETAL ALCHEMIST",
    9253: "命运石之门",
    38524: "进击的巨人 第三季 Part.2",
    28977: "银魂°",
    39486: "银魂 THE FINAL",
    41467: "王者天下 第四季",
    11061: "全职猎人 (2011)",
    4181: "CLANNAD ~AFTER STORY~",
    19: "怪物",
    59978: "葬送的芙莉莲 第二季",
    57555: "电锯人 蕾洁篇"
}

def get_top_anime(limit=10):
    url = f"https://api.jikan.moe/v4/top/anime?limit={limit}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        print(f"🏆 Top {limit} Anime (Live)\n")
        for i, anime in enumerate(data['data'], 1):
            mal_id = anime['mal_id']
            title_en = anime['title_english'] or anime['title']
            title_jp = anime['title_japanese']
            title_zh = CHINESE_TITLES.get(mal_id, "暂无中文标题")
            
            score = anime['score']
            genres = ", ".join([g['name'] for g in anime['genres']])
            
            print(f"{i}. {title_en}")
            print(f"   🇨🇳 {title_zh}")
            print(f"   🇯🇵 {title_jp}")
            print(f"   ⭐ Score: {score} | Rank: {anime['rank']}")
            print(f"   📂 Genres: {genres}")
            print(f"   🔗 {anime['url']}\n")
            
    except Exception as e:
        print(f"Error fetching top anime: {e}")

if __name__ == "__main__":
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    get_top_anime(limit)
