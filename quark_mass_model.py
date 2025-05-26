
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

def fit_quark_mass(R, known_mass, sweep_ranges, resolution=50):
    k1_range, k2_range, gamma_range = sweep_ranges
    return sweep_kernels(R, known_mass, k1_range, k2_range, gamma_range, resolution)

# Example: Fit for a down quark (~4.8 MeV/c²)
# Note: Must convert MeV/c² to atomic mass units if needed
if __name__ == "__main__":
    R = 0.84  # approximate radius for light quarks in fm
    known_mass = 0.0051  # u (atomic mass units), roughly 4.8 MeV/c²
    sweep_ranges = ((8, 12), (2, 6), (0.3, 1.0))
    params, error = fit_quark_mass(R, known_mass, sweep_ranges, resolution=40)
    print("Best-fit parameters for quark mass:", params)
    print("Absolute error:", error)
