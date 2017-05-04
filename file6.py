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
import functools
import pandas as pd
import functions as func
from datetime import datetime
import os
from statsmodels.tsa.vector_ar import var_model
import statsmodels.tsa.stattools as tsa_stats
import json

emo = ['cheerful','depressing','exciting','fun','happy','hate','joy','love','lovely','melancholy','mellow','sad','senti','sentimental','shock','terrible','very_happy']


for e in emo:
    path1 = "/Users/praneelrathore/PycharmProjects/Project_8_sem/data_voxels/" + e + "/Male/"
    #infile = "Male_02_data-slorTransposed.txt"
    file3 = "MNI-BAs-6239-voxels.csv"
    path2 = "Granger_lists/"+e+"/Male/"


    for infile in os.listdir(path1):
        if not infile.startswith('.'):
            outfile = "Output_"+infile[0:7]+"_"+e+".txt"
            print ('infile', infile)
            print ('outfile', outfile)
            tstart = datetime.now()
            data = pd.DataFrame.as_matrix(pd.read_csv(path1+infile, sep="\t", header=None))
            print data.shape
            '''
            data_excel = list(csv.reader(open(file3, 'rb'), delimiter=','))

            fs = 128
            i = 0

            final_list = []
            final_voxel_list = []

            for l in data_excel:
                l.insert(0,i)
                f, Pxx_spec = signal.periodogram(data[i, :], fs, 'flattop', scaling='spectrum')
                l.append(np.sqrt(Pxx_spec.max()))
                i += 1

            data_excel.sort(key=itemgetter(6))
            for col5, g1 in groupby(data_excel, itemgetter(6)):

                g1 = list(g1)
                g1.sort(key=itemgetter(5))

                for col6, g2 in groupby(g1, itemgetter(6)):
                    lst1 = []
                    g2 = list(g2)
                    for g in g2:
                        lst = []
                        lst.append(g[5])
                        lst.append(g[6])
                        lst.append(g[0])
                        lst.append(g[8])
                        lst1.append(lst)
                    final_list.append(lst1)

            for l1 in final_list:
                lst2 = func.maxval(l1,-1)
                final_voxel_list.append(lst2)

            n = len(final_voxel_list)
            print 'final voxel list prepared (grouped)'
            print final_voxel_list
            print datetime.now() - tstart
            tstart = datetime.now()

            mat = np.zeros((n,n))
            ii=0
            test_voxels = []

            for l in final_voxel_list:
                test_voxels.append(l[0])

            for i in test_voxels:
                jj=0
                for j in test_voxels:
                    if (i != j):

                        #y1 = data[i]
                        #y2 = data[j]

                        #mn1 = np.median(y1)
                        #mn2 = np.median(y2)

                        #y1[y1 <= mn1] = 0
                        #y1[y1 > mn1] = 1
                        #y2[y2 <= mn2] = 0
                        #y2[y2 > mn2] = 1

                        #X = [int(x) for x in y1]
                        #Y = [int(x) for x in y2]

                        tstart2 = datetime.now()
                        #val1 = func.SchreiberEntropy(X, Y)
                        val1 = func.grangerCausality(data,i,j)
                        mat[ii][jj] = val1
                        print (val1, datetime.now() - tstart2)
                    jj += 1
                ii += 1

            np.save(path2+outfile, mat)
            print 'saved ' + outfile
            print datetime.now() - tstart
            break
            '''
            relation_list=[]
            for i in range(0,32):

                for j in range(0,32):
                    if i != j:
                        local = []
                        testarray = data[:,[i,j]]
                        model = var_model.VAR(testarray)
                        results = model.fit()
                        lag_order = results.k_ar
                        #coeffs = results.coefs
                        #print results
                        #break
                        pval, stats_val = func.grangerCausality(data,i,j,lag_order)
                        if pval<0.01:
                            local.append(i)
                            local.append(j)
                            local.append(stats_val)
                        if local:
                            relation_list.append(local)

            with open(path2+outfile,'w') as myfile:
                json.dump(relation_list,myfile)
            myfile.close()




