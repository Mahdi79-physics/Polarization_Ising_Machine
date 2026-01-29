✨ Polarization Ising Machine (PIM)

This repository contains simulation codes of mine for the uncoupled spins of the Polarization Ising Machine (PIM) with different in initial polarization conditions, based on:

Salvatore Chiavazzo, Marcello Calvanese Strinati, Claudio Conti, Davide Pierangeli,
Ising Machine by Dimensional Collapse of Nonlinear Polarization Oscillators, Phys. Rev. Lett. 135, 063801 (2025)
🔗 DOI: 10.1103/qs29-2xqc
✨but with Leap-frog numerical scheme.

🧠 Background

The PIM is a high-dimensional Ising machine that uses nonlinear polarization oscillators (NPOs) to encode spins in the polarization of light on the Poincaré sphere.

🌐 Dimensional collapse: 3D polarization dynamics spontaneously collapse into binary Ising spins.

⚡ Feedback & anisotropic loss: Drives each NPO toward stable fixed points representing spin-up or spin-down.

🌀 Different initial variations: This simulation explores the effect of wide-ranging starting polarizations on the final spin configurations, showing how different initial conditions affect the collapse.

📂 Repository Structure
Polarization_Ising_Machine/
│
├─ README.md
├─ requirements.txt
└─ code_1.py
└─ code_2.py
└─ code_3.py
└─ code_4.py
└─ code_5.py


⚙️ Installation

Clone the repository and install dependencies:

git clone https://github.com/YOUR_USERNAME/Polarization_Ising_Machine.git
cd Polarization_Ising_Machine
pip install -r requirements.txt


Dependencies: numpy, matplotlib

▶️ Usage

Run the simulation script for different initial variations:

python code_1.py
python code_2.py
python code_3.py
python code_4.py
python code_5.py



Trajectories of the Stokes vectors are plotted on the Poincaré sphere.

The final polarization states show how each NPO collapses into an Ising spin.

📚 References

Chiavazzo, S., Calvanese Strinati, M., Conti, C., & Pierangeli, D. (2025).
Ising Machine by Dimensional Collapse of Nonlinear Polarization Oscillators. Phys. Rev. Lett., 135, 063801.
