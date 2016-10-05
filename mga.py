# METAMERIC GENETIC ALGORITHM (MGA)
#
# MODULE:     mga.py
# AUTHOR:     Jinseok Yeom
# VERSION:    0.2
# SINCE:      10/03/2016
#

import numpy as np
import numpy.random as npr

# MGA parameters
NUM_GENERATION = 100 # number of generations
POPULATION_SIZE = 100 # size of genome population
METAVAR_SIZE = 5 # number of design variables in a metavariable
GENOME_LEN_MIN = 2 # minimum number of metavariables in a genome
GENOME_LEN_MAX = 8 # maximum number of metavariables in a genome
RECOMBINATION_RATE = 0.1 # recombination rate
MUTATION_RATE = 0.1 # mutation rate

# Metavar implements a metavariable, which includes its metavariable ID and
# a fixed number of design variables. 
class Metavar(object):
    def __init__(self, mv_id):
        self.mv_id = mv_id 
        self.dv = npr.rand(METAVAR_SIZE)

    def __str__(self):
        return "MV_ID %d: %s" % (self.mv_id, np.array_str(self.dv))

    # calculate dissimilarity with other metavariable.
    def dissimilarity(self, m1):
        diff = 0.0
        for x in range(METAVAR_SIZE):
            # assuming each design variable is already normalized
            diff += abs(self.dv[x] - m1.dv[x])
        return diff / float(METAVAR_SIZE)

    __repr__ = __str__
# end of Metavar

# Genome implements a variable-length genome which includes genome ID,
# random variable length, and a set of metavariables.
class Genome(object):
    def __init__(self, g_id):
        length = npr.randint(GENOME_LEN_MIN, GENOME_LEN_MAX)
        self.g_id = g_id
        self.length = length
        self.genotype = [Metavar(i) for i in range(length)]

    def __str__(self):
        return "G_ID %d:\n%s" % (self.g_id, "\n".join([str(mv) for mv in self.genotype]))

    # design variable mutation 
    def dv_mutate(self):
        
        # to be implemented

        return

    # metavariable insertion/deletion mutation
    def mv_mutate(self):
        
        # to be implemented
    
        return
    
    __repr__ = __str__
# end of Genome

# Metameric Genetic Algorithm
class MGA(object):
    def __init__(self):
        self.best_genome = []
        self.population = [Genome(i) for i in range(POPULATION_SIZE)]

    # NSGA-II based selection
    def select(self):
        
        # to be implemented

        return

    # similar-metavariable recombination
    def sm_recombination(self, p0, p1):
        # initialize subsets
        p0_subset = [[] for i in range(len(p1.genotype))]
        p1_subset = [[] for i in range(len(p0.genotype))]

        # form parent 0's subset
        for mv0 in p0.genotype:
            match_index = 0
            lowest_diss = 1.0
            for index, mv1 in enumerate(p1.genotype):
                diss = mv0.dissimilarity(mv1)
                if diss < lowest_diss:
                    match_index = index
                    lowest_diss = diss
            p0_subset[match_index].append(mv0.mv_id)

        # form parent 1's subset
        for mv1 in p1.genotype:
            match_index = 0
            lowest_diss = 1.0
            for index, mv0 in enumerate(p0.genotype):
                diss = mv1.dissimilarity(mv0)
                if diss < lowest_diss:
                    match_index = index
                    lowest_diss = diss
            p1_subset[match_index].append(mv1.mv_id)

        # temporary
        return [s for s in p0_subset if len(s) > 0], [s for s in p1_subset if len(s) > 0]

# testing function
def test():
    # metavariable test
    print("=== METAVARIABLE TEST ===")
    mv0 = Metavar(0)
    mv1 = Metavar(1)
    print(mv0)
    print(mv1)
    
    # dissimilarity test
    print("=== DISSIMILARITY TEST ===")
    diss0 = mv0.dissimilarity(mv1)
    diss1 = mv1.dissimilarity(mv0)
    print("mv0 dissimilarity with mv1: %f" % diss0)
    print("mv1 dissimilarity with mv0: %f" % diss1)
    assert (diss0 == diss1), "DISSIMILARITY TEST FAILED"

    # genome test
    print("=== GENOME TEST ===")
    g0 = Genome(0)
    g1 = Genome(1)
    print(g0)
    print(g1)

    # recombination test
    print("=== RECOMBINATION TEST ===")
    mga = MGA()
    s0, s1 = mga.sm_recombination(g0, g1)
    print("similar-metavariable recombination between g0 and g1")
    print(s0)
    print(s1)

if __name__ == '__main__':
    test()
