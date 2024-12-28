import pandas as pd
import numpy as np

data2015 = pd.read_csv("2015.csv")

data2015['Year'] = 2015
#data2015.drop(columns=['Region'], inplace=True)
data2015.to_csv("2015.csv", index=False)
data2015.info()

data2016 = pd.read_csv("2016.csv")
data2016['Year'] = 2016
#data2016.drop(columns=['Region'], inplace=True)
data2016.to_csv("2016.csv", index=False)
data2016.info()

data2017 = pd.read_csv("2017.csv")
data2017['Year'] = 2017
data2017.rename(columns={
    'Country or region': 'Country',
    'Happiness.Rank': 'Happiness Rank',
    'Happiness.Score': 'Happiness Score',
    'Economy..GDP.per.Capita.': 'Economy (GDP per Capita)',
    'Health..Life.Expectancy.':'Health (Life Expectancy)',
    'Trust..Government.Corruption.': 'Trust (Government Corruption)',
    'Dystopia.Residual':'Dystopia Residual'
    }, inplace=True)
data2017.to_csv("2017.csv", index=False)
data2017.info()

data2018 = pd.read_csv("2018.csv")
data2018['Year'] = 2018
data2018.rename(columns={
    'Country or region': 'Country',
    'Overall rank': 'Happiness Rank',
    'Score':'Happiness Score',
    'GDP per capita': 'Economy (GDP per Capita)',
    'Social support': 'Family',
    'Healthy life expectancy':'Health (Life Expectancy)',
    'Freedom to make life choices': 'Freedom',
    'Perceptions of corruption': 'Trust (Government Corruption)'
    }, inplace=True)
data2018.to_csv("2018.csv", index=False)
data2018.info()

data2019 = pd.read_csv("2019.csv")
data2019['Year'] = 2019
data2019.rename(columns={
    'Country or region': 'Country',
    'Overall rank': 'Happiness Rank',
    'Score':'Happiness Score',
    'GDP per capita': 'Economy (GDP per Capita)',
    'Social support': 'Family',
    'Healthy life expectancy':'Health (Life Expectancy)',
    'Freedom to make life choices': 'Freedom',
    'Perceptions of corruption': 'Trust (Government Corruption)'
    }, inplace=True)
data2019.to_csv("2019.csv", index=False)
data2019.info()

# %% merged files
excelFiles = ["2015.csv", "2016.csv", "2017.csv", "2018.csv","2019.csv"]

dataFrames = []

for i in excelFiles:
    df = pd.read_csv(i)
    dataFrames.append(df)

mergedData = pd.concat(dataFrames, ignore_index=True)

mergedData.to_csv("mergedData.csv", index=False)

print("Succsess...")

data = pd.read_csv("mergedData.csv")


# %% null column

temporary = data.copy()

for column in temporary.columns:
    if data[column].dtype in ['float64', 'int64']:    
        mean_value = temporary[column].mean()  
        temporary[column] = temporary[column].fillna(mean_value)

data = temporary.copy()
data.info()

dataClean = data.to_excel("dataClean.xlsx", index=False)