import numpy as np
from matplotlib import pyplot as plt
import networkx as nx
import functions as func
import os
from datetime import datetime

#FOR COMBINING GRAPHS INTO ONE
#for all emotions
emo = ['cheerful','depressing','exciting','fun','happy','hate','joy','love','lovely','melancholy','mellow','sad','senti','sentimental','shock','terrible','very_happy']
for e in emo:
    #Remember to change male/female accordingly
    path1 = "Graphs/"+e+"/Male/"
    path2 = "Graphs/"+e+"/Male/Combined/"
    infile_or = ""
    A = np.zeros((32,32))
    tstart = datetime.now()

    for infile in os.listdir(path1):
        if not infile.startswith('.'):

            if (infile != 'Combined'):
                print ('infile', infile)
                infile_or = infile
                G = nx.read_pajek(path1+infile)
                A = nx.adjacency_matrix(G).todense()
                break

    print A

    outfile = "Combined_Matrix_" + infile_or[6:13] + "_"+e+".net"   #[6:13] for males, [6:15] for females
    for infile in os.listdir(path1):
        if not infile.startswith('.'):

            if (infile != 'Combined'):
                if (infile != infile_or):
                    print ('infile', infile)
                    G = nx.read_pajek(path1 + infile)
                    A1 = nx.adjacency_matrix(G).todense()
                    for i in range(len(A)):
                        for j in range(len(A)):
                            if (A[(i,j)] == 0.0 and A1[(i,j)] > 0.0):
                                A[(i,j)] = A1[(i,j)]
                            elif (A[(i,j)] > 0.0 and A1[(i,j)] > 0.0):
                                A[(i,j)] = max(A[(i,j)], A1[(i,j)])


    #print A
    #plt.matshow(A, cmap=plt.cm.Blues)
    #plt.show()

    G=nx.from_numpy_matrix(A, create_using=nx.DiGraph())
    nx.write_pajek(G, path2+outfile)
    print 'saved ' + outfile
    print datetime.now()-tstart


