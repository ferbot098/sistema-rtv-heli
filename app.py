import streamlit as st

# --- MOTOR DE CÁLCULO (Tu lógica de ingeniero) ---
def calcular_rtv(h1, m1, h2, m2):
    # Convertimos todo a minutos (Base 60)
    inicio = int(h1) * 60 + int(m1)
    fin = int(h2) * 60 + int(m2)
    total_minutos = fin - inicio
    
    # Devolvemos a formato sexagesimal
    horas_final = total_minutos // 60
    minutos_final = total_minutos % 60
    return f"{horas_final:02d}:{minutos_final:02d}"

# --- INTERFAZ (Para tu papá) ---
st.title("🚁 Calculadora RTV - Helicópteros")

col1, col2 = st.columns(2)
with col1:
    h_inicio = st.number_input("Hora Inicio", 0, 23, 8)
    m_inicio = st.number_input("Minutos Inicio", 0, 59, 30)

with col2:
    h_fin = st.number_input("Hora Fin", 0, 23, 10)
    m_fin = st.number_input("Minutos Fin", 0, 59, 45)

if st.button("CALCULAR TIEMPO DE VUELO"):
    resultado = calcular_rtv(h_inicio, m_inicio, h_fin, m_fin)
    st.success(f"El tiempo total es: {resultado}")