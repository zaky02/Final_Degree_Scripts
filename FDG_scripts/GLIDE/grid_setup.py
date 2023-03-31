import prepare_proteins
import bsc_calculations
import shutil
import os

schrodinger = '/data/general_software/schrodinger_2023-1/'

grid_dir = '/home/alma/zak/KRAS_LigBuilder_glide/S4_glide/grid/'

# prepwizard and ligprep previously
models = prepare_proteins.proteinModels('structures')
for model in models:
    print(models.structures[model])

center_atom = {} # Create dictionary to store the atom 3-element tuple for each model
center_atom[model] = ('A', 64, 'CZ')

jobs = models.setUpDockingGrid('grid', center_atom) # Set grid calcualtion
bsc_calculations.local.parallel(jobs, cpus=min([40, len(jobs)])) # Write the scripts to run them locally.

os.system('%s/utilities/structconvert -ipdb structures/7RPZ_prep.pdb -omae %s/input_models/7RPZ_prep.mae' % (schrodinger, grid_dir))

with open('/home/alma/zak/KRAS_LigBuilder_glide/S4_glide/grid/grid_inputs/7RPZ_pred.in', "a+") as file_object: # Add constraibts to the .in file generated for the grid
    file_object.write("\n")
    file_object.write("HBOND_CONSTRAINTS    \"A:ASP:12:OD1(hbond) 164\",")
    file_object.write("\n")
    file_object.write("POSIT_CONSTRAINTS   \"hydrophobic_1 -4.260000 3.390000 -24.380000 2.400000\"")

os.system('%s/glide %s/grid_inputs/7RPZ_pred.in -OVERWRITE -HOST localhost -TMPLAUNCHDIR -WAIT' % (schrodinger, grid_dir))
