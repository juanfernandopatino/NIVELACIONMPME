"""Tablero Nivelacion y Ventas Internas Materias Primas y Material Empaque."""

import streamlit as st

from styles import GLOBAL_CSS, CLASIFICACION_COLORES
from components import (
    render_header,
    render_grouped_table,
    render_card,
    render_pill_filtro_css,
    render_traslados_table,
    render_count_badges,
)
from data import cargar_inventario_necesidad
from logic_inventario import (
    construir_filas_inventario_necesidad,
    construir_filas_traslados,
    centros_disponibles,
    CENTROS_MP,
    CENTROS_ME,
)

st.set_page_config(page_title="Nivelacion y Ventas Internas MP y ME", layout="wide")
st.markdown(GLOBAL_CSS, unsafe_allow_html=True)

# ---------- Header ----------
st.markdown(
    render_header("Nivelación y Ventas Internas Materias Primas y Material Empaque"),
    unsafe_allow_html=True,
)

with st.spinner("Cargando datos desde Snowflake..."):
    df_consolidado = cargar_inventario_necesidad()

tab_inventario, tab_traslados = st.tabs(["Inventario y Necesidad", "Nivelaciones y Ventas Internas"])

# ================= Pestaña 1: Inventario y Necesidad =================
with tab_inventario:
    col_orden, col_semana, col_grupo, col_modo = st.columns(4)
    with col_orden:
        st.markdown("**Orden**")
        orden_label = st.radio(
            "orden", ["Por lugar físico", "Por razón social"],
            horizontal=True, label_visibility="collapsed", key="orden_c1",
        )
    with col_semana:
        st.markdown("**Semana**")
        semana_label = st.radio(
            "semana", ["Semana actual", "Próxima semana", "Semana actual + 2"],
            horizontal=True, label_visibility="collapsed", key="semana_c1",
        )
    with col_grupo:
        st.markdown("**Grupo**")
        grupo_label = st.radio(
            "grupo", ["Materia Prima", "Material de Empaque"],
            horizontal=True, label_visibility="collapsed", key="grupo_c1",
        )
    with col_modo:
        st.markdown("**Inventario**")
        modo_label = st.radio(
            "modo", ["Actual", "Simulado"],
            horizontal=True, label_visibility="collapsed", key="modo_c1",
        )

    orden = "fisico" if orden_label == "Por lugar físico" else "razon_social"
    semana_c1 = {"Semana actual": 0, "Próxima semana": 1, "Semana actual + 2": 2}[semana_label]
    grupo_c1 = "MP" if grupo_label == "Materia Prima" else "ME"
    modo_c1 = "actual" if modo_label == "Actual" else "simulado"

    st.markdown("**Centro**")
    opciones_centro = centros_disponibles(grupo_c1, orden)

    if st.session_state.get("centro_activo") not in opciones_centro:
        st.session_state["centro_activo"] = None

    st.markdown(render_pill_filtro_css(opciones_centro, st.session_state["centro_activo"], "pill"), unsafe_allow_html=True)

    with st.container(key="fila_pills_centro"):
        for nombre in opciones_centro:
            clave_boton = f"pill_{nombre}".replace(" ", "_")
            with st.container(key=clave_boton):
                if st.button(nombre, key=f"pill_btn_{clave_boton}"):
                    st.session_state["centro_activo"] = (
                        None if st.session_state["centro_activo"] == nombre else nombre
                    )

    centro_filtro = st.session_state["centro_activo"]

    filas_cuadro1 = construir_filas_inventario_necesidad(
        df_consolidado, grupo=grupo_c1, semana=semana_c1, orden=orden, centro_filtro=centro_filtro, modo=modo_c1,
    )

    st.markdown(render_card(render_grouped_table(filas_cuadro1)), unsafe_allow_html=True)

# ================= Pestaña 2: Nivelaciones y Ventas Internas =================
with tab_traslados:
    col_semana2, col_grupo2, col_modo2 = st.columns(3)
    with col_semana2:
        st.markdown("**Semana**")
        semana_label2 = st.radio(
            "semana", ["Semana actual", "Próxima semana", "Semana actual + 2"],
            horizontal=True, label_visibility="collapsed", key="semana_c2",
        )
    with col_grupo2:
        st.markdown("**Grupo**")
        grupo_label2 = st.radio(
            "grupo", ["Materia Prima", "Material de Empaque"],
            horizontal=True, label_visibility="collapsed", key="grupo_c2",
        )
    with col_modo2:
        st.markdown("**Inventario**")
        modo_label2 = st.radio(
            "modo", ["Actual", "Simulado"],
            horizontal=True, label_visibility="collapsed", key="modo_c2",
        )

    semana_c2 = {"Semana actual": 0, "Próxima semana": 1, "Semana actual + 2": 2}[semana_label2]
    grupo_c2 = "MP" if grupo_label2 == "Materia Prima" else "ME"
    modo_c2 = "actual" if modo_label2 == "Actual" else "simulado"

    centros_grupo = CENTROS_MP if grupo_c2 == "MP" else CENTROS_ME

    col_origen, col_destino, col_clasif = st.columns(3)
    with col_origen:
        st.markdown("**Origen**")
        origen_label = st.selectbox(
            "origen_traslado", ["Todos"] + centros_grupo, label_visibility="collapsed", key="origen_c2",
        )
    with col_destino:
        st.markdown("**Destino**")
        destino_label = st.selectbox(
            "destino_traslado", ["Todos"] + centros_grupo, label_visibility="collapsed", key="destino_c2",
        )
    with col_clasif:
        st.markdown("**Clasificación**")
        clasificacion_label = st.radio(
            "clasificacion_traslado", ["Todas", "Nivelacion", "Venta Interna"],
            horizontal=True, label_visibility="collapsed", key="clasificacion_c2",
        )

    origen_filtro = None if origen_label == "Todos" else origen_label
    destino_filtro = None if destino_label == "Todos" else destino_label
    clasificacion_filtro = None if clasificacion_label == "Todas" else clasificacion_label

    filas_traslados = construir_filas_traslados(
        df_consolidado, grupo=grupo_c2, semana=semana_c2, modo=modo_c2,
        origen_filtro=origen_filtro, destino_filtro=destino_filtro, clasificacion_filtro=clasificacion_filtro,
    )

    total_nivelacion = sum(1 for f in filas_traslados if f["Clasificacion"] == "Nivelacion")
    total_venta_interna = sum(1 for f in filas_traslados if f["Clasificacion"] == "Venta Interna")

    st.markdown(
        render_count_badges([
            ("TOTAL TRASLADOS", str(len(filas_traslados)), "#013066"),
            ("NIVELACION", str(total_nivelacion), CLASIFICACION_COLORES["Nivelacion"]),
            ("VENTA INTERNA", str(total_venta_interna), CLASIFICACION_COLORES["Venta Interna"]),
        ]),
        unsafe_allow_html=True,
    )

    st.markdown(render_card(render_traslados_table(filas_traslados)), unsafe_allow_html=True)
