import pandas as pd
import os
from model import model
from data import data_explorer
import numpy as np
import InterfaceUtilisateur as iu




stock = True
if not stock:
    donne = data_explorer("donnees.csv")
    
    out = donne.df["Post_Semester_GPA"]
    donne.suprimer_categories(["Student_ID", "Post_Semester_GPA", "Skill_Retention_Score", "Burnout_Risk_Level"], True)
    mod = model(inputs=donne.df,output=out.values.ravel(),hidden_layer=10, iter_max=20000, rng_state=0, test_size=0.3,stocked=stock )
    print(mod.train())
    mod.save_model()
else:
    donne = data_explorer("donnees.csv")
   #donne.tracer_colonnes("Post_Semester_GPA","Weekly_GenAI_Hours", titre= "GPA en fin de session en fonction de l'usage de l'IA par semaine" , type_graphique="scatter")
  
    out = donne.df["Post_Semester_GPA"]
    donne.suprimer_categories(["Student_ID", "Post_Semester_GPA", "Skill_Retention_Score", "Burnout_Risk_Level"], True)
    mod = model(file_path="model_file", stocked=stock,inputs=donne.df,output=out.values.ravel(),hidden_layer=10, iter_max=20000, rng_state=0, test_size=0.3,)

##student = model.create_student("STEM", "Junior", 3.4,5.8,"Ideation","Intermediate", 2,True, 10.4, 7,"Strict_Ban",4)
#print(mod.predict(student))
#print(mod.R2_score())
iu.window.mainloop()


