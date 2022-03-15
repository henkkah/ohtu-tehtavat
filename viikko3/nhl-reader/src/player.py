class Player:
    def __init__(self, name, nationality, assists, goals, penalties, team, games):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games
    
    def __str__(self):
        return self.name

    def get_nationality(self):
        return self.nationality
    
    def get_team(self):
        return self.team
    
    def get_goals(self):
        return self.goals
    
    def get_assists(self):
        return self.assists
