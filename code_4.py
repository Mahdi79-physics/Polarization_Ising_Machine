import numpy as np
import matplotlib.pyplot as plt

# -------------------------
# Constants
# -------------------------
N = 100      # number of oscillators
N_iter = 200 # iterations
chi = 0.3
eta = 1.1
L = 0.05     # smaller step size for stability

a = 0.95
c = 0.98
b = 0.01

# -------------------------
# Initial Stokes vectors
# -------------------------
S1 = np.random.uniform(-0.02, 0.02, N)
S2 = np.full(N, 0.66)
S3 = np.random.uniform(-0.02, 0.02, N)

# Normalize to have S0 = 1
S0_initial = 1.0
S0_current = np.sqrt(S1**2 + S2**2 + S3**2)
S1 = S1 * S0_initial / S0_current
S2 = S2 * S0_initial / S0_current
S3 = S3 * S0_initial / S0_current

# Derivatives
S1_dot = np.zeros(N)
S2_dot = np.zeros(N)
S3_dot = np.zeros(N)

# Store history
S1_hist = np.zeros((N, N_iter))
S2_hist = np.zeros((N, N_iter))
S3_hist = np.zeros((N, N_iter))
S0_hist = np.zeros((N, N_iter))

# -------------------------
# Predictor-corrector Leap-Frog iteration
# -------------------------
for k in range(N_iter):
    # Current S0
    S0 = np.sqrt(S1**2 + S2**2 + S3**2)
    
    # Coefficients
    r2 = S1**2 + (S2**2)/eta
    alpha = chi**2 * eta * (S0**2 + (1 - 2*eta) * r2)
    beta = 2 * chi**2 * eta * (eta - 1)
    
    # -------------------------
    # Predictor (Euler step)
    # -------------------------
    S1_pred = S1 + L*S1_dot
    S2_pred = S2 + L*S2_dot
    S3_pred = S3 + L*S3_dot
    
    S1_dot_pred = S1_dot - L*(alpha*S1 + beta*S1**3)
    S2_dot_pred = S2_dot - L*(alpha*S2 + beta*S2**3)
    S3_dot_pred = S3_dot - L*(alpha*S3 + beta*S3**3)
    
    # -------------------------
    # Corrector (trapezoidal)
    # -------------------------
    S1_dot_new = S1_dot - 0.5*L*((alpha*S1 + beta*S1**3) + (alpha*S1_pred + beta*S1_pred**3))
    S2_dot_new = S2_dot - 0.5*L*((alpha*S2 + beta*S2**3) + (alpha*S2_pred + beta*S2_pred**3))
    S3_dot_new = S3_dot - 0.5*L*((alpha*S3 + beta*S3**3) + (alpha*S3_pred + beta*S3_pred**3))
    
    S1 = S1 + L*S1_dot_new
    S2 = S2 + L*S2_dot_new
    S3 = S3 + L*S3_dot_new
    
    # -------------------------
    # Feedback (uncoupled)
    # -------------------------
    S0 = np.sqrt(S1**2 + S2**2 + S3**2)
    f = S1 / (S0 + 1e-12)
    
    S1 = a*S1 + b*f
    S2 = a*S2
    S3 = c*S3
    
    # Store history
    S0_hist[:, k] = np.sqrt(S1**2 + S2**2 + S3**2)
    S1_hist[:, k] = S1 / (S0_hist[:, k] + 1e-12)
    S2_hist[:, k] = S2 / (S0_hist[:, k] + 1e-12)
    S3_hist[:, k] = S3 / (S0_hist[:, k] + 1e-12)
    
    # Update derivatives for next step
    S1_dot = S1_dot_new
    S2_dot = S2_dot_new
    S3_dot = S3_dot_new

# -------------------------
# Plotting
# -------------------------
plt.figure(figsize=(12,8))

plt.subplot(4,1,1)
for i in range(N):
    plt.plot(S0_hist[i], color='blue', alpha=0.1)
plt.ylabel("S0")
plt.title("PIM high-dimensional dynamics")

plt.subplot(4,1,2)
for i in range(N):
    plt.plot(S1_hist[i], color='red', alpha=0.1)
plt.ylabel("S1/S0")

plt.subplot(4,1,3)
for i in range(N):
    plt.plot(S2_hist[i], color='green', alpha=0.1)
plt.ylabel("S2/S0")

plt.subplot(4,1,4)
for i in range(N):
    plt.plot(S3_hist[i], color='orange', alpha=0.1)
plt.ylabel("S3/S0")
plt.xlabel("Iteration")

plt.tight_layout()
plt.show()
