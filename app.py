import streamlit as st
import pandas as pd

# 1. Configuración de la página
st.set_page_config(page_title="Guía Farmacéutica DM2", layout="wide")

# 2. Base de Datos (Simulada para la demo, luego se conecta a Google Sheets)
data = {
    "Fármaco": ["Metformina", "Empagliflozina", "Semaglutida", "Sitagliptina", "Glibenclamida"],
    "Familia": ["Biguanida", "iSGLT2", "Análogo GLP-1", "iDPP-4", "Sulfonilurea"],
    "Mecanismo": [
        "Reduce producción hepática de glucosa.",
        "Bloquea reabsorción de glucosa en el riñón.",
        "Imita incretinas, mejora secreción de insulina.",
        "Inhibe enzima DPP-4, prolonga efecto GLP-1.",
        "Estimula secreción de insulina pancreática."
    ],
    "Consejo Paciente": [
        "Tomar con comidas para evitar malestar estomacal.",
        "Beber mucha agua para prevenir infecciones urinarias.",
        "Siga el plan de escalada de dosis para evitar náuseas.",
        "Se puede tomar con o sin alimentos, muy bien tolerado.",
        "Cargue siempre un dulce por riesgo de baja de azúcar."
    ],
    "Ajuste Renal": ["VFG > 30", "VFG > 20", "No requiere", "Requiere ajuste", "No recomendado"]
}

df = pd.DataFrame(data)

# 3. Interfaz de Usuario
st.title("🔍 Buscador de Actualización en DM2")
st.markdown("---")

# Buscador dinámico
busqueda = st.text_input("Ingrese nombre del fármaco o familia:", "")

# Lógica de filtrado
if busqueda:
    resultado = df[df['Fármaco'].str.contains(busqueda, case=False) | 
                   df['Familia'].str.contains(busqueda, case=False)]
    
    if not resultado.empty:
        for index, row in resultado.iterrows():
            with st.expander(f"📌 {row['Fármaco']} ({row['Familia']})", expanded=True):
                col1, col2 = st.columns(2)
                with col1:
                    st.write("**Mecanismo:**", row['Mecanismo'])
                    st.write("**Ajuste Renal:**", row['Ajuste Renal'])
                with col2:
                    st.info(f"💡 **Consejo para el paciente:**\n{row['Consejo Paciente']}")
    else:
        st.error("No se encontraron resultados.")
else:
    st.write("Escriba algo arriba para comenzar la consulta.")
