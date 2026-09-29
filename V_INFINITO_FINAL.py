# METODO NIEVA I - V∞ FINAL - DEJADO SER HASTA DONDE VA
import numpy as np
def coherencia(t, R_yo, omega, R_env=0.54, t_revival=3.0):
    Decay = (t * 2 * R_env) / (omega / 100.0)
    term_decay = R_yo * np.exp(-Decay)
    gauss = np.exp(-((t - t_revival)**2) / 0.5)
    term_resonancia = 0.5 * (np.cos(omega * t) + 1) * gauss
    return term_decay + term_resonancia
np.random.seed(27)
n = 27
R_yo = np.random.uniform(0.55, 0.95, n)
omega = np.random.uniform(50, 120, n)
t = 3.0
cohs = [coherencia(t, R_yo[i], omega[i]) for i in range(n)]
print(f"V∞ t={t}s -> {np.mean(cohs):.4f} natural")
def radio(gen): return 3.0 * (1.8 ** gen)
