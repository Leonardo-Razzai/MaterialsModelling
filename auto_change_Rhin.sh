#!bin/bash
# Script used to automate the process of
# - changing value of lattice parameter (alat) in Rh.pwi
# - running jobscript on it
# - save result to Rh*.pwo with correct name to match alat value

mul_fact=8 # multiplication factor to get ecutrho from ecutwfc
echo Insert cut off energy : 
read ecutwfc
ecutrho=$(($ecutwfc * $mul_fact))

echo Insert lattice parameter :
read alat

echo "Set values: 
ecutwfc = $ecutwfc, 
ecutrho = $ecutrho,
celldm(1) = $alat
"
int_alat=${alat:0:1}
dec_alat=${alat:2:1}

# increment decimal part from dec_alat-3 to dec_alat+3
# for each value do
for i in {-3..3..1}
do
  inc_alat=$(($i + $dec_alat))
  new_alat="$int_alat.$inc_alat"
  # change celldm(1) in Rh.pwi
  bash set_alat.sh $ecutwfc $new_alat
  echo "Executing jobscript_change_alat on Rh.pwi"
  # execute jobscript on this new Rh.pwi and put result to Rh*.pwo
  # sbatch jobscript_change_alat Rh _$alat
  echo "Saved result to Rh_$new_alat.pwo
  " 
done

