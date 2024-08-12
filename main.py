import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
from census import Census
from us import states
import os
from dotenv import dotenv_values
import requests
import json

config = dotenv_values(".env")
key = os.environ.get("APIKEY")


# host = "https://api.census.gov/data"
# year = "/2019"
# dataset_acronym = "/acs/acs1"
# g = "?get="
# variables = "NAME,B01001_001E"
# location = "&for=us:*"
# # I have my API Key saved in a Class in a separate file so my
# # information can't be seen :)
# usr_key = f"&key={key}"
# Put it all together in one f-string:
# query_url = f"{host}{year}{dataset_acronym}{g}{variables}{location}{usr_key}"
# realUrl = "https://api.census.gov/data/2019/acs/acs1?get=NAME,B01001_001E&for=us:*&key=732036086eed9681751ca3d7a89bc9af0a7d20d6"
# query_url = "https://api.census.gov/data/2022/acs/acs1/profile?get=group(DP04)&ucgid=pseudo(0100000US$0400000)&key=732036086eed9681751ca3d7a89bc9af0a7d20d6"
titleKey = "https://api.census.gov/data/2019/acs/acs5/profile/groups/DP04.json"
print(titleKey)
# Use requests package to call out to the API
response = requests.get(titleKey)
# Convert the Response to text and print the result
print(response)
data = response.json()
print(type(data))

blarg = []

for x, obj in data.items():

    for y in obj:
        newRow = y , obj[y]["label"]
        blarg.append(newRow)

print(len(blarg))
df = pd.DataFrame(blarg)
print(df.head())
print(df.shape)
pd.DataFrame(df).to_csv("dp04Group.csv", index=False)
