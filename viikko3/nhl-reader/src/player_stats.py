from datetime import datetime

class PlayerStats:
    def top_scorers_by_nationality(self, players, nationality):
        print("Players from " + nationality + " " + str(datetime.now()) + "\n")
        nat = []
        for player in players:
            if player.get_nationality() == nationality:
                nat.append((player.get_goals()+player.get_assists(), player.get_goals(), player))
        nat = sorted(nat, key=lambda tup: (tup[0],tup[1]), reverse=True)
        for player_tpl in nat:
            player = player_tpl[2]
            print( str(player) + ' '*(20-len(str(player))) + player.get_team() + ' ' + ' '*(2-len(str(player.get_goals()))) + str(player.get_goals()) + ' + ' + ' '*(2-len(str(player.get_assists()))) + str(player.get_assists()) + ' = ' + ' '*(2-len(str(player.get_goals()+player.get_assists()))) + str(player.get_goals()+player.get_assists()) )
