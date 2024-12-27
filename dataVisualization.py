<<<<<<< HEAD
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

veri = pd.read_csv("olimpiyatlar_temizlenmis.csv")

# %% scatter plot

sns.set_style("white")
plt.figure()
sns.scatterplot(x= "boy", y = "kilo", data = veri)
plt.title("boy vs kilo")
plt.show()

sns.set_style("darkgrid")
plt.figure()
sns.scatterplot(x= "boy", y = "kilo", data = veri)
plt.title("boy vs kilo")
plt.show()

sns.set_style("whitegrid")
plt.figure()
sns.scatterplot(x= "boy", y = "kilo", data = veri)
plt.title("boy vs kilo")
plt.show()

# boy vs kilo cinsiyet type
plt.figure()
sns.scatterplot(x = "boy", y="kilo", data = veri, hue="cinsiyet")
plt.show()

# scatter plot with linear reg
plt.figure()
sns.regplot(x = "boy", y="kilo", data = veri, marker = "+", scatter_kws={"alpha":0.2})
plt.show()

#renk paletleri

plt.figure()
sns.scatterplot(x = "boy", y="kilo", data = veri, hue="madalya", palette="Blues")
plt.show()

# sezona göre boy ve kilo karşılaştırma

plt.figure()
sns.scatterplot(x = "boy", y="kilo", data = veri, hue="sezon", palette="Reds")
plt.title("Boy ve Kilo Dağılımı")
plt.show()

# %% line plot

plt.figure()
sns.lineplot(x = "boy", y ="kilo", data= veri)
plt.show()

# categorical line graph

plt.figure()
sns.lineplot(x = "boy", y ="kilo", data= veri, hue="madalya")
plt.show()

# %% histogram

plt.figure()
sns.histplot(veri, x="kilo")
plt.show()

plt.figure()
sns.histplot(veri, x="kilo", hue="cinsiyet")
plt.show()

plt.figure()
sns.displot(veri, x="kilo", col="cinsiyet")
plt.show()

#iki boyutlu his

plt.figure()
sns.displot(veri, x="kilo", y="boy", kind="kde", hue="cinsiyet")
plt.show()

plt.figure()
sns.displot(veri, x="kilo", y="boy", kind="kde", hue="sezon")
plt.show()

# %% bar plot

plt.figure()
sns.barplot(x = "madalya", y = "boy", data = veri)
plt.show()

plt.figure()
sns.barplot(x = "madalya", y = "yas", data = veri, hue="cinsiyet")
plt.show()

plt.figure()
sns.catplot(x = "madalya", y = "yas", data = veri, hue="cinsiyet", col="sezon", kind="bar")
plt.show()

# spor vs boy cinsiyet kategorisine ve sezon sutununa gore
plt.figure()
sns.catplot(x = "spor", y = "boy", data = veri, hue="cinsiyet", col="sezon", kind="bar")
plt.xticks(rotation = 90)
plt.show()


# %% box plot

plt.figure()
sns.boxplot(x="sezon", y="boy", data=veri)
plt.show()

plt.figure()
sns.boxplot(x="sezon", y="boy", data=veri, hue="cinsiyet")
plt.show()

plt.figure()
sns.boxplot(x="boy", y="sezon", data=veri, hue="cinsiyet", orient="h")
plt.show()

plt.figure()
sns.catplot(x="sezon", y="boy", hue="cinsiyet", col="madalya", data=veri, kind="box")
plt.show()

#cinsiyet vs yas
plt.figure()
sns.catplot(x="cinsiyet", y="yas", hue="madalya", col="sezon", data=veri, kind="box")
plt.show()

# %% heat map

veri_gecici = veri.loc[:,["yas","boy","kilo"]]
correlation = veri_gecici.corr()

plt.figure()
sns.heatmap(correlation, annot=True, fmt=".2f", linewidths=0.5)
plt.show()

# %% violin plot

plt.figure()
sns.violinplot(x="sezon", y="boy", data=veri)
plt.show()

plt.figure()
sns.violinplot(x="sezon", y="boy", data=veri, hue="cinsiyet")
plt.show()

plt.figure()
sns.violinplot(x="sezon", y="boy", data=veri, hue="cinsiyet", split=True)
plt.show()

plt.figure()
sns.catplot(x="sezon", y="boy",hue="cinsiyet", col="madalya", data=veri, kind="violin", split=True)
plt.show()


# %% joint plot

plt.figure()
sns.jointplot(data=veri, x="kilo", y="boy", hue="sezon",kind="kde")
plt.show()

plt.figure()
g = sns.jointplot(data=veri, x="kilo", y="boy")
g.plot_joint(sns.histplot)
g.plot_marginals(sns.boxplot)
plt.show()

# %% pairplot

plt.figure()
sns.pairplot(veri)
plt.show()

plt.figure()
g = sns.PairGrid(veri)
g.map_upper(sns.histplot)
g.map_lower(sns.kdeplot)
g.map_diag(sns.histplot, kde=True)
plt.show()


# %% count plot

plt.figure()
sns.countplot(x="sehir", data=veri)
plt.xticks(rotation=90)
plt.show()



