import pandas as pd
import numpy as np
import os
path = os.path.join("C:\\Ecole\\inf1007\\Projet_final_1007", "C:\\Ecole\\inf1007\\Projet_final_1007\\donnees.csv")
print("path : ",path)
data =pd.read_csv(path)
print(data.head())
print(data.describe())
print(data.groupby(["Major_Category"]).mean())