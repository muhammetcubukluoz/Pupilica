import pandas as pd
import numpy as np

veri = pd.read_csv("olimpiyatlar.csv")
veri_head = veri.head(15)

veri.info()

column = veri.columns
veri.rename(columns ={
      "ID"   :    "id" ,
      "Name"  :  "isim",
      "Sex"     :  "cinsiyet",
      "Age"     :"yas",
      "Height"  :"boy",
      "Weight"  :"kilo",
      "Team"  : "takim",
      "NOC"  : "uok",
      "Games"  : "oyunlar",
      "Year"  :"yil",
      "Season"  :"sezon",
      "City"  :"sehir",
      "Sport" :"spor",
      "Event" :"etkinlik",
      "Medal" :"madalya",
    
    }, inplace = True)

veri = veri.drop(["id","oyunlar"], axis=1)

veri_duplicated = veri[veri.duplicated()]

"""
boy, kilo bulunan kayip verileri doldurulmalı (etkinlik ort ?)
cinsiyete gore doldurma?, ort || medyan ???? bu veri seti için farketmez
madalya alamayan sporculari veri setinden cikartalim
"""

import matplotlib.pyplot as plt

plt.figure()
plt.hist(veri.boy, bins=100)
plt.title("boy")
plt.show()

plt.figure()
plt.hist(veri.kilo, bins=100)
plt.title("kilo")
plt.show()

describe = veri.describe()

# boy kilo sutununda bulunan kayip verileri dolduralım (etkn ort)

esssiz_etkinlik = pd.unique(veri.etkinlik)

veri_gecici = veri.copy()
boy_kilo_list = ["boy", "kilo"]
 
for e in esssiz_etkinlik:
    
    #etkinlik filtresi
    etkinlik_filtresi = veri_gecici.etkinlik == e
    
    #veri etkinlige gore filtrele
    veri_filtreli = veri_gecici[etkinlik_filtresi]
    
    #boy ve kilo icin etkinlik ozelinde ortalaam bul
    for s in boy_kilo_list:
        
        ortalama = np.mean(veri_filtreli[s])
        
        if np.isnan(ortalama)== False:
            veri_filtreli[s] = veri_filtreli[s].fillna(ortalama)
        else:
            tum_veri_ortalamasi = np.mean(veri[s])
            veri_filtreli[s] = veri_filtreli[s].fillna(tum_veri_ortalamasi)
            
        veri_gecici[etkinlik_filtresi]= veri_filtreli
    

veri = veri_gecici.copy()
veri.info()


#yasda bulunan kayip veri sorununu cinsiyet ve spora gore dolduralım


esssiz_cinsiyet = pd.unique(veri.cinsiyet)
esssiz_spor = pd.unique(veri.spor)

veri_gecici = veri.copy()
boy_kilo_list = ["boy", "kilo"]
 
for c in esssiz_cinsiyet:
    for s in esssiz_spor:
    
    #cinsiyet ve spor filtresi
        cinsiyet_spor_filtresi = np.logical_and(veri_gecici.cinsiyet == c, veri_gecici.spor == s)
    
    
    #veri cinsiyet ve spor gore filtrele
        veri_filtreli = veri_gecici[cinsiyet_spor_filtresi]
    
        
        ortalama = np.mean(veri_filtreli["yas"])
        
        if np.isnan(ortalama)== False:
            veri_filtreli["yas"] = veri_filtreli["yas"].fillna(ortalama)
        else:
            tum_veri_ortalamasi = np.mean(veri["yas"])
            veri_filtreli["yas"] = veri_filtreli["yas"].fillna(tum_veri_ortalamasi)
            
        veri_gecici[cinsiyet_spor_filtresi]= veri_filtreli
    

veri = veri_gecici.copy()
veri.info()


#madalya alamayan sporcularin bulunmasi

madalya_degiskeni = veri.madalya
null_sayisi = pd.isnull(madalya_degiskeni).sum() ##madalya alamayan 231k


madalya_degiskeni_filtresi = pd.isnull(madalya_degiskeni)

veri = veri[~madalya_degiskeni_filtresi]

veri.to_csv("olimpiyatlar_temizlenmis.csv", index=False)

# %% single variable data analysis
import matplotlib.pyplot as plt
def plotHistogram(degisken):
    plt.figure()
    plt.hist(veri[degisken], bins=85, color="orange")
    plt.xlabel(degisken)
    plt.show()
    
sayisal_degisken = ["yas", "boy", "kilo", "yil"]

for degisken in sayisal_degisken:
    plotHistogram(degisken)
    
    
def plotBox(degisken):
    plt.figure()
    plt.boxplot(veri[degisken])
    plt.xlabel(degisken)
    plt.show()
    
sayisal_degisken = ["yas", "boy", "kilo"]

for degisken in sayisal_degisken:
    plotBox(degisken)
    
# %% Categorical Data

veri = pd.read_csv("olimpiyatlar_temizlenmis.csv")

