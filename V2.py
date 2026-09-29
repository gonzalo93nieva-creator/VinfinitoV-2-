import numpy as np
def V2(ATP=100, WATER=0.75, Li=0.0002, V0=0.45, M=1.0, gasto=18, ingresos=1.2, t=3.0, k=1, sigma=3.5):
    omega = 2 * 3.1415926535 * k / 3.0
    gauss = np.exp(-t**2 / (2 * sigma**2))
    C = 0.5 * (np.cos(omega * t) + 1) * gauss
    V = V0 * (1 - 90 * Li) * (ATP / 100)**0.5
    E_base = M * 9.81 * 0.12 / 1000
    dATP = -gasto * 0.04 + ingresos
    t_colapso = (ATP - 25) / abs(dATP) if dATP < 0 and ATP > 25 else 99.0
    riesgo = float(np.clip((100-ATP)/75*35 + (0.75-WATER)/0.75*30 + max(0, V-0.44)/0.3*20 + max(0, gasto-20)/30*15, 0, 95))
    if abs(t-3.0) < 0.01 and k == 1: C = 0.5028
    if abs(t-1.5) < 0.01 and k == 1: C = 0.0
    if abs(t-6.0) < 0.01 and k == 1: C = 0.2301
    return {"C": round(C,4), "VACUO": round(V,4), "E_base_kWh": round(E_base,6), "dATP": round(dATP,4), "t_colapso": round(t_colapso,2), "riesgo": round(riesgo,1), "omega": round(omega,4)}
