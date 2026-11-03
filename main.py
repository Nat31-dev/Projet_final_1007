import pandas as pd
import os

data = pd.read_csv("projet_fin_session\\donnees.csv")
pd.crosstab(data, data.columns)