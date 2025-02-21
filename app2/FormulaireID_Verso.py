import streamlit as st
import requests
import datetime


# Fonction principale pour la page "FormulaireID_Recto"
def app():

    if "page" not in st.session_state:
        st.session_state["page"] = "IntroFormulaireComplet"  # État par défaut

    # Vérifie que l'UUID est bien disponible
    if "uuid" not in st.session_state:
        st.error("Erreur : Aucun UUID trouvé. Revenez à la page précédente.")
        st.stop()

    uuid = st.session_state["uuid"]

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
    if "display_time_verso" not in st.session_state:
        st.session_state["display_time_verso"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Ajouter un état pour l'envoi des données
    if "data_sent" not in st.session_state:
        st.session_state["data_sent"] = False

    # Configuration Supabase
    SUPABASE_URL = "https://dlhhyjclkvsmivlhraaz.supabase.co"
    SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRsaGh5amNsa3ZzbWl2bGhyYWF6Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTczNzU2NjIxNiwiZXhwIjoyMDUzMTQyMjE2fQ.-bXX5wmoBZB22PXaLNcIv457ZueifpG7HZNc7tiJtrQ"

    # Création de deux colonnes pour le formulaire et l'image
    col1, col2 = st.columns(2)

    # Colonne de gauche : formulaire
    with col1:
        st.title("Carte nationale d'identité")

        st.header("Attributs d'identité")

        Taille = st.text_input("TAILLE", value="1,68 m")
        DateDeliv = st.text_input("DATE DE DELIVRANCE", autocomplete="off")
        AdresseP1 = st.text_input("ADRESSE", value="44 rue DESIRE SAINT CLEMENT")
        AdresseP2 = st.text_input("COMPELMENT ADRESSE", value="RESIDENCE DU PLEIN AIR BAT 4")
        CP = st.text_input("CODE POSTAL", autocomplete="off")
        Ville = st.text_input("VILLE", autocomplete="off")
        Pays = st.text_input("PAYS", autocomplete="off")

        st.header("MRZ")
        st.write("Complétez sans les '<<'")
        MRZ1 = st.text_input("MRZ LIGNE 1", autocomplete="off")
        MRZ2 = st.text_input("MRZ LIGNE 2", value="9007138F3002119FRA")
        MRZ3 = st.text_input("MRZ ligne 3", value="MARTIN<<MAELYS<GAELLE<MARIE")


        # Bouton "Terminer"
        if st.button("Terminer"):

            # initialisation
            update_payload = {
                "DateDeliv" : DateDeliv,
                "CP": CP,
                "Ville": Ville,
                "Pays": Pays,
                "MRZ1": MRZ1,
                "DisplayTime_verso": st.session_state["display_time_verso"]
            }
            endpoint = f"{SUPABASE_URL}/rest/v1/OldUI?id=eq.{uuid}"
            headers = {
                "apikey": SUPABASE_KEY,
                "Authorization": f"Bearer {SUPABASE_KEY}",
                "Content-Type": "application/json",
                "Prefer": "return=minimal" }

            # Envoi des données
            try:
                response = requests.patch(endpoint, json=update_payload, headers=headers)

                if response.status_code == 204:  # 204 = Modification réussie
                    st.success("Données envoyées")
                    st.session_state["data_sent"] = True
                    st.session_state["page"] = "FinFormulaireComplet"  # Rediriger vers page de fin
                    st.rerun()
                else:
                    st.error(f"Erreur lors de la mise à jour : {response.status_code}")
                    st.write("Détails :", response.text)
            except Exception as e:
                st.error(f"Erreur lors de la connexion à Supabase : {e}")

    # Affichage de l'image dans la colonne de droite
    with col2:
        try:
            st.image("app2/assets/ID_Verso.jpg", caption="ID verso", use_container_width=True)
        except FileNotFoundError:
            st.warning("Image non trouvée.")