import streamlit as st
import pickle
import pandas as pd
import numpy as np


# Charger le modèle depuis le fichier
with open("model.pkl", 'rb') as file:
    model_lr = pickle.load(file)

st.title("Assur'Aimant")
st.subheader("Faites votre devis d'assurance en 2 minutes !")

# Ajout d'une image
st.image(image = "/home/simplon/Bureau/dossier_machine_learning/dossier pour github/Assuraimant.jpeg")


# Demande des informations à l'utilisateur
age = st.number_input("Quel est votre âge?", min_value=0, max_value=120)
sexe = st.radio("Quel est votre sexe?", ("male", "femelle"))
if sexe == 'male' :
    sexe = int(0)
if sexe == 'femelle' :
    sexe = int(1)
bmi = st.number_input("Quel est votre IMC?", min_value=0, max_value=50)
nombre_enfants = st.number_input("Combien avez-vous d'enfants?", min_value=0, max_value=20)
fumeur = st.radio("Êtes-vous fumeur?", ("yes", "no"))
if fumeur == 'yes' :
    fumeur = int(0)
if fumeur == 'no' :
    fumeur = int(1)
region = st.selectbox("Quelle est votre région?", ["Nord-Est", "Nord-Ouest", "Sud-Est", "Sud-Ouest"])
if region == 'Nord-Est' :
    region = int(0)
if region == 'Nord-Ouest' :
    region = int(1)
if region == 'Sud-Est' :
    region = int(2)
if region == 'Sud-Ouest' :
    region = int(3)

liste = [int(age), sexe, bmi, int(nombre_enfants), fumeur, region]

liste_col = ['age', 'sex', 'bmi', 'children', 'smoker', 'region']

if st.button("Démarrez l'estimation"):
    df = pd.DataFrame(np.array(liste).reshape(1, -1),columns = liste_col)
    st.write(model_lr.predict(df))
    charges = int(model_lr.predict(df))
    st.success("Votre estimation est de {} $".format(charges))