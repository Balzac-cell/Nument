import streamlit as st
import requests
import datetime


def app():
    if "page" not in st.session_state:
        st.session_state["page"] = "IntroFormulaireComplet"  # État par défaut

    # Vérifie que l'UUID est bien disponible
    if "uuid" not in st.session_state:
        st.error("Erreur : Aucun UUID trouvé. Revenez à la page précédente.")
        st.stop()

    uuid = st.session_state["uuid"]

    # Enregistrer l'heure d'affichage de la page
    if "display_time" not in st.session_state:
        st.session_state["display_time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Ajouter un état pour l'envoi des données
    if "data_sent" not in st.session_state:
        st.session_state["data_sent"] = False

    # Configuration Supabase (Nouvelle table : OptimisedOldUI)
    SUPABASE_URL = "https://dlhhyjclkvsmivlhraaz.supabase.co"
    SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRsaGh5amNsa3ZzbWl2bGhyYWF6Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTczNzU2NjIxNiwiZXhwIjoyMDUzMTQyMjE2fQ.-bXX5wmoBZB22PXaLNcIv457ZueifpG7HZNc7tiJtrQ"

    # Création de deux colonnes pour le formulaire et l'image
    col1, col2 = st.columns([2, 1])

    # Colonne de gauche : formulaire
    with col1:
        st.title("Saisissez les données".upper())
        st.markdown("---")
        st.header("BDR")

        try:
            st.image("app4/assets/Split/BDR/BDR.jpg", use_container_width=False, width=175)
        except FileNotFoundError:
            st.warning("Image non trouvée.")
        st.markdown("")
        BDR = st.text_input("Saisissez la donnée encadrée en vert et appuyez sur entrer", key="BDR")

        if BDR:

            # initialisation
            update_payload = {"BDR": BDR}
            endpoint = f"{SUPABASE_URL}/rest/v1/NewUI?id=eq.{uuid}"
            headers = {
                "apikey": SUPABASE_KEY,
                "Authorization": f"Bearer {SUPABASE_KEY}",
                "Content-Type": "application/json",
                "Prefer": "return=minimal"
            }

            # Envoi des données
            try:
                response = requests.patch(endpoint, json=update_payload, headers=headers)

                if response.status_code == 204:  # 204 = Modification réussie
                    st.success("Données envoyées, Votre teste est terminé. Merci !")
                    st.session_state["data_sent"] = True
                    st.session_state["page"] = "page6"  # Rediriger vers page6
                    st.rerun()
                else:
                    st.error(f"Erreur lors de la mise à jour : {response.status_code}")
                    st.write("Détails :", response.text)
            except Exception as e:
                st.error(f"Erreur lors de la connexion à Supabase : {e}")

    # Affichage de l'image dans la colonne de droite
    with col2:
        try:
            st.markdown("Facture de santé")
            st.image("app4/assets/Split/BDR/SplitBDR.jpg", caption="Bloc 5 sur 6", width=400)
        except FileNotFoundError:
            st.warning("Image non trouvée.")
