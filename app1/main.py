import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Application Streamlit",
    layout="wide",
    initial_sidebar_state="collapsed"  # Barre latérale masquée par défaut
)

# Initialisation des variables dans `st.session_state`
if "is_admin" not in st.session_state:
    st.session_state["is_admin"] = False
if "page" not in st.session_state:
    st.session_state["page"] = "Welcome"

# Système d'authentification simple (admin)
ADMIN_PASSWORD = "admin"  # Mot de passe pour accéder aux pages avec barre latérale

# Authentification admin
if not st.session_state["is_admin"]:
    with st.expander("Authentification admin (facultatif)"):
        password = st.text_input("Mot de passe admin", type="password")
        if st.button("Se connecter"):
            if password == ADMIN_PASSWORD:
                st.session_state["is_admin"] = True
                st.rerun()  # Recharge la page après authentification
            else:
                st.error("Mot de passe incorrect.")

# Gestion de la navigation
if st.session_state["is_admin"]:
    st.sidebar.title("Navigation")
    selected_page = st.sidebar.radio(
        "Choisissez votre page",
        ["Welcome", "page1", "IntroFormulaireComplet", "FormulaireComplet", "FinFormulaireComplet"],
        index=["Welcome", "page1", "IntroFormulaireComplet", "FormulaireComplet", "FinFormulaireComplet"].index(st.session_state["page"]),
        key="navigation"
    )
    if st.session_state["page"] != selected_page:
        st.session_state["page"] = selected_page
        st.rerun()  # Recharge la page après un changement de page

# Affichage des pages en fonction de la sélection
if st.session_state["page"] == "Welcome":
    st.title("Bienvenue sur la Welcome page")
    st.write("Bienvenue dans l'application !")
elif st.session_state["page"] == "page1":
    import page1
    page1.app()
elif st.session_state["page"] == "IntroFormulaireComplet":
    import IntroFormulaireComplet
    IntroFormulaireComplet.app()
elif st.session_state["page"] == "FormulaireComplet":
    import FormulaireComplet
    FormulaireComplet.app()
elif st.session_state["page"] == "FinFormulaireComplet":
    import FinFormulaireComplet
    FinFormulaireComplet.app()

