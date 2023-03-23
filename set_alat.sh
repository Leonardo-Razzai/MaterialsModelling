#!bin/bash
# Script to set lattice parameter in Rh.pwi

mul_fact=8 # multiplication factor to get ecutrho from ecutwfc
ecutwfc=$1 # first input at command line
ecutrho=$(($ecutwfc * $mul_fact))

alat=$2 # input string at command line
# change celldm(1) in Rh.pwi
head -10 Rh.pwi > temp1
echo "    celldm(1) = $alat" > temp2
echo "    nat = 1" >> temp2
echo "    ntyp = 1" >> temp2
echo "    ecutwfc = $ecutwfc" >> temp2
echo "    ecutrho = $ecutrho" >> temp2
tail -22 Rh.pwi > temp3 
cat temp1 temp2 temp3 > Rh_$alat.pwi
rm temp*
