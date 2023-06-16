import requests
import pandas as pd
from bs4 import BeautifulSoup, Comment
import urllib.request, urllib.error
import xlsxwriter

def url_test(url):
    try:
        conn = urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
        # Return code error (e.g. 404, 501, ...)
        # ...
        return 'HTTPError: {}'.format(e.code)
    except urllib.error.URLError as e:
        # Not an HTTP-specific error (e.g. connection refused)
        # ...
        return 'URLError: {}'.format(e.reason)
    else:
        # 200
        # ...
        return 'good'

teams = [  
    'abilene-christian', 'air-force',
    'akron', 'alabama-am',
    'alabama', 'alabama-state',
    'alabama-birmingham', 'albany-ny',
    'alcorn-state',
    'american',
    'appalachian-state', 'arizona-state',
    'arizona', 'arkansas',
    'arkansas-state', 'arkansas-pine-bluff',
    'armstrong', 'army',
    'auburn', 'augusta-state',
    'augustana-il', 'austin-peay',
    'baker-university', 'baldwin-wallace',
    'ball-state', 'baltimore',
    'baylor', 'belmont',
    'beloit', 'bethune-cookman',
    'binghamton', 'birmingham-southern',
    'bloomsburg', 'boise-state',
    'boston-college', 'boston-university',
    'bowling-green-state', 'bradley',
    'brigham-young', 'brooklyn',
    'brown', 'bryant',
    'bucknell', 'buffalo',
    'butler', 'cal-poly',
    'cal-state-bakersfield', 'cal-state-fullerton',
    'long-beach-state', 'cal-state-los-angeles',
    'cal-state-northridge', 'california-baptist',
    'campbell', 'canisius',
    'carleton-college', 'carnegie-mellon',
    'catholic', 'centenary-la',
    'central-arkansas', 'central-connecticut-state',
    'central-florida', 'central-michigan',
    'central-missouri', 'central-normal',
    'central-pennsylvania-college', 'centre-ky',
    'charleston-southern', 'charlotte',
    'chattanooga', 'cheyenne-business',
    'chicago', 'chicago-state',
    'cincinnati', 'citadel',
    'city-college-of-new-york', 'clemson',
    'cleveland-state', 'coastal-carolina',
    'colgate', 'college-of-charleston',
    'college-of-new-jersey', 'colorado',
    'colorado-college', 'colorado-state',
    'columbia', 'concordia',
    'connecticut', 'coppin-state',
    'cornell',
    'cotner',
    'creighton',
    'cumberland-university',
    'dakota-wesleyan',
    'dartmouth',
    'davidson',
    'dayton',
    'delaware',
    'delaware-state',
    'denison',
    'denver',
    'depaul',
    'depauw',
    'detroit-mercy',
    'dickinson-college',
    'drake',
    'drexel',
    'duke',
    'duquesne',
    'east-carolina',
    'east-central',
    'east-tennessee-state',
    'eastern-illinois',
    'eastern-kentucky',
    'eastern-michigan',
    'eastern-washington',
    'elon',
    'emporia-state',
    'evansville',
    'fairfield',
    'fairleigh-dickinson',
    'florida-am',
    'florida-atlantic',
    'florida',
    'florida-gulf-coast',
    'florida-international',
    'florida-state',
    'fordham',
    'franklin',
    'fresno-state',
    'furman',
    'gardner-webb',
    'geneva',
    'george-mason',
    'george-washington',
    'georgetown',
    'georgia',
    'georgia-southern',
    'georgia-state',
    'georgia-tech',
    'gettysburg',
    'gonzaga',
    'grambling',
    'grand-canyon',
    'green-bay',
    'grinnell',
    'grove-city',
    'hamline',
    'hampton',
    'hardin-simmons',
    'hartford',
    'harvard',
    'haskell-ks',
    'hawaii',
    'high-point',
    'hiram',
    'hofstra',
    'holy-cross',
    'hope',
    'houston-baptist',
    'houston',
    'howard',
    'idaho-state',
    'idaho',
    'illinois',
    'illinois-state',
    'illinois-wesleyan',
    'illinois-chicago',
    'incarnate-word',
    'indiana',
    'indiana-state',
    'iona',
    'iowa',
    'iowa-state',
    'iupui',
    'jackson-state',
    'jacksonville',
    'jacksonville-state',
    'james-madison',
    'john-carroll',
    'kalamazoo',
    'kansas',
    'kansas-state',
    'kennesaw-state',
    'kent-state',
    'kentucky-wesleyan',
    'kentucky',
    'la-salle',
    'lafayette',
    'lake-forest',
    'lamar',
    'latter-day-saints',
    'lawrence',
    'lehigh',
    'lewis',
    'liberty',
    'lipscomb',
    'arkansas-little-rock',
    'long-island-university',
    'longwood',
    'louisiana',
    'louisiana-state',
    'louisiana-tech',
    'louisiana-monroe',
    'louisville',
    'loyola-il',
    'loyola-la',
    'loyola-md',
    'loyola-marymount',
    'macalester',
    'maine',
    'manchester',
    'manhattan',
    'marietta',
    'marist',
    'marquette',
    'marshall',
    'maryland',
    'maryland-baltimore-county',
    'maryland-eastern-shore',
    'massachusetts-institute-of-technology',
    'massachusetts',
    'massachusetts-lowell',
    'mcneese-state',
    'memphis',
    'mercer',
    'merchant-marine-academy',
    'merrimack',
    'miami-fl',
    'miami-oh',
    'michigan-state',
    'michigan',
    'middle-tennessee',
    'millikin',
    'millsaps',
    'milwaukee',
    'minnesota-am',
    'minnesota',
    'mississippi',
    'mississippi-state',
    'mississippi-valley-state',
    'missouri-state',
    'missouri',
    'missouri-kansas-city',
    'monmouth',
    'montana',
    'montana-state',
    'morehead-state',
    'morgan-state',
    'morris-brown',
    'mount-st-marys',
    'mount-union',
    'muhlenburg',
    'murray-state',
    'muskingum',
    'navy',
    'nebraska',
    'nebraska-wesleyan',
    'nevada',
    'nevada-las-vegas',
    'new-hampshire',
    'new-mexico',
    'new-mexico-state',
    'new-orleans',
    'new-york-university',
    'newberry',
    'niagara',
    'nicholls-state',
    'njit',
    'norfolk-state',
    'north-alabama',
    'north-carolina-at',
    'north-carolina-central',
    'north-carolina-state',
    'north-carolina',
    'north-carolina-asheville',
    'north-carolina-greensboro',
    'north-carolina-wilmington',
    'north-central',
    'north-dakota',
    'north-dakota-state',
    'north-florida',
    'north-texas',
    'northeastern',
    'northeastern-illinois',
    'northern-arizona',
    'northern-colorado',
    'northern-illinois',
    'northern-iowa',
    'northern-kentucky',
    'northwest-missouri-state',
    'northwestern-state',
    'northwestern',
    'notre-dame',
    'oakland',
    'oberlin',
    'ohio',
    'ohio-state',
    'ohio-wesleyan',
    'oklahoma-city',
    'oklahoma',
    'oklahoma-state',
    'old-dominion',
    'nebraska-omaha',
    'oral-roberts',
    'oregon',
    'oregon-state',
    'pacific',
    'penn-state',
    'pennsylvania',
    'pepperdine',
    'phillips',
    'pittsburg-state',
    'pittsburgh',
    'portland',
    'portland-state',
    'prairie-view',
    'pratt-institute',
    'presbyterian',
    'princeton',
    'providence',
    'purdue', 'ipfw',
    'quinnipiac',
    'radford',
    'regis-co',
    'rensselaer',
    'rhode-island',
    'rice',
    'richmond',
    'rider',
    'ripon',
    'roanoke',
    'robert-morris',
    'rochester-ny',
    'rose-hulman',
    'rutgers',
    'sacramento-state',
    'sacred-heart',
    'saint-francis-pa',
    'saint-josephs',
    'saint-louis',
    'saint-marys-ca',
    'saint-peters',
    'sam-houston-state',
    'samford',
    'san-diego-state',
    'san-diego',
    'san-francisco',
    'san-jose-state',
    'santa-clara',
    'savannah-state',
    'scranton',
    'seattle',
    'seton-hall',
    'sewanee',
    'siena',
    'south-alabama',
    'south-carolina',
    'south-carolina-state',
    'south-carolina-upstate',
    'south-dakota',
    'south-dakota-state',
    'south-florida',
    'southeast-missouri-state',
    'southeastern-louisiana',
    'southern-california',
    'southern-illinois',
    'southern-illinois-edwardsville',
    'southern',
    'southern-methodist',
    'southern-mississippi',
    'southern-utah',
    'southwestern-ks',
    'southwestern-tx',
    'springfield',
    'st-bonaventure',
    'st-francis-ny',
    'st-johns-ny',
    'st-johns-college',
    'st-lawrence',
    'stanford',
    'stephen-f-austin',
    'stetson',
    'stevens-institute',
    'stony-brook',
    'suny-potsdam',
    'swarthmore',
    'syracuse',
    'temple',
    'tennessee-state',
    'tennessee-tech',
    'tennessee',
    'tennessee-martin',
    'texas-am',
    'texas-am-corpus-christi',
    'texas-christian',
    'texas',
    'texas-southern',
    'texas-state',
    'texas-tech',
    'texas-wesleyan',
    'texas-arlington',
    'texas-el-paso',
    'texas-pan-american',
    'texas-san-antonio',
    'toledo',
    'towson',
    'trinity-ct',
    'trinity-tx',
    'troy',
    'tulane',
    'tulsa',
    'us-international',
    'california-davis',
    'california-irvine',
    'california-riverside',
    'california-santa-barbara',
    'ucla',
    'union-ny',
    'california',
    'utah-state',
    'utah',
    'utah-valley',
    'utica',
    'valparaiso',
    'vanderbilt',
    'vermont',
    'villanova',
    'virginia',
    'virginia-commonwealth',
    'virginia-military-institute',
    'virginia-tech',
    'wabash-little',
    'wagner',
    'wake-forest',
    'washburn',
    'washington-jefferson',
    'washington-lee',
    'washington-mo',
    'washington-college',
    'washington',
    'washington-state',
    'wayne-state-mi',
    'weber-state',
    'wesleyan-ct',
    'west-chester',
    'west-texas-am',
    'west-virginia',
    'western-carolina',
    'western-colorado',
    'western-illinois',
    'western-kentucky',
    'western-michigan',
    'westminster-mo',
    'westminster-pa',
    'wheaton-il',
    'whittier',
    'wichita-state',
    'widener',
    'william-mary',
    'williams',
    'winthrop',
    'wisconsin',
    'wisconsin-stevens',
    'wisconsin-superior',
    'wittenberg',
    'wofford',
    'wooster-fighting',
    'worcester-tech',
    'wright-state',
    'wyoming',
    'xavier', 
    'yale', 
    'youngstown-state'
]
# teams = [
#     'brown',
#     'abilene-christian'
# ]
final_df = pd.DataFrame()

