import streamlit as st
import requests

# Configuration Supabase
SUPABASE_URL = "https://dlhhyjclkvsmivlhraaz.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRsaGh5amNsa3ZzbWl2bGhyYWF6Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTczNzU2NjIxNiwiZXhwIjoyMDUzMTQyMjE2fQ.-bXX5wmoBZB22PXaLNcIv457ZueifpG7HZNc7tiJtrQ"

def app():
    st.title("Fin du formulaire")

    # Vérifie que l'UUID est bien disponible
    if "uuid" not in st.session_state:
        st.error("Erreur : Aucun UUID trouvé. Revenez à la page précédente.")
        st.stop()

    uuid = st.session_state["uuid"]

    # Formulaire de feedback utilisateur
    st.write("### Indiquez votre niveau d'expérience en saisie (en mois)")
    slider_value = st.slider(
        "Nombre de mois d'expérience en saisie :",
        min_value=0,
        max_value=120,
        value=12,
        step=1
    )

    st.write("### Choisissez un pseudo si vous le souhaitez")
    pseudo = st.text_input(
        "Entrez votre pseudo :",
        placeholder="Ex: Chuck Norris"
    )

    st.write("### Laissez un commentaire concernant votre expérience :")
    commentaire = st.text_area(
        "Vos remarques ou suggestions :",
        placeholder="Votre commentaire ici..."
    )

    # Bouton pour envoyer les données à Supabase
    if st.button("Terminer"):
        update_payload = {
            "Exp": slider_value,  # Niveau d'expérience
            "Comments": commentaire,  # Commentaires
            "Pseudo": pseudo  # Pseudo enregistré
        }

        endpoint = f"{SUPABASE_URL}/rest/v1/OptimisedOldUI?id=eq.{uuid}"
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
                st.session_state["page"] = "Fin"  # Rediriger vers nouvelle page
                st.rerun()
            else:
                st.error(f"Erreur lors de la mise à jour : {response.status_code}")
                st.write("Détails :", response.text)
        except Exception as e:
            st.error(f"Erreur lors de la connexion à Supabase : {e}")