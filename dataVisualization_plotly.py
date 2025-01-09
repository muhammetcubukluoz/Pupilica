import plotly as py
import plotly.graph_objs as go
from plotly.offline import plot

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import plotly.io as pio
import plotly.figure_factory as ff

veri = pd.read_csv("universite_siralamasi.csv")

# sütun isimlerinin değiştirilmesi
veri.rename(columns={'world_rank'             : 'dunya_siralama', 
                     'university_name'        : 'uni_isim', 
                     'country'                : 'ulke', 
                     'teaching'               : 'ogretim', 
                     'international'          : 'uluslararası', 
                     'research'               : 'arastirma', 
                     'citations'              : 'alinti', 
                     'income'                 : 'gelir', 
                     'total_score'            : 'toplam_puan',
                     'num_students'           : 'ogrenci_sayisi', 
                     'student_staff_ratio'    : 'ogrenci_calisan_orani', 
                     'international_students' : 'uluslararası_ogrenci',
                     'female_male_ratio'      : 'kadin_erkek_orani',
                     'year'                   : 'yil'}, inplace=True) # inplace = True dediğimiz zaman ismi değiştirilen veri otomatik olarak veri variable'a kaydedili

# %%plotly line + scatter plot
df = veri.iloc[:100,:]

cizgi1= go.Scatter(x = df.dunya_siralama, 
                   y= df.alinti,
                   mode = "lines+markers",
                   name= "Alıntı",
                   marker = dict(color="rgba(78,78,250,0.85)"),
                   text = df.uni_isim
                   )

cizgi2= go.Scatter(x = df.dunya_siralama, 
                   y= df.ogretim,
                   mode = "lines+markers",
                   name= "Ogretim",
                   marker = dict(color="rgba(254,0,0,1)"),
                   text = df.uni_isim
                   )
veri_ = [cizgi1, cizgi2]

yerlesim = dict(title ="ilk 100 Alıntı Puanı",
                xaxis = dict(title = "dunya siralamasi")
                )

fig = dict(data = veri_, layout = yerlesim)
plot(fig, filename="plotly_cizgi1.html")

# %% bar plot

veri2014 = veri[veri.yil == 2014].iloc[:5,:]

bar1 = go.Bar(x = veri2014.uni_isim,
              y = veri2014.alinti,
              name = "Alıntı",
              marker = dict(color = "rgba(255,127,35,0.5)", 
                            line = dict(color = "rgba(0,0,0,0)", width = 1.5)),
              text = veri2014.ulke
              )

bar2 = go.Bar(x = veri2014.uni_isim,
              y = veri2014.ogretim,
              name = "Öğretim",
              marker = dict(color = "rgba(64, 0, 128, 0.5)", 
                            line = dict(color = "rgba(0,0,0,0)", width = 1.5)),
              text = veri2014.ulke
              )


veri_ = [bar1, bar2]
yerlesim = go.Layout(barmode = "group")
fig = go.Figure(data = veri_, layout=yerlesim)
plot(fig, filename="plotly_bar.html")

# %%
"""
2015 yilina ait ilk 10 uninin ogretim skorlarını bar plot olarak 
alıntı skorlarını ise line+scatter plot olarak cizdirelim
"""



veri2015 = veri[veri.yil == 2015].iloc[:10,:]

bar1= go.Scatter(x = veri2015.uni_isim, 
                   y= veri2015.alinti,
                   mode = "lines+markers",
                   name= "Alıntı",
                   marker = dict(color="rgba(78,78,250,0.85)"),
                   text = df.ulke
                   )

bar2 = go.Bar(x = veri2015.uni_isim,
              y = veri2015.ogretim,
              name = "Öğretim",
              marker = dict(color = "rgba(64, 0, 128, 0.5)", 
                            line = dict(color = "rgba(0,0,0,0)", width = 1.5)),
              text = veri2015.ulke
              )


veri_ = [bar1, bar2]
yerlesim = go.Layout(barmode = "group")
fig = go.Figure(data = veri_, layout=yerlesim)
plot(fig, filename="plotly_bar2.html")



# %% pie chart

veri2016 = veri[veri.yil == 2016].iloc[:8,:]
dilim1 = veri2016.ogrenci_sayisi
dilim1_liste = [float(each.replace(',', '.')) for each in veri2016.ogrenci_sayisi]
etiketler = veri2016.uni_isim

cizgi = go.Pie(labels = etiketler, 
               values = dilim1_liste,
               hoverinfo = 'label+value+percent', 
               textinfo = 'value+percent', 
               textfont = dict(size=15),
               rotation = 180,
               hole = 0.05,
               marker = dict(line=dict(color='#000000', width=1)))

