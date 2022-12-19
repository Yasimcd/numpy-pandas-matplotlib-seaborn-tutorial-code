import pandas as pd

tgt = pd.read_csv('target.csv')
date_df = tgt['Volume']
print(date_df.head())
