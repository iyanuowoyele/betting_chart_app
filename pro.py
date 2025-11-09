# a chart visualization project 
import pandas as pd
import json as json
import matplotlib.pyplot as mplot
import streamlit as st 
import plotly.graph_objects as gobj
import random







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

# streamlit dashboard title and dropdown selections 
st.title('player performance dashboard') 
chart_type = st.radio('chart type:',['line graph','candlesticks'])
selected_stat = st.selectbox('choose a stat',['points','assists','rebounds'])




# assign a color to each stat
set_color = None
if selected_stat == 'points':
    set_color = 'red'
elif selected_stat == 'assists':
    set_color = 'green' 
else:
    set_color = 'yellow'       

#plotting our values - for candlestick pattern
df['open'] = df[selected_stat].shift(1).fillna(df[selected_stat])
df['close'] = df[selected_stat]
df['high'] = df[['open','close']].max(axis= 1) +[random.uniform(0.5,1.5) for _ in range (len(df))]
df['low'] = df[['open','close']].min(axis= 1) -[random.uniform(0.5,1.5) for _ in range (len(df))]


if chart_type == 'line graph':

#plotting our values - line chart section
    fig,axes = mplot.subplots()
    axes.plot(df['game_date'],df[selected_stat],marker = 'o', label = selected_stat,color = set_color)
    axes.set_title(f'Chart showing {player_name} performance')
    axes.set_xlabel('GAME DATE')
    axes.set_ylabel('STAT VALUES')
    axes.grid(True)
    axes.legend()
    st.pyplot(fig)
else :
#create a candlestick figure 
    fig = gobj.Figure(data=[gobj.Candlestick(
    x = df['game_date'],
    open = df['open'],
    close = df['close'],
    high = df['high'],
    low = df['low'],
    increasing_line_color='green',
    decreasing_line_color='red',
    name = selected_stat
)])    


    fig.update_layout (
        title = f'Chart showing {player_name} performance',
        xaxis_title="Game Date",
        yaxis_title="Stat Value",
        template = 'plotly_white',
        xaxis_rangeslider_visible = False
    )
    fig.update()

    st.plotly_chart(fig) 