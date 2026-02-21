import streamlit as st
import time

# Estética profissional para Planejador Financeiro
st.set_page_config(page_title="Gestão de Atendimento - Evandro", page_icon="💰")

# Customização de CSS para parecer um App
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 20px; height: 3em; background-color: #25D366; color: white; }
    .stProgress > div > div > div > div { background-color: #25D366; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎙️ Funil de Áudios - Evandro Vieira")
st.info("Utilize este painel para enviar a sequência de diagnóstico financeiro.")

# Mapeamento dos seus arquivos enviados
audios = [
    {"file": "audio1.ogg", "label": "1️⃣ Analogia do Médico (Abertura)", "desc": "Explica a importância do diagnóstico inicial."},
    {"file": "audio2.ogg", "label": "2️⃣ Plano de Ação (Grupo Primo)", "desc": "Fala sobre o benefício exclusivo e sua agenda."},
    {"file": "audio3.ogg", "label": "3️⃣ Call to Action (Fechamento)", "desc": "Pergunta o melhor horário: Manhã, Tarde ou Noite."}
]

for i, item in enumerate(audios):
    with st.expander(item["label"], expanded=True):
        st.write(item["desc"])
        
        # Botão para baixar/enviar
        with open(item["file"], "rb") as f:
            st.download_button(
                label=f"📥 Baixar e Enviar Passo {i+1}",
                data=f,
                file_name=item["file"],
                mime="audio/ogg",
                key=f"btn_{i}"
            )
        
        # Lógica do Delay de 10 segundos
        if i < 2: # Não precisa de delay após o último
            if st.button(f"⏱️ Iniciar Espera para o Áudio {i+2}", key=f"timer_{i}"):
                barra = st.progress(0)
                for t in range(10):
                    time.sleep(1)
                    barra.progress((t + 1) * 10)
                st.success(f"Pode enviar o próximo áudio agora!")

st.markdown("---")
st.caption("Foco: Profissionais de Construção Civil | Renda > R$7k")
