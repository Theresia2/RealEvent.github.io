# Importation de la biblotheque
from tkinter import *
from customtkinter import *
from PIL import ImageTk, Image
import os
# importation de msql
import mysql.connector
from tkinter import messagebox
import random

bd = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd = "",
        database="realevent"
)
cursor = bd.cursor()


# creation de la fenetre
window =Tk()
window.title("RealEvent")
window.geometry("1065x638")
window.resizable(False,False)
window.configure(background="white")

# Creation de fonction ou on retrouve le different code



def acceuil():
    # conteneur texte
    # Acceuil
    conteneur =  Frame(
        window,
        width=650,
        height=600,
        background="white"
)
    conteneur.place(x=350, y=20)

# Creation d'une image pour le logo
    source_de_image2 = PhotoImage(file='img/logo.png').zoom(5).subsample(10)
    image_logo2= Canvas(conteneur, width=255, height=260 , background="white")
    image_logo2.create_image(125, 10, image = source_de_image2)
    image_logo2.place(x=0, y=130)


    Titre = Label(
        conteneur,
        text="Bienvenu a",
        background="white",
        font=("Arial Black", 24)
)
    Titre.place(x=100, y=20)
 
    Titre2 = Label(
        conteneur,
        text="RealEvent",
        background="white",
        font=("Bradley Hand ITC", 27)
)
    Titre2.place(x=310, y=25)

    groupe = Label(
        conteneur,
        text="Pixel",
        background="white",
        font=("Arial Black", 25)
)
    groupe.place(x=310, y=100)

    text = Label(
        conteneur,
        text="Transformez chaque moment en",
        background="white",
        font=("Calibri", 15)
)
    text.place(x=310, y=200)

    text2 = Label(
        conteneur,
        text="souvenir inoubliable: réservez vos",
        background="white",
        font=("Calibri", 15)
)
    text2.place(x=310, y=230)

    text3 = Label(
        conteneur,
        text="événements en utilisant notre",
        background="white",
        font=("Calibri", 15)
)
    text3.place(x=310, y=260)

    text4 = Label(
        conteneur,
        text="application !",
        background="white",
        font=("Calibri", 15)
)
    text4.place(x=310, y=290)

# Creation
    copy = Label(
        conteneur,
        text="Copyright : Pionniers de Pixel",
        background="white",
        font=("Yu Gothic UI Semibold", 15)
)
    copy.place(x=350, y=500)

# Fin de la function acceuil


#  creation de la function evenement

def evenement():
    conteneur =  Frame(
        window,
        width=650,
        height=600,
        background="white"
)
    conteneur.place(x=350, y=20)

    # Creation d'un titre pour l'venement
    Titre_evenement = CTkLabel(
        conteneur,
        text="TYPE D'EVENEMENTS",
        text_color="black",
        fg_color="white",
        font=("Arial Rounded MT Bold",24)
    )
    Titre_evenement.place(x=210, y=40)

  

    # Creation conteneur pour le image d'evenement
    conteneur_evenement = Frame(
        conteneur,
        height=200, 
        width=300,
        background="white"
    )
    conteneur_evenement.place( y=120)

    source_de_image_mariage = PhotoImage(file='img/logo.png').zoom(5).subsample(10)
    image_mariage= Canvas(conteneur_evenement, width=255, height=260 , background="white")
    image_mariage.create_image(125, 10, image = source_de_image_mariage)
    image_mariage.place(x=0, y=130)

    texte_mariage = CTkLabel(
        conteneur_evenement,
        text="Pour mariage",
        text_color="white",
        corner_radius=10,
        fg_color="#423d3d",
        font=("Calibri", 30),
        width=150,
        height=30
    )
    texte_mariage.place(x=45, y=158)
    # Creation conteneur reception

    conteneur_evenement_recepection = Frame(
        conteneur,
        height=200, 
        width=300,
        background="white"
    )
    conteneur_evenement_recepection.place(x=350, y=120)

    texte_reception = CTkLabel(
        conteneur_evenement_recepection,
        text="Pour réception",
        text_color="white",
        corner_radius=10,
        fg_color="#423d3d",
        font=("Calibri", 35),
        width=150,
        height=30
    )
    texte_reception.place(x=45, y=158)

    # Creation conteneur anniversaire

    conteneur_evenement_anniversaire = Frame(
        conteneur,
        height=200, 
        width=300,
        background="white"
    )
    conteneur_evenement_anniversaire.place( y=360)

    texte_anniversaire = CTkLabel(
        conteneur_evenement_anniversaire,
        text="Pour anniversaire",
        text_color="white",
        corner_radius=10,
        fg_color="#423d3d",
        font=("Calibri", 30),
        width=150,
        height=30
    )
    texte_anniversaire.place(x=30, y=158)


    # Creation conteneur reception

    conteneur_evenement_conferance = Frame(
        conteneur,
        height=200, 
        width=300,
        background="white"
    )
    conteneur_evenement_conferance.place(x=350, y=360)

    texte_conferance = CTkLabel(
        conteneur_evenement_conferance,
        text="Pour conférence",
        text_color="white",
        corner_radius=10,
        fg_color="#423d3d",
        font=("Calibri", 30),
        width=150,
        height=30
    )
    texte_conferance.place(x=35, y=158)


