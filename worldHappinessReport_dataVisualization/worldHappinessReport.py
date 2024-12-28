import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

happinessData = pd.read_excel("dataClean.xlsx")
happinessData.info()

sns.set_style("whitegrid")
plt.figure()
sns.scatterplot(x= "Happiness Score", y = "Economy (GDP per Capita)", hue = "Year", data = happinessData)
plt.title("Happiness Score vs Economy (GDP per Capita)")
plt.show()


plt.figure()
sns.regplot(x= "Happiness Score", y = "Economy (GDP per Capita)",data = happinessData, scatter_kws={"alpha":0.2})
plt.title("Happiness Score vs Economy (GDP per Capita) with Line Graph")
plt.show()

plt.figure()
numerical_data = happinessData.select_dtypes(include=['float64', 'int64'])
sns.heatmap(numerical_data.corr(), annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Korelasyon Matrisi")
plt.show()

plt.figure()
sns.lineplot(x = "Happiness Score", y ="Economy (GDP per Capita)", data= happinessData, hue="Year")
plt.show()

plt.figure()
sns.boxplot(data=happinessData, x="Year", y="Happiness Score")
plt.title("Year-wise Happiness Score Distribution")
plt.show()

plt.figure()
sns.boxplot(data=happinessData, x="Year", y="Economy (GDP per Capita)")
plt.title("Year-wise Happiness Score Distribution")
plt.show()

plt.figure()
sns.violinplot(data=happinessData, x="Year", y="Happiness Score", palette="muted")
plt.title("Year-wise Happiness Score (Violin Plot)")
plt.show()