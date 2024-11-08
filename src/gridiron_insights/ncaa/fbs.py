import sys
import requests

from gridiron_insights.ncaa.scoreboard import fetch_ncaa_scoreboard, display_scores

if __name__ == "__main__":
    try:
        scoreboard = fetch_ncaa_scoreboard("fbs", 2024, 11)
        display_scores(scoreboard)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

    sys.exit(0)