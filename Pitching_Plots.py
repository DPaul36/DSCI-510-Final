# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 18:31:31 2022

@author: David
"""
import Code_Functions as cf
from baseball_scraper import pitching_stats_range
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
    
    ax1.set_title('Fastball')
    ax2.set_title('Slider')
    return ax1,ax2

month_team_pitch_data = cf.month_data(pitching_stats_range)


houston = cf.month_pitch_stats('Houston',month_team_pitch_data,'WHIP')
yankees = cf.month_pitch_stats('New York Yankees',month_team_pitch_data,'WHIP')
dodgers = cf.month_pitch_stats('Los Angeles Dodgers',month_team_pitch_data,'WHIP')
mets = cf.month_pitch_stats('New York Mets',month_team_pitch_data,'WHIP')
philly = cf.month_pitch_stats('Philadelphia',month_team_pitch_data,'WHIP')
braves = cf.month_pitch_stats('Atlanta',month_team_pitch_data,'WHIP')
padres = cf.month_pitch_stats('San Diego',month_team_pitch_data,'WHIP')
guard = cf.month_pitch_stats('Cleveland',month_team_pitch_data,'WHIP')
seattle = cf.month_pitch_stats('Seattle',month_team_pitch_data,'WHIP')
tampa = cf.month_pitch_stats('Tampa Bay',month_team_pitch_data,'WHIP')
cards = cf.month_pitch_stats('St. Louis',month_team_pitch_data,'WHIP')
toronto = cf.month_pitch_stats('Toronto',month_team_pitch_data,'WHIP')

houston1 = cf.month_pitch_stats('Houston',month_team_pitch_data,'ERA')
yankees1 = cf.month_pitch_stats('New York Yankees',month_team_pitch_data,'ERA')
dodgers1 = cf.month_pitch_stats('Los Angeles Dodgers',month_team_pitch_data,'ERA')
mets1 = cf.month_pitch_stats('New York Mets',month_team_pitch_data,'ERA')
philly1 = cf.month_pitch_stats('Philadelphia',month_team_pitch_data,'ERA')
braves1 = cf.month_pitch_stats('Atlanta',month_team_pitch_data,'ERA')
padres1 = cf.month_pitch_stats('San Diego',month_team_pitch_data,'ERA')
guard1 = cf.month_pitch_stats('Cleveland',month_team_pitch_data,'ERA')
seattle1 = cf.month_pitch_stats('Seattle',month_team_pitch_data,'ERA')
tampa1 = cf.month_pitch_stats('Tampa Bay',month_team_pitch_data,'ERA')
cards1 = cf.month_pitch_stats('St. Louis',month_team_pitch_data,'ERA')
toronto1 = cf.month_pitch_stats('Toronto',month_team_pitch_data,'ERA')



houston2 = cf.month_pitch_stats('Houston',month_team_pitch_data,'BAbip')
yankees2 = cf.month_pitch_stats('New York Yankees',month_team_pitch_data,'BAbip')
dodgers2 = cf.month_pitch_stats('Los Angeles Dodgers',month_team_pitch_data,'BAbip')
mets2 = cf.month_pitch_stats('New York Mets',month_team_pitch_data,'BAbip')
philly2 = cf.month_pitch_stats('Philadelphia',month_team_pitch_data,'BAbip')
braves2 = cf.month_pitch_stats('Atlanta',month_team_pitch_data,'BAbip')
padres2 = cf.month_pitch_stats('San Diego',month_team_pitch_data,'BAbip')
guard2 = cf.month_pitch_stats('Cleveland',month_team_pitch_data,'BAbip')
seattle2 = cf.month_pitch_stats('Seattle',month_team_pitch_data,'BAbip')
tampa2 = cf.month_pitch_stats('Tampa Bay',month_team_pitch_data,'BAbip')
cards2 = cf.month_pitch_stats('St. Louis',month_team_pitch_data,'BAbip')
toronto2 = cf.month_pitch_stats('Toronto',month_team_pitch_data,'BAbip')


houston3 = cf.month_pitch_stats('Houston',month_team_pitch_data,'SO9')
yankees3 = cf.month_pitch_stats('New York Yankees',month_team_pitch_data,'SO9')
dodgers3 = cf.month_pitch_stats('Los Angeles Dodgers',month_team_pitch_data,'SO9')
mets3 = cf.month_pitch_stats('New York Mets',month_team_pitch_data,'SO9')
philly3 = cf.month_pitch_stats('Philadelphia',month_team_pitch_data,'SO9')
braves3 = cf.month_pitch_stats('Atlanta',month_team_pitch_data,'SO9')
padres3 = cf.month_pitch_stats('San Diego',month_team_pitch_data,'SO9')
guard3 = cf.month_pitch_stats('Cleveland',month_team_pitch_data,'SO9')
seattle3 = cf.month_pitch_stats('Seattle',month_team_pitch_data,'SO9')
tampa3 = cf.month_pitch_stats('Tampa Bay',month_team_pitch_data,'SO9')
cards3 = cf.month_pitch_stats('St. Louis',month_team_pitch_data,'SO9')
toronto3 = cf.month_pitch_stats('Toronto',month_team_pitch_data,'SO9')


def final_4():
    H = 8*8

    N = 4*8
    PH = 6*8
    P = 4*8
    
    
    fig, (ax1,ax2) = plt.subplots(1,2, figsize=(15,8))
    fig, (ax3,ax4) = plt.subplots(1,2, figsize=(15,8))

    ax1.scatter(months,houston,s=H,label = 'HOU')
    ax1.scatter(months,yankees,s=N,label = 'NYY')
    ax1.scatter(months,padres,s=P,label = 'SD')
    ax1.scatter(months,philly,s=PH,label = 'PHI')

    ax2.scatter(months,houston1,s=H,label = 'HOU')
    ax2.scatter(months,yankees1,s=N,label = 'NYY')
    ax2.scatter(months,padres1,s=P,label = 'SD')
    ax2.scatter(months,philly1,s=PH,label = 'PHI')

    ax3.scatter(months,houston2,s=H,label = 'HOU')
    ax3.scatter(months,yankees2,s=N,label = 'NYY')
    ax3.scatter(months,padres2,s=P,label = 'SD')
    ax3.scatter(months,philly2,s=PH,label = 'PHI')
    
    ax4.scatter(months,houston3,s=H,label='HOU')
    ax4.scatter(months,philly3,s=PH,label='PHI')
    ax4.scatter(months,yankees3,s=N,label='NYY')
    ax4.scatter(months,padres3,s=P,label='SD')

    
    
    
    
    
    
    ax1.legend()
    ax2.legend()
    ax3.legend()
    ax4.legend()
    
    ax1.set_xlabel('Month')
    ax2.set_xlabel('Month')
    ax3.set_xlabel('Month')
    ax4.set_xlabel('Month')

    ax1.set_ylabel('WHIP')
    ax2.set_ylabel('ERA')
    ax3.set_ylabel('BAbip')
    ax4.set_ylabel('SO/9')

    ax1.set_title('Walks + Hits / IP') 
    ax2.set_title('Earned Run Average')
    ax3.set_title('BA on Balls in Play')
    ax4.set_title('Strike Outs per 9 IP')

    return ax1,ax2,ax3,ax4