veri_ = [cizgi]
yerlesim = dict(title = "2016 yılında dünya sıralamasında ilk 8 de bulunan üniversitelerin öğrenci sayıları ve oranı",
                legend=dict(orientation="h"))

fig = dict(data=veri_,layout=yerlesim)
plot(fig, filename = 'pieChart_OgrenciSayisi.html')

# %%

"""
ilk 8 uni 2016 gelir dağılımı, pie chart
"""

veri2016 = veri[veri.yil == 2016].iloc[:8,:]
dilim2 = veri2016.gelir
dilim2_liste = [float(i) for i in veri2016.gelir]
etiketler = veri2016.uni_isim

cizgi = go.Pie(labels = etiketler, 
               values = dilim2_liste,
               hoverinfo = 'label+value+percent', 
               textinfo = 'value+percent', 
               textfont = dict(size=15),
               rotation = 180,
               hole = 0.05,
               marker = dict(line=dict(color='#000000', width=1)))

veri_ = [cizgi]
yerlesim = dict(title = "2016 yılında dünya sıralamasında ilk 8 de bulunan üniversitelerin öğrenci sayıları ve oranı",
                legend=dict(orientation="h"))

fig = dict(data=veri_,layout=yerlesim)
plot(fig, filename = 'pieChart_OgrenciSayisi.html')

# %% histogram

veri2011 = veri.ogrenci_calisan_orani[veri.yil == 2011]
veri2012 = veri.ogrenci_calisan_orani[veri.yil == 2012]

cizgi1 = go.Histogram(x = veri2011,
                      opacity = 0.75,
                      name = "2011",
                      marker = dict(color='rgba(171, 50, 144, 0.6)'))
cizgi2 = go.Histogram(x = veri2012,
                      opacity = 0.75,
                      name = "2012",
                      marker = dict(color='rgba(23, 150, 196, 0.6)'))

veri_ = [cizgi1, cizgi2]
yerlesim = go.Layout(barmode = 'overlay',
                   title = '2011 ve 2012 yıllarında öğrenci/çalışan oranı',
                   xaxis = dict(title='Öğrenci Çalışan Oranı'),
                   yaxis = dict(title='Frekans'),
)

fig = go.Figure(data=veri_, layout=yerlesim)
plot(fig, filename = 'histogram_OgrenciCalisanOrani.html')

# %% box plot

veri2015 = veri[veri.yil == 2015]

cizgi1 = go.Box( y = veri2015.toplam_puan,
                 name = '2015 yılında Toplam Puan',
                 marker = dict(
                 color = 'rgb(255, 86, 4)'))
cizgi2 = go.Box( y = veri2015.arastirma,
                 name = '2015 yılında Araştırma Puanı',
                 marker = dict(
                 color = 'rgb(14, 149, 233)'))

veri_ = [cizgi1, cizgi2]
plot(veri_, filename = 'boxPlot_Puan.html')

# %% 

"""
ogrenci isleri oranı
2013,14,15 yillari için ilk 100 üni box plot
"""
veri2013 = veri[veri.yil == 2013].iloc[:100,:]
veri2014 = veri[veri.yil == 2014].iloc[:100,:]
veri2015 = veri[veri.yil == 2015].iloc[:100,:]

cizgi1 = go.Box( y = veri2013.ogrenci_calisan_orani,
                 name = '2013 yılında Toplam Puan',
                 text = veri2013.uni_isim + " / " + veri2013.ulke
                )
cizgi2 = go.Box( y = veri2014.ogrenci_calisan_orani,
                 name = '2014 yılında Toplam Puan',
                 text = [f"{uni},{ulke}" for uni,ulke in 
                         zip(veri2014.uni_isim, veri2014.ulke)]
                )
cizgi3 = go.Box( y = veri2015.ogrenci_calisan_orani,
                 name = '2015 yılında Toplam Puan',
                 text = veri2015.uni_isim + " / " + veri2015.ulke
                
                )

veri_ = [cizgi1, cizgi2, cizgi3]
plot(veri_, filename = 'boxPlot_Puan2.html')

# %% scatter plot matrix

veri_gecici = veri[veri.yil == 2015]

veri2015 = veri_gecici.loc[:,["arastirma","uluslararası", "toplam_puan"]]
veri2015["index"] = np.arange(1,len(veri2015)+1)

