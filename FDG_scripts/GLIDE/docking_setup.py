import prepare_proteins
import bsc_calculations
import shutil
import os
import glob

# prepwizard and ligprep previously
models = prepare_proteins.proteinModels('/home/cactus/old_data/municoy/bscuser/zak/KRAS_LigBuilder_glide/S2_glide/structures')
for model in models:
    print(models.structures[model])

jobs = models.setUpGlideDocking('/home/cactus/old_data/municoy/bscuser/zak/KRAS_LigBuilder_glide/S2_glide/docking', '/home/cactus/old_data/municoy/bscuser/zak/KRAS_LigBuilder_glide/S2_glide/grid', '/home/cactus/old_data/municoy/bscuser/zak/KRAS_LigBuilder_glide/S2_glide/ligands', poses_per_lig=5)
bsc_calculations.local.parallel(jobs, cpus=min([40, len(jobs)]))

schrodinger = '/home/cactus/Programs/schrodinger2023-1/'

docking_dir = '/home/cactus/old_data/municoy/bscuser/zak/KRAS_LigBuilder_glide/S2_glide/docking/output_models/7RPZ_prep/'

pattern = docking_dir + '*.in'
for filepath in glob.iglob(pattern, recursive=True):
    with open(filepath) as file:
        s = file.read()
    s = s.replace('../../../', '')
    s1 = s.replace('GRID_PATH/7RPZ_prep.zip', '/home/cactus/old_data/municoy/bscuser/zak/KRAS_LigBuilder_glide/S2_glide/grid/output_models/7RPZ_prep.zip')
    s2 = s1.replace('PRECISION SP', 'PRECISION XP')

    with open(filepath, "w") as file:
        file.write(s2)
        file.write('\n')
        file.write('[CONSTRAINT_GROUP:1]')
        file.write('\n')
        file.write("\tUSE_CONS    A:ASP:12:OD1(hbond):1,")
        file.write("\n")
        file.write("\tNREQUIRED_CONS ALL")
        file.write('\n')
        file.write('\n')
        file.write('[FEATURE:1]')
        file.write('\n')
        file.write('\tPATTERN1   \"[#1][#7] 1 include\"')
        file.write('\n')
        file.write('\tPATTERN2   \"[#1][S;X2] 1 include\"')
        file.write('\n')
        file.write('\tPATTERN3   \"[#1][O-] 1 include\"')
        file.write('\n')
        file.write('\tPATTERN4   \"[#1][O;X2] 1 include\"')
        file.close()

for filename in os.listdir(docking_dir):
    if os.path.exists(docking_dir + filename):
        path = docking_dir + filename
        print('Currently processing file %s' % filename)
        os.system('%s/glide %s -OVERWRITE -adjust -HOST localhost:1 -TMPLAUNCHDIR' % (schrodinger, path))
