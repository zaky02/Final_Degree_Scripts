import prepare_proteins
import os

dir_path = '/home/alma/zak/KRAS_LigBuilder_glide/'

for directories in os.listdir(dir_path):
    if os.path.exists(dir_path + directories):

        os.system("/home/alma/zak/KRAS_LigBuilder_glide/%s/prep_lig.py" % (directories)) # line to execute the ligand preparation script for all sub pocket dircetories

        os.system("/home/alma/zak/KRAS_LigBuilder_glide/%s/grid_setup.py" % (directories)) # line to execute the grid receptor build and generation script for all sub pocket directories

        os.system("/home/alma/zak/KRAS_LigBuilder_glide/%s/docking_setup.py" % (directories)) # line to execute the glide docking preparation and execution script for all sub pocket directories

