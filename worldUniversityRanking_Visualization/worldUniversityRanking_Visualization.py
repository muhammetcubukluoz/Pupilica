# %%  import library

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import plotly as py
import plotly.graph_objs as go
from plotly.offline import plot
import plotly.io as pio
import plotly.figure_factory as ff

timesData = pd.read_csv("timesData.csv")

timesData.info()

dataHead = timesData.head(2603)

dataColumns = timesData.columns

copyData = timesData.copy()

selected_columns = timesData[['world_rank', 'year']]

# %%

def get_repeated_values(copyData, start_year=2011, end_year=2016):
    repeated_values_df = pd.DataFrame()

    for year in range(start_year, end_year + 1):
        repeated_values = copyData[copyData['year'] == year]['world_rank'].value_counts()
        repeated_values = repeated_values[repeated_values > 1]  # Sadece tekrarlananları al
        temp_df = pd.DataFrame(repeated_values.index, columns=['world_rank'])
        temp_df['count'] = repeated_values.values  # count sütunu ekle
        temp_df['year'] = year
        repeated_values_df = pd.concat([repeated_values_df, temp_df], ignore_index=True)
    
    return repeated_values_df

repeated_values_df = get_repeated_values(copyData)

# %% Clean world_rank 

def clean_world_rank_by_year(dataframe):
    def clean_value(value):
        if isinstance(value, str):
            # Eğer "=" varsa, değeri temizle
            if "=" in value:
                return int(value.replace("=" , "").strip())
            # Eğer "-" varsa, "-" işareti öncesi kısmı al
            elif "-" in value:
                return int(value.split("-")[0].strip())
        return value

    # Yıllara göre işlem yapılıyor
    for year in dataframe['year'].unique():
        dataframe.loc[dataframe['year'] == year, 'world_rank'] = dataframe.loc[dataframe['year'] == year, 'world_rank'].apply(lambda x: clean_value(x))

    return dataframe

clean_world_rank_by_year(copyData)


repeated_values_df2 = get_repeated_values(copyData)

# %% clean university_name

selected_columns_name = timesData[['university_name', 'year']]

from unidecode import unidecode

# Unicode işlemi uygulama
copyData['university_name'] = copyData['university_name'].apply(unidecode)

copyData['university_name'] = copyData['university_name'].str.replace("-", "", regex=False)

copyData['university_name'] = [" ".join(line.split()) for line in copyData['university_name']]

# %% clean country

copyData["country"].unique()

#Unted Kingdom, Unisted States of America,

copyData["country"].replace ( {
    "Unisted States of America" : "United States of America" , 
    "Unted Kingdom"             : "United Kingdom"
} , inplace = True)

copyData["country"].unique()

# %% teaching 

copyData["teaching"].unique()

# %% international

copyData["international"].unique()

copyData['international'] = copyData['international'].fillna(np.nan)

copyData['international'] = copyData['international'].str.replace("-", "")
copyData['international'] = copyData['international'].replace(r'^\s*$', np.nan, regex=True)
copyData['international'] = copyData['international'].astype(float)

copyData.info()

# %% research

copyData["research"].unique()

# %% citations

copyData["citations"].unique()

# %% income

copyData["income"].unique()

copyData['income'] = copyData['income'].str.replace("-", "")
copyData['income'] = copyData['income'].replace(r'^\s*$', np.nan, regex=True)
copyData['income'] = copyData['income'].astype(float)


copyData.info()

# %% total_score

copyData["total_score"].unique()
copyData['total_score'] = copyData['total_score'].str.replace("-", "")
copyData['total_score'] = copyData['total_score'].replace(r'^\s*$', np.nan, regex=True)
copyData['total_score'] = copyData['total_score'].astype(float)

copyData.info()
# %% num_students

copyData["num_students"].unique()
#copyData['num_students'] = copyData['num_students'].str.replace(",", "").astype(float)

copyData.info()

# %% student_staff_ratio

copyData["student_staff_ratio"].unique()

copyData.info()

# %% international_students

copyData.rename(columns={'international_students': 'international_students (%)'}, inplace=True)

#copyData['international_students (%)'] = copyData['international_students (%)'].str.replace('%', '').astype(float)

copyData.info()

# %% female_male_ratio

copyData[['female_ratio', 'male_ratio']] = copyData['female_male_ratio'].str.split(' : ', expand=True)

# String olan oranları integer veya float'a çevir
copyData['female_ratio'] = copyData['female_ratio'].replace(['-', 'None'], np.nan).astype(float)
copyData['male_ratio'] = copyData['male_ratio'].replace(['-', 'None'], np.nan).astype(float)

copyData['female_male_ratio'] = copyData.apply(
    lambda row: 1 if row['male_ratio'] == 0 
    else (row['female_ratio'] / row['male_ratio'] if pd.notnull(row['female_ratio']) and pd.notnull(row['male_ratio']) else np.nan),
    axis=1
)

copyData.info()

# %% year

copyData["year"].unique()

columns = [col for col in copyData.columns if col != 'year']  # 'year' dışındaki tüm sütunları al
columns.append('year')  # 'year' sütununu en sona ekle



copyData.info()

