import tkinter as tkinter
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
import os
import model
from data import data_explorer 





def assigner():
    """
    Assigne chaque variable dans la fonction de calcul du modele
    """
    domaine_etude = liste_domaine[domaine.get()]
    niveau_etude = liste_niveaux[niveau.get()]
    gpa_before = float(gpa_avant.get())
    heures = float(heure_ia_semaine.get())
    usage = liste_usages[usage_principal.get()]
    prompt = liste_prompt[prompt_engineering.get()]
    outils = outils_ia.get()
    abonnement_payant = abonnement.get() == 1
    etude_trad = float(etude.get())
    dependance_percu = dependance.get()
    politique_ia = liste_politique[politique.get()]
    anxieu = anxiete.get()

    stock = False
    if not stock:
        donne = data_explorer("donnees.csv")
        out = donne.df["Post_Semester_GPA"]
        donne.suprimer_categories(["Student_ID", "Post_Semester_GPA", "Skill_Retention_Score", "Burnout_Risk_Level"], True)
        mod = model(inputs=donne.df,output=out.values.ravel(),hidden_layer=10, iter_max=20000, rng_state=0, test_size=0.3,stocked=stock )
        print(mod.train())
        mod.save_model()
    else:
        mod = model(file_path="model_file", stocked=stock)

    student = model.create_student(domaine_etude, niveau_etude, gpa_before, heures,
                                   usage, prompt, outils, abonnement_payant,
                                   etude_trad, dependance_percu, politique_ia,
                                   anxieu)
    
    new_gpa = mod.predict(student)

    show_GPA(new_gpa)
    create_figure_tabs()



def create_figure_tabs():
    """
    Produit un onglet pour chacune des figures
    """
    folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figures")
    i = 1
    for name in os.listdir(folder):
        path = os.path.join(folder, name)
        if os.path.isfile(path):
            tab = tkinter.Frame(notebook)
            notebook.add(tab, f"Figure #{i}")
            figure = tkinter.PhotoImage(file=path)
            tkinter.Label(tab, image=figure).pack()

def show_GPA(new_gpa : int):
    """
    Produit un onglet pour le nouveaux GPA, puis l'affiche
    """
    tab = tkinter.Frame(notebook)
    notebook.add(tab, "Nouveaux GPA")
    tkinter.Label(tab, f"Votre nouveau GPA serait : {new_gpa}").pack()

            

