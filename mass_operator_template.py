# Wave-Based Mass Operator Template
# Replace the following placeholders with actual values:
# ELEMENT_NAME: Full name of the element (e.g., "Hydrogen-1")
# ELEMENT_TAG: Short lowercase tag (e.g., "h1")
# A0_VALUE, K1_VALUE, K2_VALUE, GAMMA_VALUE: Fitted model parameters
# RADIUS_VALUE: Nuclear radius in femtometers (fm)

# The compute_mass_ELEMENT_TAG function integrates the waveform
# to yield the predicted mass in atomic mass units (u).



import numpy as np
from scipy.integrate import quad

# Calibrated parameters for ELEMENT_NAME
A0 = A0_VALUE
k1 = K1_VALUE
k2 = K2_VALUE
gamma = GAMMA_VALUE

def mass_operator_ELEMENT_TAG(r):
    return A0 * np.sin(k1 * r) * np.sin(k2 * r) * np.exp(-gamma * r)

def compute_mass_ELEMENT_TAG(R=RADIUS_VALUE):
    result, _ = quad(mass_operator_ELEMENT_TAG, 0, R)
    return result
