import pandas as pd

# Box Office Data Analysis

# Collect all of the worldwide gross income from each film into a list (using pandas)
data = pd.read_csv("BatmanBoxOffice.csv")
Title = data['Title'].tolist()
Gross = data['Worldwide_Gross'].tolist()
print('Films by Gross Worldwide Income USD ($)')
print('Title:', Title)
print('Gross Worldwide:', Gross)

# Output the total sales across all months (using pandas)
df = pd.read_csv("BatmanBoxOffice.csv")
print('Total Gross Income for All Batman Films USD ($): ')
print(df['Worldwide_Gross'].sum())

# Highest and Lowest Grossing Batman Films (using index and min/max)
df = pd.read_csv("BatmanBoxOffice.csv")
print('Income statistics for All Batman Films USD ($): ')

print('Lowest grossing USD ($): ')
i = df['Worldwide_Gross'].idxmin()
print(df['Title'][i])
print(df['Worldwide_Gross'].min())

print('Highest grossing USD ($): ')
i = df['Worldwide_Gross'].idxmax()
print(df['Title'][i])
print(df['Worldwide_Gross'].max())

# Mean Gross Worldwide Income
print('Mean Worldwide Gross Income USD ($): ', df['Worldwide_Gross'].mean())

# Number of Unique Box Office Release Batman Actors
actor_data = pd.read_csv("BatmanBoxOffice.csv")
batman_actor = actor_data['Batman_Actor']
print('No of Actors that have played Batman: ', batman_actor.nunique())

# Batman Actors by Box Office Appearance
actor_data = pd.read_csv("BatmanBoxOffice.csv")
batman_actor = actor_data['Batman_Actor']
print('Batman Actor Data: ')
occur = data.groupby(['Batman_Actor']).size()
print(occur)

# Batman Actors by Box Office Appearance in Ascending Order
Asc_Appearances = occur.sort_values()
print('No of Appearances as Batman (Asc): ', Asc_Appearances)

# Batman Actors by Box Office Appearance in Descending
Desc_Appearances = occur.sort_values(ascending=False)
print('No of Appearances as Batman (Decs): ', Desc_Appearances)
