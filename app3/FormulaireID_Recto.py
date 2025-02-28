import streamlit as st
import requests
import datetime


# Fonction principale pour la page "FormulaireID_Recto"
def app():

    st.html(
        "<p><span style='text-decoration: line-through double red;'>Oops</span>!</p>"
    )

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
    if "display_time_recto" not in st.session_state:
        st.session_state["display_time_recto"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

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

        NomDeFamille = st.text_input("Nom", autocomplete="off")
        Prenoms_1 = st.text_input("Prénom 1", autocomplete="off")
        Prenoms_2 = st.text_input("Prénom 2", autocomplete="off")
        DateNaissance = st.text_input("DATE DE NAISSANCE", autocomplete="off")
        LieuNaissance = st.text_input("LIEU DE NAISSANCE", autocomplete="off")
        DateExpir = st.text_input("DATE D'EXPIRATION", autocomplete="off")
        NumDoc = st.text_input("N° DU DOCUMENT", autocomplete="off")


        # Bouton "Terminer"
        if st.button("Terminer"):

            # initialisation
            update_payload = {
                "NomDeFamille": NomDeFamille,
                "Prenoms_1": Prenoms_1,
                "Prenoms_2": Prenoms_2,
                "DateNaissance": DateNaissance,
                "LieuNaissance": LieuNaissance,
                "DateExpir": DateExpir,
                "NumDoc": NumDoc,
                "DisplayTime_recto": st.session_state["display_time_recto"]
            }
            endpoint = f"{SUPABASE_URL}/rest/v1/OptimisedOldUI?id=eq.{uuid}"
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
                    st.session_state["page"] = "FormulaireID_Verso"  # Rediriger vers nouvelle page
                    st.rerun()
                else:
                    st.error(f"Erreur lors de la mise à jour : {response.status_code}")
                    st.write("Détails :", response.text)
            except Exception as e:
                st.error(f"Erreur lors de la connexion à Supabase : {e}")

    # Affichage de l'image dans la colonne de droite
    with col2:
        try:
            st.image("app3/assets/ID_Recto.jpg", caption="ID recto", use_container_width=True)
        except FileNotFoundError:
            st.warning("Image non trouvée.")