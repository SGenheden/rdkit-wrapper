from rdkit import Chem


class Molecule:
    def __init__(self, smiles):
        self.smiles = smiles
        self.rd_mol = Chem.MolFromSmiles(smiles)

    @property
    def inchi_key(self):
        return Chem.MolToInchiKey(self.rd_mol)
