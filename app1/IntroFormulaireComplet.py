import streamlit as st


def app():
    # Centrer le contenu avec une disposition générée par des colonnes
    col1, col2, col3 = st.columns([1, 2, 1])  # Les colonnes permettent de centrer le contenu

    with col2:
        # Titre centré
        st.title("Test de Saisie Complète")

        # Texte informatif avec des blocs explicatifs
        st.subheader(
            """
            Bonjour et bienvenue dans le test de saisie complète
            
            **Objectif** :  
            Saisissez les données manquantes d'une facture de santé exactement comme vous le faites habituellement.  
            """
        )

        # Espacement vertical pour bien séparer les éléments
        st.write("Appuyez sur le bouton **commencer la saisie** pour lancer le test")
        st.write("")
        st.write("")


        # Bouton placé et centré
        if st.button("Commencer la saisie"):
            st.session_state["page"] = "FormulaireComplet"  # Change la page actuelle
            st.rerun()  # Recharge la page pour appliquer le changement