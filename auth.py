# Importation de la biblotheque
from tkinter import *
from customtkinter import *
from PIL import ImageTk, Image
import os
# importation de msql
import mysql.connector
from tkinter import messagebox


# creation de la fenetre
window = CTk()
window.title("RealEvent")
window.geometry("1065x638")
window.resizable(False,False)


# Connexion a la bd
bd = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd = "",
        database="realevent"
)
cursor = bd.cursor()

# creation de la function pour la connexion
def connex():
        # recuperation du nom est mot de passe
        nom = user.get()
        mdp = code.get()
        requet = f"SELECT * FROM Administrateur WHERE Administrateur= '{nom}'"
        cursor.execute(requet)
        result = cursor.fetchone()
                
        if result:
                requette = f"SELECT * FROM Administrateur WHERE password= '{mdp}'"
                cursor.execute(requette)
                result = cursor.fetchone()
                if result :
                        os.system("python main.py")
                        window.quit()
                else:
                        messagebox.showerror("Error","Le password incorect!")         
        else:
                messagebox.showerror("Error","Le nom saisie : '" + nom + "' N'est fais pas partie de username !")         
        



# Creation image de font 
src_img = Image.open('img\\font.png')
photo = ImageTk.PhotoImage(src_img)
bg_img = Label(window, image=photo)
bg_img.pack(fill="both", expand="yes")

# Creation du formulaire authentification

conteneur = CTkFrame(
    master=window,
    width=690,
    height=460,
    corner_radius=3,
    fg_color="transparent"
)
conteneur.place(x=180,y=105)

# Creation titre login

Titre = CTkLabel(
    master=conteneur,
    text="Login",
    font=("Blackadder ITC", 55),
    text_color='black'
)
Titre.place(relx=0.45, rely=0.1)

# Creation champ saisie pour username

user = CTkEntry(
    conteneur,
    placeholder_text="Saisir Username",
    width=300,
    height=40
)
user.place(relx=0.3, rely=0.4)

# Creation champ saisie pour password

code = CTkEntry(
    conteneur,
    placeholder_text="Saisir Password",
    width=300,
    height=40,
    show="°"
)
code.place(relx=0.3, rely=0.6)


CTkButton(
    conteneur,
    text="Connexion",
    width=250,
    corner_radius=5,
    fg_color="#1dad31",
    hover_color="#0ed128",
    command=connex
).place(relx=0.33, rely=0.75)


window.mainloop()
