import streamlit as st
import random

st.title("📝 Prova de Polímeros")

questoes = [
    {
        "pergunta": "O que é fluência?",
        "alternativas": ["Deformação ao longo do tempo", "Ruptura", "Elasticidade", "Compressão"],
        "correta": "Deformação ao longo do tempo"
    },
    {
        "pergunta": "A Tg representa:",
        "alternativas": ["Mobilidade molecular", "Ruptura", "Carga", "Densidade"],
        "correta": "Mobilidade molecular"
    }
]

random.shuffle(questoes)

respostas = {}

for i, q in enumerate(questoes):
    respostas[i] = st.radio(q["pergunta"], q["alternativas"], key=i)

if st.button("Finalizar"):
    acertos = 0
    for i, q in enumerate(questoes):
        if respostas[i] == q["correta"]:
            acertos += 1

    nota = (acertos / len(questoes)) * 10
    st.success(f"Sua nota: {nota:.1f}")
