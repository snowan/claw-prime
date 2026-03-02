import requests
import sys

def get_anime_drop():
    try:
        # Get image
        img_res = requests.get("https://api.waifu.pics/sfw/waifu").json()
        img_url = img_res.get("url")
        
        # Get random fact/quote (using neckos.best for fact since animechan is flaky)
        fact_res = requests.get("https://nekos.best/api/v2/fact").json()
        fact = fact_res["results"][0]["fact"]
        
        print(f"🎨 Anime Image: {img_url}")
        print(f"📖 Fact: {fact}")
    except Exception as e:
        print(f"Error fetching anime data: {e}")

if __name__ == "__main__":
    get_anime_drop()
