SCORE_TEXT = ["Love", "Fifteen", "Thirty", "Forty"]
FIRST_PHASE_TIE = "All"
END_PHASE_THRESHOLD = 4
END_PHASE_TIE = "Deuce"
ADVANTAGE_TEXT = "Advantage"
WIN_TEXT = "Win for"

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.names = [player1_name, player2_name]
        self.scores = [0, 0]

    def won_point(self, player_name):
        player = self.names.index(player_name)
        self.scores[player] += 1

    def get_score(self):
        winner = self._get_winner()
        if winner is not None:
            return self._get_winner_text(winner)
        else:
            if not self._is_end_phase():
                return self._get_first_phase_text()
            else:
                return self._get_end_phase_text()

    def _is_end_phase(self):
        return max(self.scores) >= END_PHASE_THRESHOLD

    def _get_winner(self):
        if not self._is_end_phase():
            return None
        else:
            for player in range(2):
                other_player = 1 if player == 0 else 0
                if self.scores[player] >= self.scores[other_player] + 2:
                    return player
            return None

    def _get_winner_text(self, winner):
        name = self.names[winner]
        return f"{WIN_TEXT} {name}"

    def _get_first_phase_text(self):
        human_scores = [SCORE_TEXT[score] for score in self.scores]
        if self.scores[0] == self.scores[1]:
            return f"{human_scores[0]}-{FIRST_PHASE_TIE}"
        else:
            return "-".join(human_scores)

    def _get_end_phase_text(self):
        if self.scores[0] == self.scores[1]:
            return END_PHASE_TIE
        else:
            advantage_player = 0 if self.scores[0] > self.scores[1] else 1
            name = self.names[advantage_player]
            return f"{ADVANTAGE_TEXT} {name}"

