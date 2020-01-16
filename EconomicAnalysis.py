import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

def make_dashboard(x, gdp_change, unemployment, title):
    plt.xlabel("Year", fontdict = None, labelpad = None)
    plt.ylabel("%", fontdict = None, labelpad = None)
    plt.title(title, fontdict = None, loc = "center", pad = None)
    plt.plot(x, gdp_change, "blue", linewidth = 4, label = "% GDP Change")
    plt.plot(x, unemployment, "red", linewidth = 4, label = "% Unemployment")
    plt.legend()
    plt.show()


links={'GDP':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_gdp.csv',\
       'unemployment':'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/projects/coursera_project/clean_unemployment.csv'}

data_frame_gdp = pd.read_csv(links["GDP"]) #display the first five rows of GDP data
print("Example GDP data")
print(data_frame_gdp.head())

data_frame_unemp = pd.read_csv(links["unemployment"]) #display the first five rows of unemployment data
print("\nExample unemployment rate")
print(data_frame_unemp.head())

print("\nUnemployment rate over 8.5%")
print(data_frame_unemp[data_frame_unemp["unemployment"] > 8.5]) #display unemployment when rate > 8.5%

x = data_frame_gdp["date"]
gdp_change = data_frame_gdp["change-current"]
unemployment = data_frame_unemp["unemployment"]
title = "Dashboard Data"

make_dashboard(x, gdp_change, unemployment, title)