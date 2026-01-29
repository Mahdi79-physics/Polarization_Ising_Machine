✨ Polarization Ising Machine (PIM) — Initializations

This repository contains simulation codes for uncoupled spins of the Polarization Ising Machine (PIM), exploring different initial polarization conditions.

Based on:

Salvatore Chiavazzo, Marcello Calvanese Strinati, Claudio Conti, Davide Pierangeli
Ising Machine by Dimensional Collapse of Nonlinear Polarization Oscillators, Phys. Rev. Lett. 135, 063801 (2025)
🔗 DOI: 10.1103/qs29-2xqc

🧠 Background

The PIM is a high-dimensional Ising machine that uses nonlinear polarization oscillators (NPOs) to encode spins in the polarization of light on the Poincaré sphere.

Key principles:

🌐 Dimensional collapse: 3D polarization dynamics spontaneously collapse into binary Ising spins.

⚡ Feedback & anisotropic loss: Drives each NPO toward stable fixed points representing spin-up or spin-down.

🌀 Initial conditions: This simulation explores how different starting polarizations affect the final spin configurations.

📂 Repository Structure
Polarization_Ising_Machine/
│
├─ README.md
├─ requirements.txt
├─ code_1.py
├─ code_2.py 
├─ code_3.py 
├─ code_4.py 
├─ code_5.py            # Simulation script for uncoupled spins
└─ figures/             # Poincaré sphere plots for different initializations
    ├─ code_1.png
    ├─ code_2.png
    ├─ code_3.png
    ├─ code_4.png
    └─ code_5.png

⚙️ Installation

Clone the repository and install dependencies:

git clone https://github.com/YOUR_USERNAME/Polarization_Ising_Machine.git
cd Polarization_Ising_Machine
pip install -r requirements.txt


Dependencies: numpy, matplotlib

▶️ Usage

Run the simulation for different initializations:

python code_1.py
python code_2.py
python code_3.py
python code_4.py
python code_5.py



The script generates trajectories of the Stokes vectors on the Poincaré sphere.

Final polarization states show how each NPO collapses into an Ising spin.

📊 Simulation Results — Five Initializations

We ran five different initializations to demonstrate how initial polarization conditions affect the final collapse:

Initialization	Description	Final Polarization States
| Initialization | Description        | Final Polarization States |
|----------------|------------------|--------------------------|
| 1              | Random initialization | ![Init 1](uncoupled_initializations/figures/code_1.png) |
| 2              | Random initialization | ![Init 2](uncoupled_initializations/figures/code_2.png) |
| 3              | Random initialization | ![Init 3](uncoupled_initializations/figures/code_3.png) |
| 4              | Random initialization | ![Init 4](uncoupled_initializations/figures/code_4.png) |
| 5              | Random initialization | ![Init 5](uncoupled_initializations/figures/code_5.png) |

Observations:


Each figure shows trajectories of the NPOs on the Poincaré sphere.

Red points correspond to spin-up states, and blue points correspond to spin-down states.

Regardless of the initial conditions, the NPOs robustly collapse into binary spin states, illustrating the effectiveness of dimensional collapse.

Differences in final configurations highlight the stochastic behavior of uncoupled NPOs under various initializations.

📝 Notes

The simulations focus on uncoupled spins, so interactions between NPOs are not included.

These results provide insights into the robustness and variability of the PIM when starting from different polarization states.

The setup can be extended to coupled spins to study ground-state convergence and Ising Hamiltonian optimization.

📚 References

Chiavazzo, S., Calvanese Strinati, M., Conti, C., & Pierangeli, D. (2025). Ising Machine by Dimensional Collapse of Nonlinear Polarization Oscillators. Phys. Rev. Lett., 135, 063801. DOI

Mohseni, N., McMahon, P. L., & Byrnes, T. (2022). Ising machines as hardware solvers of combinatorial optimization problems. Nat. Rev. Phys., 4, 363.

Lucas, A. (2014). Ising formulations of many NP problems. Front. Phys., 2, 5.
