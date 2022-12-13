# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 14:06:10 2022
Code for building plots
@author: David
"""
import Code_Functions as cf
from baseball_scraper import batting_stats_range
import matplotlib.pyplot as plt



teams_list = ['HOU','SEA','ATL','NYY','NYM','LAD','SD','PHI','TB','STL','TOR','CLE']
Months = ["Apr",'May','June','July','Aug','Sep','Oct']
#month_team_data = cf.month_data(batting_stats_range)



#houston_ops = cf.month_ops('Houston',month_team_data)
#yankees_ops = cf.month_ops('New York Yankees',month_team_data)
#dodgers_ops = cf.month_ops('Los Angeles Dodgers',month_team_data)
#mets_ops = cf.month_ops('New York Mets',month_team_data)
#philly_ops = cf.month_ops('Philadelphia',month_team_data)
#braves_ops = cf.month_ops('Atlanta',month_team_data)
#padres_ops = cf.month_ops('San Diego',month_team_data)
#guard_ops = cf.month_ops('Cleveland',month_team_data)
#seattle_ops = cf.month_ops('Seattle',month_team_data)
#tampa_ops = cf.month_ops('Tampa Bay',month_team_data)
#cards_ops = cf.month_ops('St. Louis',month_team_data)
#toronto_ops = cf.month_ops('Toronto',month_team_data)


team_statcast = cf.teams_statcast(teams_list)
team_statcast_ro = cf.teams_statcast_ro(teams_list)
team_statcast_pitch = cf.teams_statcast_pitch(teams_list)

sorted_statcast = cf.month_statcast(team_statcast)
sorted_statcast_ro = cf.month_statcast(team_statcast_ro)
sorted_statcast_pitch = cf.month_statcast(team_statcast_pitch)

months = ['4','5','6','7','8','9','10']
HOU = []
ATL= []
NYY= []
LAD= []
SD= []
TB= []
TOR= []
SEA= []
CLE= []
PHI= []
NYM= []
STL= []

for month in months:
    HOU.append(cf.team_month_stat('HOU',month,sorted_statcast_ro,'launch_speed')*cf.team_month_stat('HOU',month,sorted_statcast_ro,'launch_angle'))
    ATL.append(cf.team_month_stat('ATL',month,sorted_statcast_ro,'launch_speed')*cf.team_month_stat('ATL',month,sorted_statcast_ro,'launch_angle'))
    NYY.append(cf.team_month_stat('NYY',month,sorted_statcast_ro,'launch_speed')*cf.team_month_stat('NYY',month,sorted_statcast_ro,'launch_angle'))
    LAD.append(cf.team_month_stat('LAD',month,sorted_statcast_ro,'launch_speed')*cf.team_month_stat('LAD',month,sorted_statcast_ro,'launch_angle'))
    SD.append(cf.team_month_stat('SD',month,sorted_statcast_ro,'launch_speed')*cf.team_month_stat('SD',month,sorted_statcast_ro,'launch_angle'))
    TOR.append(cf.team_month_stat('TOR',month,sorted_statcast_ro,'launch_speed')*cf.team_month_stat('TOR',month,sorted_statcast_ro,'launch_angle'))
    TB.append(cf.team_month_stat('TB',month,sorted_statcast_ro,'launch_speed')*cf.team_month_stat('TB',month,sorted_statcast_ro,'launch_angle'))
    STL.append(cf.team_month_stat('STL',month,sorted_statcast_ro,'launch_speed')*cf.team_month_stat('STL',month,sorted_statcast_ro,'launch_angle'))
    CLE.append(cf.team_month_stat('CLE',month,sorted_statcast_ro,'launch_speed')*cf.team_month_stat('CLE',month,sorted_statcast_ro,'launch_angle'))
    SEA.append(cf.team_month_stat('SEA',month,sorted_statcast_ro,'launch_speed')*cf.team_month_stat('SEA',month,sorted_statcast_ro,'launch_angle'))
    NYM.append(cf.team_month_stat('NYM',month,sorted_statcast_ro,'launch_speed')*cf.team_month_stat('NYM',month,sorted_statcast_ro,'launch_angle'))
    PHI.append(cf.team_month_stat('PHI',month,sorted_statcast_ro,'launch_speed')*cf.team_month_stat('PHI',month,sorted_statcast_ro,'launch_angle'))
    
for month in months:
    HOU.append(cf.team_month_stat('HOU',month,sorted_statcast_ro,'launch_speed'))
    ATL.append(cf.team_month_stat('ATL',month,sorted_statcast_ro,'launch_speed'))
    NYY.append(cf.team_month_stat('NYY',month,sorted_statcast_ro,'launch_speed'))
    LAD.append(cf.team_month_stat('LAD',month,sorted_statcast_ro,'launch_speed'))
    SD.append(cf.team_month_stat('SD',month,sorted_statcast_ro,'launch_speed'))
    TOR.append(cf.team_month_stat('TOR',month,sorted_statcast_ro,'launch_speed'))
    TB.append(cf.team_month_stat('TB',month,sorted_statcast_ro,'launch_speed'))
    STL.append(cf.team_month_stat('STL',month,sorted_statcast_ro,'launch_speed'))
    CLE.append(cf.team_month_stat('CLE',month,sorted_statcast_ro,'launch_speed'))
    SEA.append(cf.team_month_stat('SEA',month,sorted_statcast_ro,'launch_speed'))
    NYM.append(cf.team_month_stat('NYM',month,sorted_statcast_ro,'launch_speed'))
    PHI.append(cf.team_month_stat('PHI',month,sorted_statcast_ro,'launch_speed'))
        

for month in months:
    HOU.append(cf.team_month_stat('HOU',month,sorted_statcast_ro,'launch_angle'))
    ATL.append(cf.team_month_stat('ATL',month,sorted_statcast_ro,'launch_angle'))
    NYY.append(cf.team_month_stat('NYY',month,sorted_statcast_ro,'launch_angle'))
    LAD.append(cf.team_month_stat('LAD',month,sorted_statcast_ro,'launch_angle'))
    SD.append(cf.team_month_stat('SD',month,sorted_statcast_ro,'launch_angle'))
    TOR.append(cf.team_month_stat('TOR',month,sorted_statcast_ro,'launch_angle'))
    TB.append(cf.team_month_stat('TB',month,sorted_statcast_ro,'launch_angle'))
    STL.append(cf.team_month_stat('STL',month,sorted_statcast_ro,'launch_angle'))
    CLE.append(cf.team_month_stat('CLE',month,sorted_statcast_ro,'launch_angle'))
    SEA.append(cf.team_month_stat('SEA',month,sorted_statcast_ro,'launch_angle'))
    NYM.append(cf.team_month_stat('NYM',month,sorted_statcast_ro,'launch_angle'))
    PHI.append(cf.team_month_stat('PHI',month,sorted_statcast_ro,'launch_angle'))
    
    
for month in months:
    HOU.append(cf.team_month_stat('HOU',month,sorted_statcast,'launch_speed')*cf.team_month_stat('HOU',month,sorted_statcast,'launch_angle'))
    ATL.append(cf.team_month_stat('ATL',month,sorted_statcast,'launch_speed')*cf.team_month_stat('ATL',month,sorted_statcast,'launch_angle'))
    NYY.append(cf.team_month_stat('NYY',month,sorted_statcast,'launch_speed')*cf.team_month_stat('NYY',month,sorted_statcast,'launch_angle'))
    LAD.append(cf.team_month_stat('LAD',month,sorted_statcast,'launch_speed')*cf.team_month_stat('LAD',month,sorted_statcast,'launch_angle'))
    SD.append(cf.team_month_stat('SD',month,sorted_statcast,'launch_speed')*cf.team_month_stat('SD',month,sorted_statcast,'launch_angle'))
    TOR.append(cf.team_month_stat('TOR',month,sorted_statcast,'launch_speed')*cf.team_month_stat('TOR',month,sorted_statcast,'launch_angle'))
    TB.append(cf.team_month_stat('TB',month,sorted_statcast,'launch_speed')*cf.team_month_stat('TB',month,sorted_statcast,'launch_angle'))
    STL.append(cf.team_month_stat('STL',month,sorted_statcast,'launch_speed')*cf.team_month_stat('STL',month,sorted_statcast,'launch_angle'))
    CLE.append(cf.team_month_stat('CLE',month,sorted_statcast,'launch_speed')*cf.team_month_stat('CLE',month,sorted_statcast,'launch_angle'))
    SEA.append(cf.team_month_stat('SEA',month,sorted_statcast,'launch_speed')*cf.team_month_stat('SEA',month,sorted_statcast,'launch_angle'))
    NYM.append(cf.team_month_stat('NYM',month,sorted_statcast,'launch_speed')*cf.team_month_stat('NYM',month,sorted_statcast,'launch_angle'))
    PHI.append(cf.team_month_stat('PHI',month,sorted_statcast,'launch_speed')*cf.team_month_stat('PHI',month,sorted_statcast,'launch_angle'))   
    
def batting_plots():
    H = 8*8
    A = 2*8
    S = 2*8
    C = 2*8
    N = 4*8
    PH = 6*8
    P = 4*8
    L = 2*8
    
    
    fig, (ax1,ax2) = plt.subplots(1,2, figsize=(15,8))
    fig, (ax3,ax4) = plt.subplots(1,2, figsize=(15,8))

    ax1.scatter(months,ATL[0:7],s=A,label = 'ATL')
    ax1.scatter(months,HOU[0:7],s=H,label = 'HOU')
    ax1.scatter(months,NYY[0:7],s=N,label = 'NYY')
    ax1.scatter(months,LAD[0:7],s=L,label = 'LAD')
    ax1.scatter(months,SD[0:7],s=P,label = 'SD')
    ax1.scatter(months,SEA[0:7],s=S,label = 'SEA')
    ax1.scatter(months,PHI[0:7],s=PH,label = 'PHI')
    ax1.scatter(months,CLE[0:7],s=C,label = 'CLE')

    ax2.scatter(months,ATL[7:14],s=A,label = 'ATL')
    ax2.scatter(months,HOU[7:14],s=H,label = 'HOU')
    ax2.scatter(months,NYY[7:14],s=N,label = 'NYY')
    ax2.scatter(months,LAD[7:14],s=L,label = 'LAD')
    ax2.scatter(months,SD[7:14],s=P,label = 'SD')
    ax2.scatter(months,SEA[7:14],s=S,label = 'SEA')
    ax2.scatter(months,PHI[7:14],s=PH,label = 'PHI')
    ax2.scatter(months,CLE[7:14],s=C,label = 'CLE')

    ax3.scatter(months,ATL[14:21],s=A,label = 'ATL')
    ax3.scatter(months,HOU[14:21],s=H,label = 'HOU')
    ax3.scatter(months,NYY[14:21],s=N,label = 'NYY')
    ax3.scatter(months,LAD[14:21],s=L,label = 'LAD')
    ax3.scatter(months,SD[14:21],s=P,label = 'SD')
    ax3.scatter(months,SEA[14:21],s=S,label = 'SEA')
    ax3.scatter(months,PHI[14:21],s=PH,label = 'PHI')
    ax3.scatter(months,CLE[14:21],s=C,label = 'CLE')
    
    
    ax4.scatter(months,ATL[21:28],s=A,label = 'ATL')
    ax4.scatter(months,HOU[21:28],s=H,label = 'HOU')
    ax4.scatter(months,NYY[21:28],s=N,label = 'NYY')
    ax4.scatter(months,LAD[21:28],s=L,label = 'LAD')
    ax4.scatter(months,SD[21:28],s=P,label = 'SD')
    ax4.scatter(months,SEA[21:28],s=S,label = 'SEA')
    ax4.scatter(months,PHI[21:28],s=PH,label = 'PHI')
    ax4.scatter(months,CLE[21:28],s=C,label = 'CLE')
    #ax4.scatter(months,houston_ops,s=H,label='HOU')
    #ax4.scatter(months,braves_ops,s=A,label='ATL')
    #ax4.scatter(months,philly_ops,s=PH,label='PHI')
    #ax4.scatter(months,yankees_ops,s=N,label='NYY')
    #ax4.scatter(months,guard_ops,s=C,label='CLE')
    #ax4.scatter(months,dodgers_ops,s=L,label='LAD')
    #ax4.scatter(months,padres_ops,s=P,label='SD')
    #ax4.scatter(months,seattle_ops,s=S,label='SEA')

    
    
    
    
    
    
    ax1.legend()
    ax2.legend()
    ax3.legend()
    ax4.legend()
    
    ax1.set_xlabel('Month')
    ax2.set_xlabel('Month')
    ax3.set_xlabel('Month')
    ax4.set_xlabel('Month')

    ax1.set_ylabel('Launch Velo x Angle')
    ax2.set_ylabel('Exit Velocity')
    ax3.set_ylabel('Launch Angle')
    ax4.set_ylabel('Launch Velo x Angle')

    ax1.set_title('Launch Angle x Velocity Runners on Base') 
    ax2.set_title('Launch Angle')
    ax3.set_title('Exit Velocity')
    ax4.set_title('Launch Angle x Velocity')

    return ax1,ax2,ax3,ax4




def final_4():
    H = 8*8

    N = 4*8
    PH = 6*8
    P = 4*8
    
    
    fig, (ax1,ax2) = plt.subplots(1,2, figsize=(15,8))
    fig, (ax3,ax4) = plt.subplots(1,2, figsize=(15,8))

    ax1.scatter(months,HOU[0:7],s=H,label = 'HOU')
    ax1.scatter(months,NYY[0:7],s=N,label = 'NYY')
    ax1.scatter(months,SD[0:7],s=P,label = 'SD')
    ax1.scatter(months,PHI[0:7],s=PH,label = 'PHI')

    ax2.scatter(months,HOU[7:14],s=H,label = 'HOU')
    ax2.scatter(months,NYY[7:14],s=N,label = 'NYY')
    ax2.scatter(months,SD[7:14],s=P,label = 'SD')
    ax2.scatter(months,PHI[7:14],s=PH,label = 'PHI')

    ax3.scatter(months,HOU[14:21],s=H,label = 'HOU')
    ax3.scatter(months,NYY[14:21],s=N,label = 'NYY')
    ax3.scatter(months,SD[14:21],s=P,label = 'SD')
    ax3.scatter(months,PHI[14:21],s=PH,label = 'PHI')
    
    
    
    ax4.scatter(months,HOU[21:28],s=H,label = 'HOU')
    ax4.scatter(months,NYY[21:28],s=N,label = 'NYY')
    ax4.scatter(months,SD[21:28],s=P,label = 'SD')
    ax4.scatter(months,PHI[21:28],s=PH,label = 'PHI')
    #ax4.scatter(months,houston_ops,s=H,label='HOU')
    #ax4.scatter(months,philly_ops,s=PH,label='PHI')
    #ax4.scatter(months,yankees_ops,s=N,label='NYY')
    #ax4.scatter(months,padres_ops,s=P,label='SD')

    
    
    
    
    
    
    ax1.legend()
    ax2.legend()
    ax3.legend()
    ax4.legend()
    
    ax1.set_xlabel('Month')
    ax2.set_xlabel('Month')
    ax3.set_xlabel('Month')
    ax4.set_xlabel('Month')

    ax1.set_ylabel('Launch Velo x Angle')
    ax2.set_ylabel('Exit Velocity')
    ax3.set_ylabel('Launch Angle')
    ax4.set_ylabel('Launch Velo x Angle')

    ax1.set_title('Launch Angle x Velocity Runners on Base') 
    ax2.set_title('Launch Angle')
    ax3.set_title('Exit Velocity')
    ax4.set_title('Launch Velo x Angle')

    return ax1,ax2,ax3,ax4