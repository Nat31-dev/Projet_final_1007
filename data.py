import pandas as pd
import numpy as np
import os
import exceptionData
import matplotlib.pyplot as plt
from scipy.stats import linregress



class data_explorer:
    def __init__(self, path:str):
        self.df = pd.read_csv(path)
        
    def suprimer_categories(self, categories:list, inplaces:bool):
        '''Suprime toute les catégories dans la liste categories'''
        for i in categories:
            if not i in self.df.columns:
                raise exceptionData.categoryException(f"{i} ne fait pas partie des catégories.")
        return self.df.drop(columns = categories, axis=1, inplace=inplaces)

    

    def tracer_colonnes(self, col_y, col_x, titre=None, type_graphique="line"):
        """
        Trace la colonne `col_y` en fonction de la colonne `col_x`.

        Paramètres
        ----------
        df : pandas.DataFrame
        Le DataFrame contenant les données.
        col_y : str
        Nom de la colonne affichée sur l'axe vertical (la première).
        col_x : str
            Nom de la colonne affichée sur l'axe horizontal (la deuxième).
        titre : str, optionnel
            Titre du graphique. Par défaut : "col_y en fonction de col_x".
        type_graphique : str, optionnel
            "line" (courbe), "scatter" (nuage de points) ou "bar" (barres).
        """
        for col in (col_y, col_x):
            if col not in self.df.columns:
                raise KeyError(f"La colonne '{col}' est absente du DataFrame.")

        fig, ax = plt.subplots(figsize=(8, 5))

        if type_graphique == "scatter":
            ax.scatter(self.df[col_x], self.df[col_y])
        elif type_graphique == "bar":
            ax.bar(self.df[col_x], self.df[col_y])
        else:
            ax.plot(self.df[col_x], self.df[col_y], marker="o")

        ax.set_xlabel(col_x)
        ax.set_ylabel(col_y)
        ax.set_title(titre or f"{col_y} en fonction de {col_x}")
        ax.grid(True, alpha=0.3)

        fig.tight_layout()
        plt.show()
        return fig, ax
   

        



      



#donne = data_explorer(data)

#print(data.head())
#print(data.describe())


#donne.tracer_colonnes("Prompt_Engineering_Skill","Post_Semester_GPA", type_graphique = "")
