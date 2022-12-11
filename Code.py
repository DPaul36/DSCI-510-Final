# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 12:47:39 2022
Code for sorting data
@author: David
"""
#Import functions and modules
import pandas as pd
import numpy as np
from baseball_scraper import statcast, batting_stats_range,batting_stats_bref, pitching_stats_range
import matplotlib.pyplot as plt


def sort_data(data):
    '''
    

    Parameters
    ----------
    data : Pandas Dataframe.

    Returns
    -------
    team_data : Sorted dictionary of the data by team.

    '''
    team_data = {}

    for i in range(len(data)):
                                      
        if data.iloc[i]['Tm'] not in team_data:
            if data.iloc[i]['Tm'] == 'New York':
                if data.iloc[i]['Lev'] == 'Maj-AL':
                    if 'New York Yankees' not in team_data:
                        team_data['New York Yankees'] = {data.iloc[i]['Name']:data.iloc[i,0:]}
                    else:
                        team_data['New York Yankees'][data.iloc[i]['Name']] = data.iloc[i,0:]
                else:
                    if 'New York Mets' not in team_data:
                        team_data['New York Mets'] = {data.iloc[i]['Name']:data.iloc[i,0:]}
                    else:
                        team_data['New York Mets'][data.iloc[i]['Name']] = data.iloc[i,0:]


            elif data.iloc[i]['Tm'] == 'Chicago':
                if data.iloc[i]['Lev'] == 'Maj-AL':
                    if 'Chicago White Sox' not in team_data:
                        team_data['Chicago White Sox'] = {data.iloc[i]['Name']:data.iloc[i,0:]}
                    else:
                        team_data['Chicago White Sox'][data.iloc[i]['Name']] = data.iloc[i,0:]
                else:
                    if 'Chicago Cubs' not in team_data:
                        team_data['Chicago Cubs'] = {data.iloc[i]['Name']:data.iloc[i,0:]}
                    else:
                        team_data['Chicago Cubs'][data.iloc[i]['Name']] = data.iloc[i,0:]    


            elif data.iloc[i]['Tm'] == 'Los Angeles':
                if data.iloc[i]['Lev'] == 'Maj-AL':
                    if 'Los Angeles Angels' not in team_data:
                        team_data['Los Angeles Angels'] = {data.iloc[i]['Name']:data.iloc[i,0:]}
                    else:
                        team_data['Los Angeles Angels'][data.iloc[i]['Name']] = data.iloc[i,0:]
                else:
                    if 'Los Angeles Dodgers' not in team_data:
                        team_data['Los Angeles Dodgers'] = {data.iloc[i]['Name']:data.iloc[i,0:]}
                    else:
                        team_data['Los Angeles Dodgers'][data.iloc[i]['Name']] = data.iloc[i,0:]                             


            else:
                team_data[data.iloc[i]['Tm']] = {data.iloc[i]['Name']:data.iloc[i,0:]}
        else:
            team_data[data.iloc[i]['Tm']][data.iloc[i]['Name']] = data.iloc[i,0:]
    return team_data




def month_data(stats):
    '''
    

    Parameters
    ----------
    stats : Function to call for web scraping. Can use any of the functions 
            imported from Baseball Scraper module

    Returns
    -------
    team_data : Dictionary of data sorted by month and team.

    '''
    Months = ["Apr",'May','June','July','Aug','Sep','Oct']
    s = [4,6,9]
    m = 4
    month_stats = {}
    i=0
    while m < 11:
        if m in s:

            month_stats[Months[i]] = stats('2022-0'+str(m)+'-01', '2022-0'+str(m)+'-30')
        elif m ==10:
            month_stats[Months[i]] = stats('2022-'+str(m)+'-01', '2022-'+str(m)+'-31')
        else:
            month_stats[Months[i]] = stats('2022-0'+str(m)+'-01', '2022-0'+str(m)+'-31')
        m+=1
        i+=1
    team_data = {}
    for month in month_stats:
        team_data[month] = sort_data(month_stats[month])
    return team_data


def team_ops(team,month,data):
    '''
    

    Parameters
    ----------
    team : Team city string - If it is a city that has more than one team, specify
            the team. ie. 'New York Yankees' or 'New York Mets'
    month : Str. month abbreviation. Only works for in season months from 'Apr'
            to 'Oct'
    data : Input a sorted dictionary using the 'month_data' function.

    Returns
    -------
    Average Team OPS for the given team and month

    '''
    team_ops = []
    pa=0
    if team not in data[month]:
        return 0
    for player_name in data[month][team]:
        
        if data[month][team][player_name]['PA'] == 0:
            pass
        else:
            
            team_ops.append(data[month][team][player_name]['OPS']*data[month][team][player_name]['PA'])
            pa += data[month][team][player_name]['PA']
    team_ops = sum(team_ops)/pa
    return team_ops

def month_ops(team,data):
    '''
    

    Parameters
    ----------
    team : Team city string - If it is a city that has more than one team, specify
            the team. ie. 'New York Yankees' or 'New York Mets'.
    data : Input a sorted dictionary using the 'month_data' function.

    Returns
    -------
    ops : list of monthly OPS averages

    '''
    
    Months = ["Apr",'May','June','July','Aug','Sep','Oct']
    ops = []
    for month in Months:
        ops.append(team_ops(team,month,data))
    return ops



'''
Statcast Functions
These functions sort the necesarry data pulled from Statcast using Baseball 
Savant. Files are saved under the data folder
'''

teams_list = ['HOU','SEA','ATL','NYY','NYM','LAD','SD','PHI','TB','STL','TOR','CLE']
def teams_statcast(teams = teams_list):
    '''
    

    Parameters
    ----------
    teams : List of teams in to be searched. The default is the list of teams
            provided above - the 12 teams in the 2022 MLB Playoffs

    Returns
    -------
    team_statcast : Output is a pandas dataframe of the data pulled from the
                    batting csv file.

    '''
    team_statcast = {}
    for team in teams:
        team_statcast[team]=pd.read_csv('Data/'+team+'.csv')
    return team_statcast
def teams_statcast_ro(teams):
    '''
    
    Parameters
    ----------
    teams : List of teams in to be searched. The default is the list of teams
            provided above - the 12 teams in the 2022 MLB Playoffs

    Returns
    -------
    team_statcast : Output is a pandas dataframe of the data pulled from the
                    batting with runners on base csv file.

    '''
    
    team_statcast = {}
    for team in teams:
        team_statcast[team]=pd.read_csv('Data_ROB/'+team+'.csv')
    return team_statcast
def teams_statcast_pitch(teams):
    '''
    
    Parameters
    ----------
    teams : List of teams in to be searched. The default is the list of teams
            provided above - the 12 teams in the 2022 MLB Playoffs

    Returns
    -------
    team_statcast : Output is a pandas dataframe of the data pulled from the
                    pitching csv file.

    '''    
    team_statcast = {}
    for team in teams:
        team_statcast[team]=pd.read_csv('Data_pitch/'+team+'.csv')
    return team_statcast
