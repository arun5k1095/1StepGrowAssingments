"""
Weather analysis using SQLite
"""
import sqlite3 as sql


import WeatherAnalysis as Weather

try:
    city =  input("Enter a city name: ")
    weather = Weather.Weather()
    weather.setForcastAPIParameters()
    df = weather.getWeatherData(city)
    # print(df)
except Exception as e:
    print("Error get weather data from OpenWeather.com: ", e)

try:
    connection = sql.connect("WeatherData.db")
    cursor = connection.cursor()
    print("Connection with Weather database established successfully...")
except Exception as e:
    print("Error connecting with Weather database: ", e)

try:
    # cursor.execute("Drop table if exists Weather")
    # connection.commit()

    query = "Create Table if not exists Weather("\
            "ID integer primary key autoincrement,"\
            "City varchar(500) not null,"\
            "Date datetime,"\
            "Weather varchar(200),"\
            "Temperature real,"\
            "MinTemp real, MaxTemp real,"\
            "Humidity real, Windspeed real)"

    cursor.execute(query)
    connection.commit()
    print("Weather table created successfully")

    data = connection.execute("select * from Weather where City ='" + city + "'").fetchall()
    if len(data) > 0:
        raise Exception("Data for this city already exists! Enter another city name.")
        connection.close()


    # read data from dataframe and insert into sql table
    try:
        data = df[["City", "Date", "Weather", "Temperature", "MinTemp", "MaxTemp", "Humidity", "WindSpeed"]]
        # print(data)
        data.to_sql(name="Weather", con=connection, if_exists="append", index=False)
        connection.commit()
        print("Records inserted into Weather table.")
        for rec in connection.execute("select * from Weather").fetchall():
            print(rec, end="\n")
    except Exception as e:
        print("Error inserting records in Weather table: ", e)

except Exception as e:
    print("Error occurred: ", e)


