import numpy as np
import networkx as nx
from giotto.graphs.create_clique_complex import CreateLaplacianMatrices, \
    CreateCliqueComplex
from giotto.graphs.heat_diffusion import HeatDiffusion
from giotto.graphs.graph_entropy import GraphEntropy


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
    return g


def compute_node_edge_entropy(g, i, taus_n, taus_e):
    cd = CreateCliqueComplex(graph=g).create_complex_from_graph()
    lap = CreateLaplacianMatrices().fit_transform(cd, (0, 1))
    n_diff = HeatDiffusion().fit_transform(lap[0], taus_n)
    e_diff = HeatDiffusion().fit_transform(lap[1], taus_e)
    mh_n = GraphEntropy().fit_transform(n_diff).T
    mh_e = GraphEntropy().fit_transform(e_diff).T

    if i % 10000 == 0:
        print("Atoms and Bonds of {} molecules have been embedded...".
              format(i))

    return [mh_n, mh_e]


def bonds_type_to_edge(g_mol):
    for i, g in enumerate(g_mol):
        d_e = dict()
        for e in g.edges():
            b = int(g.get_edge_data(e[0], e[1])['bond_type'])
            d_e[e] = np.zeros(4)
            if b == 12:
                d_e[e][3] = 1
            else:
                d_e[e][b-1] = 1
        nx.set_edge_attributes(g, name='bonds_one_hot', values=d_e)


def bonds_type(g_mol):
    for g in g_mol:
        d_n = dict()
        for n in g.nodes():
            d_n[n] = np.zeros(4)

            for i in g.neighbors(n):
                # encoding type
                edge_type = int(g.get_edge_data(n, i)['bond_type'])
                if edge_type == 12:
                    d_n[n][3] += 1
                else:
                    d_n[n][edge_type - 1] += 1
        nx.set_node_attributes(g, name='bonds_one_hot', values=d_n)


def graph_to_points(g_mol, n):
    j = 0
    d = dict()
    for i in range(len(g_mol)):
        if n == 0:
            d[i] = np.arange(j, j + g_mol[i].number_of_nodes())
            j += g_mol[i].number_of_nodes()
        else:
            d[i] = np.arange(j, j + g_mol[i].number_of_edges())
            j += g_mol[i].number_of_edges()

    return d
