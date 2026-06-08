# 🎓 Fuzzy Mamdani Student Performance Predictor

> Sistem prediksi performa mahasiswa menggunakan **Fuzzy Inference System (FIS) metode Mamdani** berbasis Python dan Streamlit.

![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red?style=flat-square&logo=streamlit)
![NumPy](https://img.shields.io/badge/NumPy-latest-013243?style=flat-square&logo=numpy)
![Matplotlib](https://img.shields.io/badge/Matplotlib-latest-11557c?style=flat-square&logo=matplotlib)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## 📌 Tentang Proyek

Proyek ini merupakan **Tugas Besar mata kuliah Logika Fuzzy** yang mengimplementasikan Fuzzy Inference System (FIS) metode **Mamdani** untuk memprediksi performa akademik mahasiswa berdasarkan tiga variabel input utama.

Sistem ini mampu mengklasifikasikan performa mahasiswa ke dalam 4 kategori: **Poor**, **Fair**, **Good**, dan **Excellent** — menggunakan 27 rule fuzzy yang dihasilkan secara otomatis dari kombinasi semua label linguistik.

---

## ✨ Fitur Utama

- 🔢 **Fuzzifikasi** input menggunakan fungsi keanggotaan segitiga (triangular)
- 📐 **27 Rule Fuzzy** yang di-generate otomatis dari kombinasi label linguistik
- ⚙️ **Inferensi Mamdani** dengan operator AND (metode MIN) dan agregasi MAX
- 📊 **Defuzzifikasi** menggunakan metode Centroid
- 🖥️ **Antarmuka interaktif** berbasis Streamlit dengan slider real-time
- 📈 **Visualisasi** fungsi keanggotaan input dan kurva agregasi output

---

## 🧠 Variabel Sistem

### Input
| Variabel | Rentang | Label Linguistik |
|---|---|---|
| `Hours Studied` | 0 – 40 jam/minggu | Low, Medium, High |
| `Attendance` | 60 – 100% | Low, Medium, High |
| `Previous Scores` | 0 – 100 | Low, Medium, High |

### Output
| Label | Rentang Skor |
|---|---|
| Poor | 0 – 40 |
| Fair | 30 – 70 |
| Good | 60 – 90 |
| Excellent | 80 – 100 |

---

## 🗂️ Struktur Proyek

```
fuzzy-mamdani-student-performance/
├── app.py                          # Aplikasi Streamlit utama
├── StudentPerformanceFactors.csv   # Dataset (6607 data, 20 kolom)
├── TuBesfuzzyBforBerkah.ipynb                  # Notebook colab               
├── requirements.txt   
└── README.md
```

---

## ⚙️ Cara Menjalankan

### 1. Clone Repository
```bash
git clone https://github.com/username/fuzzy-mamdani-student-performance.git
cd fuzzy-mamdani-student-performance
```

### 2. Install Dependencies
```bash
pip install streamlit numpy matplotlib pandas
```

### 3. Jalankan Aplikasi
```bash
streamlit run app.py
```

Buka browser dan akses `http://localhost:8501`

---

## 🔬 Alur Sistem FIS Mamdani

```
Input Numerik
     │
     ▼
┌─────────────┐
│ Fuzzifikasi │  → Hitung derajat keanggotaan setiap variabel
└─────────────┘
     │
     ▼
┌──────────────────┐
│ Evaluasi 27 Rule │  → AND (MIN) antar anteseden
└──────────────────┘
     │
     ▼
┌──────────────┐
│  Implikasi   │  → Clipping (MIN) sesuai firing strength
└──────────────┘
     │
     ▼
┌───────────┐
│ Agregasi  │  → MAX dari semua rule aktif
└───────────┘
     │
     ▼
┌──────────────────┐
│ Defuzzifikasi    │  → Centroid → Crisp Output
└──────────────────┘
     │
     ▼
  Skor Performa (0–100)
```

---

## 📊 Dataset

Dataset yang digunakan: **Student Performance Factors** (Kaggle)

- **Jumlah data:** 6.607 baris
- **Jumlah kolom:** 20 kolom
- **Kolom yang digunakan:** `Hours_Studied`, `Attendance`, `Previous_Scores`, `Exam_Score`

---

## 👥 Tim Pengembang

| Nama | NIM |
|---|---|
| [Kurnia Dwi Surya] | [F1D02310013] |
| [Wicaksono Hadidulmanan] | [F1D02310095] |
| [Karina Septia Suwandi] | [F1D02310066] |
| [Zamzami Satria Tegar] | [F1D02310029] |


> Proyek ini dibuat sebagai bagian dari **Tugas Besar Logika Fuzzy**

## Link Streamlit
https://rainardw-fuzzy-mamdani-student-performance.streamlit.app/
---

## 📄 Lisensi

Didistribusikan di bawah lisensi MIT. Lihat `LICENSE` untuk informasi lebih lanjut.
