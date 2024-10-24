import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class Weather:
    forcast_url = "http://api.openweathermap.org/data/2.5/forecast"
    forcast_appid = "fced52f453e4753f9c2e897dd3acfcc4"


    def __init__(self):
        self.url = ""
        self.appid = ""


    def setForcastAPIParameters(self):
        self.url = self.forcast_url
        self.appid = self.forcast_appid
        print("Initializing API parameters...")

    def getWeatherData(self,city):
        values = {"q": city, "appid": self.appid}
        response = requests.get(url=self.url, params=values)
        if response.status_code == 200:
            print("Received weather data!")
            try:

                data = response.json()
                # print(data)
                df = pd.DataFrame(
                    columns=["City", "Date", "Weather", "Temperature", "MinTemp", "MaxTemp", "Humidity", "WindSpeed"])
                cnt = data["cnt"]
                for index in range(0, cnt):
                    record = dict(data["list"][index])
                    # print(record)
                    df.loc[len(df)] = {"City": city, "Date": record["dt_txt"], \
                                       "Weather": record["weather"][0]["main"], \
                                       "Temperature": record["main"]["temp"], \
                                       "MinTemp": record["main"]["temp_min"], \
                                       "MaxTemp": record["main"]["temp_max"], \
                                       "Humidity": record["main"]["humidity"], \
                                       "WindSpeed": record["wind"]["speed"]
                                       }
                # print(df)
                return df
            except Exception as e:
                print("Error occurred:", e)
        else:
            print("error", response.status_code, response.reason)


#
# city = input("Enter a city name: ") #"Bombay"
# # values = {"q": city, "appid": }
# weather = Weather()
# weather.setAPIParameters("http://api.openweathermap.org/data/2.5/forecast","fced52f453e4753f9c2e897dd3acfcc4")
# df = weather.getWeatherData(city)
#
# """
# Time-Based Analysis:
# ▪ If you want to expand the project, retrieve weather data over a
# period of time (e.g., over several days) for one or more cities, and
# analyze how temperature and humidity change over time.
# """
# df["Dt"] = pd.to_datetime(df["Date"]).dt.date
# # print(df)
# dt_df = df.groupby("Dt")[["Temperature","Humidity"]].mean().reset_index()
# # print(dt_df)
# # plt.plot(dt_df["Dt"],dt_df["Temperature"], color="blue",label="Temperature",scalex=True,scaley=True,marker=".")
# # plt.plot(dt_df["Dt"],dt_df["Humidity"], color="red", label="Humidity",scalex=True,scaley=True,marker="*")
# # plt.title("Temperature v/s Humidity analysis for " + city)
# # plt.xticks(rotation=60)
# # plt.xlabel("Date")
# # plt.ylabel("Temperature/Humidty")
# # plt.legend(loc="best")
# # plt.subplots_adjust(bottom=0.2,top=0.4)
# # plt.axhspan(xmin=5,xmax=10, ymin=5, ymax=10)
# # plt.show()
# """
# Weather Forecast:
# ▪ Retrieve forecast data using the 5-day forecast endpoint and
# analyze trends for a single city.
# """
# maxTemp_df = df.groupby("Dt")["MaxTemp"].max().reset_index()
# minTemp_df = df.groupby("Dt")["MinTemp"].min().reset_index()
# temp_df = pd.DataFrame.merge(maxTemp_df,minTemp_df,how="inner")
# # print(temp_df)
#
#
# X = temp_df["Dt"]
# Y = temp_df["MinTemp"]
# Z = temp_df["MaxTemp"]
#
# X_axis = np.arange(len(X))
#
# bar1 = plt.bar(X_axis - 0.2, Y, 0.4, label="Min Temp")
# bar2 = plt.bar(X_axis + 0.2, Z, 0.4, label="Max Temp")
#
# for bar in bar1:
#     yval = bar.get_height()
#     plt.text(bar.get_x(), yval + 0.010, yval)
#
# for bar in bar2:
#     yval = bar.get_height()
#     plt.text(bar.get_x(), yval+0.010, yval)
#
# plt.xticks(X_axis, X)
# plt.xlabel("Date")
# plt.ylabel("Temperature")
# plt.title("Temperature analysis for " + city)
# # plt.legend("best")
# plt.show()