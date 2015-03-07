import requests
from bs4 import BeautifulSoup # To get everything
from lxml import etree # to parse the table from beautiful soup
import csv

def setup_data(year):
    params = {"type":"detail","league":"ncb","rating_id":"512","season_id":"",
        "cat_type":"2","view":"team_v2","view_type":"team","table_view":"team_v2",
        "force_period_id":"","is_rpi_ranking":"","date":"03/08/"+str(year)}
    r = requests.post('http://www.teamrankings.com/ajax/league/v3/rankings_controller.php',data=params)
    return r.text


def parse_html(html_stuff):
    soup = BeautifulSoup(''.join(html_stuff))
    tree = soup.findAll('table')[0].prettify()
    table = etree.XML(str(tree))
    table_headers, table_rows = iter(table)

    # get the headers if it is not a white space, since whitespaces are "falsey"
    header_names = [str(i.text).strip() for i in iter(table_headers[0]) 
                    if str(i.text).strip()] 
    table_item_rows = iter(table_rows)
    writeable = []
    for row in table_item_rows:
        writeable.append([str(row[1][0].text).strip(),str(row[2].text).strip()])
    print len(writeable)
    #table_items = [str(item[1].text).strip() for item in table_item_rows]
    print header_names
    #print table_items
    print "\n\n\n\n"
    print table_rows
    return writeable

if __name__ == '__main__':
    #target = open('sos_test.html','wb')
    #the_html = setup_data("2014")
    #target.write(the_html)
    years = ['1998','1999','2000','2001','2002',
            '2003','2004','2005','2006','2007','2008',
            '2009','2010','2011','2012','2013','2014']
    #target = open('sos_test.html','rb')
    for year in years:
        target = open('sos_'+str(year)+'.csv','wb')
        wr = csv.writer(target)
        the_html = setup_data(year)
        data = parse_html(the_html)
        wr.writerows(data)
        target.close()
        print "closed target"
