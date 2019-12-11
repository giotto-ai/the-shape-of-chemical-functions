#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx


def plot_entropies(entropies, s_list):

    """
    Utility function to plot entropies as a function of time steps
    """

    colors = ['blue', 'red', 'black', 'yellow', 'orange', 'green', 'grey',
              'brown']

    for i in s_list:
        # plot entropies Vs temporal indexes
        hs1 = entropies[:, i]
        _ = plt.plot(hs1, label="clique " + str(i), color=colors[i % len(colors)])

    plt.xticks()
    plt.title('Entropy profiles of different cliques')
    plt.legend()

    return


def plot_network_diffusion(G, pos, node_vector=None, edge_vector=None,
                           node_labels=False, edge_labels=False):

    # Find edge labels
    l_e = list(G.edges)
    e = dict((tuple(sorted(l_e[x])), x) for x in range(0, len(l_e)))
    e_labels = {tuple(x): 'e' + str(y) for x, y in e.items()}

    if edge_vector is not None:
        colors_edge = np.squeeze(np.asarray(edge_vector))
        _ = nx.draw_networkx_edges(G, pos, edge_color=colors_edge,
                                   width=3, with_labels=False)
    else:
        _ = nx.draw_networkx_edges(G, pos, edge_color="gray",
                                   width=2, with_labels=False)

    if node_vector is not None:
        colors_node = np.squeeze(np.asarray(node_vector))
        _ = nx.draw_networkx_nodes(G, pos, node_color=colors_node,
                                   with_labels=False, node_size=500)
    else:
        _ = nx.draw_networkx_nodes(G, pos, node_color="blue",
                                   with_labels=False, node_size=500)

    if edge_labels:
        _ = nx.draw_networkx_edge_labels(G, pos, e_labels, alpha=1)
    if node_labels:
        _ = nx.draw_networkx_labels(G, pos)

    return 
