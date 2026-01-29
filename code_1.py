import numpy as np
import matplotlib.pyplot as plt

# -------------------------
# Parameters (Fig. 2b)
# -------------------------
chi = 0.3  # cm/GW
eta = 1.1
L = 1.2
a = 0.95
b = 0.01
c = 0.98

N = 100
N_iter = 200

# -------------------------
# Initial conditions
# -------------------------
S0_init = 1.0
S2_ratio = 0.66

# Random small S1 and S3
S1 = np.random.uniform(-0.7, 0.7, N)
S3 = np.random.uniform(-0.7, 0.7, N)
# S2 to satisfy S2/S0 = 0.66
S2 = S2_ratio * np.ones(N)

# Normalize S0
current_S0 = np.sqrt(S1**2 + S2**2 + S3**2)
S1 = S1 * S0_init / current_S0
S2 = S2 * S0_init / current_S0
S3 = S3 * S0_init / current_S0

# History
S1_hist = np.zeros((N, N_iter))
S2_hist = np.zeros((N, N_iter))
S3_hist = np.zeros((N, N_iter))
S0_hist = np.zeros((N, N_iter))

# -------------------------
# Iterative map (uncoupled NPOs)
# -------------------------
for k in range(N_iter):
    # Intensity
    S0 = np.sqrt(S1**2 + S2**2 + S3**2) + 1e-12

    # Nonlinear coefficients
    r2 = S1**2 + (S2**2)/eta
    alpha = chi**2 * eta * (S0**2 + (1 - 2*eta) * r2)
    beta  = 2 * chi**2 * eta * (eta - 1)

    # Propagation (Eq.3)
    S1L = S1 - L**2 * (alpha*S1 + beta*S1**3)
    S2L = S2 - L**2 * (alpha*S2 + beta*S2**3)
    S3L = S3 - L**2 * (alpha*S3 + beta*S3**3)

    # Feedback (per NPO, uncoupled)
    f = S1L / S0

    # Iterative map (Eq.2)
    S1 = a*S1L + b*f
    S2 = a*S2L
    S3 = c*S3L

    # Store normalized values
    S0_new = np.sqrt(S1**2 + S2**2 + S3**2)
    S0_hist[:, k] = S0_new
    S1_hist[:, k] = S1 / S0_new
    S2_hist[:, k] = S2 / S0_new
    S3_hist[:, k] = S3 / S0_new

# -------------------------
# Plots
# -------------------------
fig, axs = plt.subplots(4,1, figsize=(10,12), sharex=True)
axs[0].set_title("PIM Uncoupled NPOs – Spin Bifurcation (Fig.2b)")
axs[0].set_ylabel("S0 (intensity)")
axs[0].plot(S0_hist.T, color='blue', alpha=0.2)
axs[1].set_ylabel("S1/S0")
axs[1].plot(S1_hist.T, color='blue', alpha=0.2)
axs[2].set_ylabel("S2/S0")
axs[2].plot(S2_hist.T, color='green', alpha=0.2)
axs[3].set_ylabel("S3/S0")
axs[3].set_xlabel("Iteration")
axs[3].plot(S3_hist.T, color='red', alpha=0.2)

for ax in axs[1:]:
    ax.axhline(1, ls='--', lw=0.8, color='black')
    ax.axhline(-1, ls='--', lw=0.8, color='black')
    ax.axhline(0, ls='-', lw=0.5, color='gray', alpha=0.3)

plt.tight_layout()
plt.show()
