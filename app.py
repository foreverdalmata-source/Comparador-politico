# Código estilo landing page premium

Reemplaza todo tu `app.py` por este código para que se vea mucho más parecido a la imagen que quieres:

```python
import streamlit as st

st.set_page_config(page_title="Voto Informado 2026", layout="wide")

st.markdown("""
<style>

.stApp {
    background: linear-gradient(to bottom, #f8f9fc, #eef2f7);
}

.block-container {
    padding-top: 1rem;
    max-width: 1200px;
}

.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 0 20px 0;
    font-size: 14px;
    color: #6b7280;
}

.logo {
    font-size: 28px;
    font-weight: 800;
    color: #2563eb;
}

.menu {
    display: flex;
    gap: 30px;
    font-size: 14px;
    font-weight: 600;
    color: #6b7280;
}

.badge {
    display: inline-block;
    padding: 8px 16px;
    border-radius: 999px;
    background-color: #eef4ff;
    color: #2563eb;
    font-size: 13px;
    font-weight: 600;
    border: 1px solid #dbe7ff;
    margin-bottom: 25px;
}

.hero {
    text-align: center;
    padding-top: 40px;
    padding-bottom: 40px;
}

.hero h1 {
    font-size: 72px;
    font-style: italic;
    color: #111827;
    margin-bottom: 0;
    line-height: 1.1;
}

.hero h2 {
    font-size: 76px;
    color: #2563eb;
    font-weight: 800;
    margin-top: -10px;
    margin-bottom: 25px;
}

.hero p {
    color: #6b7280;
    font-size: 20px;
    max-width: 700px;
    margin: auto;
    line-height: 1.7;
}

.stats {
    display: flex;
    justify-content: center;
    gap: 40px;
    margin-top: 40px;
    margin-bottom: 60px;
}

.stat-box {
    text-align: center;
    color: #6b7280;
    font-size: 13px;
}

.search-card {
    background: white;
    max-width: 650px;
    margin: auto;
    padding: 30px;
    border-radius: 24px;
    box-shadow: 0 8px 30px rgba(0,0,0,0.08);
    border: 1px solid #e5e7eb;
}

.card-title {
    font-size: 34px;
    font-style: italic;
    color: #111827;
    margin-bottom: 20px;
}

.stTextInput > div > div > input {
    border-radius: 14px;
    padding: 14px;
    border: 1px solid #d1d5db;
}

.tema-label {
    margin-top: 20px;
    margin-bottom: 12px;
    color: #6b7280;
    font-size: 13px;
    font-weight: 700;
}

.chips {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-bottom: 25px;
}

.chip {
    background: #f3f4f6;
    color: #4b5563;
    padding: 8px 14px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 500;
}

.stButton > button {
    width: 100%;
    background: #6b7280;
    color: white;
    border: none;
    border-radius: 14px;
    padding: 16px;
    font-size: 18px;
    font-weight: 700;
}

.info-box {
    margin-top: 20px;
    background: #eef4ff;
    border: 1px solid #dbe7ff;
    border-radius: 12px;
    padding: 14px;
    color: #2563eb;
    font-size: 13px;
}

</style>
""", unsafe_allow_html=True)

st.markdown('''
<div class="navbar">
    <div class="logo">VOTOINFORMADO2026</div>
    <div class="menu">
        <span>PLANES</span>
        <span>PARTIDOS</span>
        <span>METODOLOGÍA</span>
    </div>
</div>
''', unsafe_allow_html=True)

st.markdown('<div class="hero">', unsafe_allow_html=True)
st.markdown('<div class="badge">INFORMACIÓN 100% VERIFICADA POR IA</div>', unsafe_allow_html=True)
st.markdown('<h1>No des tu voto a cualquiera</h1>', unsafe_allow_html=True)
st.markdown('<h2>PIENSA!</h2>', unsafe_allow_html=True)
st.markdown('''
<p>
Compara los planes de gobierno de los 36 partidos políticos del Perú.<br>
Análisis profundo, citas textuales y visualizaciones de datos para un voto consciente.
</p>
''', unsafe_allow_html=True)

st.markdown('''
<div class="stats">
    <div class="stat-box">📘<br>36 PLANES</div>
    <div class="stat-box">📊<br>ANÁLISIS DATA</div>
    <div class="stat-box">☑️<br>VOTO LIBRE</div>
</div>
''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="search-card">', unsafe_allow_html=True)
st.markdown('<div class="card-title">¿Qué quieres comparar hoy?</div>', unsafe_allow_html=True)

tema = st.text_input(
    "",
    placeholder="Ej: Reforma de pensiones, Seguridad ciudadana, Minería..."
)

st.markdown('<div class="tema-label">EJE TEMÁTICO:</div>', unsafe_allow_html=True)

st.markdown('''
<div class="chips">
    <div class="chip">General</div>
    <div class="chip">Economía y Empleo</div>
    <div class="chip">Seguridad Ciudadana</div>
    <div class="chip">Educación</div>
    <div class="chip">Salud</div>
    <div class="chip">Lucha contra la Corrupción</div>
    <div class="chip">Infraestructura</div>
    <div class="chip">Medio Ambiente</div>
    <div class="chip">Desarrollo Social</div>
    <div class="chip">Relaciones Exteriores</div>
</div>
''', unsafe_allow_html=True)

if st.button("Comparar Propuestas"):
    st.subheader(f"Resultados para: {tema}")
    st.write("Aquí aparecerán las propuestas comparadas.")

st.markdown('''
<div class="info-box">
Esta herramienta utiliza inteligencia artificial para sintetizar información de los planes de gobierno oficiales presentados ante el JNE. Siempre verifica las fuentes citadas.
</div>
''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
```

Este código ya se parece mucho más a la captura que quieres: encabezado arriba, gran mensaje central, tarjeta de búsqueda, etiquetas redondeadas y botón elegante.
