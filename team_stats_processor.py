def categorize_stat(stat_name):
    categories = {
        'Passing': ['passCompletions', 'passAttempts', 'passingYards', 'passingTDs', 'interceptions'],
        'Rushing': ['rushingAttempts', 'rushingYards', 'rushingTDs'],
        'Total Offense': ['totalYards', 'netPassingYards'],
        'Downs': ['firstDowns', 'thirdDowns', 'thirdDownConversions', 'fourthDowns', 'fourthDownConversions'],
        'Defense': ['tacklesForLoss', 'sacks', 'passesIntercepted', 'interceptionYards', 'interceptionTDs'],
        'Special Teams': ['puntReturns', 'puntReturnYards', 'puntReturnTDs', 'kickReturns', 
                          'kickReturnYards', 'kickReturnTDs'],
        'Turnovers': ['turnovers', 'fumblesLost', 'fumblesRecovered'],
        'Time': ['possessionTime'],
        'Penalties': ['penalties', 'penaltyYards'],
        'General': ['games']
    }

    for category, stats in categories.items():
        if stat_name in stats:
            return category
    
    return 'Other'

def process_team_stats(stats):
    if not stats:
        return "No team stats available for this season."

    categorized_stats = {}

    for stat in stats:
        stat_name = stat['statName']
        stat_value = stat['statValue']
        category = categorize_stat(stat_name)

        if category not in categorized_stats:
            categorized_stats[category] = []
        categorized_stats[category].append(f"{stat_name}: {stat_value}")

    formatted_stats = ["Team Stats:"]
    for category, stats in categorized_stats.items():
        formatted_stats.append(f"\n{category}:")
        formatted_stats.extend([f"  {stat}" for stat in stats])

    return "\n".join(formatted_stats)


