# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 11:48:33 2020

@author: jimmy
"""

# NBA Simulation
import csv
import random
import datetime

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
        
        self.m_wins = 0
        self.m_losses = 0
        

    def NumberOfPlayers(self):
        return len(self.m_players)

    def GetStartingPlayers(self):
        starters = []

        curr_index = 0        
        while len(starters) < 5:
            disabled_factor = random.random()
            if disabled_factor > 0.5:
                disabled = True
                curr_index += 1
                
            player = self.m_players[curr_index]
            
            starters.append(player)
            curr_index += 1
            
        return starters
    
    def SortPlayers(self):
        self.m_players.sort(key=lambda x: x.m_avg_points, reverse=True)


# Player Object
class Player:

    def __init__(self):
        self.m_name = None
        self.m_team_code = None
        self.m_games_played = None
        self.m_avg_points = None
        self.m_avg_rebounds = None
        self.m_avg_assists = None

    def __repr__(self):
        return '''{0}'''.format(self.m_name)
    
# Game Object
class Game:
    def __init__(self):
        self.m_game_id = None
        self.m_game_date = None
        
        self.m_away_team = None
        self.m_home_team = None
        

    def __repr__(self):
        return '''Game: {0}, Date: {1}, {2}-{3}'''.format(self.m_game_id, 
                        self.m_game_date, self.m_away_team, self.m_home_team)
        
    def PlayGame(self):
        
        home_starters = self.m_home_team.GetStartingPlayers()
        home_total_points = 0
        for player in home_starters:
            home_total_points += player.m_avg_points

        rand_factor = random.random() * 2.0
        home_total_points *= rand_factor
        home_total_points *= 1.1
        
        away_starters = self.m_away_team.GetStartingPlayers()
        away_total_points = 0
        for player in away_starters:
            away_total_points += player.m_avg_points
        
        rand_factor = random.random() * 2.0
        away_total_points *= rand_factor
        
        if home_total_points == away_total_points:
            home_total_points += random.random() * 15
            away_total_points += random.random() * 15
            
        if away_total_points > home_total_points:
            self.m_away_team.m_wins += 1
            self.m_home_team.m_losses += 1
        else:
            self.m_home_team.m_wins += 1
            self.m_away_team.m_losses += 1
            
        return (round(away_total_points), round(home_total_points))
        
    
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
                games_played = int(row[name_index['gp']])
                avg_points = float(row[name_index['pts']])
                avg_reb = float(row[name_index['reb']])
                avg_ast = float(row[name_index['ast']])
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

        for team in teams_.values():
            team.SortPlayers()
            
    return teams_

def LoadGames(teams_):
    games = {}

    with open(r'..\data\nba_full_schedule_2019_2020.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        seen_index = False
        name_index = None
        for row in csv_reader:
            if not seen_index:
                # game_id,	game_date, away_team, home_team
                name_index = {name:index for index, name in enumerate(row)}
                seen_index = True
            else:
                game_id = row[name_index['game_id']]
                game_date_str = row[name_index['game_date']]
                game_date = datetime.datetime.strptime(game_date_str, '%m/%d/%Y')
                
                away_team = row[name_index['away_team']]
                home_team = row[name_index['home_team']]

                game = Game()
                game.m_game_id = game_id
                game.m_game_date = game_date
                game.m_away_team = teams_[away_team]
                game.m_home_team = teams_[home_team]
                
                if game_date not in games:
                    games[game_date] = []
                    
                games[game_date].append(game)

        return games
    
def GetConferenceTeams(teams_, conference_):
    conf_teams = []
    for team in teams_.values():
        if team.m_conference == conference_:
            conf_teams.append(team)

    return conf_teams

def DisplayTeams(allteams_, withplayers_ = False):
    allteams_.sort(key=lambda x:x.m_wins, reverse=True)
    
    for team in allteams_:
        print(team.m_name, team.m_wins)
            
        if withplayers_ == True:
            for player in team.m_players:
                print('\t',player.m_name)

def PlayGames(games_):
    for day,days_games in games_.items():
        print(day.strftime('%m/%d/%y'))
            
        for game in days_games:
            print('\t',game.m_away_team.m_code, game.m_home_team.m_code, game.PlayGame())

def main():
        
    # Load the teams. players and games
    teams = LoadTeams()
    LoadPlayers(teams)
        
    games = LoadGames(teams)
        
    #DisplayTeams(teams)
    PlayGames(games)
    
    eastern = GetConferenceTeams(teams, 'Eastern')
    western = GetConferenceTeams(teams, 'Western')
    
    # show standings
    print()
    print()
    
    print('Eastern Conference Standings')
    DisplayTeams(eastern)
    
    print()
    print()
    
    print('Western Conference Standings')
    DisplayTeams(western)
    
if __name__ == '__main__':
    main()
    
# End of File
