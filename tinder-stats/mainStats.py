import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("")
df1 = df['Interest'].value_counts()/df['Id'].max()
print(df1.head(20))
print(df.groupby(['Id','Interest']).size())