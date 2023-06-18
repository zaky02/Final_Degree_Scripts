import prepare_proteins
import bsc_calculations
import shutil
import os
import glob

schrodinger = '/home/cactus/Programs/schrodinger2023-1/'

grid_dir = '/home/cactus/old_data/municoy/bscuser/zak/KRAS_LigBuilder_glide/S2_glide/grid'

# prepwizard and ligprep previously
models = prepare_proteins.proteinModels('/home/cactus/old_data/municoy/bscuser/zak/KRAS_LigBuilder_glide/S2_glide/structures')
for model in models:
    print(models.structures[model])

center_atom = {} # Create dictionary to store the atom 3-element tuple for each model
center_atom[model] = ('A', 64, 'CZ')

jobs = models.setUpDockingGrid('/home/cactus/old_data/municoy/bscuser/zak/KRAS_LigBuilder_glide/S2_glide/grid', center_atom) # Set grid calcualtion
bsc_calculations.local.parallel(jobs, cpus=min([40, len(jobs)])) # Write the scripts to run them locally.

os.system('%s/utilities/structconvert -ipdb structures/7RPZ_prep.pdb -omae %s/input_models/7RPZ_prep.mae' % (schrodinger, grid_dir))

with open('/home/cactus/old_data/municoy/bscuser/zak/KRAS_LigBuilder_glide/S2_glide/grid/grid_inputs/7RPZ_prep.in', "a+") as f: # Add constraints to the .in file generated for the grid
    f.write("HBOND_CONSTRAINTS    \"A:ASP:12:OD1(hbond) 164\",")
    f.write("\n")
    f.write("POSIT_CONSTRAINTS    \"hydrophobic_1 -4.260000 3.390000 -24.380000 2.400000\"")

fin = open("/home/cactus/old_data/municoy/bscuser/zak/KRAS_LigBuilder_glide/S2_glide/grid/grid_inputs/7RPZ_prep.in", "rt")
data = fin.read()
data = data.replace('../input_models/7RPZ_prep.mae', '/home/cactus/old_data/municoy/bscuser/zak/KRAS_LigBuilder_glide/S2_glide/grid/input_models/7RPZ_prep.mae')
fin.close()

fin = open("/home/cactus/old_data/municoy/bscuser/zak/KRAS_LigBuilder_glide/S2_glide/grid/grid_inputs/7RPZ_prep.in", "wt")
fin.write(data)
fin.close()

os.system('%s/glide %s/grid_inputs/7RPZ_prep.in -OVERWRITE -HOST localhost -TMPLAUNCHDIR -WAIT' % (schrodinger, grid_dir))

old_dir = '/home/cactus/old_data/municoy/bscuser/zak/KRAS_LigBuilder_glide/S2_glide'
new_dir = '/home/cactus/old_data/municoy/bscuser/zak/KRAS_LigBuilder_glide/S2_glide/grid/output_models/'

pattern = old_dir + '/7RPZ*'
for file in glob.iglob(pattern, recursive=True):
    file_name = os.path.basename(file)
    shutil.move(file, new_dir + file_name)
    print('Moved:', file)
