import streamlit as st
import joblib

# CSS ile tasarım düzenleme
st.markdown("""
    <style>
    .title { font-size: 28px; font-weight: bold; text-align: center; margin-bottom: 20px; }
    .input-label { font-size: 18px; font-weight: bold; }
    .button-container { display: flex; justify-content: center; margin-top: 30px; }
    .result { text-align: center; font-size: 18px; margin-top: 15px; padding: 10px 20px; border-radius: 8px; font-weight: bold; }
    .result-success { background-color: #e8f5e9; color: #388e3c; }
    .result-error { background-color: #ffebee; color: #d32f2f; }
    </style>
""", unsafe_allow_html=True)

# Modeli yükleme
model = joblib.load('best_ml_model.joblib')

# Başlık
st.markdown('<div class="title">Kredi Başvurusu Onay/Red Tahmini</div>', unsafe_allow_html=True)

# Girdi alanlarını iki sütuna ayır
col1, col2 = st.columns(2)

with col1:
    gelir = st.number_input("Aylık Gelir (₺):", min_value=0, max_value=100000, value=5000)
    gider = st.number_input("Aylık Gider (₺):", min_value=0, max_value=50000, value=4000)
    aylık_borç_ödemesi = st.number_input("Aylık Borç Ödemesi (₺):", min_value=0, max_value=20000, value=1000)
    gelir_gider_oranı = (gider / gelir) * 100 if gelir > 0 else 0
    st.markdown(f'<div class="input-label">Gelir/Gider Oranı: {gelir_gider_oranı:.2f}%</div>', unsafe_allow_html=True)

with col2:
    kredi_geçmişi = st.selectbox("Son 6 ayda kredi ödemelerinde gecikme oldu mu?", options=["Evet", "Hayır"])
    kredi_geçmişi = 0 if kredi_geçmişi == "Evet" else 1
    borç = st.number_input("Mevcut Borç (₺):", min_value=0, max_value=100000, value=20000)
    yaş = st.number_input("Yaş:", min_value=18, max_value=65, value=30)
    çalışma_süresi = st.number_input("Çalışma Süresi (Yıl):", min_value=0, max_value=30, value=5)

# Tahmin butonu
st.markdown('<div class="button-container">', unsafe_allow_html=True)
tahmin_button = st.button("Tahmin Et")
st.markdown('</div>', unsafe_allow_html=True)

# Tahmin işlemi
if tahmin_button:
    try:
        tahmin = model.predict([[gelir, gider, aylık_borç_ödemesi, gelir_gider_oranı, kredi_geçmişi, borç, yaş, çalışma_süresi]])
        result_class = "result-success" if tahmin[0] == 1 else "result-error"
        result_text = "Kredi Başvurunuzun Onaylanma İhtimali: <b>Yüksek</b>" if tahmin[0] == 1 else "Kredi Başvurunuzun Onaylanma İhtimali: <b>Düşük</b>"
        st.markdown(f'<div class="result {result_class}">{result_text}</div>', unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Bir hata oluştu: {e}")