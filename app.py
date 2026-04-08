import streamlit as st

st.set_page_config(
    page_title="Comparador Político",
    layout="wide"
)

st.markdown("""
<style>
body {
    background-color: #f5f7fb;
}

.main-title {
    font-size: 52px;
    font-style: italic;
    font-weight: 400;
    color: #111827;
    margin-bottom: 30px;
}

.search-box {
    margin-bottom: 30px;
}

.section-title {
    font-size: 16px;
    font-weight: 700;
    color: #6b7280;
    margin-top: 20px;
    margin-bottom: 10px;
}

.party-card {
    background-color: white;
    border: 1px solid #e5e7eb;
    border-radius: 18px;
    padding: 22px;
    margin-bottom: 20px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.04);
    height: 100%;
}

.party-title {
    font-size: 20px;
    font-weight: 700;
    color: #111827;
    margin-bottom: 10px;
}

.badge-high {
    background-color: #eaf8ee;
    color: #16a34a;
    padding: 6px 12px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 600;
    display: inline-block;
    margin-bottom: 12px;
}

.badge-medium {
    background-color: #fff7e6;
    color: #d97706;
    padding: 6px 12px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 600;
    display: inline-block;
    margin-bottom: 12px;
}

.badge-low {
    background-color: #fdecec;
    color: #dc2626;
    padding: 6px 12px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 600;
    display: inline-block;
    margin-bottom: 12px;
}

.score-row {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 14px;
}

.score-bar {
    width: 100%;
    height: 8px;
    background-color: #e5e7eb;
    border-radius: 999px;
    overflow: hidden;
}

.score-fill {
    height: 100%;
    background-color: #2563eb;
    border-radius: 999px;
}

.score-text {
    font-size: 14px;
    font-weight: 700;
    color: #6b7280;
    min-width: 55px;
}

.detail-label {
    font-size: 14px;
    font-weight: 700;
    color: #6b7280;
    margin-bottom: 10px;
}

.proposal-text {
    font-size: 16px;
    line-height: 1.7;
    color: #1f2937;
}

.compare-button button {
    background-color: #6b7280;
    color: white;
    border-radius: 14px;
    padding: 14px 30px;
    font-size: 18px;
    font-weight: 600;
    border: none;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">¿Qué quieres comparar hoy?</div>', unsafe_allow_html=True)

tema = st.text_input(
    "",
    placeholder="Ej: Seguridad Ciudadana, Educación, Salud..."
)

st.markdown('<div class="section-title">EJE TEMÁTICO:</div>', unsafe_allow_html=True)

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.button("General")
with col2:
    st.button("Economía y Empleo")
with col3:
    st.button("Seguridad Ciudadana")
with col4:
    st.button("Educación")
with col5:
    st.button("Salud")

col6, col7, col8, col9, col10 = st.columns(5)

with col6:
    st.button("Lucha contra la Corrupción")
with col7:
    st.button("Infraestructura")
with col8:
    st.button("Medio Ambiente")
with col9:
    st.button("Desarrollo Social")
with col10:
    st.button("Relaciones Exteriores")

st.markdown("<br>", unsafe_allow_html=True)

comparar = st.button("Comparar Propuestas")

if comparar:

    propuestas = {
        "Seguridad Ciudadana": [
            {
                "partido": "Fuerza Popular",
                "propuesta": "Enfoque en mano dura y protección legal al policía. Propone fortalecer la investigación criminal y la reforma del sistema de justicia penal para evitar la liberación de delincuentes.",
                "claridad": "Alto",
                "puntaje": 85
            },
            {
                "partido": "Alianza para el Progreso",
                "propuesta": "Propone un enfoque municipalista articulando el Serenazgo con la PNP, con fuerte inversión en tecnología de videovigilancia y programas de prevención juvenil.",
                "claridad": "Alto",
                "puntaje": 78
            },
            {
                "partido": "Renovación Popular",
                "propuesta": "Propone la intervención de las Fuerzas Armadas en apoyo a la PNP de manera sostenida, expulsión inmediata de extranjeros delincuentes y construcción de megacárceles.",
                "claridad": "Alto",
                "puntaje": 82
            },
            {
                "partido": "Podemos Perú",
                "propuesta": "Centrado en la creación de unidades de flagrancia y la reforma de la ley de defensa propia. Propone mayor presencia policial efectiva mediante la eliminación del servicio 24x24.",
                "claridad": "Medio",
                "puntaje": 70
            },
            {
                "partido": "Perú Libre",
                "propuesta": "Enfoque en las causas estructurales del delito y la democratización de la seguridad a través de rondas urbanas y campesinas coordinadas con el Estado.",
                "claridad": "Bajo",
                "puntaje": 45
            },
            {
                "partido": "Avanza País",
                "propuesta": "Propone la participación del sector privado en la gestión de penales y la tecnificación de la inteligencia para desarticular bandas de extorsión.",
                "claridad": "Medio",
                "puntaje": 65
            },
            {
                "partido": "Partido Morado",
                "propuesta": "Prioriza el fortalecimiento institucional de la PNP, la reforma judicial y la implementación de sistemas de denuncia digital y patrullaje inteligente.",
                "claridad": "Alto",
                "puntaje": 75
            },
            {
                "partido": "Acción Popular",
                "propuesta": "Propone fortalecer el Serenazgo, ampliar las comisarías de barrio y promover programas de reinserción social para jóvenes en riesgo.",
                "claridad": "Medio",
                "puntaje": 60
            },
            {
                "partido": "Somos Perú",
                "propuesta": "Busca integrar la seguridad ciudadana con programas de desarrollo social y recuperación de espacios públicos.",
                "claridad": "Medio",
                "puntaje": 62
            }
        ]
    }

    if tema in propuestas:

        st.markdown("## Comparación por Partido")

        cols = st.columns(3)

        for i, p in enumerate(propuestas[tema]):

            claridad = p["claridad"]

            if claridad == "Alto":
                badge_class = "badge-high"
            elif claridad == "Medio":
                badge_class = "badge-medium"
            else:
                badge_class = "badge-low"

            with cols[i % 3]:
                st.markdown(f"""
                <div class="party-card">
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
                        <div class="party-title">{p['partido']}</div>
                        <div class="{badge_class}">Claridad: {p['claridad']}</div>
                    </div>

                    <div class="score-row">
                        <div class="score-bar">
                            <div class="score-fill" style="width:{p['puntaje']}%;"></div>
                        </div>
                        <div class="score-text">{p['puntaje']}/100</div>
                    </div>

                    <div class="detail-label">NIVEL DE DETALLE</div>

                    <div class="proposal-text">
                        {p['propuesta']}
                    </div>
                </div>
                """, unsafe_allow_html=True)

    else:
        st.warning("Escribe exactamente: Seguridad Ciudadana")
