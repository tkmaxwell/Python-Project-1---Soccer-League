import csv


#Open the csv doc and crate the list of players in the league
def OpenExcel():
  with open('soccer_players.csv', newline='') as csvfile:
    soccerreader = csv.DictReader(csvfile, delimiter=',')
    allplayers = list(soccerreader)
  createteams(allplayers)
  balanceteam(allplayers)
  letters(allplayers)

#Build the team first by generating a list of experienced and non-experienced players
def createteams(allplayers):

  for row in allplayers:
    if row['Soccer Experience'] == 'YES':
      experienced.append(row)
    else:
      inexperienced.append(row)

#Construct the teams by having three experienced and three unexperienced on each team
def balanceteam(allplayers):
  count = 0
  for each in experienced:
    league[count].append(each)
    count += 1
    
    if count == 3:
      count = 0
  
  for each in inexperienced:
    league[count].append(each)
    count += 1
    
    if count == 3:
      count = 0
      
#Define the league as a list of three lists for each team 
league = [ 
  
  [],
  [],
  [],
  
]    
experienced = []
inexperienced = []

#Assign team names and practice time to the players and write the letter
def letters(allplayers):
  for player in allplayers:
    Team = None
    Date = None
    if player in league[0]:
      Team = 'Dragons'
      Date = 'March 17, 1pm'
    elif player in league[1]:
      Team = 'Sharks'
      Date = 'March 17, 3pm'
    else:
      Team = 'Raptors'
      Date = 'March 18, 1pm'
      
    with open(player['Name'].replace(' ','_').lower()+ ".txt", "w") as file:
      file.write("""Dear {}:
      
      We would like to formally welcome {} to the {}.
      
      The first practice will take place at {}\n""".format(player['Guardian Name(s)'],player['Name'],Team,Date))

#execute program      
if __name__ == "__main__":
  OpenExcel()
      