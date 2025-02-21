import streamlit as st
import requests
import datetime


# Fonction principale pour la page "FormulaireComplet"
def app():
    st.session_state["page"] = "FormulaireComplet"

    st.markdown(
        """
        <script>
        window.scrollTo(0, 0);
        </script>
        <style>
            .highlight-label {
                font-size: 20px;
                font-weight: bold;
                color: red;
            }
            input[value=""] {
                border: 3px solid red;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

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
        NomDuPatient = st.text_input("Nom du patient",autocomplete="off")

        st.header("Assuré")
        Num = st.text_input("N°", autocomplete="off")
        Org = st.text_input("Org.", autocomplete="off")

        st.header("Obser.")
        au = st.text_input("au", autocomplete="off")

        # Valeurs par défaut pour le tableau
        column_titles = ["DESIGNATION", "TARIF", "BASE DE REMBOURSEMENT", "TAUX", "A VOTRE CHARGE"]
        column_data = {
            "DESIGNATION": ["Désignation", "ADI PU", "ADI PU", "TOTAL"],
            "TARIF": ["Tarifs", "69,00", "0,75", "-"],
            "BASE DE REMBOURSEMENT": ["BDR","69,00", "", "-"],
            "TAUX": ["Taux", "30", "", "-"],
            "A VOTRE CHARGE": ["AVC", "20,70", "0,22", "20,92"]
        }

        if "table_data" not in st.session_state:
            st.session_state["table_data"] = [
                [column_data[title][row] for title in column_titles]
                for row in range(4)
            ]

        for row_idx in range(4):  # Boucle sur chaque ligne
            row_cols = st.columns(len(column_titles))  # Création des colonnes pour cette ligne
            for col_idx, col in enumerate(row_cols):  # Boucle sur chaque cellule/colonne
                # Rendre la première ligne et la première colonne non éditables
                is_editable = not (row_idx == 0 or col_idx == 0)
                st.session_state["table_data"][row_idx][col_idx] = col.text_input(
                    label="",
                    value=st.session_state["table_data"][row_idx][col_idx],
                    key=f"cell_{row_idx}_{col_idx}",
                    disabled=not is_editable,  # Désactive la cellule si dans la première ligne ou colonne
                    autocomplete="off"
                )

        # Bouton "Terminer"
        if st.button("**Terminer**") and not st.session_state["data_sent"]:
            base_remboursement_cell = st.session_state["table_data"][2][2]
            taux_cell = st.session_state["table_data"][2][3]
            charge_cell = st.session_state["table_data"][3][4]

            # Récupérer l'IP utilisateur
            try:
                response = requests.get("https://api64.ipify.org?format=json")
                ip_address = response.json().get("ip") if response.status_code == 200 else "IP inconnue"
            except Exception:
                ip_address = "Erreur IP"

            # Préparer les données pour Supabase
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

            # Envoi des données à Supabase
            SUPABASE_URL = "https://dlhhyjclkvsmivlhraaz.supabase.co"
            SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRsaGh5amNsa3ZzbWl2bGhyYWF6Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTczNzU2NjIxNiwiZXhwIjoyMDUzMTQyMjE2fQ.-bXX5wmoBZB22PXaLNcIv457ZueifpG7HZNc7tiJtrQ"
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
            st.write("Redirection vers une nouvelle page")
            st.session_state["page"] = "FormulaireID_Recto"
            st.rerun()

    # Affichage de l'image dans la colonne de droite
    with col2:
        try:
            st.image("app3/assets/Fake.jpg", caption="Facture de santé", use_container_width=True)
        except FileNotFoundError:
            st.warning("Image non trouvée.")