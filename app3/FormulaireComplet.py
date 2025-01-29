#code qui envoie le données à la abse ok

import streamlit as st
import requests
import datetime

# Configuration Supabase (Nouvelle table : OptimisedOldUI)
SUPABASE_URL = "https://dlhhyjclkvsmivlhraaz.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRsaGh5amNsa3ZzbWl2bGhyYWF6Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTczNzU2NjIxNiwiZXhwIjoyMDUzMTQyMjE2fQ.-bXX5wmoBZB22PXaLNcIv457ZueifpG7HZNc7tiJtrQ"

def app():
    st.session_state["page"] = "FormulaireComplet"

    # Enregistrer l'heure d'affichage de la page
    if "display_time" not in st.session_state:
        st.session_state["display_time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Ajouter un état pour l'envoi des données
    if "data_sent" not in st.session_state:
        st.session_state["data_sent"] = False

    # Création de deux colonnes pour le formulaire et l'image
    col1, col2 = st.columns(2)

    # Colonne de gauche : formulaire
    with col1:
        st.title("AVIS DES SOMMES A PAYER")

        st.header("Patient")
        NomDuPatient = st.text_input("Nom du patient")

        st.header("Assuré")
        Num = st.text_input("N°")
        Org = st.text_input("Org.")

        st.header("Obser.")
        au = st.text_input("au")

    # Valeurs par défaut pour le tableau
    column_titles = ["DESIGNATION", "TARIF", "BASE DE REMBOURSEMENT", "TAUX", "A VOTRE CHARGE"]
    column_data = {
        "DESIGNATION": ["ADI PU", "ADI PU", "TOTAL"],
        "TARIF": ["69,00", "0,75", ""],
        "BASE DE REMBOURSEMENT": ["69,00", "", ""],
        "TAUX": ["30", "", ""],
        "A VOTRE CHARGE": ["20,70", "0,22", "20,90"]
    }

    if "table_data" not in st.session_state:
        st.session_state["table_data"] = [
            [column_data[title][row] for title in column_titles]
            for row in range(3)
        ]

    # Affichage du tableau interactif
    for row_idx in range(2):
        row_cols = st.columns(len(column_titles))
        for col_idx, col in enumerate(row_cols):
            st.session_state["table_data"][row_idx][col_idx] = col.text_input(
                label="",
                value=st.session_state["table_data"][row_idx][col_idx],
                key=f"cell_{row_idx}_{col_idx}"
            )

    # Bouton "Terminer"
    if st.button("**Terminer**") and not st.session_state["data_sent"]:
        base_remboursement_cell = st.session_state["table_data"][1][2]  # 1ère ligne, colonne 1
        taux_cell = st.session_state["table_data"][1][3]  # 1ère ligne, colonne 2

        # Récupérer l'IP utilisateur
        try:
            response = requests.get("https://api64.ipify.org?format=json")
            ip_address = response.json().get("ip") if response.status_code == 200 else "IP inconnue"
        except Exception:
            ip_address = "Erreur IP"

        # Préparer les données pour Supabase (OptimisedOldUI)
        payload = {
            "ip_address": ip_address,
            "nom_du_patient": NomDuPatient,
            "N°": Num,
            "Org.": Org,
            "au": au,
            "BDR": base_remboursement_cell,
            "TAUX": taux_cell,
            "DisplayTime": st.session_state["display_time"]
        }

        # Envoi des données vers OptimisedOldUI
        endpoint = f"{SUPABASE_URL}/rest/v1/OptimisedOldUI"
        headers = {
            "apikey": SUPABASE_KEY,
            "Authorization": f"Bearer {SUPABASE_KEY}",
            "Content-Type": "application/json",
            "Prefer": "return=representation"
        }

        try:
            supabase_response = requests.post(endpoint, json=payload, headers=headers)

            # Vérifie que la réponse est bien en JSON
            if supabase_response.status_code == 201:
                try:
                    data = supabase_response.json()
                    if data and isinstance(data, list) and "id" in data[0]:
                        st.session_state["uuid"] = data[0]["id"]
                        st.success("Données envoyées avec succès !")
                        st.session_state["data_sent"] = True
                    else:
                        st.error("Erreur : L'UUID n'a pas été renvoyé par Supabase.")
                except Exception:
                    st.error("Erreur : La réponse de Supabase n'est pas valide.")
                    st.write(supabase_response.text)
            else:
                st.error(f"Erreur lors de l'envoi : {supabase_response.status_code}")
                st.write("Détails :", supabase_response.text)
        except Exception as e:
            st.error(f"Erreur lors de la connexion à Supabase : {e}")

    # Redirection une fois les données envoyées
    if st.session_state["data_sent"]:
        st.write("Redirection vers la page de fin...")
        st.session_state["page"] = "FinFormulaireComplet"
        st.rerun()

    # Affichage de l'image dans la colonne de droite
    with col2:
        try:
            st.image("app1/assets/Fake.jpg", caption="Facture de santé", use_container_width=True)
        except FileNotFoundError:
            st.warning("Image non trouvée.")