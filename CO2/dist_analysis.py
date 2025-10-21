import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

Ry_to_J = 2.1798741e-18
au_to_m = 0.529177249e-10

dist_data = pd.read_csv('en_vs_dist.dat', sep=' ')
dist_data = dist_data.sort_values('dist')

dist = dist_data['dist'].to_numpy()[2:]
energy = dist_data['energy(Ry)'].to_numpy()[2:]

to_fit_index = (dist < 0.2) * (dist > -0.2)
to_fit_dist = dist[to_fit_index]
to_fit_energy = energy[to_fit_index]

popt, _ = np.polyfit(to_fit_dist, to_fit_energy, deg=2, cov=True)
half_k, c1, c0 = popt
print(f'k = {2 * half_k * Ry_to_J / (au_to_m)**2:.2f} J / m^2')

def energy_approx(x):
  return  c0 + x*c1 + x**2 * half_k

to_plot_dist = np.linspace(-0.3, 0.35, 100)
_, ax = plt.subplots(1, 1, figsize=(9,6))
ax.plot(dist, energy, 'o')
ax.plot(to_plot_dist, energy_approx(to_plot_dist), color='red')
plt.savefig(f'../../report/Figures/CO2/CO2_energy_plot.png')
plt.show()