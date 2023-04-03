import matplotlib.pyplot as plt
from alat_sample import ecut_sample
import pandas as pd

MEDIUM_SIZE = 19
BIGGER_SIZE = 22

plt.rc('font', size=MEDIUM_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=BIGGER_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)    # legend fontsize

base_font = {'family': 'serif',
        'color':  'black',
        'size': MEDIUM_SIZE,
        }

title_font = {'family': 'serif',
        'color':  'black',
        'size': BIGGER_SIZE,
        'weight' : 'normal'
        }

_, ax = plt.subplots(1, 1, figsize=(12, 8))
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

data = {
        'ecut (Ry)': [30, 35, 40],
        'alat (a.u.)': [alat_min_30, alat_min_35, alat_min_40]
}

df = pd.DataFrame(data)
latex_table = (
df.style
.format({'alat (a.u.)': "{:.4f}"})
.to_latex(
        caption='Resulting lattice parametrs corresponding to different cut off energies.',
        label='ecut_table',
        position_float="centering",
        position='h',
        column_format="ccc",
        hrules=True
)
)
with open("../../report/Sections/sec1/ecut_table.tex", "w") as ecut_f:
        ecut_f.write(latex_table)
        
print(latex_table)

ax.grid()
ax.legend(loc='upper left')
plt.savefig('../../report/Figures/ecut_vs_alat.png')
