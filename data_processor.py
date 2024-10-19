from collections import defaultdict
from config import POSITION_STATS

def process_player_stats(stats, position, player_id):
    if not stats:
        return "No stats available for this player in the specified year."

    relevant_stats = set(POSITION_STATS.get(position, []))
    player_stats = defaultdict(lambda: defaultdict(lambda: "N/A"))
    
    for stat in stats:
        if stat['playerId'] == player_id and stat['statType'] in relevant_stats:
            player_stats[stat['category']][stat['statType']] = stat['stat']
    
    if not player_stats:
        return f"No relevant stats found for position: {position}"
    
    formatted_stats = []
    for category in sorted(player_stats.keys()):
        category_stats = player_stats[category]
        if category_stats:
            formatted_stats.append(f"\n{category.upper()}:")
            for stat_type in POSITION_STATS.get(position, []):
                if stat_type in category_stats:
                    formatted_stats.append(f"  {stat_type}: {category_stats[stat_type]}")
    
    return "\n".join(formatted_stats) if formatted_stats else f"No relevant stats found for position: {position}"