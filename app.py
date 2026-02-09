import streamlit as st

# Configuração da página
st.set_page_config(page_title="Staff Infernal Cruelty", page_icon="🔥")

# Estilização básica
st.markdown("""
    <style>
    .stTextArea textarea {height: 100px;}
    h1, h2 {color: #ff4b4b;}
    </style>
    """, unsafe_allow_html=True)

st.title("🔥 Formulário Staff - Infernal Cruelty")
st.warning("⚠️ Aviso: Respostas copiadas ou mal feitas resultarão em reprovação automática.")

with st.form(key="form_staff"):
    
    # --- INFORMAÇÕES BÁSICAS ---
    st.header("📋 Informações Básicas")
    nick = st.text_input("Nick no servidor:")
    nome_real = st.text_input("Nome real (opcional):")
    idade = st.number_input("Idade:", min_value=1, max_value=99, step=1)
    tempo_jogo = st.text_input("Quanto tempo joga no servidor?")
    tempo_online = st.text_input("Quanto tempo pode ficar online por dia?")
    ja_foi_staff = st.text_area("Já foi staff antes? Se sim, onde?")

    # --- CONHECIMENTO E EXPERIÊNCIA ---
    st.header("🧠 Conhecimento e Experiência")
    p1 = st.text_area("O que faz um bom staff?")
    p2 = st.text_area("O que você faria se dois jogadores começassem a brigar no chat?")
    p3 = st.text_area("O que faria se um amigo seu quebrasse as regras?")
    p4 = st.text_area("Se outro staff estivesse abusando do poder, o que você faria?")
    p5 = st.text_area("Você sabe gravar provas (print/vídeo)? Como faria?")

    # --- SITUAÇÕES PRÁTICAS ---
    st.header("🛠️ Situações Práticas")
    s1 = st.text_area("Um jogador está xingando no chat. Qual sua atitude?")
    s2 = st.text_area("Um player é acusado de hack, mas você não tem provas. O que faz?")
    s3 = st.text_area("Um jogador novo pede ajuda várias vezes. Como você responde?")
    s4 = st.text_area("Se você errar uma punição, o que faria?")

    # --- COMPROMISSO ---
    st.header("🤝 Compromisso")
    c1 = st.text_area("Por que devemos escolher você?")
    c2 = st.text_area("O que te diferencia dos outros?")
    c3 = st.radio("Está disposto a seguir TODAS as regras da staff?", ("Sim", "Não"))
    c4 = st.radio("Se for rejeitado, continuará jogando normalmente?", ("Sim", "Não"))

    st.markdown("---")
    enviar = st.form_submit_button("ENVIAR CANDIDATURA")

if enviar:
    if nick and p1 and c1:
        st.success(f"✅ Obrigado, {nick}! Sua candidatura foi visualizada.")
        st.balloons()
        # Como não há banco de dados, os dados apenas aparecem na tela para quem enviou.
    else:
        st.error("❌ Por favor, preencha as informações obrigatórias.")

st.caption("Infernal Cruelty ")
