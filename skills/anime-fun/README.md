# Anime Fun Agent 🌸

This project uses various public anime APIs to generate random "drops" (images, facts, and quotes) and track top-rated series.

## Features
- **Daily Drops**: Random SFW anime images via `waifu.pics` and facts via `nekos.best`.
- **Top 10 Tracker**: Live top-rated anime list with categorization (genres, scores) via `Jikan` (MyAnimeList API).
- **Personal Recommendation Engine**: Recommends top-rated anime based on your favorite genres.

## How to run
### Random Drop
```bash
python3 skills/anime-fun/drop.py
```

### Top 10 List
```bash
python3 skills/anime-fun/top_10.py
```

### Get Recommendations
Run with comma-separated genres (e.g., `action,sci-fi,fantasy`).
```bash
python3 skills/anime-fun/recommend.py "action,sci-fi,fantasy"
```
