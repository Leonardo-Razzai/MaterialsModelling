#!bin/bash
# Script to set lattice parameter in Rh.pwi

mul_fact=8 # multiplication factor to get ecutrho from ecutwfc
ecutwfc=35
ecutrho=$(($ecutwfc * $mul_fact))
echo "ecutwfc = $ecutwfc, ecutrho = $ecutrho
"
alat=$1 # input string at command line
echo "Set celldm(1) = $alat" in Rh.pwi
# change celldm(1) in Rh.pwi
head -10 Rh.pwi > temp1
echo "    celldm(1) = $alat" > temp2
echo "    nat = 1" >> temp2
echo "    ntyp = 1" >> temp2
echo "    ecutwfc = $ecutwfc" >> temp2
echo "    ecutrho = $ecutrho" >> temp2
tail -22 Rh.pwi > temp3 
cat temp1 temp2 temp3 > Rh.pwi
rm temp*
