# a chart visualization project 
import pandas as pd
import json as json
import matplotlib.pyplot as mplot
import streamlit as st 

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

st.title('player performance dashboard') # streamlit dashboard title 
selected_stat = st.selectbox('choose a stat',['points','assists','rebounds'])
fig,axes = mplot.subplots()
#plotting our values 


set_color = None
if selected_stat == 'points':
    set_color = 'red'
elif selected_stat == 'assists':
    set_color = 'green' 
else:
    set_color = 'yellow'       




axes.plot(df['game_date'],df[selected_stat],marker = 'o', label = selected_stat,color = set_color)
axes.set_title(f'Chart showing {player_name} performance')
axes.set_xlabel('GAME DATE')
axes.set_ylabel('STAT VALUES')
axes.grid(True)
axes.legend()
st.pyplot(fig)



# print(df)

#load and preview the data 
# lf = pd.read_csv('month.csv')
# lf = pd.read_json('data.json')
# print(lf.head())


# mplot.plot(lf[''])