=======
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

veri = pd.read_csv("olimpiyatlar_temizlenmis.csv")

# %% scatter plot

sns.set_style("white")
plt.figure()
sns.scatterplot(x= "boy", y = "kilo", data = veri)
plt.title("boy vs kilo")
plt.show()

sns.set_style("darkgrid")
plt.figure()
sns.scatterplot(x= "boy", y = "kilo", data = veri)
plt.title("boy vs kilo")
plt.show()

sns.set_style("whitegrid")
plt.figure()
sns.scatterplot(x= "boy", y = "kilo", data = veri)
plt.title("boy vs kilo")
plt.show()

# boy vs kilo cinsiyet type
plt.figure()
sns.scatterplot(x = "boy", y="kilo", data = veri, hue="cinsiyet")
plt.show()

# scatter plot with linear reg
plt.figure()
sns.regplot(x = "boy", y="kilo", data = veri, marker = "+", scatter_kws={"alpha":0.2})
plt.show()

#renk paletleri

plt.figure()
sns.scatterplot(x = "boy", y="kilo", data = veri, hue="madalya", palette="Blues")
plt.show()

# sezona göre boy ve kilo karşılaştırma

plt.figure()
sns.scatterplot(x = "boy", y="kilo", data = veri, hue="sezon", palette="Reds")
plt.title("Boy ve Kilo Dağılımı")
plt.show()

# %% line plot

plt.figure()
sns.lineplot(x = "boy", y ="kilo", data= veri)
plt.show()

# categorical line graph

plt.figure()
sns.lineplot(x = "boy", y ="kilo", data= veri, hue="madalya")
plt.show()

# %% histogram

plt.figure()
sns.histplot(veri, x="kilo")
plt.show()

plt.figure()
sns.histplot(veri, x="kilo", hue="cinsiyet")
plt.show()

plt.figure()
sns.displot(veri, x="kilo", col="cinsiyet")
plt.show()

#iki boyutlu his

plt.figure()
sns.displot(veri, x="kilo", y="boy", kind="kde", hue="cinsiyet")
plt.show()

plt.figure()
sns.displot(veri, x="kilo", y="boy", kind="kde", hue="sezon")
plt.show()

# %% bar plot

plt.figure()
sns.barplot(x = "madalya", y = "boy", data = veri)
plt.show()

plt.figure()
sns.barplot(x = "madalya", y = "yas", data = veri, hue="cinsiyet")
plt.show()

plt.figure()
sns.catplot(x = "madalya", y = "yas", data = veri, hue="cinsiyet", col="sezon", kind="bar")
plt.show()

# spor vs boy cinsiyet kategorisine ve sezon sutununa gore
plt.figure()
sns.catplot(x = "spor", y = "boy", data = veri, hue="cinsiyet", col="sezon", kind="bar")
plt.xticks(rotation = 90)
plt.show()


# %% box plot

plt.figure()
sns.boxplot(x="sezon", y="boy", data=veri)
plt.show()

plt.figure()
sns.boxplot(x="sezon", y="boy", data=veri, hue="cinsiyet")
plt.show()

plt.figure()
sns.boxplot(x="boy", y="sezon", data=veri, hue="cinsiyet", orient="h")
plt.show()

plt.figure()
sns.catplot(x="sezon", y="boy", hue="cinsiyet", col="madalya", data=veri, kind="box")
plt.show()

#cinsiyet vs yas
plt.figure()
sns.catplot(x="cinsiyet", y="yas", hue="madalya", col="sezon", data=veri, kind="box")
plt.show()

# %% heat map

veri_gecici = veri.loc[:,["yas","boy","kilo"]]
correlation = veri_gecici.corr()

plt.figure()
sns.heatmap(correlation, annot=True, fmt=".2f", linewidths=0.5)
plt.show()

# %% violin plot

plt.figure()
sns.violinplot(x="sezon", y="boy", data=veri)
plt.show()

plt.figure()
sns.violinplot(x="sezon", y="boy", data=veri, hue="cinsiyet")
plt.show()

plt.figure()
sns.violinplot(x="sezon", y="boy", data=veri, hue="cinsiyet", split=True)
plt.show()

plt.figure()
sns.catplot(x="sezon", y="boy",hue="cinsiyet", col="madalya", data=veri, kind="violin", split=True)
plt.show()


# %% joint plot

plt.figure()
sns.jointplot(data=veri, x="kilo", y="boy", hue="sezon",kind="kde")
plt.show()

plt.figure()
g = sns.jointplot(data=veri, x="kilo", y="boy")
g.plot_joint(sns.histplot)
g.plot_marginals(sns.boxplot)
plt.show()

# %% pairplot

plt.figure()
sns.pairplot(veri)
plt.show()

plt.figure()
g = sns.PairGrid(veri)
g.map_upper(sns.histplot)
g.map_lower(sns.kdeplot)
g.map_diag(sns.histplot, kde=True)
plt.show()


# %% count plot

plt.figure()
sns.countplot(x="sehir", data=veri)
plt.xticks(rotation=90)
plt.show()



>>>>>>> 5423c9480c08cd8ee3229f1d3ec760838be12825
