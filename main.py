

import requests
import os
from dotenv import load_dotenv
from collections import defaultdict

load_dotenv()
api_key=os.getenv('RIOT_API_KEY')


# Try3: add to debug unknown api key error (when code being run in Terminal)
print(f"API Key loaded: {api_key}")

if not api_key:
    print("ERROR: API key not found! Check your .env file")
    exit()


summoner_name = "Jack J"
tag_line = "ITERO"

# Get account
account_url = f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{summoner_name}/{tag_line}"
headers = {"X-Riot-Token": api_key}
account_response = requests.get(account_url, headers=headers)


# Try2: print to debug
print("Response:", account_response.json())

puuid = account_response.json()['puuid']

# Get match IDs
match_ids_url = f"https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids"
match_ids_response = requests.get(match_ids_url, headers=headers)
match_ids = match_ids_response.json()


# Try4: add print lines to debug potential API error (list? dict/?)
print("Match IDs response:", match_ids)
print("Type:", type(match_ids))



# Track wins/losses by champion
champion_stats = defaultdict(lambda: {"wins": 0, "losses": 0})

# Loop through matches and extract champion + win/loss
for match_id in match_ids[:10]:  # Start with 10
    match_url = f"https://europe.api.riotgames.com/lol/match/v5/matches/{match_id}"
    match_response = requests.get(match_url, headers=headers)
    match_data = match_response.json()

    # Find your participant data
    for participant in match_data['info']['participants']:
        if participant['puuid'] == puuid:
            champion_name = participant['championName']
            win = participant['win']

            if win:
                champion_stats[champion_name]['wins'] += 1
            else:
                champion_stats[champion_name]['losses'] += 1

# Display results
print("\n=== Champion Win Rates ===")
for champion, stats in sorted(champion_stats.items()):
    total = stats['wins'] + stats['losses']
    win_rate = (stats['wins'] / total * 100) if total > 0 else 0
    print(f"{champion}: {stats['wins']}-{stats['losses']} ({win_rate:.1f}%)")


