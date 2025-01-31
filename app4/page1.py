import streamlit as st
import requests
import datetime

def app():
    if "page" not in st.session_state:
        st.session_state["page"] = "IntroFormulaireComplet"

    # Enregistrer l'heure d'affichage de la page
    if "DT1" not in st.session_state:
        st.session_state["DT1"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

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
        st.header("Nom")

        try:
            st.image("app4/assets/Split/Name/NaneB.jpg", use_container_width=True)
        except FileNotFoundError:
            st.warning("Image non trouvée.")
        st.markdown("")
        NomDuPatient = st.text_input("Saisissez la donnée encadrée en vert et appuyez sur entrer", key="NomDuPatient")

        # Envoie de données"
        if NomDuPatient and not st.session_state["data_sent"]:

            # Récupérer l'IP utilisateur
            try:
                response = requests.get("https://api64.ipify.org?format=json")
                ip_address = response.json().get("ip") if response.status_code == 200 else "IP inconnue"
            except Exception:
                ip_address = "Erreur IP"

            # Préparer les données pour Supabase (OptimisedOldUI)
            payload = {
                "nom_du_patient": st.session_state["NomDuPatient"],  # Utilisation du champ sauvegardé
                "ip_address": ip_address,  # Ajout de l'adresse IP récupérée ou par défaut
                "DT1" : st.session_state["DT1"]
            }

            # Envoi des données vers OptimisedOldUI
            endpoint = f"{SUPABASE_URL}/rest/v1/NewUI"
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
                            st.session_state["page"] = "page2"  # Mettre à jour pour la redirection
                            st.rerun()  # Recharger pour afficher la page 2
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

    # Affichage de l'image dans la colonne de droite
    with col2:
        try:
            st.markdown("Facture de santé")
            st.image("app4/assets/Split/Name/SplitName.jpg", caption="Bloc 1 sur 6", width=400)
        except FileNotFoundError:
            st.warning("Image non trouvée.")