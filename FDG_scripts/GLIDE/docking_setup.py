import prepare_proteins
import bsc_calculations
import shutil
import os

# prepwizard and ligprep previously
models = prepare_proteins.proteinModels('structures')
for model in models:
    print(models.structures[model])

jobs = models.setUpGlideDocking('docking', 'grid', 'ligands', poses_per_lig=5)
bsc_calculations.local.parallel(jobs, cpus=min([40, len(jobs)]))

schrodinger = '/data/general_software/schrodinger_2023-1/'

docking_dir = '/home/alma/zak/KRAS_LigBuilder_glide/S4_glide/docking/output_models/7RPZ_prep/'

for filename in os.listdir(docking_dir):
    if os.path.exists(docking_dir + filename):
        path = docking_dir + filename
        print('Currently processing file %s' % filename)
        os.system('%s/glide %s -OVERWRITE -adjust -HOST localhost:1 -TMPLAUNCHDIR -WAIT' % (schrodinger, path))
