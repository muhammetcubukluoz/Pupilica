import pandas as pd

excelFiles = ["2015.csv", "2016.csv", "2017.csv", "2018.csv","2019.csv"]

dataFrames = []

for i in excelFiles:
    df = pd.read_csv(i)
    dataFrames.append(df)

mergedData = pd.concat(dataFrames, ignore_index=True)

mergedData.to_csv("mergedFile.csv", index=False)

print("Succsess...")

data = pd.read_csv("mergedFile.csv")

data_head = data.head(782)

data = data_head.copy()

data = data.drop(["Region","Happiness Rank","Happiness.Rank","Overall rank"], axis=1)
data_duplicated = data[data.duplicated()]

#data.info()

temporary = data.copy()
temporary["Country"] = temporary["Country"].fillna(temporary["Country or region"])
temporary["Country or region"] = temporary["Country or region"].fillna(temporary["Country"])

for column in temporary.columns:
    if column not in ["Country", "Country or region"]: 
        mean_value = temporary[column].mean()  
        temporary[column] = temporary[column].fillna(mean_value)  

data = temporary.copy()
data.info()

dataClean = data.to_csv("mergedFileClean.csv", index=False)

# %% tek degiskenli veri analizi
import matplotlib.pyplot as plt
def plotBox(degisken):
    plt.figure()
    plt.boxplot(data[degisken])
    plt.xlabel(degisken)
    plt.show()
    
sayisal_degisken = ["Standard Error","Generosity", "Perceptions of corruption"]

for degisken in sayisal_degisken:
    plotBox(degisken)

def plotHistogram(degisken):
    plt.figure()
    plt.hist(data[degisken], bins=25, color="orange")
    plt.xlabel(degisken)
    plt.show()
    
sayisal_degisken = ["Happiness Score"]

for degisken in sayisal_degisken:
    plotHistogram(degisken)
