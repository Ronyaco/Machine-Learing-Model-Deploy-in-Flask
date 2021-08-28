import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import warnings

raw_data = pd.read_excel("..\\model_creation\data\\toproutesjuly2014jan2021.xlsx")
raw_data.columns = raw_data.iloc[11]
#dropping the first 12 rows with irrelevant information
df = raw_data.iloc[12:,:]

#creating a new column called date, concatenating month/year
df["date"] = df["Month"].astype(str)+'/'+df["Year"].astype(str) 

#standardising column labels
df.columns = df.columns.str.replace(' ','_') #replacing blanks for underscores
df.columns = map(str.lower, df.columns) #all names in lowercase

#filtering destination SYD and MEl
df = df[pd.Series(df.city_pair_destination.str.contains('SYD'))]

df = df[pd.Series(df.city_pair_origin.str.contains('MEL'))]

#converting date column from object to data
df['date'] = pd.to_datetime(df.date) 


#creating a route column concatenating Origin and Destination as "Segment"
df["segment"] = df["city_pair_origin"].astype(str)  +'-' +df["city_pair_destination"].astype(str) 

df.to_csv('routes.csv',index=False)