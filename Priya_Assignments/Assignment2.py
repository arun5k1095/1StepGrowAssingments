import datetime

import pandas as pd
import requests
import matplotlib.pyplot as plt
from matplotlib.pyplot import legend
import numpy as np
import WeatherAnalysis as Weather

url = "https://api.openweathermap.org/data/2.5/weather"
# all_cities  = list(input("Enter city names separated by ',': ").split(","))
all_cities = ["Delhi","Bombay","Calcuta","Ahmedabad","Pune","Patna","Bhopal"]
df = pd.DataFrame(columns=["City","Date","Weather","Temperature","MinTemp","MaxTemp","Humidity","WindSpeed"])
try:
    for city in all_cities :
        values = { "q" :city , "appid" : "8bd7eaa73d60fa03c1208bbc77283217"}
        response = requests.get(url, params=values)
        data = response.json()
        # print(data)
        # print("Weather data of ", data["name"], "as on", pd.to_datetime(data["dt"]).strftime("%d-%b-%Y"), ":")
        # print("\tWeather: ",data["weather"][0]["main"], ",", data["weather"][0]["description"])
        # print("\tTemperature min: ", data["main"]["temp_min"], "Temperature max: ", data["main"]["temp_max"])
        # print("\tHumidity: ", data["main"]["humidity"])
        # print("\tWind speed: ", data["wind"]["speed"])
        df.loc[len(df)] = {"City": data["name"], "Date": data["dt"], "Weather":data["weather"][0]["main"],\
                           "Temperature":data["main"]["temp"], "MinTemp":data["main"]["temp_min"],\
                           "MaxTemp": data["main"]["temp_max"], "Humidity": data["main"]["humidity"],\
                           "WindSpeed": data["wind"]["speed"]}
    # print(df)
except Exception as e:
    if KeyError:
        print("You have entered incorrect City name, enter correct city name and re-try.")
    else:
        print("Error occurred: ", e)

#Weather Data Analysis
"""
Temperature Comparison:
▪ Compare the current temperatures across the selected cities.
▪ Identify the city with the highest and lowest temperature.
"""
print("City with highest temperature is ", df.loc[df["Temperature"] == df["Temperature"].max()]["City"].to_string(index=False))
print("City with lowest temperature is ", df.loc[df["Temperature"] == df["Temperature"].min()]["City"].to_string(index=False))

"""
Humidity Analysis:
▪ Analyze the humidity levels and find which cities have the highest and lowest humidity.
▪ Is there a pattern between temperature and humidity across cities?
"""
print("City having higest humidity is ", df.loc[df["Humidity"] == df["Humidity"].max()]["City"].to_string(index=False))
print("City having lowest humidity is ", df.loc[df["Humidity"] == df["Humidity"].min()]["City"].to_string(index=False))

plt.bar(df["City"],df["Temperature"], color="blue",label="Temperature")
plt.plot(df["City"],df["Humidity"], color="red",label="Humidity")
plt.title("City Temperature v/s Humidity analysis")
plt.legend("best")
plt.show()

"""
Weather Conditions:
▪ Group the cities by general weather conditions (e.g., clear, cloudy, rainy, etc.)
  and determine how many cities fall into each category.
"""
city_weather = df.groupby("Weather")["City"].count().reset_index()
print(city_weather)

"""
Visualization:
Create at least 3 visualizations (e.g., bar charts, scatter plots) that:
▪ Compare temperatures across cities.
▪ Show the relationship between temperature and humidity.
▪ Display the distribution of different weather conditions across the cities.
"""
fig, (ax1,ax2,ax3) = plt.subplots(3,1)
bars = ax1.bar(df["City"], df["Temperature"],width=.50)
for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x(), yval+ 0.010, yval)
ax1.set_ylim(df["Temperature"].min()-10, df["Temperature"].max()+10)
ax1.set_title("City Temperature Analysis")
ax1.set_xlabel("City")
ax1.set_ylabel("Temperature")

ax2.scatter(df["Temperature"],df["Humidity"])
ax2.grid()
ax2.set_xlim(df["Temperature"].min()-5, df["Temperature"].max()+5)
ax2.set_xlabel("Temperature")
ax2.set_ylabel("Humidity")
ax2.set_title("Temperature v/s Humidity analysis")

ax3.plot(df["City"],df["Weather"])
ax3.set_xlabel("City")
ax3.set_ylabel("Weather")
ax3.set_title("City weather distribution")

plt.subplots_adjust(hspace=0.9)
plt.autoscale(True)
plt.show()

"""
5 Days weather forcast for a single city
"""
city = input("Enter a city name: ") #"Bombay"
# values = {"q": city, "appid": }
weather = Weather.Weather()
weather.setForcastAPIParameters()
df = weather.getWeatherData(city)

"""
Time-Based Analysis:
▪ If you want to expand the project, retrieve weather data over a
period of time (e.g., over several days) for one or more cities, and
analyze how temperature and humidity change over time.
"""
df["Dt"] = pd.to_datetime(df["Date"]).dt.date
# print(df)
dt_df = df.groupby("Dt")[["Temperature","Humidity"]].mean().reset_index()
# print(dt_df)
plt.plot(dt_df["Dt"],dt_df["Temperature"], color="blue",label="Temperature",scalex=True,scaley=True,marker=".")
plt.plot(dt_df["Dt"],dt_df["Humidity"], color="red", label="Humidity",scalex=True,scaley=True,marker="*")
plt.title("Temperature v/s Humidity analysis for " + city)
plt.xticks(rotation=60)
plt.xlabel("Date")
plt.ylabel("Temperature/Humidty")
plt.legend(loc="best")
plt.subplots_adjust(bottom=0.2,top=0.4)
plt.axhspan(xmin=5,xmax=10, ymin=5, ymax=10)
plt.show()
"""
Weather Forecast:
▪ Retrieve forecast data using the 5-day forecast endpoint and
analyze trends for a single city.
"""
maxTemp_df = df.groupby("Dt")["MaxTemp"].max().reset_index()
minTemp_df = df.groupby("Dt")["MinTemp"].min().reset_index()
temp_df = pd.DataFrame.merge(maxTemp_df,minTemp_df,how="inner")
# print(temp_df)


X = temp_df["Dt"]
Y = temp_df["MinTemp"]
Z = temp_df["MaxTemp"]

X_axis = np.arange(len(X))

bar1 = plt.bar(X_axis - 0.2, Y, 0.4, label="Min Temp")
bar2 = plt.bar(X_axis + 0.2, Z, 0.4, label="Max Temp")

for bar in bar1:
    yval = bar.get_height()
    plt.text(bar.get_x(), yval + 0.010, yval)

for bar in bar2:
    yval = bar.get_height()
    plt.text(bar.get_x(), yval+0.010, yval)

plt.xticks(X_axis, X)
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.title("Temperature analysis for " + city)
# plt.legend("best")
plt.show()

