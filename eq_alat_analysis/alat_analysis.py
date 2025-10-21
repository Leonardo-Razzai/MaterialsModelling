import matplotlib.pyplot as plt
from alat_sample import ecut_sample
import pandas as pd
bohr_to_A = 0.529177249
SMALL_SIZE = 20
MEDIUM_SIZE = 22
BIGGER_SIZE = 25

plt.rc('font', size=MEDIUM_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=BIGGER_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)    # legend fontsize

base_font = {'family': 'serif',
        'color':  'black',
        'size': MEDIUM_SIZE,
        }

title_font = {'family': 'serif',
        'color':  'black',
        'size': BIGGER_SIZE,
        'weight' : 'bold'
        }

_, ax = plt.subplots(1, 1, figsize=(11, 10))
ax.set_xlabel(r'lat. param. ($\AA$)', fontdict=base_font)
ax.set_ylabel('energy (Ry) + 171 Ry', fontdict=base_font)
ax.set_ylim(-0.21,-0.05)
ax.set_title('Energy vs lattice parameter',fontdict=title_font)

ecut_30 = ecut_sample(30)
ecut_30.plot_fit(ax, color='blue')
ecut_35 = ecut_sample(35)
ecut_35.plot_fit(ax, color='red')
ecut_40 = ecut_sample(40)
ecut_40.plot_fit(ax, color='green')

alat_min_30 = ecut_30.alat_min_en * bohr_to_A
alat_min_35 = ecut_35.alat_min_en * bohr_to_A
alat_min_40 = ecut_40.alat_min_en * bohr_to_A

print(f"alat_min ecut=30 : {alat_min_30}\nalat_min ecut=35 : {alat_min_35}\nalat_min ecut=40 : {alat_min_40}")
rel_diff = (alat_min_40 - alat_min_35) / alat_min_40
print(f'Relative difference between ecut 35 and 40 is : {rel_diff*100:.4f} %')

data = {
        'ecut (Ry)': [30, 35, 40],
        'lat. param. (\AA)': [alat_min_30, alat_min_35, alat_min_40]
}

df = pd.DataFrame(data)
latex_table = (
df.style.hide(axis='index')
.format({'lat. param. (\AA)': "{:.4f}"})
.to_latex(
        caption='Resulting lattice parametrs corresponding to different cut off energies.',
        label='ecut_table',
        position_float="centering",
        position='h',
        column_format="cc",
        hrules=True
)
)
with open("../../report/Sections/bulk/ecut_table.tex", "w") as ecut_f:
        ecut_f.write(latex_table)
        
# print(latex_table)
print(f'Minimum energy at ecut = 35 is {ecut_35.min_energy:.5f} Ry')
ax.grid()
ax.legend(loc='upper left')
plt.savefig('../../report/Figures/ecut_vs_alat.png')
plt.show()
