#This file will read the granger causality data, and will compute graphs from it, saving it in direcory graphs.
from scipy import signal
import pandas as pd
import numpy as np
import csv
from itertools import groupby
from operator import itemgetter
import math
from matplotlib import pyplot as plt
from scipy import signal
import cPickle
import networkx as nx
import json
import functools
import pandas as pd
import functions as func
from datetime import datetime
import os

#for all the emotions
emo = ['cheerful','depressing','exciting','fun','happy','hate','joy','love','lovely','melancholy','mellow','sad','senti','sentimental','shock','terrible','very_happy']

for e in emo:
    #change male/female accordingly
    path1 = "Granger_lists/"+e+"/Male/"
    path2 = "Graphs/" + e + "/Male/"
    thres = 0.01


    for infile in os.listdir(path1):
        #[7:14] for males, [7:16] for females.
        outfile = "Graph_"+infile[7:14]+"_"+e+".net"
        print ('infile', infile)
        print ('outfile', outfile)
        tstart = datetime.now()

        #mat = np.load(path1+infile)
        lst=[]
        with open(path1+infile,'r') as myfile:
            lst= json.load(myfile)
        graph_list=[]
        for l in lst:
            #for ll in l:
            graph_list.append(l)

        #print graph_list

        G = nx.DiGraph()
        G.add_weighted_edges_from(graph_list)
        #edges = []
        '''
        for i in range(len(mat)):
            for j in range(len(mat)):
                if (mat[i][j] > 0.0 and mat[i][j] < thres and i != j):
                    edges.append((i, j, mat[i][j]))
        '''

        print ('no. of edges', len(G.edges()))#len(edges))
        #G.add_weighted_edges_from(edges)

        nx.write_pajek(G, path2+outfile)
        print 'saved ' + outfile
        print datetime.now()-tstart

