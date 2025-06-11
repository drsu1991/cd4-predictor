import sys
import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load model
model = joblib.load("model_cd4_regresi.pkl")

# UI
st.title("Prediksi Nilai CD4 Berdasarkan Data Hematologi")
st.markdown("Masukkan data pasien untuk memprediksi CD4 (sel/μL):")

usia = st.number_input("Usia", 0, 100, 35)
jenis_kelamin = st.selectbox("Jenis Kelamin", ["Laki-laki", "Perempuan"])
leukosit = st.number_input("Leukosit", 0.0, 20.0, 5.5)
neutrofil_abs = st.number_input("Neutrofil Absolut", 0.0, 15.0, 3.0)
limfosit_abs = st.number_input("Limfosit Absolut", 0.0, 10.0, 1.2)
hemoglobin = st.number_input("Hemoglobin", 0.0, 20.0, 12.0)
trombosit = st.number_input("Trombosit", 50.0, 1000.0, 250.0)
hematokrit = st.number_input("Hematokrit", 20.0, 60.0, 38.0)
mcv = st.number_input("MCV", 60.0, 120.0, 85.0)
mch = st.number_input("MCH", 20.0, 40.0, 30.0)
mchc = st.number_input("MCHC", 28.0, 38.0, 34.0)

jk_encoded = 1 if jenis_kelamin == "Laki-laki" else 0

input_data = pd.DataFrame([{
    'usia': usia,
    'jenis_kelamin': jk_encoded,
    'leukosit': leukosit,
    'neutrofil_abs': neutrofil_abs,
    'limfosit_abs': limfosit_abs,
    'hemoglobin': hemoglobin,
    'trombosit': trombosit,
    'hematokrit': hematokrit,
    'mcv': mcv,
    'mch': mch,
    'mchc': mchc
}])

if st.button("Prediksi CD4"):
    pred = model.predict(input_data)[0]
    st.success(f"Prediksi CD4 pasien: **{pred:.0f} sel/μL**")