def plotBar(degisken, n=5):  # en çok 5 adet veriyi görselleştir
    
    veri_ = veri[degisken]  # Eksik değerleri kaldır
    veri_sayma = veri_.value_counts()
    veri_sayma = veri_sayma.iloc[:n]  # Pozisyon tabanlı slicing yap
    
    if veri_sayma.empty:
        print(f"{degisken} değişkeni için veri bulunamadı.")
        return
    
    plt.figure(figsize=(8, 6))  # Şekil boyutunu belirle
    plt.bar(veri_sayma.index, veri_sayma, color="orange")
    plt.xticks(rotation=45)  # Eksen etiketlerini döndür
    plt.ylabel("Frekans")
    plt.title(f"Veri Frekansı: {degisken}")
    plt.show()
    print(f"{veri_sayma}")
    
categorical_columns = veri.select_dtypes(include=["object"]).columns

if len(categorical_columns) == 0:
    print("Kategorik değişken bulunamadı.")
else:
    for degisken in categorical_columns:
        plotBar(degisken, 50)

    


# %% iki degiskneli veri analizi

# cinsiyete gore boy ve kilo vs


erkek= veri[veri.cinsiyet=="M"]
kadin= veri[veri.cinsiyet=="F"]

plt.figure()
plt.scatter(kadin.boy, kadin.kilo, alpha = 0.8, label = "Kadin")
plt.scatter(erkek.boy, erkek.kilo, alpha = 0.2, label = "Erkek")
plt.xlabel("boy")
plt.ylabel("kilo")
plt.title("Boy ve Kilo arasındaki İlişki")
plt.legend()
plt.show()


numeric_correlation = veri.loc[:, ["yas","boy","kilo"]].corr()

veri_gecici = veri.copy()
veri_gecici =pd.get_dummies(veri_gecici, columns=["madalya"])
numeric_correlation_yas_madalya = veri_gecici.loc[:, ["yas",'madalya_Bronze', 'madalya_Gold','madalya_Silver']].corr()

#takımların madalya sayisi
#groupby

groupby_takim = veri_gecici[["takim", 'madalya_Gold','madalya_Silver',"madalya_Bronze"]].groupby(["takim"], as_index = False).sum()
groupby_takim_sorted = groupby_takim.sort_values(by = "madalya_Gold", ascending = False)
groupby_takim_sorted_10 = groupby_takim_sorted[:20]


turkey = groupby_takim.query("takim == 'Turkey'")


#sehirlere gore kazanilan madalyalarin ortalamalari
groupby_sehir = veri_gecici[["sehir",'madalya_Gold','madalya_Silver',"madalya_Bronze"]].groupby(["sehir"],as_index= False).sum().sort_values(by = "madalya_Gold", ascending = False)


groupby_cinsiyet = veri_gecici[["cinsiyet",'madalya_Gold','madalya_Silver',"madalya_Bronze"]].groupby(["cinsiyet"],as_index= False).sum().sort_values(by = "madalya_Gold", ascending = False)


# %% cok degiskenli veri analizi
#pivot table

#madalya alan sporuclarin cinsiyetlerin e göre boy kilo ve yas ortalamalrina bakalim
#3 madalya, 2(sex)*3(boy,kilo,yas)*3(mean,max,min)=18
veri_pivot = veri.pivot_table(index="madalya",
                              columns="cinsiyet",
                              values=["boy","kilo","yas"],
                              aggfunc = {"boy": np.mean, 
                                        "kilo": np.median,
                                        "yas": [np.min, np.max, np.std]})
                             


# takimlara ve cinsiyete göre alınan madalya sayilarinin toplami ve max, min degereleri

veri_pivot_takim_cinsiyet = veri_gecici.pivot_table(index=["takim","sehir"],
                              columns=["cinsiyet","sezon"],
                              values=["madalya_Gold",'madalya_Silver',"madalya_Bronze"],
                              aggfunc = {"madalya_Gold": [np.sum], 
                                        'madalya_Silver': [np.sum],
                                        "madalya_Bronze": [np.sum]})
                             
veri_pivot_takim_cinsiyet["total"]=(
    veri_pivot_takim_cinsiyet["madalya_Gold"].sum(axis=1)+
    veri_pivot_takim_cinsiyet['madalya_Silver'].sum(axis=1)+
    veri_pivot_takim_cinsiyet["madalya_Bronze"].sum(axis=1))

veri_pivot_takim_cinsiyet =veri_pivot_takim_cinsiyet.sort_values(by ="total", ascending=False)[:100]

veri_pivot_takim_cinsiyet.to_excel("veri_pivot_takim_cinsiyet.xlsx",)

# %% outlier detection
"""
yas = veri.yas

plt.hist(yas, bins = 100)
plt.show()

Q1 = np.percentile(yas, 25)

Q3 = np.percentile(yas, 75)

IQR = Q3-Q1

outlier_step = 1*5 + IQR

upper = Q3 + outlier_step
lower = Q1- outlier_step

#outlier degerlerinin indeklerinin tespiti
outlier_list_col = df[(df[c] < lower) | (df[c]> upper)].index

outlier_indices.extend(outlier_list_col)


veri_anomali = veri.loc[anomaliTespiti(veri, ["yas","kilo","boy"])]
anomali_spor = veri_anomali.spor.value_counts()
anomali_etkinlik = veri_anomali.etkinlik.value_counts()

plt.figure()
plt.bar(anomali_sapor.index, anomali_spor.values)
plt.xticks(rotation = 30)

anomali_index_list = veri_anomali.index.tolist()
veri_cleaned = veri.drop(index = anomali_index_list)
"""
