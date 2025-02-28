import streamlit as st

# Configuration de la page — cela doit être la PREMIÈRE commande Streamlit
st.set_page_config(
    page_title="Introduction Formulaire",
    layout="wide",
    initial_sidebar_state="collapsed"
)

import IntroFormulaireComplet
import page1, page2, page3, page4, page5, page6, page7,page8, page9, page10, page11, page12, page13, page14, page15,page16,page17,Fin, FinFormulaireComplet




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
elif st.session_state["page"] == "page7":
    page7.app()
elif st.session_state["page"] == "page8":
    page8.app()
elif st.session_state["page"] == "page9":
    page9.app()
elif st.session_state["page"] == "page10":
    page10.app()
elif st.session_state["page"] == "page11":
    page11.app()
elif st.session_state["page"] == "page12":
    page12.app()
elif st.session_state["page"] == "page13":
    page13.app()
elif st.session_state["page"] == "page14":
    page14.app()
elif st.session_state["page"] == "page15":
    page15.app()
elif st.session_state["page"] == "page16":
    page16.app()
elif st.session_state["page"] == "page17":
    page17.app()
elif st.session_state["page"] == "FinFormulaireComplet":
    FinFormulaireComplet.app()
elif st.session_state["page"] == "Fin":
    Fin.app()