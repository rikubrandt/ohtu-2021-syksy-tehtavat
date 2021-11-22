class Player:
    def __init__(self, name, team, assists, goals, nationality):
        self.name = name
        self.team = team
        self.assists = assists
        self.goals = goals
        self.nationality = nationality
        self.points = self.goals + self.assists
    
    def __str__(self):
        return f"{self.name} {self.team} {self.goals}+{self.assists} = {self.goals+self.assists}"
