"""CSS global del tablero: paleta, header, tarjetas, pildoras y tabla."""

# Paleta de marca
COLOR_AZUL_CORP = "#013066"
COLOR_TEXTO = "#2C2C2C"
COLOR_FONDO_PAGINA = "#F2F4F7"

# Colores por compania (pildoras)
COLOR_GLOBAL = "#0B4DA2"
COLOR_SUPER = "#013066"
COLOR_TRULULU = "#E6007E"
COLOR_BIANCHI = "#F5821F"

COMPANIA_COLORES = {
    "Global": COLOR_GLOBAL,
    "Super": COLOR_SUPER,
    "Trululu": COLOR_TRULULU,
    "Bianchi": COLOR_BIANCHI,
}

# Colores de pastilla para la columna "Centro" del Cuadro 1
COLOR_OKA_LOKA = "#7E57C2"
COLOR_COMERCIALIZADORA = "#6B7280"
COLOR_CENTRO_ROBOTIZADO = "#546E7A"

CENTRO_COLORES = {
    **COMPANIA_COLORES,
    "Oka Loka": COLOR_OKA_LOKA,
    "Comercializadora": COLOR_COMERCIALIZADORA,
    "Centro robotizado": COLOR_CENTRO_ROBOTIZADO,
}

# Colores de estado de inventario vs politicas MRP
COLOR_STOCK_MINIMO = "#E53935"
COLOR_STOCK_MAXIMO = "#F5A623"
COLOR_DENTRO_RANGO = "#4CAF50"
COLOR_SIN_MRP_CON_INV = "#2196F3"
COLOR_QUIEBRE_INVENTARIO = "#9C27B0"

CLASIFICACION_COLORES = {
    "Nivelacion": COLOR_DENTRO_RANGO,
    "Venta Interna": COLOR_SIN_MRP_CON_INV,
}

ESTADO_COLORES = {
    "Stock minimo": COLOR_STOCK_MINIMO,
    "Stock maximo": COLOR_STOCK_MAXIMO,
    "Dentro de rango": COLOR_DENTRO_RANGO,
    "Sin MRP con Inv": COLOR_SIN_MRP_CON_INV,
    "Quiebre inventario": COLOR_QUIEBRE_INVENTARIO,
}

