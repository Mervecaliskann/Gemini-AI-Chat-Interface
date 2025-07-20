import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv
import os

# .env dosyasından API key'i yükle
load_dotenv()
my_key = os.getenv("google_apikey")

# API yapılandırması
genai.configure(api_key=my_key)

# Model başlatma
model = genai.GenerativeModel('gemini-2.5-flash')

def generate_response(user_prompt):  
    try:
        
        response = model.generate_content(
            user_prompt,  
            generation_config=genai.GenerationConfig(
                temperature=0.7,  
                max_output_tokens=2048,  # Token limitini artır
                top_p=0.8,
                top_k=40
            )
        )
        
        # Yanıt kontrolü
        if response.parts:  # parts kontrolü eklendi
            return response.text
        else:
            return "Üzgünüm, yanıt üretilemedi. Lütfen başka bir soru sorun."
            
    except Exception as e:
        return f"Bir hata oluştu: {str(e)}"

# Streamlit arayüzü
st.header("Gemini ile İletişim Kurun")
st.divider()

# Kullanıcı girişi
prompt = st.text_input("Mesajınızı Giriniz:")
submit_btn = st.button("Gönder")

# Yanıt gösterme
if submit_btn and prompt:  # Boş prompt kontrolü eklendi
    response = generate_response(prompt)
    st.write(f"Siz: {prompt}")  # Kullanıcı mesajını göster
    st.write(f"Gemini: {response}")  # AI yanıtını göster
