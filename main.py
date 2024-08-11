import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
from census import Census
from us import states
import os
from dotenv import load_dotenv, dotenv_values
import requests

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
query_url = "https://api.census.gov/data/2022/acs/acs1/profile?get=group(DP04)&ucgid=pseudo(0100000US$0400000)&key=732036086eed9681751ca3d7a89bc9af0a7d20d6"
print(query_url)
# Use requests package to call out to the API
response = requests.get(query_url)
# Convert the Response to text and print the result
print(response)
data = response.json()
print(data)
df = pd.json_normalize(data)
pd.DataFrame(data).to_csv("out.csv", index=False)
