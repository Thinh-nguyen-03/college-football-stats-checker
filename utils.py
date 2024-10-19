def display_player_search_results(players):
    for i, player in enumerate(players, 1):
        print(f"{i}. {player['name']} - {player['team']} ({player['position']})")