# Creation de la function reervation

def reservation():
    # Cration de la function pour inserser une valeur
    def formulaire():
        identite = Champ_identite.get()
        coordonne = Champ_coordone.get()
        motif_reservation = Champ_motif.get()
        salle = champ_salle.get()
        date_debut = Champ_debut.get()
        date_fin = Champ_fin.get()
        # requette pour verifie si le valleur saisie existe
        sql_rqt = f"SELECT * FROM reservation where identite = '{identite}' and coordonne = '{coordonne}' and 	Motif_de_reservation = '{motif_reservation}' and Date_debut ='{date_debut}' and Date_fin = '{date_fin}' and nom_salle = '{salle}'"
        cursor.execute(sql_rqt)
        resultat = cursor.fetchone()
        if resultat:
            # Notification d'erreur
            error_text = 'Vous avais deja une reservation'
            noti_error = CTkLabel(
            forme_reservation,
            fg_color="red",
            width=450,
            height=50,
            text=error_text,
            font=("Arial black",20),
            corner_radius=10)
            noti_error.place(x=50, y=20)
        else :
            # requette sql pour enregistre le information
            sql_rqt = f"INSERT INTO reservation (identite,coordonne,Motif_de_reservation,Date_debut,Date_fin, nom_salle) VALUES ( '{identite}','{coordonne}','{motif_reservation}','{date_debut}', '{date_fin}', '{salle}')"
            cursor.execute(sql_rqt)
            rqt2 = f"INSERT INTO client (nom_client, coordonne) VALUES ('{identite}', '{coordonne}')"
            cursor.execute(rqt2)
            bd.commit()
            messagebox.showinfo("Merci", "Merci votre reservation et effectue avec succes")
            # Genere un code de reservation
            reservation_code = ["123", "4473", "thesesia", "Divine","Test", "Realevent"]
            for _ in range(1):
                code= random.choice(reservation_code)
                error_text = "Voici votre code de reservation '"+ code+"'"
                noti_error = CTkLabel(
                forme_reservation,
                fg_color="green",
                width=450,
                height=50,
                text=error_text,
                font=("Arial black",20),
                corner_radius=10)
                noti_error.place(x=50, y=20)
                sql_rqt = f"INSERT INTO reservation (Code_reservation) VALUES ('{code}')"
                cursor.execute(sql_rqt)
                bd.commit()
        

    # Reservation
    conteneur =  Frame(
        window,
        width=650,
        height=650,
        background="white"

)
    conteneur.place(x=350, y=20)

    forme_reservation = CTkFrame(
        conteneur,
        width=550,
        height=550,
        fg_color="#2e2b2b",
        corner_radius=20
)
    forme_reservation.place(x=100)
# champ de saisie

    identite = Label(
        forme_reservation,
        text="Identite :",
        font=("Arial", 19),
        fg='white',
        background='#2e2b2b'
)

    identite.place(x=15, y=100)

    Champ_identite = CTkEntry(
        forme_reservation,
        width=354,
        height=30,
        font=("Calibri", 14)
)
    Champ_identite.place(x=183, y=105)
# coordonne
    coordonne = Label(
        forme_reservation,
        text="Coordonne :",
        font=("Arial", 19),
        fg='white',
        background='#2e2b2b'
)
    coordonne.place(x=10, y=155)

    Champ_coordone = CTkEntry(
        forme_reservation,
        width=354,
        height=30,
        font=("Calibri", 14)
)
    Champ_coordone.place(x=183, y=159)
