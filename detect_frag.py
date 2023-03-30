from MolecularAnalysis import mollib
from rdkit import Chem

molecules_DB = mollib.MolDB(sdfDB = '/home/apolo/zak/S3_LigBuilderV3/unique_molecules/results/unique_ligand_2_filter.sdf', verbose = False)

fragment_DB = mollib.MolDB(sdfDB = '/home/apolo/zak/S3_LigBuilderV3/data/S3_joinfrags_uniq_DB.sdf', verbose = False)

seed = Chem.MolFromMol2File('/home/apolo/zak/S3_LigBuilderV3/unique_molecules/data/7RPZ_seed.mol2', removeHs = True)
#file = open("test_seed.mol", "w+")
#file.write(Chem.MolToMolBlock(seed))
#file.close()

file_out = open("unique_ligand_2_filter_fragments.csv", "w")
file_out.write("ligbuilder_molecules;fragment\n")

for i,molecule in enumerate(molecules_DB.mols):
    
    name_molec = molecule.mol.GetProp("_Name")
    #molecule.write_mol('test.mol')
    
    frag_molec = Chem.ReplaceCore(molecule.mol, seed)
    atoms_molec = frag_molec.GetNumAtoms()
    #file = open("test_frag_molec.mol", "w+")
    #file.write(Chem.MolToMolBlock(frag_molec))
    #file.close()
    
    Chem.SanitizeMol(frag_molec)
    frag_molec = mollib.Mol(mol2 = frag_molec)

    aux=False
    frags = []
    for frag in fragment_DB.mols:
        atoms_frag = frag.mol.GetNumAtoms()
        
        if atoms_frag != atoms_molec:
            continue
        
        sim = mollib.get_MolSimilarity(frag_molec, frag, fingerprint = 'Morgan2')
        if sim == 1 and not aux:
            name_frag = frag.mol.GetProp("_Name")
            file_out.write("%s;%s\n"%(name_molec, name_frag))
            aux = True
            frags.append(frag)
        
        elif sim == 1 and aux:
            frags.append(frag)
            
            for j,frag in enumerate(frags):
                frag.write_mol('frag%d.mol'%j)
            
            raise ValueError('Two frags with sim = 1')

    molecule.mol.SetProp("original_fragment", name_frag)

molecules_DB.save_tosdf('/home/apolo/zak/S3_LigBuilderV3/unique_molecules/results/orignal_frag_molecule_DB.sdf')
