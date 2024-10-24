import pandas as pd
import sqlite3 as sql
import matplotlib.pyplot as plt


try:
    connection = sql.connect("WeatherData.db")
    cursor = connection.cursor()
    print("Connection with Weather database established successfully...")
except Exception as e:
    print("Error connecting with Weather database: ", e)

query = "select City,Date,Weather,Temperature,Humidity from Weather"
result = cursor.execute(query)
# print(list(map(lambda x:x[0], result.description)))
data = pd.DataFrame(result.fetchall(),columns=list(map(lambda x:x[0], result.description)))
# print(data)

temp_data = data.groupby("City")["Temperature"].mean().reset_index()
humidity_data = data.groupby("City")["Humidity"].mean().reset_index()
"""
City-wise Data Analysis:
▪ Retrieve and compare the current temperatures and humidity levels for the cities stored in the database.
"""
# print(data.loc[(data["Temperature"]> 200) & (data["Humidity"]<20)])
# print(data[["City","Date","Temperature","Humidity"]])
"""
Filter and Sort:
▪ Query the database to retrieve cities where the temperature is above a certain threshold, or where humidity is lower
than a given value.
▪ Sort the results by temperature, humidity, or another attribute.
"""
# fltquery = "select * from Weather where Temperature > 300 or Humidity < 30"
# result= cursor.execute(fltquery)
# df = pd.DataFrame(result.fetchall(), columns=list(map(lambda x:x[0], result.description)))
# print("Filtered data for Temperature > 300 or Humidity < 30: \n",df[["City","Date","Temperature","Humidity"]].sort_values(by=["Date","Temperature","Humidity"],ascending=[False,False,True]))

"""
Group and Aggregate Data:
▪ Group cities by weather conditions (e.g., clear, cloudy, rainy)
and count how many cities fall into each category.
"""
city_weather = data.groupby("Weather")["City"].count().reset_index()
print(city_weather)

"""
Statistical Insights:
▪ Calculate the average temperature and humidity across all cities in the database.
▪ Find the highest and lowest temperatures stored in the database.
"""
# city_avg_temp = data.groupby("City")[["Temperature","Humidity"]].mean().reset_index()
# print("Average temperature and humidity of each City:\n",city_avg_temp)
# print("Highest temperature city:\n", data.loc[data["Temperature"] == data["Temperature"].max()].to_string(index=False))
# print("Lowest temperature city:\n", data.loc[data["Temperature"] == data["Temperature"].min()].to_string(index=False))

"""
Create visualizations based on the data retrieved from the SQLite database:
▪ Visualize the distribution of temperature and humidity across different cities.
▪ Show how many cities fall under different weather conditions.
"""
fig, (ax1,ax2,ax3) = plt.subplots(1,3)
bars = ax1.bar(x=temp_data["City"], height=temp_data["Temperature"], color="green")
ax1.set_xlabel("City")
ax1.set_ylabel("Temperature")
ax1.set_title("City Temperature variation analysis")
for bar in bars:
    yval = round(bar.get_height(),0)
    ax1.text(bar.get_x(),yval+0.015,yval)

ax2.plot(humidity_data["City"],humidity_data["Humidity"],marker="*")
ax2.set_xlabel("City")
ax2.set_ylabel("Humidity")
ax2.set_title("City Humidity variation analysis")

city_bars = ax3.bar(city_weather["Weather"],city_weather["City"],color="yellow", width=0.5, label="Count of cities")
for bar in city_bars:
    yval = round(bar.get_height(),0)
    ax3.text(bar.get_x(),yval+0.015,yval)

ax3.set_xlabel("Weather")
ax3.set_ylabel("Count of cities")
ax3.set_title("Weather analysis")
ax3.set_ylim(city_weather["City"].min()-5, city_weather["City"].max() + 10)


# plt.legend("best")
plt.subplots_adjust(left=0.05,right=0.92)
# plt.axhspan(xmin=5,xmax=10, ymin=5, ymax=10)
# plt.autoscale(True,tight=True)
plt.show()