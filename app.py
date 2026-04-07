import streamlit as st

st.title("Comparador de Planes de Gobierno 🇵🇪")

tema = st.text_input("Ingresa un tema (ej: educación, seguridad, economía)")

if st.button("Comparar"):
    st.write(f"Resultados para: {tema}")
    
    partidos = [f"Partido {i}" for i in range(1, 37)]
    
    for p in partidos:
        st.subheader(p)
        st.write("Propuesta resumida sobre el tema")
        st.write("Fuente: Plan de gobierno oficial")
