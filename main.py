import asyncio
import aiohttp
from api_client import search_players, get_player_stats
from data_processor import process_player_stats
from utils import display_player_search_results

async def main():
    async with aiohttp.ClientSession() as session:
        while True:
            name = input("Enter player name (or 'quit' to exit): ")
            if name.lower() == 'quit':
                break
            
            year = input("Enter year: ")
            
            try:
                players = await search_players(session, name, year)
                
                if not players:
                    print("No players found matching that name and year.")
                    continue
                
                print("\nMatching players:")
                display_player_search_results(players)
                
                choice = int(input("\nEnter the number of the player you want to view stats for: ")) - 1
                if choice < 0 or choice >= len(players):
                    print("Invalid selection. Please try again.")
                    continue
                
                selected_player = players[choice]
                
                stats = await get_player_stats(session, selected_player['id'], year)
                formatted_stats = process_player_stats(stats, selected_player['position'], selected_player['id'])
                
                print(f"\nStats for {selected_player['name']} ({selected_player['position']}) in {year}:")
                print(formatted_stats)
            
            except Exception as e:
                print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())