# motif

    Motif = Label(
        forme_reservation,
        text="Motif de reservation:",
        font=("Arial", 14),
        fg='white',
        background='#2e2b2b'
)

    Motif.place(x=10, y=210)

    Champ_motif = CTkEntry(
        forme_reservation,
        width=350,
        height=30,
        font=("Calibri", 14)
)
    Champ_motif.place(x=185, y=210)

# Nom de la salle

    salle = Label(
        forme_reservation,
        text="Nom de la salle :",
        font=("Arial", 14),
        fg='white',
        background='#2e2b2b'
)

    salle.place(x=10, y=270)

    champ_salle = CTkComboBox(
        forme_reservation,
        values=["","Salle Resia", "Salle Amili", "Salle Tmg", "Salle Diva","salle Levis", "Salle team"],
)
    champ_salle.place(x=390, y=270)
# Date de debut

    date = Label(
        forme_reservation,
    text="Date de debut :",
    font=("Arial", 14),
    fg='white',
    background='#2e2b2b'
)
    date.place(x=10, y=330)

    Champ_debut = CTkEntry(
        forme_reservation,
        width=350,
        height=30,
        font=("Calibri", 14)
)
    Champ_debut.place(x=185, y=330)


# Date fin

    date_fin = Label(
        forme_reservation,
        text="Date de fin :",
        font=("Arial", 14),
        fg='white',
        background='#2e2b2b'
)

    date_fin.place(x=10, y=390)

    Champ_fin = CTkEntry(
        forme_reservation,
        width=350,
        height=30,
        font=("Calibri", 14)
)
    Champ_fin.place(x=185, y=390)



# Bouton valider

    btn_reservation_valider = CTkButton(
        forme_reservation,
        text="Valider la reservation",
        fg_color="#119644",
        font=("Arial Black", 15),
        width=400,
        height=45,
        corner_radius=10,
        hover_color="#19b833",
        command=formulaire
)
    btn_reservation_valider.place(x=70, y=470)

# Fin de la creation de la function reservation


# Creation de la function reclamation

def reclamation():
    # Code pour verifier si le code de reservation existe dans la base de donne
    def code_reclamation():
        Champ = Champ_code.get()
        requette = f"SELECT * FROM reservation where Code_reservation = '{Champ}'"
        cursor.execute(requette)
        resultat = cursor.fetchone()
        if  resultat:
            messagebox.showinfo("Code", "Code marche")
        else:
            messagebox.showerror("Erreur", "le code saisie n'est pas le code de reservation")    


   



    conteneur =  Frame(
        window,
        width=650,
        height=600,
        background="white"
)
    conteneur.place(x=350, y=20)
    # Creation d'un conteneur pour le code de reservation
    Contenur_reclamation = CTkFrame(
        conteneur,
        width=350,
        height=215,
        corner_radius=20,
        fg_color="#2e2b2b"
    )
    Contenur_reclamation.place(x=150, y=40)
    text_titre = Label(
        Contenur_reclamation,
        text="Code de confirmation",
        fg='white',
        background="#2e2b2b",
        font=("Arial Black",15)
    )
    text_titre.place(x=55, y=50)

    # Champ de saisie pour le code
    Champ_code = CTkEntry(
        Contenur_reclamation,
        width=200,
        height=40,
        font=("Calibri", 14)
)
    Champ_code.place(x=75, y=100)

    btn_valider_reclamation = CTkButton(
        Contenur_reclamation,
        text="Valider le code !",
        fg_color="green",
        width=200,
        height=40,
        command=code_reclamation
    )
    btn_valider_reclamation.place(x=75, y=150)

# fin de la creation de la function reclamation

