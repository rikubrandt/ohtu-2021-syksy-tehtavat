

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality):
        players = self.reader.get_players()
        filtered = filter(lambda x: x.nationality == nationality, players)
        newList = sorted(filtered, key=lambda x: x.points, reverse=True)
        return newList


