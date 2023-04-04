#!/bin/bash

n_layers=" 3 4 5 6 7 8 9 "

for i in $n_layers
do

python3 generate_points.py $i

FILE=n_layers$i

cat > $FILE.pwi << EOF
&CONTROL
    calculation = 'relax'
    restart_mode = 'from_scratch'
    pseudo_dir = '/home/software/materia/pseudo'
    outdir = '/home/STUDENTI/leonardo.razzai/WORK/Rh_111'
    prefix = '9L'
    disk_io = 'nowf'
    max_seconds = 36000
/
&SYSTEM
    ibrav = 4
    celldm(1) = 5.122776
    celldm(3) = 10.96
    nat = $i
    ntyp = 1
    ecutwfc = 35
    ecutrho = 280
    nspin = 2
    starting_magnetization(1) = 0.01
    occupations = 'smearing'
    smearing = 'gaussian'
    degauss = 0.02
/
&ELECTRONS
    diagonalization = 'david'
    electron_maxstep = 200
    mixing_mode = 'local-TF'
    mixing_beta = 0.40
    conv_thr = 1.0d-6
/

ATOMIC_SPECIES
Rh      102.905    rh_pbe_v1.4.uspp.F.UPF 

ATOMIC_POSITIONS angstrom
EOF

cat points.txt >> $FILE.pwi

cat >> $FILE.pwi << EOF

K_POINTS automatic
9 9 1 1 1 0

EOF

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# running

#cd $SLURM_SUBMIT_DIR
#srun --cpu-bind=core $PW  -input  $FILE.pwi >> $FILE.pwo

done
