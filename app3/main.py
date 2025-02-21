import streamlit as st

# Configuration de la page — cela doit être la PREMIÈRE commande Streamlit
st.set_page_config(
    page_title="Introduction Formulaire",
    layout="wide",
    initial_sidebar_state="collapsed"
)

import IntroFormulaireComplet
import FormulaireComplet
import FinFormulaireComplet
import FormulaireID_Recto
import FormulaireID_Verso
import Fin


# Initialiser la navigation dans la variable session_state
if "page" not in st.session_state:
    st.session_state["page"] = "IntroFormulaireComplet"  # Définir la page de démarrage

# Charger la page en fonction de session_state["page"]
if st.session_state["page"] == "IntroFormulaireComplet":
    IntroFormulaireComplet.app()
elif st.session_state["page"] == "FormulaireComplet":
    FormulaireComplet.app()
elif st.session_state["page"] == "FormulaireID_Recto":
    FormulaireID_Recto.app()
elif st.session_state["page"] == "FormulaireID_Verso":
    FormulaireID_Verso.app()
elif st.session_state["page"] == "FinFormulaireComplet":
    FinFormulaireComplet.app()
elif st.session_state["page"] == "Fin":
    Fin.app()