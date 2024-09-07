# tpss_classes.py

import math
from datetime import datetime, timedelta

class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.rank = 0
        self.tournament_history = []
        self.participation_points = 0
        self.match_points = 0
        self.opponent_difficulty_multiplier = 1

    def update_points(self, wins, placements, opponent_difficulty):
        self.participation_points += 10
        self.match_points += wins * 5 + placements * 2
        self.points += self.participation_points + self.match_points * opponent_difficulty

    def calculate_seed(self, coefficient):
        if self.points > 0:
            self.rank = math.log(self.points) * coefficient
        else:
            self.rank = 0
        return self.rank

    def adjust_rank(self):
        if self.points >= 100:
            self.rank += 1
        else:
            self.rank = max(0, self.rank - 1)
        return self.rank


class Tournament:
    def __init__(self, name, difficulty_multiplier=1.0):
        self.name = name
        self.difficulty_multiplier = difficulty_multiplier
        self.match_results = {}

    def update_match_results(self, player_name, wins, placements):
        self.match_results[player_name] = {"wins": wins, "placements": placements}

    def distribute_points(self, players):
        for player in players:
            if player.name in self.match_results:
                results = self.match_results[player.name]
                player.update_points(results['wins'], results['placements'], self.difficulty_multiplier)


class TPSS:
    def __init__(self, coefficient=1.0, points_correction_interval=7):
        self.players = []
        self.coefficient = coefficient
        self.points_correction_interval = points_correction_interval
        self.last_correction = datetime.now()

    def add_player(self, player):
        self.players.append(player)

    def assign_points_based_on_results(self, tournament):
        tournament.distribute_points(self.players)

    def calculate_dynamic_rank(self):
        for player in self.players:
            player.calculate_seed(self.coefficient)
            player.adjust_rank()

    def verify_and_correct_points(self):
        current_time = datetime.now()
        if current_time >= self.last_correction + timedelta(days=self.points_correction_interval):
            for player in self.players:
                if player.points > 1000:
                    player.points = 1000
            self.last_correction = current_time
