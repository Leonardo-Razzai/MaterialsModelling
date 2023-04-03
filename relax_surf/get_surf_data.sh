#!bin/bash
# This script is meant to automate the process of:
# - grep all the total energies from n_layers*.pwo
# - write data to be analyzed with n_layers and corresponding energies (Ry)
#   to file en_vs_kpoints.dat

# grep from .pwo 
grep ! n_layers*.pwo > temp 
awk '{print $5}' temp > temp1
echo 'n_layers energy(Ry)' > en_vs_nlayers.dat

paste -d" " n_layers_used.dat temp1 >> en_vs_nlayers.dat
rm temp*
