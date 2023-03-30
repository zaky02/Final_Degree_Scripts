import sys
#sys.path.append("MolecularAnalysis")
#import mollib
from MolecularAnalysis import mollib

#ligand1DB = mollib.MolDB(sdfDB = '/home/apolo/zak/S3_LigBuilderV3/unique_molecules/data/zero_gen_DB.sdf')
#ligand1DB.filter_similarity(simthreshold=1,fingerprint='Morgan4')
#ligand1DB.save_MolDB_sdf(output='/home/apolo/zak/S3_LigBuilderV3/unique_molecules/results/unique_zero_gen_DB.sdf')

'''
filter1DB = mollib.MolDB(sdfDB = '/home/apolo/zak/S3_LigBuilderV3/unique_molecules/results/unique_ligand_filter_1DB.sdf', verbose = False)
zero1DB = mollib.MolDB(sdfDB = '/home/apolo/zak/S3_LigBuilderV3/unique_molecules/results/unique_zero_gen_DB.sdf', verbose = False)

filter1DB.filter_similarity(simthreshold=1,fingerprint='Morgan4')
zero1DB.filter_similarity(simthreshold=1,fingerprint='Morgan4')

print(f"gen1size {filter1DB.size} \n gen0size {zero1DB.size}")

joined_DB = mollib.join_MolDBs([filter1DB, zero1DB])
print(f"join1size {joined_DB.size}")

joined_DB.filter_similarity(simthreshold=1,fingerprint='Morgan4')
print(f"join1size {joined_DB.size}")

joined_DB.save_MolDB_sdf(output='/home/apolo/zak/S3_LigBuilderV3/unique_molecules/results/joined_DB.sdf')
'''


ligand1DB = mollib.MolDB(sdfDB = '/home/apolo/zak/S3_LigBuilderV3/unique_molecules/data/output_S3.sdf')
ligand1DB.filter_similarity(simthreshold=1,fingerprint='Morgan4')
ligand1DB.save_tosdf(output='/home/apolo/zak/S3_LigBuilderV3/unique_molecules/results/unique_output_S3.sdf')

#grep "RDKit" filename | wc

