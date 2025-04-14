
import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("previsoes_etr.csv")


st.set_page_config(page_title="Previsões com ExtraTrees", layout="wide")

# Título
st.title("📊 Dashboard Interativo - Previsões do ativo AAPL")

# Carrega o CSV
try:
    df = pd.read_csv("previsoes_etr.csv")
except FileNotFoundError:
    st.error("Arquivo 'previsoes_etr.csv' não encontrado. Verifique se ele está na mesma pasta do app.")
    st.stop()

# Mostra tabela
st.subheader("🔍 Tabela de Resultados")
st.dataframe(df, use_container_width=True)

# Gráfico de dispersão
st.subheader("📈 Gráfico: Valor Real vs Predição")
fig = px.scatter(df, x="Valor_Real", y="Predicao", trendline="ols",
                 title="Dispersão entre valores reais e predições",
                 labels={"Valor_Real": "Valor Real", "Predicao": "Predição"},
                 color_discrete_sequence=["#2E86AB"])
st.plotly_chart(fig, use_container_width=True)

# Métrica simples
erro_abs = (df['Valor_Real'] - df['Predicao']).abs()
st.metric("Erro Médio Absoluto", f"{erro_abs.mean():.2f}")

st.markdown("---")
st.caption("Desenvolvido com ❤️ usando Streamlit.")