import streamlit as st

# Configuration de la page — cela doit être la PREMIÈRE commande Streamlit
st.set_page_config(
    page_title="Introduction Formulaire",
    layout="wide",
    initial_sidebar_state="collapsed"
)

import IntroFormulaireComplet
import page1, page2, page3, page4, page5, page6, FinFormulaireComplet



# Initialiser la navigation dans la variable session_state
if "page" not in st.session_state:
    st.session_state["page"] = "IntroFormulaireComplet"  # Définir la page de démarrage

# Charger la page en fonction de session_state["page"]
if st.session_state["page"] == "IntroFormulaireComplet":
    IntroFormulaireComplet.app()
elif st.session_state["page"] == "page1":
    page1.app()
elif st.session_state["page"] == "page2":
    page2.app()
elif st.session_state["page"] == "page3":
    page3.app()
elif st.session_state["page"] == "page4":
    page4.app()
elif st.session_state["page"] == "page5":
    page5.app()
elif st.session_state["page"] == "page6":
    page6.app()
elif st.session_state["page"] == "FinFormulaireComplet":
    FinFormulaireComplet.app()