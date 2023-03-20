#!bin/bash
# Grep all the total energies and put to murn.in

E=$1

grep ! Rh*.pwo > temp 
awk '{print $5, $6}' temp > temp1
head -5 murn_30.in > murn_$E.in
paste -d" " alat_used.dat temp1 >> murn_$E.in
rm temp*

murn_FHI.x < murn_$E.in > murn_$E.out

tail -500 murn_$E.out > temp
echo 'alat(a.u.) energy(Ry)' > murn_$E.dat
awk '{print $1, $2}' temp >> murn_$E.dat
rm temp
