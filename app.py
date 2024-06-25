import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

# Connect to SQLite database
conn = sqlite3.connect('world_happiness.db')

# Query the database
query = "SELECT * FROM 'mytable'"
df = pd.read_sql_query(query, conn)

# Streamlit app
st.title('World Happiness Report 2019 Visualization')

# Sidebar filters
st.sidebar.header('Filter Options')

# Select top N countries
top_n = st.sidebar.slider('Top N Countries by Happiness Score', min_value=1, max_value=len(df), value=10)

# Get the top N happiest countries
top_countries_df = df.sort_values(by='Score', ascending=False).head(top_n)

# Display top N happiest countries
st.subheader(f'Top {top_n} Happiest Countries')
st.write(top_countries_df)



# Plotly visualization for the top N happiest countries with unique colors for each bar
fig = px.bar(top_countries_df, x='Country or region', y='Score', color='Country or region', 
             title=f'Top {top_n} Happiest Countries by Score', 
             labels={'Score': 'Happiness Score', 'Country or region': 'Country'})
st.plotly_chart(fig)

# GDP per capita vs Happiness Score scatter plot for the top N countries
fig2 = px.scatter(top_countries_df, x='GDP per capita', y='Score', size='Social support', color='Country or region',
                  hover_name='Country or region', title='GDP per capita vs Happiness Score for Top Countries')
st.plotly_chart(fig2)

#Genorosity vs Perception of corruption 
fig3 = px.histogram(top_countries_df, x='Generosity', y='Perceptions of corruption', color='Country or region',
                hover_data='Generosity', title='Perception of corruption vs Generosity')
st.plotly_chart(fig3)

# 
fig4 = px.scatter(top_countries_df, x='Healthy life expectancy', y='Overall rank', size='Social support', color='Country or region',
                  hover_name='Healthy life expectancy', title='Overall rank vs Health life Expectancy',)
fig4.update_traces(marker_size=10)
st.plotly_chart(fig4)




# Close the connection
conn.close()