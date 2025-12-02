import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("bike_sales_india.csv")
df.head()

df.info()

df.describe()
df.isnull().sum()
df.duplicated().sum()