window = tkinter.Tk()
window.geometry("500x500")
window.title("Calcul du GPA selon analyse de données sur l'étudiant")
icon = tkinter.PhotoImage(file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Images", "Polylogo.png"))
window.iconphoto(True, icon)
window.config(bg="#0d052c")

notebook = ttk.Notebook(window)


tkinter.Label(window, text = "Veuillez entrer les informations nécessaires : ", font=("Arial", 15, "bold")).grid(row=0, column=2)
tkinter.Label(window, bg="#0d052c").grid(row=1,column=0)
tkinter.Label(window, bg="#0d052c").grid(row=1,column=1)

tkinter.Label(window, text = "Quel est votre domaine d'études?").grid(row=4,column=0)
domaine = tkinter.IntVar()
liste_domaine = ["Humanities", "Medical", "Business", "STEM", "Arts"]
for i in range(len(liste_domaine)):
    radiobutton = tkinter.Radiobutton(window, text = liste_domaine[i], variable=domaine, value = i)
    radiobutton.grid(row=i + 2, column=1)
    radiobutton.config(indicatoron=0,
                       width= 20)
tkinter.Label(window, bg="#0d052c").grid(row=7, column=0)
tkinter.Label(window, bg="#0d052c").grid(row=7, column=1)

tkinter.Label(window, text = "Quel est votre niveau d'études?").grid(row=9,column=0)
niveau = tkinter.IntVar()
liste_niveaux = ["Freshman", "Junior", "Sophomore", "Senior"]
for i in range(len(liste_niveaux)):
    radiobutton = tkinter.Radiobutton(window, text = liste_niveaux[i], variable=niveau, value = i)
    radiobutton.grid(row=i + 8, column=1)
    radiobutton.config(indicatoron=0,
                       width= 20)
tkinter.Label(window, bg="#0d052c").grid(row=12, column=0)
tkinter.Label(window, bg="#0d052c").grid(row=12, column=1)

tkinter.Label(window, text = "Quel est votre GPA avant le semestre?").grid(row=13,column=0)
gpa_avant = tkinter.Entry(window).grid(row=13, column=1)
tkinter.Label(window, bg="#0d052c").grid(row=14, column=0)
tkinter.Label(window, bg="#0d052c").grid(row=14, column=1)


tkinter.Label(window, text = "Combien d'heure utilisez-vous l'IA générative chaque semaine?").grid(row=15,column=0)
heure_ia_semaine = tkinter.Entry(window).grid(row=15, column=1)
tkinter.Label(window, bg="#0d052c").grid(row=16, column=0)
tkinter.Label(window, bg="#0d052c").grid(row=16, column=1)

tkinter.Label(window, text = "Quel est votre usage principale de l'IA?").grid(row=19,column=0)
usage_principal = tkinter.IntVar()
liste_usages = ["Copywriting/Drafting", "Ideation", "Summarizing_Reading", "Debugging/Troubleshooting", "Direct_Answer_Generation"]
for i in range(len(liste_usages)):
    radiobutton = tkinter.Radiobutton(window, text = liste_usages[i], variable=usage_principal, value = i)
    radiobutton.grid(row=i + 17, column=1)
    radiobutton.config(indicatoron=0,
                       width= 20)
tkinter.Label(window, bg="#0d052c").grid(row=22, column=0)
tkinter.Label(window, bg="#0d052c").grid(row=22, column=1)

tkinter.Label(window, text = "Quel est votre niveau en « Prompt Engineering »?").grid(row=24,column=0)
prompt_engineering = tkinter.IntVar()
liste_prompt = ["Beginner", "Intermediate", "Advanced"]
for i in range(len(liste_prompt)):
    radiobutton = tkinter.Radiobutton(window, text = liste_prompt[i], variable=prompt_engineering, value = i)
    radiobutton.grid(row=i + 23, column=1)
    radiobutton.config(indicatoron=0,
                       width= 20)
tkinter.Label(window, bg="#0d052c").grid(row=26, column=0)
tkinter.Label(window, bg="#0d052c").grid(row=26, column=1)

tkinter.Label(window, text = "Combien d'outils d'IA utilisez-vous?").grid(row=27,column=0)
outils_ia = tkinter.Scale(window,
                      from_ = 0,
                      to = 10,
                      length = 146,
                      orient="horizontal",
                      font=("Arial",10, "bold"),
                      tickinterval=10,
                      resolution= 1)
outils_ia.grid(row=27, column=1)
tkinter.Label(window, bg="#0d052c").grid(row=28, column=0)
tkinter.Label(window, bg="#0d052c").grid(row=28, column=1)

tkinter.Label(window, text = "Possédez-vous un abonnement payant?").grid(row=29,column=0)
abonnement = tkinter.IntVar()
checkbox = tkinter.Checkbutton(window, variable = abonnement, onvalue=1, offvalue=0)
checkbox.grid(row=29, column=1)
checkbox.config(font=("Arial", 15, "bold"),
                activebackground = "#ffffff",
                activeforeground = "#000000",
                padx= 60,
                )
tkinter.Label(window, bg="#0d052c").grid(row=30, column=0)
tkinter.Label(window, bg="#0d052c").grid(row=30, column=1)





tkinter.Label(window, text = "Quelle est la politique de votre institution face à l'IA?").grid(row=4,column=3)
politique = tkinter.IntVar()
liste_politique = ["Allowed_With_Citation", "Strict_Ban", "Actively_Encouraged"]
for i in range(len(liste_politique)):
    radiobutton = tkinter.Radiobutton(window, text = liste_politique[i], variable=politique, value = i)
    radiobutton.grid(row=i + 3, column=4)
    radiobutton.config(indicatoron=0,
                       width= 20)




tkinter.Label(window, text = "Combien d'heures étudiez-vous chaque semaine?").grid(row=13,column=3)
etude = tkinter.Entry(window).grid(row=13, column=4)

tkinter.Label(window, text = "Quel est votre niveau de dépendance à l'IA?").grid(row=27,column=3)
dependance = tkinter.Scale(window,
                      from_ = 0,
                      to = 10,
                      length = 146,
                      orient="horizontal",
                      font=("Arial",10, "bold"),
                      tickinterval=10,
                      resolution= 1)
dependance.grid(row=27, column=4)

tkinter.Label(window, text = "Quel est votre niveau d'anxiété lors d'un examen?").grid(row=29,column=3)
anxiete = tkinter.Scale(window,
                      from_ = 0,
                      to = 10,
                      length = 146,
                      orient="horizontal",
                      font=("Arial",10, "bold"),
                      tickinterval=10,
                      resolution= 1)
anxiete.grid(row=29, column=4)


boutton_predire = tkinter.Button(window, text="Prédire", command=assigner)
boutton_predire.grid(row= 27, column=2)
boutton_predire.config(
              font=("Arial", 20, "bold"),
              bg="green",
              fg="white",
              activebackground="#54130e",
              activeforeground="#212120",
              state="normal")


#window.mainloop()