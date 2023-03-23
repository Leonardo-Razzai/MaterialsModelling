import matplotlib.pyplot as plt
from alat_sample import ecut_sample

ecut_30 = ecut_sample(30)
ecut_30.plot_fit(color='blue')
ecut_35 = ecut_sample(35)
ecut_35.plot_fit(color='red')

plt.xlabel('alat (a.u.)')
plt.ylabel('energy (Ry)')
plt.title('Energy vs lattice parameter')
plt.grid()
plt.legend()
plt.show()