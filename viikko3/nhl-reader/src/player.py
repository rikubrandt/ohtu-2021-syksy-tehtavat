class Player:
    def __init__(self, name, team, assists, goals, nationality):
        self.name = name
        self.team = team
        self.assists = assists
        self.goals = goals
        self.nationality = nationality
    
    def __str__(self):
        return "%s team %s goals %d assists %d" % (self.name, self.team, self.goals, self.assists)