fig = ff.create_scatterplotmatrix(veri2015, diag='box', index='index',
                                  colormap='Jet',
                                  colormap_type='cat',
                                  height=700, width=700)
"""
Örnek renk haritaları:
'Greys', 'YlGnBu', 'Greens', 'YlOrRd', 'Bluered', 
'RdBu', 'Reds', 'Blues', 'Picnic', 'Rainbow', 
'Portland', 'Jet', 'Hot', 'Blackbody', 'Earth', 
'Electric', 'Viridis', 'Cividis']
"""
plot(fig, filename = 'scatterPlotMatrix_puan.html')

# %% subplots

veri2015 = veri[veri.yil == 2015]

cizgi1 = go.Scatter(x=veri2015.dunya_siralama,
                    y=veri2015.arastirma,
                    name = "Araştırma")

cizgi2 = go.Scatter(x=veri2015.dunya_siralama,
                    y=veri2015.alinti,
                    xaxis='x2',
                    yaxis='y2',
                    name = "Alıntı")

cizgi3 = go.Scatter(x=veri2015.dunya_siralama,
                    y=veri2015.gelir,
                    xaxis='x3',
                    yaxis='y3',
                    name = " Gelir")

cizgi4 = go.Scatter(x=veri2015.dunya_siralama,
                    y=veri2015.toplam_puan,
                    xaxis='x4',
                    yaxis='y4',
                    name = "Toplam Puan")

veri_ = [cizgi1, cizgi2, cizgi3, cizgi4]

yerlesim = go.Layout( xaxis=dict(domain=[0, 0.45]),
                      yaxis=dict(domain=[0, 0.45]),
                      xaxis2=dict(domain=[0.55, 1]),
                      xaxis3=dict(domain=[0, 0.45],anchor='y3'),
                      xaxis4=dict(domain=[0.55, 1],anchor='y4'),
                      yaxis2=dict(domain=[0, 0.45],anchor='x2'),
                      yaxis3=dict(domain=[0.55, 1]),
                      yaxis4=dict(domain=[0.55, 1],anchor='x4'),
                      title = 'Üniversite Sıralamalarına göre araştırma, alıntı, gelir ve toplam puan'
)
fig = go.Figure(data=veri_, layout=yerlesim)
plot(fig, filename = 'subplots_Puan.html')

# %%scatter3d

veri2015 = veri[veri.yil == 2015]

cizgi1 = go.Scatter3d( x=veri2015.dunya_siralama,
                       y=veri2015.arastirma,
                       z=veri2015.alinti,
                       mode='markers',
                       marker=dict(size=10,color="seagreen"),opacity = 0.5)

veri_ = [cizgi1]
yerlesim = go.Layout(margin=dict(l=0,r=0,b=0,t=0))

fig = go.Figure(data=veri_, layout=yerlesim)
plot(fig, filename = 'scatter3d.html')

# %%earth map

veri2016 = veri[veri.yil == 2016]
veri2016.ulke.value_counts() 
ulkeye_gore_toplam_veriler = veri2016.groupby("ulke").sum()

cizgi1 = go.Choropleth( locations = ulkeye_gore_toplam_veriler.index,
                       locationmode='country names',
                       z = ulkeye_gore_toplam_veriler['arastirma'],
                       text = ulkeye_gore_toplam_veriler.index,
                       autocolorscale =False,
                       reversescale = True,
                       colorscale = "iceFire",
                       marker = dict(line = dict(color = 'rgb(255,255,255)',width = 1)),
                                     colorbar = dict( title = 'Araştırma Puanı',tickprefix = ''))
veri_ = [cizgi1]
yerlesim = go.Layout( title = "Ülkelerin Toplam Araştırma Puanları",
                      geo = dict(showframe = True,
                      showlakes = False,
                      showcoastlines = True,
                      projection = dict( type = 'natural earth')))

fig = dict( data=veri_, layout=yerlesim )
plot(fig, filename = 'earthMap.html')

# %% bubble chart

veri2016 = veri[veri.yil == 2016].iloc[:20,:]
ogrenci_sayisi  = [float(each.replace(',', '.')) for each in veri2016.ogrenci_sayisi]
uluslararasi_renk = [float(each) for each in veri2016.uluslararası]

data = [{'y': veri2016.ogretim,
         'x': veri2016.dunya_siralama,
         'mode': 'markers',
         'marker': { 'color': uluslararasi_renk,
                     'size': ogrenci_sayisi,
                     'showscale': True},
         "text" :  veri2016.uni_isim}]

plot(data, filename = 'bubbleChart_OgrenciSayisi.html')

