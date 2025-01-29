import streamlit as st

def app():
    st.title("Page 1")
    st.write("Bienvenue sur cette nouvelle page test")

    # Champ texte
    mot = st.text_input("Dis-nous quelque chose")

    # Si du texte est entré, redirige automatiquement vers la page 2
    if mot:
        # Met à jour la page active dans `session_state`
        st.session_state["page"] = "page2"
        # Recharge la page pour appliquer la redirection
        st.rerun()

    # Optionnel : un bouton pour afficher le texte avant la redirection
    if st.button("Affiche ce que j'ai écrit"):
        st.write(f"Voici ton message : {mot}")