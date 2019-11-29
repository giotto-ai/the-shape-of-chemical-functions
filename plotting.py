#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx


def plot_entropies(entropies, s_list):

    """
    Utility function to plot entropies as a function of time steps
    """

    fig1 = plt.figure(figsize=(7, 4))
    a1 = fig1.add_subplot(111)
    colors = ['blue', 'red', 'black', 'yellow', 'orange', 'green', 'grey', 'brown']

    for i in s_list:
        # plot entropies Vs time
        hs1 = entropies[:, i]
        a1.plot(hs1, label="simplex " + str(i), color=colors[i % len(colors)])

    plt.xticks()
    a1.set_title('Entropy profiles of different simplices')
    a1.legend()

    return


def plot_network_diffusion(G, pos, node_vector=None, edge_vector=None, node_labels=False, edge_labels=False):

    #Find edge labels
    l_e = list(G.edges)
    e = dict((tuple(sorted(l_e[x])), x) for x in range(0, len(l_e)))
    e_labels = { tuple(x) : 'e'+ str(y) for x,y in e.items()}

    #Print diffusions
    fig = plt.figure(figsize=(20,10))

    if (edge_vector is not None):
        colors_edge = np.squeeze(np.asarray(edge_vector))
        nc_e = nx.draw_networkx_edges(G, pos, edge_color=colors_edge,width=3, with_labels=False)
    else:
        nx.draw_networkx_edges(G, pos, edge_color="blue", width=3, with_labels=False)

    if (node_vector is not None):
        colors_node = np.squeeze(np.asarray(node_vector))
        nc = nx.draw_networkx_nodes(G, pos, node_color=colors_node,with_labels=False, node_size=800)
    else:
        nx.draw_networkx_nodes(G, pos, node_color="blue",with_labels=False)

    if (edge_labels):
        nx.draw_networkx_edge_labels(G, pos, e_labels, alpha=1)
    if (node_labels):
        nx.draw_networkx_labels(G, pos)

    plt.axis('off')
    plt.savefig("graphClass.png")
    plt.show()

    return
