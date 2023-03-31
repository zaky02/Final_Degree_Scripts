from rdkit import Chem
import rdkit.Chem.Descriptors as Descriptors
import rdkit.Chem.rdMolDescriptors as rDescriptors

mol = Chem.MolFromMol2File("/home/apolo/zak/S3_LigBuilderV3/data/7RPZ_ligand.mol2")

mw = Descriptors.ExactMolWt(mol)
print(mw)

logp = Descriptors.MolLogP(mol)
print(logp)

nhd = Descriptors.NumHDonors(mol)
print(nhd)

nha = Descriptors.NumHAcceptors(mol)
print(nha)

seed = Chem.MolFromMol2File("/home/apolo/zak/S3_LigBuilderV3/data/7RPZ_seed.mol2")

nhd = Descriptors.NumHDonors(seed)
print(nhd)

arom = rDescriptors.CalcNumAromaticRings(seed)
print(arom)

arom = rDescriptors.CalcNumAliphaticRings(seed)
print(arom)
