from sklearn.neural_network import MLPRegressor
import sklearn
from data import data_explorer
import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import joblib as jb


class model:
   def __init__(self,inputs:pd.core.frame.dataframe = None,output:np.ndarray = None, hidden_layer:int = 0, iter_max:int = 0, rng_state:int = 0,test_size:int = 0, file_path:str = "", stocked:bool = False  ):
      '''Si stocked = True, entrer le path vers le fichier où est stoqué le modèle, sinon mettre touts les autres variables pour initialiser le modèle.'''
      inputs = model.numériser_categories(inputs)
      self.__x_train, self.__x_test,self.__y_train,self.__y_test = sklearn.model_selection.train_test_split(inputs, output,random_state=rng_state, test_size=test_size)
      if not stocked:
         self.model = MLPRegressor(hidden_layer_sizes=(hidden_layer,), max_iter=iter_max, random_state=rng_state)
         self.__trained__ = False
      else:
         self.model = jb.load(filename=file_path )
         self.__trained__ = True

   def train(self):
      '''Entraine le modèle et renvoi "entrainement du modèle réussi" si Trained  = False sinon renvoi "Le modèle à déja été entrainer."'''
      if not self.__trained__:
         self.model.fit(self.__x_train, self.__y_train)
         self.__trained__ = True
         return "entrainement du modèle réussi"
      else:
         return "Le modèle à déja été entrainé"

   def R2_score(self) -> float:
      '''Retourne le score R2 de la courbe du modèle.'''
      return self.model.score(self.__x_test, self.__y_test)
   def predict(self, to_predict:pd.core.frame.dataframe) -> float:
      return self.model.predict(to_predict)
   @staticmethod
   def numériser_categories(df:pd.core.frame.dataframe):
      '''Prend en entré le dataframe contenant les variables et remplace les variables catégoricielles par des entiers'''
      cat = {
            "Humanities": 1, "Medical": 2, "Business": 3,"STEM": 4,"Arts": 5,
            "Freshman":1,"Sophomore": 2,"Junior" :3,"Senior":4, "Graduate":5,
            "Copywriting/Drafting" : 1, "Ideation":2, "Summarizing_Reading" : 3, "Debugging/Troubleshooting" : 4,"Direct_Answer_Generation" : 5,
            "Beginner" : 1, "Intermediate" : 2, "Advanced" : 3,
            "Allowed_With_Citation" : 1, "Strict_Ban" :2, "Actively_Encouraged" : 3
            }
      return df.replace(cat, inplace=False)
   @staticmethod
   def  create_student(Major:str,Year_of_Study:str, Pre_Semester_GPA:float,Weekly_GenAI_Hours:float, Primary_Use_Case:str,Prompt_Engineering_Skill:str,Tool_Diversity:int, Paid_Subscription:bool, Traditional_Study_Hours:float, Perceived_AI_Dependency:int,Institutional_Policy:str,Anxiety_Level_During_Exams:int) -> pd.core.frame.dataframe:
      """"""
      dic = {
         "Major_Category" : [Major],
         "Year_of_Study" : [Year_of_Study],
         "Pre_Semester_GPA" : [Pre_Semester_GPA],
         "Weekly_GenAI_Hours" : [Weekly_GenAI_Hours],
         "Primary_Use_Case" : [Primary_Use_Case],
         "Prompt_Engineering_Skill" : [Prompt_Engineering_Skill],
         "Tool_Diversity" : [Tool_Diversity],
         "Paid_Subscription" : [Paid_Subscription],
         "Traditional_Study_Hours" : [Traditional_Study_Hours],
         "Perceived_AI_Dependency" : [Perceived_AI_Dependency],
         "Institutional_Policy" : [Institutional_Policy],
         "Anxiety_Level_During_Exams" : [Anxiety_Level_During_Exams]
      }
      return model.numériser_categories(pd.DataFrame(dic))
   def save_model(self):
      jb.dump(value = self.model, filename="model_file")

 


#path = os.path.join("C:\\Ecole\\inf1007\\Projet_final_1007", "C:\\Ecole\\inf1007\\Projet_final_1007\\donnees.csv")
#modele = MLPRegressor(hidden_layer_sizes=(10,), max_iter=20000, random_state=235)
#entre = data_explorer(path)
#print(entre.df.shape)
#cat_exclus_entre = ["Student_ID", "Post_Semester_GPA"]
#cat_exclus_sortie = ["Student_ID","Major_Category","Year_of_Study","Perceived_AI_Dependency","Pre_Semester_GPA","Weekly_GenAI_Hours", "Traditional_Study_Hours","Student_ID","Primary_Use_Case","Prompt_Engineering_Skill","Tool_Diversity","Paid_Subscription","Institutional_Policy","Anxiety_Level_During_Exams","Skill_Retention_Score","Burnout_Risk_Level"]
#sortie = entre.suprimer_cattégories(cat_exclus_sortie,False)
#entre.suprimer_cattégories(cat_exclus_entre,True)
#print(entre.df.shape)
#print(sortie.shape)
#major_cat ={
 #           "Humanities": 1, "Medical": 2, "Business": 3,"STEM": 4,"Arts": 5,
  #          "Freshman":1,"Sophomore": 2,"Junior" :3,"Senior":4, "Graduate":5,
   #         "Copywriting/Drafting" : 1, "Ideation":2, "Summarizing_Reading" : 3, "Debugging/Troubleshooting" : 4,"Direct_Answer_Generation" : 5,
    #        "Beginner" : 1, "Intermediate" : 2, "Advanced" : 3,
     #       "Allowed_With_Citation" : 1, "Strict_Ban" :2, "Actively_Encouraged" : 3,
      #      "Low" : 1, "Medium" : 2, "High" :3
       #     }


#entre.df.replace(major_cat,inplace=True)



#print(type(sortie.values.ravel()))
#student = pd.DataFrame({"Major_Category" : [major_cat["Medical"]], "Year_of_Study":[major_cat["Junior"]],"Pre_Semester_GPA":[1.4], "Weekly_GenAI_Hours":[1.5],"Traditional_Study_Hours" :[10], "Perceived_AI_Dependency" :[0]})
#x_train, x_test,y_train,y_test = sklearn.model_selection.train_test_split(entre.df, sortie.values.ravel(),random_state=35, test_size=0.2)
#modele.fit(x_train, y_train)

#for i in range(len(y_test)):
   # print(F"test : {modele.predict(x_test)[i]} : {y_test[i]} ")



#print(f"score: {modele.score(x_test, y_test)}")
#plt.plot(modele.predict(x_test), color="red",label="prediction")
#plt.plot(y_test,color = "blue",label="vrai",alpha=0.5)
#plt.legend()
#plt.xlim(500, 600)     # L'axe X ira de 0 à 50
#plt.ylim(0, 5)  # L'axe Y ira de -10 à 100
#plt.show()
#print(modele.predict(student))