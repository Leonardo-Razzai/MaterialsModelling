#!/bin/bash

# Create  a file called data_dist.dat with total final energy (E_tot)
# for each distance (dist) of Oxigen from surface

echo Initial height: 
read dist_i
echo Final height:
read dist_f

echo "dist E_tot" > data_dist.dat
E_tot=1
for dist in $(seq $dist_f 0.5 $dist_i)
do
  # E_tot=$(grep -a Final ../diss_at_$dist.pwo | awk '{print $4}')
  echo "$dist $E_tot" >> data_dist.dat
done