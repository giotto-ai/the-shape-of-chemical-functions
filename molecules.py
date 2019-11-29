import networkx as nx
from create_clique_complex import CreateCliqueComplex, CreateBoundaryMatrices, CreateLaplacianMatrices
from heat_diffusion import HeatDiffusion
from graph_entropy import GraphEntropy


def mol_to_nx(mol):
    g = nx.Graph()
    for atom in mol.GetAtoms():
        g.add_node(atom.GetIdx(),
        atomic_num=atom.GetAtomicNum(),
        formal_charge=atom.GetFormalCharge(),
        chiral_tag=atom.GetChiralTag(),
        hybridization=atom.GetHybridization(),
        num_explicit_hs=atom.GetNumExplicitHs(),
        is_aromatic=atom.GetIsAromatic())
    for bond in mol.GetBonds():
        g.add_edge(bond.GetBeginAtomIdx(),
                    bond.GetEndAtomIdx(),
                    bond_type=bond.GetBondType())
    return G


def compute_node_edge_entropy(g, i, taus_n, taus_e):
    cd = CreateCliqueComplex(graph=g).create_complex_from_graph()
    lap = CreateLaplacianMatrices().fit().transform(cd, (0, 1))
    mh_n = GraphEntropy().fit().transform(HeatDiffusion().fit(taus_n).transform(lap[0])).T
    mh_e = GraphEntropy().fit().transform(HeatDiffusion().fit(taus_e).transform(lap[1])).T

    if i % 1000 == 0:
        print(i)
    return [mh_n, mh_e]


