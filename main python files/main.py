import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
df = pd.read_csv('../csv files/Global Temperature.csv')
df.columns = df.columns.str.strip()
#print(df.columns)
df = df[df['Month'] == 12]
df = df[['Year',"Five-Year Anomaly"]].copy()
df.dropna(inplace =True)
df = df[(df["Year"]>=2000) & (df["Year"]<=2019)]
df = df[df["Five-Year Anomaly"].notna()]
print(df.head())
#plot code
plt.figure(figsize=(12,6))
plt.plot(df['Year'],df['Five-Year Anomaly'],color = "Tomato",linewidth = 2)
plt.axhline(0,color ="gray",linestyle="--",linewidth = 1)
plt.title("Global Five-Year Temperature Anomaly over Time",fontsize = 14)
plt.xlabel("Year")
plt.ylabel("Temperature Anomaly (degree Celsius)")
plt.grid(True)

plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(20))
plt.xticks(df["Year"].unique(),rotation = 45)
plt.tight_layout()
plt.show()

