import pandas as pd

tgt = pd.read_csv('/Users/yasimcruzdiaz/Desktop/SDCCD/Class 663 PYTHON 4/CODE/target.csv')
date_df = tgt['Volume']
print(date_df.head())