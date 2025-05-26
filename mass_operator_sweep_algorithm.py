# Sweep Algorithm for Wave Mass Operator Parameter Fitting
# R: radius in fm
# M: known atomic mass (u)
# k1_range, k2_range, gamma_range: (min, max) tuples
# resolution: number of steps in linspace
# Returns best-fit A0, k1, k2, gamma, and minimum error.



import numpy as np
from scipy.integrate import quad
import itertools

def sweep_kernels(R, M, k1_range, k2_range, gamma_range, resolution):
    best_error = float('inf')
    best_params = (0, 0, 0, 0)
    for k1, k2, gamma in itertools.product(
        np.linspace(*k1_range, resolution),
        np.linspace(*k2_range, resolution),
        np.linspace(*gamma_range, resolution)
    ):
        denom = np.sin(k1 * R) * np.sin(k2 * R)
        if np.abs(denom) < 1e-6:
            continue
        A0 = M * np.exp(gamma * R) / denom
        def kernel(r): return A0 * np.sin(k1 * r) * np.sin(k2 * r) * np.exp(-gamma * r)
        result, _ = quad(kernel, 0, R)
        error = abs(result - M)
        if error < best_error:
            best_error = error
            best_params = (A0, k1, k2, gamma)
    return best_params, best_error
