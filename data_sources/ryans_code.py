import requests
from pattern import web
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

years = ['1993-94','1994-95','1995-96','1996-97','1997-98','1998-99','1999-00','2000-01','2001-02','2002-03','2003-04','2004-05','2005-06','2006-07','2007-08','2008-09','2009-10','2010-11','2011-12','2012-13','2013-14']
url = "http://www.cbssports.com/collegebasketball/bracketology/nitty-gritty-report"
r = []
r.append([requests.get(url+year) for year in years]) #get rid of this.
dom = web.Element(r.text)

team_rpi = []
tbl = dom.by_class('data')[0]
for row in tbl.by_tag('tr.row1'):    
    team_rpi.append([row.by_tag('td')[1]('a')[0].content, row.by_tag('td')[4].content])
for row in tbl.by_tag('tr.row2'):    
     team_rpi.append([row.by_tag('td')[1]('a')[0].content, row.by_tag('td')[4].content])
team_rpi = pd.DataFrame(team_rpi, columns = ['Team', 'RPI'])
#team_rpi
print team_rpi.head()
#team_rpi.to_csv("ryans_output.csv")

teams = pd.read_csv('team_spellings.csv')
team_id = []
teams_dict = dict(zip(teams.name_spelling, teams.team_id))
for team in team_rpi.Team:
    team = team.lower()
    team_id.append(teams_dict[team])
team_rpi['id'] = team_id
team_rpi

# team_rpi['year'] = 2015
cols = team_rpi.columns.tolist()
cols = cols[-1:] + cols[-2:-1] + cols[0:-2]
team_rpi = team_rpi[cols]
team_rpi

url = "http://www.cbssports.com/collegebasketball/bracketology/nitty-gritty-report/2013-14"
r = requests.get(url)
dom = web.Element(r.text)
team_rpi_2014 = []
tbl = dom.by_class('data')[0]
for row in tbl.by_tag('tr.row1'):    
    team_rpi_2014.append([row.by_tag('td')[1]('a')[0].content, row.by_tag('td')[4].content])
for row in tbl.by_tag('tr.row2'):    
     team_rpi_2014.append([row.by_tag('td')[1]('a')[0].content, row.by_tag('td')[4].content])
team_rpi_2014 = pd.DataFrame(team_rpi_2014, columns = ['Team', 'RPI'])

team_id = []
for team in team_rpi_2014.Team:
    team = team.lower()
    team_id.append(teams_dict[team])
team_rpi_2014['id'] = team_id
team_rpi_2014['year'] = 2014
cols = team_rpi_2014.columns.tolist()
cols = cols[-1:] + cols[-2:-1] + cols[0:-2]
team_rpi_2014 = team_rpi_2014[cols]

team_rpi = team_rpi.append(team_rpi_2014, ignore_index = True)
team_rpi

