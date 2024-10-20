from datetime import datetime
from dateutil import parser
import pytz

def get_upcoming_opponent(schedule, team):
    # Use UTC for consistency
    current_date = datetime.now(pytz.UTC)
    upcoming_games = [game for game in schedule if parser.parse(game['start_date']).replace(tzinfo=pytz.UTC) > current_date]
    
    if not upcoming_games:
        return "No upcoming games found."
    
    next_game = upcoming_games[0]
    opponent = next_game['away_team'] if next_game['home_team'] == team else next_game['home_team']
    game_date = parser.parse(next_game['start_date']).astimezone(pytz.UTC)
    
    # Convert to Eastern Time for display
    eastern = pytz.timezone('US/Eastern')
    game_date_eastern = game_date.astimezone(eastern)
    formatted_date = game_date_eastern.strftime('%B %d, %Y')
    
    return f"{opponent} on {formatted_date}", opponent