#import prepare_proteins
import os

schrodinger = '/data/general_software/schrodinger_2023-1/'

ligand_unprep_dir = '/home/alma/zak/KRAS_LigBuilder_glide/S4_glide/ligands_unprep/'
ligand_prep_dir = '/home/alma/zak/KRAS_LigBuilder_glide/S4_glide/ligands/'

for filename in os.listdir(ligand_unprep_dir):
    if os.path.exists(ligand_unprep_dir + filename):
        path_unprep = ligand_unprep_dir + filename
        path_prep_without_extension = ligand_prep_dir + filename[:-4]
        print('Currently processing file %s' % filename)
        os.system('%s/ligprep -epik -imae %s -omae %s_prep.mae -s 1' % (schrodinger, path_unprep, path_prep_without_extension))
