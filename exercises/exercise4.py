import pandas as pd
import zipfile
import urllib.request
from sqlalchemy import create_engine

#               ***Fetching***          
url = "https://www.mowesta.com/data/measure/mowesta-dataset-20221107.zip"
path = "./exercises/mowesta-dataset-20221107.zip"    
urllib.request.urlretrieve(url, path)

#               ***Extracting***        
with zipfile.ZipFile(path, 'r') as zip_ref:
    zip_ref.extractall('./exercises')

#               ***Reading***           


df = pd.read_csv("./exercises/data.csv", delimiter=';', index_col=False, usecols=["Geraet", "Hersteller", "Model", "Monat", "Temperatur in °C (DWD)", "Batterietemperatur in °C", "Geraet aktiv"])

#               ***Columns Renaming***      
df = df.rename(columns={"Temperatur in °C (DWD)": "Temperatur", "Batterietemperatur in °C": "Batterietemperatur"})

#               ***Data Transformation***
# Data Transformation
df["Temperatur"] = pd.to_numeric(df["Temperatur"], errors='coerce')
df["Batterietemperatur"] = pd.to_numeric(df["Batterietemperatur"], errors='coerce')

# Columns Renaming
df = df.rename(columns={"Temperatur in °C (DWD)": "Temperatur", "Batterietemperatur in °C": "Batterietemperatur"})

# Data Transformation
df["Temperatur"] = df["Temperatur"] * 9/5 + 32
df["Batterietemperatur"] = df["Batterietemperatur"] * 9/5 + 32

#               ***Types Validation***
column_types = {
        'Geraet': int,
        'Hersteller': str,
        'Model': str,
        'Monat': int,
        'Temperatur': float,
        'Batterietemperatur': float,
        'Geraet aktiv': str
        }
df = df.astype(column_types)

# write to sqlite database

df.to_sql("temperatures", 'sqlite:///temperatures.sqlite', if_exists="replace", index=False)

