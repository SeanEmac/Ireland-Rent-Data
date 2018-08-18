import pandas as pd
import matplotlib.pyplot as plt

cities = [
    "Dublin",
    "Galway City",
    "Cork City",
    "Limerick City"
]

df = pd.read_csv('RentByQuarter.csv')  # import csv
df = df[df.num != '".."']  # drop null rows 750,000 -> 220,000
df = df[df.Location.isin(cities)]  # 220,000 -> 8,500
df = df[df.Quarter.str.contains("Q2|Q4")]  # Drop Q1 Q3

df['num'] = df['num'].apply(pd.to_numeric)  # change num to float

cityData = []
for i in range(len(cities)):
    cityData.append(df.loc[(df['Property Type'] == 'Apartment') & (df['Number of Bedrooms'] == 'Two bed') & (df['Location'] == cities[i])])
    plt.plot(cityData[i]['Quarter'], cityData[i]['num'])


plt.legend(['Dublin', 'Galway', 'Cork', 'Limerick', 'Athlone', 'Waterford'], loc='upper left')
plt.ylabel('Rent €')
plt.xlabel('Year')

plt.title('Average price of 2 Bed apartment')
plt.grid(True)
plt.show()
