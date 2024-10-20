import asyncio
import aiohttp
from api_client import search_players, get_player_stats, get_team_schedule, get_team_stats
from data_processor import process_player_stats
from schedule_processor import get_upcoming_opponent
from team_stats_processor import process_team_stats
from utils import display_player_search_results

async def main():
    async with aiohttp.ClientSession() as session:
        while True:
            # Get player name input from user
            name = input("Enter player name (or 'quit' to exit): ")
            if name.lower() == 'quit':
                break
            
            # Get year input from user
            year = input("Enter year: ")
            
            try:
                # Search for players matching the input name and year
                players = await search_players(session, name, year)
                
                if not players:
                    print("No players found matching that name and year.")
                    continue
                
                # Display the list of matching players
                print("\nMatching players:")
                display_player_search_results(players)
                
                # Get user's choice of player
                choice = int(input("\nEnter the number of the player you want to view stats for: ")) - 1
                if choice < 0 or choice >= len(players):
                    print("Invalid selection. Please try again.")
                    continue
                
                selected_player = players[choice]
                
                # Fetch and display player stats
                stats = await get_player_stats(session, selected_player['id'], year)
                formatted_stats = process_player_stats(stats, selected_player['position'], selected_player['id'])
                print(f"\nStats for {selected_player['name']} ({selected_player['position']}) in {year}:")
                print(formatted_stats)
                
                # Fetch and display upcoming opponent
                schedule = await get_team_schedule(session, selected_player['team'], year)
                opponent_list, upcoming_opponent = get_upcoming_opponent(schedule, selected_player['team'])
                print(f"\nUpcoming opponent: {opponent_list}")
                
                # Fetch and display team stats
                team_stats = await get_team_stats(session, upcoming_opponent, year)
                formatted_team_stats = process_team_stats(team_stats)
                print(formatted_team_stats)
            
            except Exception as e:
                print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())