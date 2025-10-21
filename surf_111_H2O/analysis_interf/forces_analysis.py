import pandas as pd
import numpy as np
Ry_to_J = 2.1798741e-18
au_to_m = 0.529177249e-10

forces_data = pd.read_csv('data/final_forces.dat')
total_force = 0
for force in forces_data['fz']:
  total_force += np.abs(force) # abs needed beacause there is always same sign in same layer

a_bohr = 7.2447 / np.sqrt(2)
a = a_bohr * au_to_m # lattice param in m
A = np.sqrt(3) * 2 * a**2 # area in m**2

total_force_N = total_force * Ry_to_J / au_to_m
press_Pa = total_force_N / (2*A)
print(f'Total force = {total_force:.2e} Ry/au = {total_force_N:.2e} N\nArea = {A:.2e} m^2\nPressure = {press_Pa*1e-9:.2f} GPa')