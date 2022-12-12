# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 18:31:31 2022

@author: David
"""
import Code_Functions as cf
import pandas as pd
import numpy as np
from baseball_scraper import statcast, batting_stats_range,batting_stats_bref, pitching_stats_range
import matplotlib.pyplot as plt


teams_list = ['HOU','SEA','ATL','NYY','NYM','LAD','SD','PHI','TB','STL','TOR','CLE']

team_statcast = cf.teams_statcast(teams_list)
team_statcast_ro = cf.teams_statcast_ro(teams_list)
team_statcast_pitch = cf.teams_statcast_pitch(teams_list)

sorted_statcast = cf.month_statcast(team_statcast)
sorted_statcast_ro = cf.month_statcast(team_statcast_ro)
sorted_statcast_pitch = cf.month_statcast(team_statcast_pitch)

months = ['4','5','6','7','8','9','10']
pitches = ['FF','FC','SL','SI','CH','CU',]
HOU = {}
ATL= {}
NYY= {}
LAD= {}
SD= {}
TB= {}
TOR= {}
SEA= {}
CLE= {}
PHI= {}
NYM= {}
STL= {}

for month in months:
    HOU[month] = {}
    ATL[month]= {}
    NYY[month]= {}
    LAD[month]= {}
    SD[month]= {}
    TB[month]= {}
    TOR[month]= {}
    SEA[month]= {}
    CLE[month]= {}
    PHI[month]= {}
    NYM[month]= {}
    STL[month]= {}
    for pitch in pitches:
        HOU[month][pitch] = cf.team_month_pitch_stat('HOU',month,sorted_statcast_pitch,'release_spin_rate')[pitch]
        
        ATL[month][pitch] = cf.team_month_pitch_stat('ATL',month,sorted_statcast_pitch,'release_spin_rate')[pitch]
        NYY[month][pitch] = cf.team_month_pitch_stat('NYY',month,sorted_statcast_pitch,'release_spin_rate')[pitch]
        LAD[month][pitch] = cf.team_month_pitch_stat('LAD',month,sorted_statcast_pitch,'release_spin_rate')[pitch]
        SD[month][pitch] = cf.team_month_pitch_stat('SD',month,sorted_statcast_pitch,'release_spin_rate')[pitch]
        TB[month][pitch] = cf.team_month_pitch_stat('TB',month,sorted_statcast_pitch,'release_spin_rate')[pitch]
        TOR[month][pitch] = cf.team_month_pitch_stat('TOR',month,sorted_statcast_pitch,'release_spin_rate')[pitch]
        SEA[month][pitch] = cf.team_month_pitch_stat('SEA',month,sorted_statcast_pitch,'release_spin_rate')[pitch]
        CLE[month][pitch] = cf.team_month_pitch_stat('CLE',month,sorted_statcast_pitch,'release_spin_rate')[pitch]
        PHI[month][pitch] = cf.team_month_pitch_stat('PHI',month,sorted_statcast_pitch,'release_spin_rate')[pitch]
        NYM[month][pitch] = cf.team_month_pitch_stat('NYM',month,sorted_statcast_pitch,'release_spin_rate')[pitch]
        STL[month][pitch] = cf.team_month_pitch_stat('STL',month,sorted_statcast_pitch,'release_spin_rate')[pitch]
        
        
        
        
HOUFF = []
ATLFF= []
NYYFF= []
LADFF= []
SDFF= []
TBFF= []
TORFF= []
SEAFF= []
CLEFF= []
PHIFF= []
NYMFF= []
STLFF= []
HOUFFc = []
ATLFFc= []
NYYFFc= []
LADFFc= []
SDFFc= []
TBFFc= []
TORFFc= []
SEAFFc= []
CLEFFc= []
PHIFFc= []
NYMFFc= []
STLFFc= []

for month in months:
    HOUFF.append(HOU[month]["FF"][0])
    HOUFFc.append(HOU[month]["FF"][1]/10)
    
    ATLFF.append(ATL[month]["FF"][0])
    ATLFFc.append(ATL[month]["FF"][1]/10)
    
    NYYFFc.append(NYY[month]["FF"][1]/10)
    NYYFF.append(NYY[month]["FF"][0])
    
    LADFF.append(LAD[month]["FF"][0])
    LADFFc.append(LAD[month]["FF"][1]/10)
    
    SDFF.append(SD[month]["FF"][0])
    SDFFc.append(SD[month]["FF"][1]/10)

    TBFF.append(TB[month]["FF"][0])
    TBFFc.append(TB[month]["FF"][1]/10)

    TORFF.append(TOR[month]["FF"][0])
    TORFFc.append(TOR[month]["FF"][1]/10)

    SEAFF.append(SEA[month]["FF"][0])
    SEAFFc.append(SEA[month]["FF"][1]/10)

    CLEFF.append(CLE[month]["FF"][0])
    CLEFFc.append(CLE[month]["FF"][1]/10)

    PHIFF.append(PHI[month]["FF"][0])
    PHIFFc.append(PHI[month]["FF"][1]/10)

    NYMFF.append(NYM[month]["FF"][0])
    NYMFFc.append(NYM[month]["FF"][1]/10)
    
    STLFF.append(STL[month]["FF"][0])
    STLFFc.append(STL[month]["FF"][1]/10)


HOUS = []
ATLS= []
NYYS= []
LADS= []
SDS= []
TBS= []
TORS= []
SEAS= []
CLES= []
PHIS= []
NYMS= []
STLS= []
HOUSc = []
ATLSc= []
NYYSc= []
LADSc= []
SDSc= []
TBSc= []
TORSc= []
SEASc= []
CLESc= []
PHISc= []
NYMSc= []
STLSc= []

for month in months:
    HOUS.append(HOU[month]["SL"][0])
    HOUSc.append(HOU[month]["SL"][1]/10)
    
    ATLS.append(ATL[month]["SL"][0])
    ATLSc.append(ATL[month]["SL"][1]/10)
    
    NYYSc.append(NYY[month]["SL"][1]/10)
    NYYS.append(NYY[month]["SL"][0])
    
    LADS.append(LAD[month]["SL"][0])
    LADSc.append(LAD[month]["SL"][1]/10)
    
    SDS.append(SD[month]["SL"][0])
    SDSc.append(SD[month]["SL"][1]/10)

    TBS.append(TB[month]["SL"][0])
    TBSc.append(TB[month]["SL"][1]/10)

    TORS.append(TOR[month]["SL"][0])
    TORSc.append(TOR[month]["SL"][1]/10)

    SEAS.append(SEA[month]["SL"][0])
    SEASc.append(SEA[month]["SL"][1]/10)

    CLES.append(CLE[month]["SL"][0])
    CLESc.append(CLE[month]["SL"][1]/10)

    PHIS.append(PHI[month]["SL"][0])
    PHISc.append(PHI[month]["SL"][1]/10)

    NYMS.append(NYM[month]["SL"][0])
    NYMSc.append(NYM[month]["SL"][1]/10)
    
    STLS.append(STL[month]["SL"][0])
    STLSc.append(STL[month]["SL"][1]/10)



def pitching_plot():
    fig, (ax1,ax2) = plt.subplots(1,2, figsize=(15,8))

    ax1.scatter(months,ATLFF,s=ATLFFc,label = 'ATL')
    ax1.scatter(months,HOUFF,s=HOUFFc,label = 'HOU')
    ax1.scatter(months,NYYFF,s=NYYFFc,label = 'NYY')
    ax1.scatter(months,LADFF,s=LADFFc,label = 'LAD')
    ax1.scatter(months,SDFF,s=SDFFc,label = 'SD')
    ax1.scatter(months,SEAFF,s=SEAFFc,label = 'SEA')
    ax1.scatter(months,PHIFF,s=PHIFFc,label = 'PHI')
    ax1.scatter(months,CLEFF,s=CLEFFc,label = 'CLE')
    ax2.scatter(months,ATLS,s=ATLSc,label = 'ATL')
    ax2.scatter(months,HOUS,s=HOUSc,label = 'HOU')
    ax2.scatter(months,NYYS,s=NYYSc,label = 'NYY')
    ax2.scatter(months,LADFF,s=LADSc,label = 'LAD')
    ax2.scatter(months,SDS,s=SDSc,label = 'SD')
    ax2.scatter(months,SEAS,s=SEASc,label = 'SEA')
    ax2.scatter(months,PHIS,s=PHISc,label = 'PHI')
    ax2.scatter(months,CLES,s=CLESc,label = 'CLE')
    ax1.legend()
    ax2.legend()
    ax1.set_xlabel('Month')
    ax2.set_xlabel('Month')

    ax1.set_ylabel('Spin Rate in rpm')
    ax2.set_ylabel('Spin Rate in rpm')
    return ax1,ax2


