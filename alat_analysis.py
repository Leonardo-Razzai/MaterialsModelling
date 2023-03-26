import matplotlib.pyplot as plt
from alat_sample import ecut_sample

base_font = {'family': 'serif',
        'color':  'black',
        'size': 12,
        }

title_font = {'family': 'serif',
        'color':  'black',
        'size': 19,
        'weight' : 'normal'
        }

_, ax = plt.subplots(1, 1)
ax.set_xlabel('alat (a.u.)', fontdict=base_font)
ax.set_ylabel('energy (Ry)', fontdict=base_font)
ax.set_ylim(-171.21,-171.09)
ax.set_title('Energy vs lattice parameter',fontdict=title_font)

ecut_30 = ecut_sample(30)
ecut_30.plot_fit(ax, color='blue')
ecut_35 = ecut_sample(35)
ecut_35.plot_fit(ax, color='red')
ecut_40 = ecut_sample(40)
ecut_40.plot_fit(ax, color='green')

alat_min_30 = ecut_30.alat_min_en
alat_min_35 = ecut_35.alat_min_en
alat_min_40 = ecut_40.alat_min_en

print(f"alat_min ecut=30 : {alat_min_30}\nalat_min ecut=35 : {alat_min_35}\nalat_min ecut=40 : {alat_min_40}")
rel_diff = (alat_min_40 - alat_min_35) / alat_min_40
print(f'Relative difference between ecut 35 and 40 is : {rel_diff*100:.4f} %')

ax.grid()
ax.legend(loc='upper left')
plt.show()