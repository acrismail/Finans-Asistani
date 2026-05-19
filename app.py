import streamlit as st
import ollama

# Sayfa ayarları
st.set_page_config(page_title="Türkçe Finans Asistanı", page_icon="📈", layout="centered")
st.title("📈 Türkçe Finans Asistanı")
st.caption("Kripto para, borsa ve genel finans konularında sorularınızı yanıtlar.")

MODEL_NAME = "FinansV2"

# Sohbet geçmişini başlat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Önceki mesajları ekranda göster
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Kullanıcıdan yeni mesaj al
if prompt := st.chat_input("BIST 100 endeksi nedir? veya MACD nasıl yorumlanır?"):
    
    # Kullanıcı mesajını ekrana yaz ve geçmişe ekle
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Asistanın cevabını ekrana yazdır
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""

        try:
            # API'ye KURALLARI ZORLA DAYATIYORUZ (OPTIONS KISMI)
            for chunk in ollama.chat(
                model=MODEL_NAME,
                messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
                stream=True,
                options={
                    "temperature": 0.3,          # Saçmalamasını önler
                    "repeat_penalty": 1.15,      # Sonsuz döngüyü ve tekrarları kesin olarak keser
                    "stop": [                    # Nerede susması gerektiğini zorla belirtiriz
                        "<|eot_id|>", 
                        "<|start_header_id|>", 
                        "<|end_header_id|>", 
                        "</think>", 
                        "</"
                    ]
                }
            ):
                full_response += chunk['message']['content']
                response_placeholder.markdown(full_response + "▌")
            
            response_placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            
        except Exception as e:
            st.error(f"Hata oluştu: {e}")
