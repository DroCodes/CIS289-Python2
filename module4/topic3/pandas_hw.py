import pandas as pd

df_temps = pd.read_csv('temps.csv', sep="|", index_col="day of week")

print(df_temps.describe())

df_precip = pd.read_csv('precip.csv', sep="|", index_col="day of week")

df_merged = pd.merge(df_temps, df_precip, on="day of week")
df_merged["Max Temp"] = (df_merged["Max Temp"] - 32) * 5/9
df_merged["Ave Temp"] = (df_merged["Max Temp"] + df_merged["Min Temp"]) / 2
df_merged = df_merged.reindex(columns=["Min Temp", "Ave Temp", "Max Temp", "Precip"])

print(df_merged)
