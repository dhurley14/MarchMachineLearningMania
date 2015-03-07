teams = pd.read_csv('team_spellings.csv')
teams_dict = dict(zip(teams.name_spelling, teams.team_id))
team_sos = pd.DataFrame()

for i in xrange(1993,2010):
    url = "http://www.cbssports.com/collegebasketball/bracketology/sos/%s-%s" % (str(i+1), str(i+2)[-2:])
    r = requests.get(url)
    dom = web.Element(r.text)
    print url
    temp_sos_list = []
    tbl = dom.by_class('data')[0]
    for row in tbl.by_tag('tr.row1'):    
        temp_sos_list.append([row.by_tag('td')[1]('a')[0].content, row.by_tag('td')[3].content])
    for row in tbl.by_tag('tr.row2'):    
         temp_sos_list.append([row.by_tag('td')[1]('a')[0].content, row.by_tag('td')[3].content])
    temp_sos = pd.DataFrame(temp_sos_list, columns = ['Team', 'SOS'])
    team_id = []
    for team in temp_sos.Team:
        team = team.lower()
        if team != '':
            team_id.append(teams_dict[team])
        else:
            team_id.append(0)
    #Create the year column
    temp_sos['id'] = team_id
    temp_sos['year'] = i+1
    #Put the columns in the "Correct" order
    cols = temp_sos.columns.tolist()
    cols = cols[-1:] + cols[-2:-1] + cols[0:-2]
    temp_sos = temp_sos[cols]
    #Append df to the master df
    team_sos = team_sos.append(temp_sos, ignore_index = True)
team_sos
    
