import numpy as np
import matplotlib.pyplot as plt

# -------------------------
# Parameters
# -------------------------
chi = 0.3
eta = 1.1
L = 0.05  # smaller step for stability

a = 0.95
c = 0.98
b = 0.01

N = 100
N_iter = 200

# -------------------------
# Initialize Stokes vectors
# -------------------------
S0_initial = 1.0
S2_ratio = 0.66

S1 = np.random.uniform(-0.02, 0.02, N)
S3 = np.random.uniform(-0.02, 0.02, N)
S2 = np.full(N, S2_ratio)

# Normalize S0
current_S0 = np.sqrt(S1**2 + S2**2 + S3**2)
S1 *= S0_initial / current_S0
S2 *= S0_initial / current_S0
S3 *= S0_initial / current_S0

# Initial velocities (nonzero for oscillations)
V1 = np.random.uniform(-0.05, 0.05, N)
V2 = np.random.uniform(-0.05, 0.05, N)
V3 = np.random.uniform(-0.05, 0.05, N)

# Storage
S0_hist = np.zeros((N, N_iter))
S1_hist = np.zeros((N, N_iter))
S2_hist = np.zeros((N, N_iter))
S3_hist = np.zeros((N, N_iter))

# -------------------------
# Leap-Frog iterations
# -------------------------
for k in range(N_iter):
    # Nonlinear coefficients
    S0 = np.sqrt(S1**2 + S2**2 + S3**2)
    r2 = S1**2 + S2**2 / eta
    alpha = chi**2 * eta * (S0**2 + (1 - 2*eta)*r2)
    beta = 2 * chi**2 * eta * (eta - 1)

    # Predictor
    S1_star = S1 + L * V1
    V1_star = V1 - L * (alpha * S1 + beta * S1**3)

    S2_star = S2 + L * V2
    V2_star = V2 - L * (alpha * S2 + beta * S2**3)

    S3_star = S3 + L * V3
    V3_star = V3 - L * (alpha * S3 + beta * S3**3)

    # Corrector (trapezoidal)
    S1 += 0.5 * L * (V1 + V1_star)
    V1 -= 0.5 * L * ((alpha * S1 + beta * S1**3) + (alpha * S1_star + beta * S1_star**3))

    S2 += 0.5 * L * (V2 + V2_star)
    V2 -= 0.5 * L * ((alpha * S2 + beta * S2**3) + (alpha * S2_star + beta * S2_star**3))

    S3 += 0.5 * L * (V3 + V3_star)
    V3 -= 0.5 * L * ((alpha * S3 + beta * S3**3) + (alpha * S3_star + beta * S3_star**3))

    # Feedback (uncoupled)
    S0_new = np.sqrt(S1**2 + S2**2 + S3**2)
    f = S1 / (S0_new + 1e-12)
    S1 = a * S1 + b * f
    S2 = a * S2
    S3 = c * S3

    # Store normalized values
    S0_hist[:, k] = np.sqrt(S1**2 + S2**2 + S3**2)
    S1_hist[:, k] = S1 / (S0_hist[:, k] + 1e-12)
    S2_hist[:, k] = S2 / (S0_hist[:, k] + 1e-12)
    S3_hist[:, k] = S3 / (S0_hist[:, k] + 1e-12)

# -------------------------
# Plotting
# -------------------------
fig, axs = plt.subplots(4, 1, figsize=(10, 12), sharex=True)

for i in range(N):
    axs[0].plot(S0_hist[i], color='blue', alpha=0.2)
axs[0].set_ylabel("S0")
axs[0].set_title("Intensity S0")

for i in range(N):
    axs[1].plot(S1_hist[i], color='red', alpha=0.2)
axs[1].axhline(1, ls='--', color='black')
axs[1].axhline(-1, ls='--', color='black')
axs[1].set_ylabel("S1/S0")
axs[1].set_title("S1/S0 Bifurcation")

for i in range(N):
    axs[2].plot(S2_hist[i], color='green', alpha=0.2)
axs[2].set_ylabel("S2/S0")
axs[2].set_title("S2/S0")

for i in range(N):
    axs[3].plot(S3_hist[i], color='purple', alpha=0.2)
axs[3].set_ylabel("S3/S0")
axs[3].set_xlabel("Iteration")
axs[3].set_title("S3/S0")

plt.tight_layout()
plt.show()