year = input('Please pick the year you want to gather: ')

for team in teams:

    if url_test('https://www.sports-reference.com/cbb/schools/' + str(team) + '/' + year + '.html') == 'good':
        url = requests.get('https://www.sports-reference.com/cbb/schools/' + str(team) + '/' + year + '.html')

        soup = BeautifulSoup(url.content,'html.parser')     # Beautiful Soup is good way for python to read url data
        # The get_table stuff I don't really understand. Got it from google. It works though :)
        get_table = soup.find_all(class_='overthrow table_container')
        comment = soup.find_all(text=lambda text:isinstance(text, Comment) and 'table_container' in text)
        for com in comment:
            get_table += BeautifulSoup(com.string,'lxml').find_all(class_="overthrow table_container")

        # Since the above get_table grabs every table, we need to get just the tables that we need (totals and advanced)
        # 'tr' are usually blocks of data. Within each 'tr' there are 'td' which contain the actual numbers
        if soup.find('div', {'id': 'all_totals'}) and soup.find('div', {'id': 'all_advanced'}):
            headers2 = get_table[6].find_all('tr')
            headers3 = get_table[9].find_all('tr')
        else:
            continue
        # print(headers2, headers3)
        # For each 'tr' we need to cycle through all the 'td'. 'td' is where data is stored
        list_headers = []
        for header in headers2:
            
            header_th = header.find_all('td')
            str_cells = str(header_th)
            Clean_text = BeautifulSoup(str_cells, 'html.parser').get_text()
            list_headers.append(Clean_text)

        # Appending the strings above made each row all one cell. Thus we need to split the rows by commas so we can get
        # each individual data point
        new_list = []
        for new in range(len(list_headers)):
            
            new_list.append(str(list_headers[new]).split(','))

        # If the length is 26 (1 extra), we know that the name had a comma in it so we have to join the first 2 items
        for list_ in new_list:
            if len(list_) == 26:
                list_[0:2] = [''.join(list_[0:2])]
        total_header = ['Player', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '2P', '2PA', '2P%', '3P', '3PA', '3P%',
                        'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']

        advanced_header = ['Player', 'G', 'GS', 'MP', 'PER', 'TS%', 'eFG%', '3PAr', 'FTr', 'PProd', 'ORB%', 'DRB%',
                           'TRB%', 'AST%', 'STL%', 'BLK%', 'TOV%', 'USG%', 'DEL', 'OWS', 'DWS', 'WS', 'WS/40',
                           'DEL2',
                           'OBPM', 'DBPM', 'BPM']

        delete_rows = []
        for x in range(len(new_list)):
            new_list[x][0] = new_list[x][0][1:]
            new_list[x][-1] = new_list[x][-1][:-1]

        # Purpose: delete the rows where the players have played less than 100 minutes
        # Since we will be deleting rows, we need to make a copy of the list so that the indexes stay the same
        temp_list = new_list.copy()
        counter = 0         # Every time we delete a row, this will increase by 1 so that future rows that need to be
                            # deleted are popped on the correct row
        for x in range(1, len(temp_list)):
            if len(temp_list[x][3]) < 4:   # For some reason the length of a 2 digit number was 3 so had to say less than 4
                new_list.pop(x-counter)
                delete_rows.append(x-counter)
                counter += 1
        
        # Data frames are easier to use for excel (at least for me). So we convert the array into a dataframe
        # Assigning the column headers make it easier to drop values we don't need
        df = pd.DataFrame(new_list, columns=total_header)

        # The last row in this list summarizes the school totals. I removed it so that both lists would be the same length
        df.drop(df.tail(1).index, inplace=True)    #Gets rid of the school totals row
        df.insert(1, "School Name", str(team))  #Inserts a column for school name
        
        # Now we move onto the advanced table. The process is pretty much the same
        list_headers_2 = []
        for header in headers3:
            header_th = header.find_all('td')
            str_cells = str(header_th)
            Clean_text = BeautifulSoup(str_cells, 'html.parser').get_text()
            list_headers_2.append(Clean_text)

        new_list2 = []
        for new in range(len(list_headers_2)):
            new_list2.append(str(list_headers_2[new]).split(','))

        # Only need to remove the bracket for the last cell on this list
        for x in range(len(new_list2)):
            new_list2[x][-1] = new_list2[x][-1][:-1]

        # If the length is 28, we know that the name had a comma in it so we have to join the two
        for list_ in new_list2:
            if len(list_) == 28:
                list_[0:2] = [''.join(list_[0:2])]

        # Need to delete the rows that we deleted from the first list
        for row in delete_rows:
            new_list2.pop(row)
        if len(new_list2) == 1:
            new_list2 = []
        # Need to delete the duplicate columns from the first table and remove the blank columns (DEL1 and DEL2)
        df2 = pd.DataFrame(new_list2, columns=advanced_header)
        df2.drop(['Player', 'G', 'GS', 'MP', 'DEL', 'DEL2'], axis=1, inplace=True)

        horizontal_stack = pd.concat([df, df2], axis=1)
        final_df = pd.concat([final_df, horizontal_stack[1:]], axis=0)

        # Just so that when the code runs, you can see how far along it is
        print(team)


# Creates an excel doc called upwork_cbb - feel free to change it to whatever you want
writer = pd.ExcelWriter('2020 Player Data.xlsx', engine='xlsxwriter')

# Appends the dataframe to a sheet. Whatever year you put in should create the sheet if you haven't done it before.
# If you have done that year before, it will update the current sheet with this one.
final_df.to_excel(writer, sheet_name=str(year) + ' Player Data')

writer.save()


