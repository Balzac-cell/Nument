import streamlit as st


def app():
    # Contenu de la page
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.title("Test de Saisie Complète")
        st.subheader(
            """
            Bonjour et bienvenue dans le test de saisie complète

            **Objectif** :  
            Saisissez les données manquantes d'une facture de santé exactement comme vous le faites habituellement.
            """
        )
        st.write("Appuyez sur le bouton **Commencer la saisie** pour lancer le test.")

        # Bouton pour changer vers la page du formulaire complet
        if st.button("Commencer la saisie"):
            st.session_state["page"] = "FormulaireComplet"
            st.rerun()  # Recharger l'application
