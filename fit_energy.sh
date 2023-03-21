#!bin/bash
# This script is meant to automate the process of:
# - grep all the total energies from Rh*.pwo
# - put to murn.in with used lat. params. found in alat_used.dat
# - fit murn.in by Murnagham fit
# - write murn.dat with fitted energy(Ry) and alat(a.u.)

# NOTE:  
# 1) murn.in is saved murn_<ecutwfc>.in, where ecutwfc is the cut off energy set in the Rh.pwi file
# 2) requires murn_30.in to exist in the folder
E=$1

# grep from .pwo and write to murn.in 
grep ! Rh*.pwo > temp 
awk '{print $5, $6}' temp > temp1
head -5 murn_30.in > murn_$E.in
paste -d" " alat_used.dat temp1 >> murn_$E.in
rm temp*

# fit data in murn.in and put result to murn.out
murn_FHI.x < murn_$E.in > murn_$E.out

# write murn.dat with fitted energy(Ry) and alat(a.u.)
tail -500 murn_$E.out > temp
echo 'alat(a.u.) energy(Ry)' > murn_$E.dat
awk '{print $1, $2}' temp >> murn_$E.dat
rm temp
