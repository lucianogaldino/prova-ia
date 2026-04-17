import streamlit as st
import json

st.title("📝 Prova de Polímeros")

# carregar prova do JSON
with open("prova.json") as f:
    dados = json.load(f)

prova = dados["prova"]
gabarito = dados["gabarito"]

respostas = {}

for i, q in enumerate(prova):
    respostas[i] = st.radio(
        q["pergunta"],
        q["alternativas"],
        key=i
    )

if st.button("Finalizar"):
    acertos = 0

    for i in respostas:
        if respostas[i] == gabarito[str(i)]:
            acertos += 1

    nota = (acertos / len(prova)) * 10
    st.success(f"Sua nota: {nota:.1f}")
