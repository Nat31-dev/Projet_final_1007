import pandas as pd
import os
data = pd.read_csv("projet_fin_session\\ai_student_impact_dataset(1).csv")
pd.crosstab(data, data.columns)

tst = "Test github"
print(tst)