#!bin/bash
# This script is meant to automate the process of:
# - grep all the total energies from k_points*.pwo
# - write data to be analyzed with k_points and corresponding energies (Ry)
#   to file en_vs_kpoints.dat

echo first k_point:
read start_k
echo last k_point:
read last_k
# grep from .pwo 
grep ! k_points*.pwo > temp 
awk '{print $5}' temp > temp1
echo 'k_points energy(Ry)' > en_vs_kpoints.dat

rm k_points_used.dat
for (( i=$start_k; i<=$last_k; i++))
do
	echo $i >> k_points_used.dat
	echo $i
done

paste -d" " k_points_used.dat temp1 >> en_vs_kpoints.dat
rm temp*
