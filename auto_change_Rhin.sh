#!bin/bash
# Script used to automate the process of
# - changing value of lattice parameter (alat) in Rh.pwi
# - running jobscript on it
# - save result to Rh*.pwo with correct name to match alat value

mul_fact=8 # multiplication factor to get ecutrho from ecutwfc
ecutrho=$(($ecutwfc * $mul_fact))
echo "ecutwfc = $ecutwfc, ecutrho = $ecutrho
"
dec_alat=3 # decimal part of lattice parameter, integer one is 7

# increment decimal part from dec_alat-3 to dec_alat+3
# for each value do
for i in {-3..3..1}
do
  inc_alat=$(($i + $dec_alat))
  echo "Set celldm(1) = 7.$inc_alat" in Rh.pwi
  # change celldm(1) in Rh.pwi
  head -10 Rh.pwi > temp1
  echo "    celldm(1) = 7.$inc_alat" > temp2
  echo "    nat = 1" >> temp2
  echo "    ntyp = 1" >> temp2
  echo "    ecutwfc = $ecutwfc" >> temp2
  echo "    ecutrho = $ecutrho" >> temp2
  tail -22 Rh.pwi > temp3 
  cat temp1 temp2 temp3 > Rh.pwi
  rm temp*
  echo "Executing joscript on Rh.pwi"
  # execute jobscript on this new Rh.pwi and put result to Rh*.pwo
  # sbatch jobscript Rh > Rh7.$inc_alat.pwo
  echo "Saved result to Rh_7.$inc_alat.pwo
  " 
done

