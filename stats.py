from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
import time

def getPlayerName(name):
    player = players.find_players_by_full_name(name)
    if(players):
        return player[0]['id']
    return None

def getPlayersStats(player_ID):
    time.sleep(1.5)
    careerStats = playercareerstats.PlayerCareerStats(player_id=player_ID)
    dataFrames = careerStats.get_data_frames()[0]

    seasonStats = dataFrames[dataFrames['SEASON_ID'] == "2024-25"]
    
    if(seasonStats.empty):
        print("Player data could not be found for this season")
        return None
    return seasonStats.iloc[0]

playerName = input("Enter player name: ")
playerID = getPlayerName(playerName)

if(playerID):
    stats = getPlayersStats(playerID)
    games_Played_this_Season = stats['GP']
    if(stats is not None):
        print(f"{playerName}'s stats this Season are : ")
        print(f"PTS: {stats['PTS'] / games_Played_this_Season:.1f}")
        print(f"REB: {stats['REB'] / games_Played_this_Season:.1f}")
        print(f"AST: {stats['AST'] / games_Played_this_Season:.1f}")
        print(f"MIN: {stats['MIN'] / games_Played_this_Season:.1f}")
    else:
        print("Stats not available for this player yet.")
else:
    print("Player could not be found")


