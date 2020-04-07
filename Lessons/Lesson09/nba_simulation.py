# NBA Simulation
import csv
import random

# Team Object
class Team:

    def __init__(self):
        self.m_name = None
        self.m_code = None
        self.m_division = None
        self.m_conference = None
        self.m_city = None
        self.m_state = None

        self.m_players = []

    def NumberOfPlayers(self):
        return len(self.m_players)

# Player Object
class Player:

    def __init__(self):
        self.m_name = None
        self.m_team_code = None
        self.m_games_played = None
        self.m_avg_points = None
        self.m_avg_rebounds = None
        self.m_avg_assists = None

# Game Object
class Game:
    def __init__(self, home_, away_):
        self.m_home = home_
        self.m_away = away_

    def FinalScore(self):
        # figure out how to pick the winner

        return ((self.m_home, self.m_away),())

def LoadTeams():
    teams = {}

    with open(r'..\data\nba_teams.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        seen_index = False
        name_index = None
        for row in csv_reader:
            if not seen_index:
                # Name	Code	Division	Conference	City	State
                name_index = {name:index for index, name in enumerate(row)}
                seen_index = True
            else:
                team_name = row[name_index['Name']]
                team_code = row[name_index['Code']]
                division = row[name_index['Division']]
                conference = row[name_index['Conference']]

                team = Team()
                team.m_name = team_name
                team.m_code = team_code
                team.m_division = division
                team.m_conference = conference
                
                teams[team_code] = team

        return teams


def LoadPlayers(teams_):

    with open(r'..\data\nba_players_all_seasons.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        seen_index = False
        name_index = None
        for row in csv_reader:
            if not seen_index:
                name_index = {name:index for index, name in enumerate(row)}
                seen_index = True
            else:
                player_name = row[name_index['player_name']]
                team_code = row[name_index['team_abbreviation']]
                games_played = row[name_index['gp']]
                avg_points = row[name_index['pts']]
                avg_reb = row[name_index['reb']]
                avg_ast = row[name_index['ast']]
                season = row[name_index['season']]

                if season != '2019-20':
                    continue

                player = Player()
                player.m_name = player_name
                player.m_team_code = team_code
                player.m_games_played = games_played
                player.m_avg_points = avg_points
                player.m_avg_reb = avg_reb
                player.m_avg_assists = avg_ast

                teams_[team_code].m_players.append(player)

    return teams_


def DisplayTeams(teams_):
    for team in teams_.values():
        print(team.m_name);
            
        for player in team.players():
            print(player.m_name)
