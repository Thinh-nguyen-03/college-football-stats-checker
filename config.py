import json

API_BASE_URL = "https://api.collegefootballdata.com"

# Load the API key from config.json
try:
    with open('config.json') as config_file:
        config = json.load(config_file)
        API_KEY = config['API_KEY']
except FileNotFoundError:
    print("Error: config.json file not found. Please create it with your API key.")
    exit(1)
except json.JSONDecodeError:
    print("Error: config.json is not a valid JSON file.")
    exit(1)
except KeyError:
    print("Error: API_KEY not found in config.json.")
    exit(1)

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "accept": "application/json"
}

POSITION_STATS = {
    "QB": ["ATT", "COMPLETIONS", "INT", "PCT", "TD", "YDS", "YPA", "CAR", "LONG", "TD", "YDS", "YPC", "FUM", "LOST"],
    "RB": ["CAR", "LONG", "TD", "YDS", "YPC", "REC", "LONG", "TD", "YDS", "YPR", "FUM", "LOST"],
    "WR": ["REC", "LONG", "TD", "YDS", "YPR", "CAR", "LONG", "TD", "YDS", "YPC", "FUM", "LOST"],
    "TE": ["REC", "LONG", "TD", "YDS", "YPR", "CAR", "LONG", "TD", "YDS", "YPC", "FUM", "LOST"],
    "OL": ["REC"],
    "DL": ["SOLO", "TOT", "SACKS", "TFL", "QB HUR", "PD", "INT", "YDS", "TD", "AVG", "REC"],
    "LB": ["SOLO", "TOT", "SACKS", "TFL", "QB HUR", "PD", "INT", "YDS", "TD", "AVG", "REC"],
    "DB": ["SOLO", "TOT", "PD", "SACKS", "TFL", "INT", "YDS", "TD", "AVG", "REC"],
    "K": ["FGA", "FGM", "LONG", "PCT", "PTS", "XPA", "XPM"],
    "P": ["NO", "YDS", "LONG", "YPP", "In 20", "TB"],
    "KR": ["NO", "YDS", "AVG", "LONG", "TD"],
    "PR": ["NO", "YDS", "AVG", "LONG", "TD"],
    "FB": ["CAR", "LONG", "TD", "YDS", "YPC", "REC", "LONG", "TD", "YDS", "YPR", "FUM", "LOST"],
    "S": ["SOLO", "TOT", "PD", "SACKS", "TFL", "INT", "YDS", "TD", "AVG", "REC"]
}