import matplotlib.pyplot as plt
from alat_sample import ecut_sample

ecut_30 = ecut_sample(30)
ecut_30.plot_fit(color='blue')
ecut_35 = ecut_sample(35)
ecut_35.plot_fit(color='red')
ecut_40 = ecut_sample(40)
ecut_40.plot_fit(color='green')

alat_min_30 = ecut_30.alat_min_en
alat_min_35 = ecut_35.alat_min_en
alat_min_40 = ecut_40.alat_min_en

print(f"alat_min ecut=30 : {alat_min_30}\nalat_min ecut=35 : {alat_min_35}\nalat_min ecut=40 : {alat_min_40}")
plt.xlabel('alat (a.u.)')
plt.ylabel('energy (Ry)')
plt.title('Energy vs lattice parameter')
plt.grid()
plt.legend()
plt.show()