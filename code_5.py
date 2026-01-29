import numpy as np
import matplotlib.pyplot as plt

# -------------------------
# Parameters
# -------------------------
chi = 0.3
eta = 1.1
L = 0.1      # smaller effective step for stability

a = 0.95
c = 0.98
b = 0.01

N = 100
N_iter = 600

# -------------------------
# Initial conditions
# -------------------------
S0_initial = 1.0
S2_ratio = 0.66

S1 = np.random.uniform(-0.02, 0.02, N)
S3 = np.random.uniform(-0.02, 0.02, N)
S2 = np.full(N, S2_ratio)

# Normalize S0
current_S0 = np.sqrt(S1**2 + S2**2 + S3**2)
S1 = S1 * S0_initial / current_S0
S2 = S2 * S0_initial / current_S0
S3 = S3 * S0_initial / current_S0

S1_dot = np.zeros(N)
S2_dot = np.zeros(N)
S3_dot = np.zeros(N)

# History
S0_hist = np.zeros((N, N_iter))
S1_hist = np.zeros((N, N_iter))
S2_hist = np.zeros((N, N_iter))
S3_hist = np.zeros((N, N_iter))

# -------------------------
# Iterative dynamics (stable)
# -------------------------
for k in range(N_iter):
    S0 = np.sqrt(S1**2 + S2**2 + S3**2) + 1e-12
    r2 = S1**2 + S2**2 / eta

    alpha = chi**2 * eta * (S0**2 + (1 - 2*eta) * r2)
    beta = 2 * chi**2 * eta * (eta - 1)

    # ---------------------
    # Semi-implicit propagation for stability
    # ---------------------
    S1L = S1 + L*S1_dot - L**2 * (alpha*S1 + beta*S1**3)
    S2L = S2 + L*S2_dot - L**2 * (alpha*S2 + beta*S2**3)
    S3L = S3 + L*S3_dot - L**2 * (alpha*S3 + beta*S3**3)

    # Update derivatives (semi-implicit)
    S1_dot = S1_dot - L * (alpha*S1L + beta*S1L**3)
    S2_dot = S2_dot - L * (alpha*S2L + beta*S2L**3)
    S3_dot = S3_dot - L * (alpha*S3L + beta*S3L**3)

    # Feedback for S1
    f = S1L / np.maximum(S0, 1e-12)

    # Iterative map
    S1_new = a*S1L + b*f
    S2_new = a*S2L
    S3_new = c*S3L

    # Soft normalization to avoid explosion
    norm = np.sqrt(S1_new**2 + S2_new**2 + S3_new**2)
    mask = norm > 10.0
    S1_new[mask] /= norm[mask]
    S2_new[mask] /= norm[mask]
    S3_new[mask] /= norm[mask]

    # Store history
    S0_hist[:, k] = np.sqrt(S1_new**2 + S2_new**2 + S3_new**2)
    S1_hist[:, k] = S1_new / np.maximum(S0_hist[:, k], 1e-12)
    S2_hist[:, k] = S2_new / np.maximum(S0_hist[:, k], 1e-12)
    S3_hist[:, k] = S3_new / np.maximum(S0_hist[:, k], 1e-12)

    # Prepare next iteration
    S1 = S1_new
    S2 = S2_new
    S3 = S3_new

# -------------------------
# Plot results
# -------------------------
fig, axs = plt.subplots(4,1, figsize=(10,12), sharex=True)

for i in range(N):
    axs[0].plot(S0_hist[i], color='blue', alpha=0.2)
axs[0].set_ylabel(r'$S_0$')
axs[0].set_title('PIM – Intensity S0')

for i in range(N):
    axs[1].plot(S1_hist[i], color='red', alpha=0.2)
axs[1].set_ylabel(r'$S_1/S_0$')
axs[1].axhline(1, ls='--', color='black', alpha=0.5)
axs[1].axhline(-1, ls='--', color='black', alpha=0.5)
axs[1].set_title('Normalized Stokes S1/S0')

for i in range(N):
    axs[2].plot(S2_hist[i], color='green', alpha=0.2)
axs[2].set_ylabel(r'$S_2/S_0$')
axs[2].set_title('Normalized Stokes S2/S0')

for i in range(N):
    axs[3].plot(S3_hist[i], color='purple', alpha=0.2)
axs[3].set_ylabel(r'$S_3/S_0$')
axs[3].set_xlabel('Iteration')
axs[3].set_title('Normalized Stokes S3/S0')

plt.tight_layout()
plt.show()

# Final spin distribution
final_spins = np.sign(S1_hist[:,-1])
unique, counts = np.unique(final_spins, return_counts=True)
print("Final spin counts (±1):", dict(zip(unique, counts)))
