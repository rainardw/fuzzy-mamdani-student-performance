
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from itertools import product

st.set_page_config(page_title="Sistem Inferensi Fuzzy Mamdani", layout="wide")
st.title("🎓 Sistem Prediksi Performa Mahasiswa")
st.markdown("Menggunakan Metode **Fuzzy Inference System (FIS) Mamdani** dengan 3 Variabel Input dan 27 Rule.")

def triangular(x, a, b, c):
    if x <= a or x >= c: return 0
    elif a < x <= b:
        return 1.0 if b == a else (x-a)/(b-a)
    else:
        return 1.0 if c == b else (c-x)/(c-b)

membership_params = {
    'hours': {'low': (0, 0, 20), 'medium': (10, 20, 30), 'high': (20, 40, 40)},
    'attendance': {'low': (60, 60, 75), 'medium': (70, 85, 95), 'high': (85, 100, 100)},
    'previous': {'low': (0, 0, 50), 'medium': (40, 70, 90), 'high': (70, 100, 100)}
}
output_params = {
    'poor': (0, 0, 40), 'fair': (30, 50, 70),
    'good': (60, 75, 90), 'excellent': (80, 100, 100)
}

def fuzzify(variable, value):
    return {label: triangular(value, p[0], p[1], p[2]) for label, p in membership_params[variable].items()}

labels = ['low', 'medium', 'high']
score_map = {'low': 1, 'medium': 2, 'high': 3}
rules = []
for h, a, p in product(labels, labels, labels):
    score = score_map[h] + score_map[a] + score_map[p]
    output = 'poor' if score <= 4 else 'fair' if score <= 6 else 'good' if score <= 8 else 'excellent'
    rules.append({'if': {'hours': h, 'attendance': a, 'previous': p}, 'then': output})

def mamdani_inference(input_values):
    fuzzified_inputs = {var: fuzzify(var, val) for var, val in input_values.items()}
    rule_outputs = []
    for rule in rules:
        mu = [fuzzified_inputs[var][rule['if'][var]] for var in ['hours', 'attendance', 'previous']]
        firing_strength = min(mu)
        if firing_strength > 0:
            rule_outputs.append({'label': rule['then'], 'params': output_params[rule['then']], 'strength': firing_strength})
    x_out = np.linspace(0, 100, 1000)
    aggregated = np.zeros_like(x_out)
    for out in rule_outputs:
        mu_out = np.array([triangular(x, out['params'][0], out['params'][1], out['params'][2]) for x in x_out])
        implied = np.minimum(mu_out, out['strength'])
        aggregated = np.maximum(aggregated, implied)
    crisp_output = np.sum(x_out * aggregated) / np.sum(aggregated) if np.sum(aggregated) > 0 else 0
    return crisp_output, x_out, aggregated

# === INPUT pakai number_input (tidak butuh JS) ===
st.sidebar.header("📊 Input Variabel")
hours = st.sidebar.number_input("Jam Belajar per Minggu (0-40)", min_value=0, max_value=40, value=15, step=1)
attendance = st.sidebar.number_input("Persentase Kehadiran % (60-100)", min_value=60, max_value=100, value=80, step=1)
previous = st.sidebar.number_input("Nilai Semester Sebelumnya (0-100)", min_value=0, max_value=100, value=65, step=1)

input_vals = {'hours': hours, 'attendance': attendance, 'previous': previous}
crisp, x_out, agg = mamdani_inference(input_vals)

if crisp <= 40: cat, color = 'Poor (Buruk)', 'red'
elif crisp <= 60: cat, color = 'Fair (Cukup)', 'orange'
elif crisp <= 80: cat, color = 'Good (Baik)', 'green'
else: cat, color = 'Excellent (Sangat Baik)', 'blue'

col1, col2, col3 = st.columns(3)
col1.markdown(f"**📚 Jam Belajar**\n\n### {hours} jam/minggu")
col2.markdown(f"**🏫 Kehadiran**\n\n### {attendance}%")
col3.markdown(f"**📝 Nilai Sebelumnya**\n\n### {previous}")

st.markdown(f"## Hasil: :{color}[{cat}] — Skor: **{crisp:.2f}**")

# === GRAFIK INPUT ===
st.markdown("---")
st.subheader("📈 Fungsi Keanggotaan Input")
fig_inputs, axs = plt.subplots(1, 3, figsize=(15, 4))
variables = [('hours', hours, 'Jam Belajar'), ('attendance', attendance, 'Kehadiran'), ('previous', previous, 'Nilai Sebelumnya')]

for ax, (var, val, title) in zip(axs, variables):
    x_range = np.linspace(0, 100, 500)
    for label, params in membership_params[var].items():
        y = [triangular(xi, params[0], params[1], params[2]) for xi in x_range]
        ax.plot(x_range, y, label=label.capitalize(), linewidth=2)
    ax.axvline(x=val, color='red', linestyle='--', linewidth=2, label=f'Input: {val}')
    ax.set_title(title)
    ax.set_ylim(0, 1.1)
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
plt.tight_layout()
st.pyplot(fig_inputs)

# === GRAFIK OUTPUT ===
st.subheader("📉 Agregasi & Defuzzifikasi Output")
fig_out, ax_out = plt.subplots(figsize=(10, 4))
ax_out.plot(x_out, agg, 'k-', linewidth=2, label='Agregasi Rule')
ax_out.fill_between(x_out, agg, color='skyblue', alpha=0.5)
ax_out.axvline(x=crisp, color='red', linestyle='--', linewidth=2, label=f'Crisp Output: {crisp:.2f}')
ax_out.set_title("Hasil Defuzzifikasi (Metode Centroid)")
ax_out.set_xlabel("Skor Performa (0-100)")
ax_out.set_ylabel("Derajat Keanggotaan")
ax_out.legend()
ax_out.grid(True, alpha=0.3)
st.pyplot(fig_out)

# === TABEL RULE pakai st.table (pure HTML, tanpa JS) ===
with st.expander("📜 Lihat 27 Rule Base (IF-THEN)"):
    import pandas as pd
    rule_display = [{'Rule': i, 'IF Hours': r['if']['hours'], 'IF Attendance': r['if']['attendance'], 'IF Previous': r['if']['previous'], 'THEN Performa': r['then']} for i, r in enumerate(rules, 1)]
    st.table(pd.DataFrame(rule_display))
