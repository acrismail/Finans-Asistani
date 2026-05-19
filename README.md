📈 Türkçe Finans Asistanı (AI-Powered)



Bu proje, Llama-3.2-3B-Instruct modeli kullanılarak, kripto para, borsa ve genel finansal piyasalar üzerine eğitilmiş yerel bir yapay zeka asistanıdır.
Modeli Hugginface'de IsmailAI/finans_asistani_3b_v2 linkinden inceleyebilirsiniz.

🚀 Proje Hakkında
Bu asistan, özellikle BIST 100, teknik analiz (MACD, RSI, vb.), risk yönetimi ve kripto ekosistemi hakkında soruları yanıtlamak için Fine-Tuning yöntemiyle geliştirilmiştir.

Temel Özellikler:

🇹🇷 Tamamen Türkçe finansal veri seti ile eğitildi.

💻 İnternet bağlantısı gerektirmeden, yerel cihazda çalışabilir.

🧠 Sonsuz döngüleri engelleyen özel "Stop Token" ve "Penalty" ayarları.

🕸️ Streamlit ile hazırlanmış modern ve şık bir kullanıcı arayüzü.

🛠 Kullanılan Teknolojiler
Model: Llama-3.2-3B-Instruct

Eğitim: Unsloth (Fine-tuning)

Arayüz: Streamlit

Çalıştırma: Ollama

Veri: Turkish-Finance-SFT-Dataset

📦 Kurulum (Yerel)
1. Ön Gereksinimler
Ollama'nın bilgisayarında kurulu olduğundan emin ol.

Python 3.10+ yüklü olmalı.

2. Modeli Ollama'ya Ekleme
Proje dizininde Modelfile dosyasını kullanarak kendi yerel modelini oluştur:

Bash
ollama create FinansV2 -f Modelfile
3. Arayüzü Başlatma
Streamlit arayüzünü çalıştırmak için:

Bash
pip install streamlit ollama
python -m streamlit run app.py
📝 Kullanım Örnekleri
Modelimize şu tarz sorular sorabilirsin:

"BIST 100 endeksi nedir?"

"Stop-loss stratejisi nasıl uygulanır?"

"MACD indikatörü kripto piyasalarında nasıl yorumlanır?"

💡 Geliştirici Notları
Bu model, [İsmail Açar] tarafından kişisel araştırma projesi kapsamında geliştirilmiştir.

Eğitim süreci 150 adımda optimize edilmiştir; repeat_penalty değerleri döngüleri önlemek için 1.05 seviyesinde tutulmuştur.

📂 Dosya Yapısı
app.py: Streamlit arayüz kodu.

Modelfile: Ollama model konfigürasyonu ve sistem promptları.

README.md: Proje dokümantasyonu.

🤝 Katkıda Bulunma
Bu projeyi geliştirmek istersen pull request gönderebilir veya önerilerini bir issue olarak açabilirsin!
