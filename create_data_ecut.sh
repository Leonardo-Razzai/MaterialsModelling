#!bin/bash
# This script is used to:
# - Get cut off energy <E> from command line
# - use data present in  matching murn_<E>.in and murn_<E>.out
# - save experimental data present in .in to a .dat file
# - save fitted data present in .out to a .dat file
# - these two files are better to be moved to a folder named with the matching ecut

echo Insert ecut: 
read E

# write data with fitted energy(Ry) and alat(a.u.)
tail -500 murn_$E.out > temp
echo 'alat(a.u.) energy(Ry)' > en_vs_alat_fit_$E.dat
awk '{print $3, $2}' temp >> en_vs_alat_fit_$E.dat
rm temp
# write experimental data
echo 'alat(a.u.) energy(Ry)' > en_vs_alat_exp_$E.dat
tail -7 murn_$E.in >> en_vs_alat_exp_$E.dat