# creation de la function deconnexion
def deconnexion():
    conteneur =  Frame(
        window,
        width=650,
        height=600,
        background="white"
)


    conteneur.place(x=350, y=20)

    forme_deco = CTkFrame(
        conteneur,
        width=450,
        height=300,
        corner_radius=30,
        fg_color="black"
)

    forme_deco.place(x=105, y=50)

    text_deco = Label(
        forme_deco,
        text="Merci d’avoir",
        font=('Arial black',20, "bold"),
        fg="white",
        background="black"
)

    text_deco.place(x=130, y=50)
    text_deco2 = Label(
        forme_deco,
        text="Contacter RealEvent",
        font=('Arial black',18, "bold"),
        fg="white",
        background="black"
)

    text_deco2.place(x=85, y=90)

    btn_Decon = CTkButton(
        forme_deco,
        text="Deconnexion",
        font=("Arial Black", 15),
        width=185,
        height=45,
        command=deconnex
    )
    btn_Decon.place(x=140, y=150)
    copy = Label(
        conteneur,
        text="Copyright : Pionniers de Pixel",
        background="white",
        font=("Yu Gothic UI Semibold", 15)
)
    copy.place(x=350, y=450)



# function quand on clique sur deconnexion
def deconnex():
    window.quit()

# Fin de la function deconnexion

# Creation conteneur pour le btn

forme = CTkFrame(
    window,
    width=250,
    height=596,
    corner_radius=32,
    fg_color="#222a35"
)
# la variable forme contiens de bouton
forme.place(x=30, y=20)

# Creation image
source_de_image1 = PhotoImage(file='img/image_home.png').zoom(2).subsample(3)
image_logo1 = Canvas(forme, width=160, height=125 , background="#222a35", highlightthickness=0)
image_logo1.create_image(80, 65, image = source_de_image1)
image_logo1.place(x=40, y=10)

# creation de button

btn_Acceuil = CTkButton(
    forme,
    text="Acceuil",
    font=("Arial Black", 15),
    width=175,
    height=45,
    command=acceuil
)
btn_Acceuil.place(x=35, y=150)


# btn Evenement

btn_Evenement = CTkButton(
    forme,
    text="Evénement",
    font=("Arial Black", 15),
    width=175,
    height=45,
    command=evenement
)
btn_Evenement.place(x=35, y=220)

# btn Reservation

btn_Reservation = CTkButton(
    forme,
    text="Réservation",
    font=("Arial Black", 15),
    width=175,
    height=45,
    command=reservation
)
btn_Reservation.place(x=35, y=290)

# btn reclamation

btn_reclamation = CTkButton(
    forme,
    text="Réclamation",
    font=("Arial Black", 15),
    width=175,
    height=45,
    command=reclamation
)
btn_reclamation.place(x=35, y=360)


# btn deconnexion

btn_Deconnexion = CTkButton(
    forme,
    text="Déconnexion",
    font=("Arial Black", 15),
    width=185,
    height=45,
    fg_color="#d10e0e",
    hover_color="#dd0303",
    command=deconnexion
)
btn_Deconnexion.place(x=35, y=520)


# Acceuil
conteneur =  Frame(
        window,
        width=650,
        height=600,
        background="white"
)
conteneur.place(x=350, y=20)

# Creation d'une image pour le logo
source_de_image = PhotoImage(file='img/logo.png').zoom(5).subsample(10)
image_logo = Canvas(conteneur, width=255, height=260 , background="white", border=None)
image_logo.create_image(125, 140, image = source_de_image)
image_logo.place(x=0, y=130)
Titre = Label(
        conteneur,
        text="Bienvenu a",
        background="white",
        font=("Arial Black", 24)
)
Titre.place(x=100, y=20)
 
Titre2 = Label(
        conteneur,
        text="RealEvent",
        background="white",
        font=("Bradley Hand ITC", 27)
)
Titre2.place(x=310, y=25)

groupe = Label(
        conteneur,
        text="Pixel",
        background="white",
        font=("Arial Black", 25)
)
groupe.place(x=310, y=100)

text = Label(
        conteneur,
        text="Transformez chaque moment en",
        background="white",
        font=("Calibri", 15)
)
text.place(x=310, y=200)

text2 = Label(
        conteneur,
        text="souvenir inoubliable: réservez vos",
        background="white",
        font=("Calibri", 15)
)
text2.place(x=310, y=230)

text3 = Label(
        conteneur,
        text="événements en utilisant notre",
        background="white",
        font=("Calibri", 15)
)
text3.place(x=310, y=260)

text4 = Label(
        conteneur,
        text="application !",
        background="white",
        font=("Calibri", 15)
)
text4.place(x=310, y=290)

# Creation

copy = Label(
        conteneur,
        text="Copyright : Pionniers de Pixel",
        background="white",
        font=("Yu Gothic UI Semibold", 13)
)
copy.place(x=400, y=550)



window.mainloop()