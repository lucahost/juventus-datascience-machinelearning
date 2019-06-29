from one import EX_GRAPH0
from one import EX_GRAPH1
from one import EX_GRAPH2

from two import generate_complete_graph

from three import compute_in_degrees

from four import in_degree_distribution

import math
import matplotlib
import random
from matplotlib import pylab
from collections import Counter
from urllib.request import urlopen


def make_complete_graph(num_nodes):
    """
    This function takes a number and returns a complete graph with that number of nodes

    """
    complete = {}
    for nodes in range(0, num_nodes):
        lista = list(range(num_nodes))
        lista.remove(nodes)
        complete[nodes] = set(lista)
    return complete


def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph

    Returns a dictionary that models a graph
    """
    graph_file = urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[: -1]

    print("Loaded graph with", len(graph_lines), "nodes")

    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1: -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph


def plot(distribution):

    keys = list(distribution.keys())
    values = list(distribution.values())
    normalize = []
    logkey = []
    soma = float(sum(values))
    for item in list(range(len(values))):
        normalize.append(math.log(values[item]/soma))
    for item in list(range(len(keys))):
        if keys[item] == 0:
            logkey.append((keys[item]))
        else:
            logkey.append(math.log(keys[item]))

    fig = matplotlib.pyplot.figure()
    matplotlib.pyplot.plot(normalize, logkey, 'bo')
    fig.suptitle("Distribution of in degrees in log/log scale")
    matplotlib.pyplot.xlabel("log of in degrees")
    matplotlib.pyplot.ylabel("log of number of nodes")
    matplotlib.pyplot.show()
    return 0


def ER(n, p):

    graph = {}

    for i in range(0, n):
        list = []
        for j in range(0, n):
            a = random.random()
            if a < p:
                list.append(j)
        graph[i] = list

    return graph


def sum_in_degrees(distribution):
    keys = distribution.keys()
    values = distribution.values()
    total = 0
    for i in range(0, len(keys)):
        total = total + keys[i]*values[i]
    return total


class DPATrial:
    """
    Simple class to encapsulate optimized trials for DPA algorithm

    Maintains a list of node numbers with multiple instances of each number.
    The number of instances of each node number are
    in the same proportion as the desired probabilities

    Uses random.choice() to select a node number from this list for each trial.
    """

    def __init__(self, num_nodes):
        """
        Initialize a DPATrial object corresponding to a 
        complete graph with num_nodes nodes

        Note the initial list of node numbers has num_nodes copies of
        each node number
        """
        self._num_nodes = num_nodes
        self._node_numbers = [node for node in range(
            num_nodes) for dummy_idx in range(num_nodes)]

    def run_trial(self, num_nodes):
        """
        Conduct num_node trials using by applying random.choice()
        to the list of node numbers

        Updates the list of node numbers so that the number of instances of
        each node number is in the same ratio as the desired probabilities

        Returns:
        Set of nodes
        """

        # compute the neighbors for the newly-created node
        new_node_neighbors = set()
        for dummy_idx in range(num_nodes):
            new_node_neighbors.add(random.choice(self._node_numbers))

        # update the list of node numbers so that each node number
        # appears in the correct ratio
        self._node_numbers.append(self._num_nodes)
        self._node_numbers.extend(list(new_node_neighbors))

        # update the number of nodes
        self._num_nodes += 1
        return new_node_neighbors

#CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"
#citation_graph = load_graph(CITATION_URL)
#distribution = in_degree_distribution (citation_graph)
# plot(distribution)


m = 13
n = 1000
complete = make_complete_graph(m)
DPA = DPATrial(m)
for i in range(m, n-1):
    complete[i] = DPA.run_trial(i)
    print("run " + repr(i) + " of total " + repr(n))
distribution = in_degree_distribution(complete)
plot(distribution)
