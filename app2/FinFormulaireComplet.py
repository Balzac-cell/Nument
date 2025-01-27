import streamlit as st


def app():
    # Centrer le contenu avec des colonnes
    col1, col2, col3 = st.columns([1, 2, 1])  # Centrage du contenu

    with col2:
        # Titre centré
        st.title("Feedback sur l'expérience")

        # Texte d'explication
        st.write(
            """
            ### Merci d'avoir participé à cette collecte de données.  
            Nous souhaitons comprendre si cette expérience reflète votre quotidien.  
            Merci de prendre un moment pour évaluer et commenter !
            """
        )

        # Slider pour noter l'expérience
        st.write("### Notez votre expérience \n (1 - Pas du tout similaire, 5 - Très similaire)")
        slider_value = st.slider(
            "À quel point cette expérience représente-t-elle ce que vous faites quotidiennement ?",
            min_value=1,
            max_value=5,
            value=3,
            step=1
        )

        # Espacement
        st.write("")

        # Zone de texte pour les commentaires
        st.write("### Laissez un commentaire libre")
        commentaire = st.text_area(
            "Ajoutez vos remarques ou suggestions pour améliorer l'expérience :",
            placeholder="Votre commentaire ici..."
        )

        # Espacement
        st.write("")

        # Bouton "Envoyer"
        if st.button("Envoyer"):
            # Logic à connecter plus tard
            st.write("Merci pour vos retours ! 🚀")
            # Vous pourrez enregistrer slider_value et commentaire ici (connexion à une base de données ou fichier)