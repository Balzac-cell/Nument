import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Application Streamlit",
    layout="wide",
    initial_sidebar_state="auto"
)

# Initialisation des variables dans `st.session_state`
if "is_admin" not in st.session_state:
    st.session_state["is_admin"] = False  # Flag pour l'accès admin (login rapide)
if "page" not in st.session_state:
    st.session_state["page"] = "Welcome"

# Mot de passe pour l'accès rapide admin
ADMIN_PASSWORD = "admin"  # Définir un mot de passe pour le login rapide

# Barre d'authentification rapide
with st.expander("Connexion rapide admin (facultatif)"):
    password = st.text_input("Entrez le mot de passe admin pour un accès rapide", type="password")
    if st.button("Se connecter"):
        if password == ADMIN_PASSWORD:
            st.session_state["is_admin"] = True
            st.success("Connexion réussie ! Accès admin activé.")
            st.rerun()  # Recharge la page pour activer admin
        else:
            st.error("Mot de passe incorrect.")

# Gestion de la navigation (admin ou utilisateur classique)
st.sidebar.title("Navigation")
if st.session_state["is_admin"]:
    st.sidebar.write("Mode **admin** activé.")  # Petit message pour mode admin
    selected_page = st.sidebar.radio(
        "Choisissez votre page",
        ["Welcome", "page1", "IntroFormulaireComplet", "FormulaireComplet", "FinFormulaireComplet"],
        index=["Welcome", "page1", "IntroFormulaireComplet", "FormulaireComplet", "FinFormulaireComplet"].index(
            st.session_state["page"]),
        key="navigation"
    )
else:
    selected_page = st.sidebar.radio(  # Version simplifiée pour utilisateur sans admin
        "Pages accessibles",
        ["Welcome", "IntroFormulaireComplet"],
        index=["Welcome", "IntroFormulaireComplet"].index(st.session_state["page"]),
        key="navigation"
    )

if st.session_state["page"] != selected_page:
    st.session_state["page"] = selected_page
    st.rerun()  # Reload pour synchroniser la navigation globale

# Gestion des pages
if st.session_state["page"] == "Welcome":
    st.title("Bienvenue sur la Welcome page")
    st.write("Bienvenue dans l'application ! Naviguez à l'aide du menu sur la gauche.")
elif st.session_state["page"] == "page1" and st.session_state["is_admin"]:
    import page1

    page1.app()
elif st.session_state["page"] == "IntroFormulaireComplet":
    import IntroFormulaireComplet

    IntroFormulaireComplet.app()
elif st.session_state["page"] == "FormulaireComplet" and st.session_state["is_admin"]:
    import FormulaireComplet

    FormulaireComplet.app()
elif st.session_state["page"] == "FinFormulaireComplet" and st.session_state["is_admin"]:
    import FinFormulaireComplet

    FinFormulaireComplet.app()
