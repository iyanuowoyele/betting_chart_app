# a chart visualization project 
import pandas as pd
import json as json
import matplotlib.pyplot as mplot

#loading my json data 
with open('data.json','r') as json_data:
    data = json.load(json_data)

#Extracting the names and games from the json file 
player_name = data['player_stats'][0]['player_name']
games_info = data['player_stats'][0]['games_info']

#we now convert to dataframe 
df = pd.DataFrame(games_info)
#convert to date time for easy manipulation and sorting 
df['game_date'] = pd.to_datetime(df['game_date'])

#plotting our values 
mplot.plot(df['game_date'],df['points'],marker = 'o', label = 'points')
mplot.title(f'Chart showing {player_name} performance')
mplot.xlabel('GAME DATE')
mplot.ylabel('POINTS')
mplot.grid(True)
mplot.legend()
mplot.show()



print(df)

#load and preview the data 
# lf = pd.read_csv('month.csv')
# lf = pd.read_json('data.json')
# print(lf.head())


# mplot.plot(lf[''])