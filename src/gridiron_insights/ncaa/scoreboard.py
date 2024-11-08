import requests
from .models import RootModel

def fetch_ncaa_scoreboard(division, year, month, day):
    url = f"https://data.ncaa.com/casablanca/scoreboard/football/{division}/{year}/{month}/{day}/scoreboard.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return RootModel(**data)
    else:
        response.raise_for_status()

# Example usage
if __name__ == "__main__":
    try:
        scoreboard = fetch_ncaa_scoreboard("fcs", 2024, 11, 1)
        print(scoreboard)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
