#!/usr/bin/env python3
"""
Systemic AI Cascade Loss (SACL) & Synapticide's Law
Monte Carlo Engine (10,000 Runs)

Author: Independent Cybernetics & Cosmology Research Group
License: MIT
Repository: Synapticides-Law
"""

import os
import numpy as np
import pandas as pd
from scipy.integrate import quad
import matplotlib.pyplot as plt

# =========================================================================
# 1. SETUP AND REPRODUCIBILITY
# =========================================================================
np.random.seed(42)
NUM_SIMULATIONS = 10000

print(f"[*] Initializing SACL Monte Carlo Engine ({NUM_SIMULATIONS:,} simulations)...")

# =========================================================================
# 2. PROBABILITY DISTRIBUTIONS & VARIABLE SAMPLING
# =========================================================================

# R_ops: Base operations per hour (Log-normal distribution)
R_ops = np.random.lognormal(mean=9.0, sigma=1.0, size=NUM_SIMULATIONS)

# M_swarm: Agent swarm size (Poisson distribution centered around ~500 agents)
M_swarm = np.random.poisson(lam=500, size=NUM_SIMULATIONS)

# alpha_swarm: Inter-agent coordination efficiency exponent (Uniform between 0.6 and 1.3)
alpha_swarm = np.random.uniform(0.6, 1.3, size=NUM_SIMULATIONS)

# Effective Velocity V_E = log10(R_effective)
R_effective = R_ops * (M_swarm ** alpha_swarm)
V_E = np.log10(R_effective)

# Temporal Parameters (Hours)
t_notice = np.random.triangular(left=2.0, mode=12.0, right=72.0, size=NUM_SIMULATIONS)  # Time-to-detection
lambda_decay = np.random.uniform(0.05, 0.5, size=NUM_SIMULATIONS)                       # Containment decay rate
T_total = np.random.uniform(24.0, 168.0, size=NUM_SIMULATIONS)                          # Total attempt window

# K_cb: Circuit breaker threshold (Operations cap; 20% unprotected infinite baseline)
K_cb = np.random.choice([100000, 500000, 1000000, np.inf], size=NUM_SIMULATIONS, p=[0.3, 0.3, 0.2, 0.2])

# Financial Loss Tensor Components (Millions USD)
L_infra = np.random.triangular(left=2.0, mode=15.0, right=50.0, size=NUM_SIMULATIONS)

# L_Model calculation: (P_GPU * H_retrain) + C_alignment + D_weight
P_GPU = 3.50  # USD per GPU hour
H_retrain = np.random.uniform(5000, 30000, size=NUM_SIMULATIONS)
C_alignment = np.random.uniform(1.0, 10.0, size=NUM_SIMULATIONS)
D_weight = np.random.uniform(5.0, 50.0, size=NUM_SIMULATIONS)
L_model = ((P_GPU * H_retrain) / 1e6) + C_alignment + D_weight

# Downstream Impact: N B2B Entities * Average Loss per Entity
N_downstream = np.random.poisson(lam=150, size=NUM_SIMULATIONS)
L_down_per_entity = np.random.uniform(0.1, 2.0, size=NUM_SIMULATIONS)
L_downstream_total = N_downstream * L_down_per_entity

# =========================================================================
# 3. PIECEWISE NUMERICAL INTEGRATION OF CONTAINMENT PHI(t)
# =========================================================================
effective_duration = np.zeros(NUM_SIMULATIONS)

print("[*] Executing numerical integration across containment regimes...")
for i in range(NUM_SIMULATIONS):
    # Determine circuit breaker trip time
    t_cb = K_cb[i] / R_effective[i] if not np.isinf(K_cb[i]) else np.inf
    t_max = min(T_total[i], t_cb)
    
    # Define piecewise decay function Phi(t)
    def phi(t, t_n, lam):
        if t < t_n:
            return 1.0
        else:
            return np.exp(-lam * (t - t_n))
            
    val, _ = quad(phi, 0, t_max, args=(t_notice[i], lambda_decay[i]))
    effective_duration[i] = val

# =========================================================================
# 4. TOTAL SYSTEMIC LOSS CALCULATION & ACTUARIAL STATS
# =========================================================================
C_total_SACL = V_E * effective_duration * (L_infra + L_model + L_downstream_total)

df_results = pd.DataFrame({
    'V_E_Velocity': V_E,
    't_notice_hrs': t_notice,
    'Effective_Duration_hrs': effective_duration,
    'L_Infra_MUSD': L_infra,
    'L_Model_MUSD': L_model,
    'L_Downstream_MUSD': L_downstream_total,
    'C_Total_SACL_MUSD': C_total_SACL
})

print("\n" + "="*60)
print("=== SACL MONTE CARLO SIMULATION RESULTS (10,000 RUNS) ===")
print("="*60)
stats = df_results['C_Total_SACL_MUSD'].describe(percentiles=[0.50, 0.75, 0.90, 0.95, 0.99])
print(stats.apply(lambda x: f"${x:,.2f}M USD"))
print("="*60 + "\n")

# =========================================================================
# 5. CHART GENERATION & EXPORT
# =========================================================================
print("[*] Exporting publication-grade figures to output directory...")

plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Plot 1: Loss Density Distribution Histogram
ax1.hist(C_total_SACL, bins=50, color='#1f77b4', edgecolor='black', alpha=0.7)
ax1.set_xscale('log')
ax1.set_title('SACL Loss Density Distribution (Log Scale)', fontsize=12, fontweight='bold')
ax1.set_xlabel('Total Systemic Loss ($C_{Total}$ in Millions USD)')
ax1.set_ylabel('Frequency (Out of 10,000 Runs)')

# Plot 2: Loss Exceedance Curve (LEC)
sorted_losses = np.sort(C_total_SACL)
p_exceedance = 1.0 - (np.arange(1, NUM_SIMULATIONS + 1) / NUM_SIMULATIONS)

ax2.plot(sorted_losses, p_exceedance * 100, color='#d62728', linewidth=2)
ax2.set_xscale('log')
ax2.set_title('Loss Exceedance Curve (LEC)', fontsize=12, fontweight='bold')
ax2.set_xlabel('Loss Threshold ($C_{Total}$ in Millions USD)')
ax2.set_ylabel('Probability of Exceedance (%)')
ax2.axvline(x=np.percentile(C_total_SACL, 95), color='black', linestyle='--', label=f'95th Percentile (${stats["95%"]:,.2f}M)')
ax2.legend()

plt.tight_layout()

# Save charts locally if output directory exists or in root
output_dir = os.path.join(os.path.dirname(__file__), "..", "paper", "figures")
if os.path.exists(output_dir):
    plt.savefig(os.path.join(output_dir, "density_plot.png"), dpi=300)
    plt.savefig(os.path.join(output_dir, "lec_curve.png"), dpi=300)
    print(f"[+] Figures successfully saved to: {output_dir}")
else:
    plt.savefig("density_plot.png", dpi=300)
    plt.savefig("lec_curve.png", dpi=300)
    print("[+] Figures saved to current directory.")

print("[*] Monte Carlo Engine execution complete.")