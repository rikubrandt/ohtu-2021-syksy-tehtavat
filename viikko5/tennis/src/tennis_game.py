class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        if self.check_winner():
            return "Win for " + self.highestScore()
        
        if self.advantage():
            return "Advantage " + self.highestScore()
        
        if self.deuce():
            return "Deuce"
        if self.player1_score == self.player2_score:
            return self.number_to_string(self.player1_score) + "-All"
        
        return self.number_to_string(self.player1_score) + "-" +self.number_to_string(self.player2_score)

    def advantage(self):
        if self.player1_score >= 4 and self.player1_score == self.player2_score + 1:
            return True
        if self.player2_score >= 4 and self.player2_score == self.player1_score + 1:
            return True
        return False

    def check_winner(self):
        if self.player1_score >= 4 and self.player1_score >=self.player2_score + 2:
            return True
        if self.player2_score >= 4 and self.player2_score>=self.player1_score + 2:
            return True
        return False

    def highestScore(self):
        if self.player1_score > self.player2_score:
            return self.player1_name
        return self.player2_name

    def deuce(self):
        return self.player1_score >=4 and self.player1_score == self.player2_score

    def number_to_string(self, num):
        point_system = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"
        }
        return point_system[num]