GLOBAL_CSS = f"""
<style>
    .stApp {{
        background-color: {COLOR_FONDO_PAGINA};
    }}

    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}

    .block-container {{
        padding-top: 1.2rem;
        padding-bottom: 2rem;
        max-width: 1400px;
    }}

    /* ---------- Header ---------- */
    .app-header {{
        background: linear-gradient(120deg, #012C5C 0%, #0B4DA2 55%, #1E8FD6 100%);
        border-radius: 14px;
        padding: 28px 32px 20px 32px;
        margin-bottom: 22px;
        position: relative;
        overflow: hidden;
        box-shadow: 0 4px 14px rgba(1, 48, 102, 0.25);
    }}
    .app-header h1 {{
        color: #FFFFFF;
        font-size: 1.7rem;
        font-weight: 700;
        margin: 0;
        text-align: center;
    }}
    .app-header .header-rule {{
        width: 90px;
        height: 4px;
        margin: 10px auto 14px auto;
        border-radius: 4px;
        background: linear-gradient(90deg, #F5A623, #E6007E, #1E8FD6);
    }}
    .app-header .header-badge {{
        display: block;
        width: fit-content;
        margin: 0 auto;
        background: rgba(255, 255, 255, 0.14);
        border: 1px solid rgba(255, 255, 255, 0.35);
        color: #FFFFFF;
        font-size: 0.8rem;
        padding: 5px 14px;
        border-radius: 20px;
    }}
    .app-header .status-dot {{
        display: inline-block;
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: #3DDC84;
        margin-right: 6px;
    }}

    /* ---------- Tarjetas blancas ---------- */
    .card {{
        background: #FFFFFF;
        border-radius: 14px;
        padding: 18px 22px;
        margin-bottom: 18px;
        box-shadow: 0 10px 30px rgba(16, 24, 40, 0.18), 0 2px 6px rgba(16, 24, 40, 0.10);
    }}
    .card-title {{
        color: {COLOR_AZUL_CORP};
        font-weight: 700;
        font-size: 0.95rem;
        margin-bottom: 10px;
    }}
    .section-title {{
        text-align: center;
        color: {COLOR_AZUL_CORP};
        font-weight: 700;
        font-size: 1.05rem;
        margin: 6px 0 16px 0;
    }}
    .section-title .rule {{
        width: 60px;
        height: 3px;
        background: {COLOR_AZUL_CORP};
        margin: 6px auto 0 auto;
        border-radius: 3px;
    }}

    /* ---------- Pildoras de compania ---------- */
    .pill {{
        display: inline-block;
        color: #FFFFFF;
        font-weight: 700;
        font-size: 0.85rem;
        padding: 6px 22px;
        border-radius: 20px;
        text-align: center;
    }}

    /* ---------- Tabla resumen (metricas por compania) ---------- */
    table.metric-table {{
        width: 100%;
        border-collapse: collapse;
    }}
    table.metric-table th {{
        text-align: center;
        padding: 10px 8px;
        border-bottom: 1px solid #EEF1F5;
    }}
    table.metric-table td {{
        text-align: center;
        padding: 10px 8px;
        border-bottom: 1px solid #EEF1F5;
        color: {COLOR_TEXTO};
    }}
    table.metric-table td:first-child, table.metric-table th:first-child {{
        text-align: left;
        color: {COLOR_AZUL_CORP};
        font-weight: 600;
    }}
    table.metric-table tr.metric-total td {{
        font-weight: 700;
        font-size: 1.05rem;
        color: {COLOR_AZUL_CORP};
    }}

    /* ---------- Franja de estados (Stock minimo, etc) ---------- */
    .status-strip {{
        display: flex;
        width: 100%;
        border-radius: 8px;
        overflow: hidden;
        margin-bottom: 4px;
    }}
    .status-strip .seg {{
        flex: 1;
        color: #FFFFFF;
        text-align: center;
        font-weight: 700;
        font-size: 0.8rem;
        padding: 8px 4px;
    }}

    /* ---------- Badge de estado dentro de tabla detalle ---------- */
    .status-dot-cell {{
        display: inline-block;
        width: 9px;
        height: 9px;
        border-radius: 50%;
        margin-right: 6px;
    }}

    /* ---------- Filtros (sidebar) ---------- */
    .filtro-label {{
        background: {COLOR_AZUL_CORP};
        color: #FFFFFF;
        font-weight: 700;
        font-size: 0.75rem;
        padding: 4px 10px;
        border-radius: 6px 6px 0 0;
        display: inline-block;
    }}

    /* ---------- Tabla de detalle con borde degradado ---------- */
    /* Separado en 2 capas: el borde/padding va en el contenedor EXTERIOR
       (sin scroll), y el interior (con scroll) queda sin padding para que
       el thead sticky quede pegado al borde superior visible sin hueco. */
    .detail-table-outer {{
        border: 2px solid transparent;
        border-radius: 12px;
        background:
            linear-gradient(#fff, #fff) padding-box,
            linear-gradient(120deg, #1E8FD6, #4CAF50, #F5A623, #E6007E) border-box;
        padding: 4px;
        margin-bottom: 10px;
    }}
    .detail-table-wrap {{
        max-height: 900px;
        overflow: auto;
        border-radius: 9px;
    }}
    table.detail-table {{
        width: 100%;
        border-collapse: collapse;
        font-size: 0.82rem;
    }}
    table.detail-table thead th {{
        position: sticky;
        top: 0;
        background: {COLOR_AZUL_CORP};
        color: #FFFFFF;
        padding: 8px 6px;
        text-align: center;
        z-index: 1;
    }}
    table.detail-table tbody td {{
        padding: 7px 8px;
        text-align: center;
        border-bottom: 1px solid #F0F2F5;
        white-space: nowrap;
    }}
    table.detail-table tbody tr:hover {{
        background: #F7F9FC;
    }}
    table.detail-table tbody tr.grupo-material-fin td {{
        border-bottom: 2px solid {COLOR_AZUL_CORP};
    }}

    /* ---------- Badges de conteo (Materias primas / Material empaque) ---------- */
    .count-badge {{
        display: inline-block;
        color: #FFFFFF;
        font-weight: 700;
        font-size: 0.8rem;
        padding: 6px 16px;
        border-radius: 20px;
        margin-right: 10px;
    }}

    /* ---------- Radio horizontal estilizado como pildoras (para secciones) ---------- */
    div[role="radiogroup"] {{
        gap: 6px;
    }}

    /* ---------- Fila de pastillas de filtro (Centro) ---------- */
    .st-key-fila_pills_centro {{
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: wrap;
        gap: 8px;
    }}
    .st-key-fila_pills_centro > div {{
        width: auto !important;
        flex: 0 0 auto !important;
    }}
</style>
"""
