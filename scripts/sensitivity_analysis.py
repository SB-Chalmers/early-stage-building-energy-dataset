"""
Sobol Global Sensitivity Analysis for ML Energy Prediction Model.

Varies 10 design parameters using Saltelli sampling and computes
first-order (S1) and total-order (ST) Sobol indices.
"""

import os
import numpy as np
import joblib
import matplotlib.pyplot as plt
from SALib.sample import sobol as sobol_sample
from SALib.analyze import sobol

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"  # suppress TF info/warnings
from tensorflow.keras.models import load_model

# ── Configuration ────────────────────────────────────────────────────────────
N_SAMPLES = 1024  # base sample size; total evals = N*(2D+2)

# Fixed geometric parameters (positions 0-3 in model input)
FIXED = {
    "building_area": 522.79,
    "building_perimeter": 97.62,
    "corridor_area": 78.01,
    "corridor_perimeter": 45.47,
}

# SALib problem definition – 10 varied features
problem = {
    "num_vars": 10,
    "names": [
        "WWR",
        "shading_type",
        "angle",
        "story_height",
        "shading_length",
        "story_number",
        "wall_u_value",
        "roof_u_value",
        "floor_u_value",
        "window_u_value",
    ],
    "bounds": [
        [0.5, 0.9],      # WWR
        [0, 2],           # shading_type (0=horiz, 1=vert, 2=combo)
        [0, 360],         # angle (degrees)
        [2.5, 3.5],       # story_height (m)
        [0.1, 1.0],       # shading_length (m)
        [2, 7],           # story_number
        [0.1, 0.6],       # wall_u_value (W/m²·K)
        [0.1, 0.6],       # roof_u_value (W/m²·K)
        [0.1, 0.5],       # floor_u_value (W/m²·K)
        [1.0, 2.0],       # window_u_value (W/m²·K)
    ],
}

# Integer parameters that need rounding
INTEGER_PARAMS = {"shading_type", "story_number"}

# ── Load model & scaler ─────────────────────────────────────────────────────
script_dir = os.path.dirname(os.path.abspath(__file__))
model = load_model(os.path.join(script_dir, "base_model.h5"), compile=False)
scaler = joblib.load(os.path.join(script_dir, "scaler_model.joblib"))

# ── Generate Saltelli samples ───────────────────────────────────────────────
print(f"Generating Saltelli samples (N={N_SAMPLES}, D={problem['num_vars']}) ...")
param_values = sobol_sample.sample(problem, N_SAMPLES)
n_evals = param_values.shape[0]
print(f"Total model evaluations: {n_evals}")

# ── Assemble full 14-feature input & evaluate ───────────────────────────────
# Model input order (14 features):
#   0: building_area      (fixed)
#   1: building_perimeter  (fixed)
#   2: corridor_area       (fixed)
#   3: corridor_perimeter  (fixed)
#   4: WWR
#   5: shading_type
#   6: angle
#   7: story_height
#   8: shading_length
#   9: story_number
#  10: wall_u_value
#  11: roof_u_value
#  12: floor_u_value
#  13: window_u_value

# Round integer params
for i, name in enumerate(problem["names"]):
    if name in INTEGER_PARAMS:
        param_values[:, i] = np.round(param_values[:, i])

# Build full input matrix
fixed_cols = np.tile(
    [FIXED["building_area"], FIXED["building_perimeter"],
     FIXED["corridor_area"], FIXED["corridor_perimeter"]],
    (n_evals, 1),
)
X_full = np.hstack([fixed_cols, param_values])  # shape: (n_evals, 14)

# Scale & predict
print("Running model predictions ...")
X_scaled = scaler.transform(X_full)
Y = model.predict(X_scaled, batch_size=512, verbose=0).flatten()
print(f"Predictions complete. Y range: [{Y.min():.2f}, {Y.max():.2f}]")

# ── Sobol analysis ──────────────────────────────────────────────────────────
print("\nComputing Sobol indices ...")
Si = sobol.analyze(problem, Y, print_to_console=False)

# ── Print results ───────────────────────────────────────────────────────────
print("\n" + "=" * 65)
print(f"{'Parameter':<18} {'S1':>8} {'S1_conf':>8} {'ST':>8} {'ST_conf':>8}")
print("-" * 65)
for i, name in enumerate(problem["names"]):
    print(
        f"{name:<18} {Si['S1'][i]:>8.4f} {Si['S1_conf'][i]:>8.4f} "
        f"{Si['ST'][i]:>8.4f} {Si['ST_conf'][i]:>8.4f}"
    )
print("-" * 65)
print(f"{'Sum S1':<18} {np.sum(Si['S1']):>8.4f}")
print("=" * 65)

# ── Plot ────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 6))

names = problem["names"]
y_pos = np.arange(len(names))

# Sort by ST descending for readability
order = np.argsort(Si["ST"])[::-1]
sorted_names = [names[i] for i in order]
s1_sorted = Si["S1"][order]
st_sorted = Si["ST"][order]
s1_conf_sorted = Si["S1_conf"][order]
st_conf_sorted = Si["ST_conf"][order]

bar_height = 0.35
ax.barh(
    y_pos + bar_height / 2, st_sorted, bar_height,
    xerr=st_conf_sorted, label="Total-order (ST)",
    color="#4C72B0", alpha=0.85, capsize=3,
)
ax.barh(
    y_pos - bar_height / 2, s1_sorted, bar_height,
    xerr=s1_conf_sorted, label="First-order (S1)",
    color="#DD8452", alpha=0.85, capsize=3,
)

ax.set_yticks(y_pos)
ax.set_yticklabels(sorted_names, fontsize=11)
ax.invert_yaxis()
ax.set_xlabel("Sobol Index", fontsize=12)
ax.set_title("Global Sensitivity Analysis — Sobol Indices", fontsize=14)
ax.legend(loc="lower right", fontsize=11)
ax.grid(axis="x", alpha=0.3)

plt.tight_layout()
out_path = os.path.join(script_dir, "sobol_sensitivity.png")
fig.savefig(out_path, dpi=200)
print(f"\nPlot saved to: {out_path}")
plt.show()
