import streamlit as st

st.set_page_config(page_title="Voto Informado 2026", layout="wide")

st.markdown("""
<style>
.main {
    background-color: #f5f5f7;
}
.titulo {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #1f4fff;
}
.subtitulo {
    text-align: center;
    font-size: 24px;
    margin-bottom: 30px;
}
.boton {
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="titulo">VOTOINFORMADO2026</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitulo">¿Qué quieres comparar hoy?</p>', unsafe_allow_html=True)

tema = st.text_input(
    "",
    placeholder="Ej: Reforma de pensiones, Seguridad ciudadana, Minería..."
)

col1, col2, col3 = st.columns(3)

with col1:
    st.button("Economía")
with col2:
    st.button("Seguridad")
with col3:
    st.button("Educación")

if st.button("Comparar Propuestas"):
    st.subheader(f"Resultados sobre: {tema}")
    for i in range(1, 37):
        st.markdown(f"### Partido {i}")
        st.write("Propuesta resumida sobre el tema")
        st.write("Fuente: Plan de gobierno oficial")
