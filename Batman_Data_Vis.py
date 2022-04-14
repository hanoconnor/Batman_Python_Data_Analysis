import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Grouped Bar Chart to show Budget in USD vs Worldwide Gross USD for all Batman Box Office Releases (via Plotly Graph Objects)

box = pd.read_csv("BatmanBoxOffice.csv")
trace1 = go.Bar(
    x = box['Title'],
    y = box['Budget_USD'],
    name = 'Budget USD',
    marker_color = 'black')

trace2 = go.Bar(
    x = box['Title'],
    y = box['Worldwide_Gross'],
    name = 'Worldwide Gross USD',
    marker_color='gold')

data = [trace1, trace2]
layout = go.Layout(barmode='group', xaxis_tickangle=-45)
fig = go.Figure(data =data, layout=layout)
fig.update_layout(title_text='Batman Box Office Releases Budget vs WorldWide Gross USD ($)')
fig.show()

# Grouped Bar Chart to show Awards and Nominations (via Plotly Graph Objects)

box = pd.read_csv("BatmanBoxOffice.csv")
trace1 = go.Bar(
    x = box['Title'],
    y = box['Award_Nominations'],
    name = 'Award Nominations',
    marker_color = 'black')

trace2 = go.Bar(
    x = box['Title'],
    y = box['Awards_Won'],
    name = 'Awards Won',
    marker_color='gold')

data = [trace1, trace2]
layout = go.Layout(barmode='group', xaxis_tickangle=-45)
fig = go.Figure(data =data, layout=layout)
fig.update_layout(title_text='Batman Box Office Releases Awards & Nominations')
fig.show()

# Batman Filming Locations Map by Appearance (using Plotly Express)

film_loc = pd.read_csv("Batman_Countries.csv")

fig = px.scatter_geo(film_loc, locations="ISO_Alpha", color="Country",
                     hover_name="Country", size="Appearances",
                     projection="natural earth")
fig.show()

# Batman Filming Locations Map by Year (using Plotly Express)

film_loc = pd.read_csv("Batman_Countries_by_Year.csv")

fig = px.scatter_geo(film_loc, locations="ISO_Alpha", color="Country",
                     hover_name="Country", size="Appearances",
                     animation_frame="Year",
                     projection="natural earth")
fig.show()