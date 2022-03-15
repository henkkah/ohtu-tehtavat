from player_reader import PlayerReader
from player_stats import PlayerStats

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    nationality = "FIN"
    
    pr = PlayerReader(url)
    players = pr.get_players()
    
    ps = PlayerStats()
    ps.top_scorers_by_nationality(players, nationality)
    
    '''
    response = requests.get(url).json()

    #print("JSON-muotoinen vastaus:")
    #print(response)

    players = []

    for player_dict in response:
        player = Player(
            player_dict['name'],
            player_dict['nationality'],
            player_dict['assists'],
            player_dict['goals'],
            player_dict['penalties'],
            player_dict['team'],
            player_dict['games']
        )

        players.append(player)
    '''
    '''
    print("Players from FIN " + str(datetime.now()) + "\n")
    for player in players:
        if player.get_nationality() == 'FIN':
            print(str(player) + ' team ' + player.get_team() + ' goals ' + str(player.get_goals()) + ' assists ' + str(player.get_assists()))
    
    print('\n-------------------------\n')
    '''
    '''
    print("Players from FIN " + str(datetime.now()) + "\n")
    finns = []
    for player in players:
        if player.get_nationality() == 'FIN':
            finns.append((player.get_goals()+player.get_assists(), player.get_goals(), player))
    finns = sorted(finns, key=lambda tup: (tup[0],tup[1]), reverse=True)
    for player_tpl in finns:
        player = player_tpl[2]
        print( str(player) + ' '*(20-len(str(player))) + player.get_team() + ' ' + ' '*(2-len(str(player.get_goals()))) + str(player.get_goals()) + ' + ' + ' '*(2-len(str(player.get_assists()))) + str(player.get_assists()) + ' = ' + ' '*(2-len(str(player.get_goals()+player.get_assists()))) + str(player.get_goals()+player.get_assists()) )
    '''
    
if __name__ == "__main__":
    main()
