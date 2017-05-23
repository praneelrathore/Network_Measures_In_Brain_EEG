import numpy as np
from matplotlib import pyplot as plt
import networkx as nx
import functions as func
import os

#FOR PLOTTING GRAPHS AND MATRICES
emo = ['cheerful','depressing','exciting','fun','happy','hate','joy','love','lovely','melancholy','mellow','sad','senti','sentimental','shock','terrible','very_happy']
for e in emo:
    #Remeber to change male/female accordingly
    
    #When you will first run the file, after executing file7, uncomment [path1 = "Graphs/"+e+"/Male/"]
    #When you will run this file for the second time after executing file9, uncomment [path1 = "Graphs/"+e+"/Male/Combined/"]
    #path1 = "Graphs/"+e+"/Male/Combined/"
    path1 = "Graphs/"+e+"/Male/"
    path2 = "Plots/"+e+"/Male/"

    for infile in os.listdir(path1):
        if not os.path.isdir(path1+infile):
            if not infile.startswith('.'):
                #infile = "Graph_Male_02_fun.net"
                #When you will first run the file, after executing file7, uncomment these two lines and comment the ones below it
                outfile1 = "Plot_graph_"+infile[6:13]+"_"+e+".png"          #[6:13] for males, [6:15] for females
                outfile2 = "Plot_matrix_"+infile[6:13]+"_"+e+".png"         #[6:13] for males, [6:15] for females
                #When you will run this file for the second time after executing file9, uncomment these two lines and comment the above two.
                #outfile1 = "Plot_graph_" + infile[16:20] + "_"+e+".png"  #FOR COMBINED PLOTS   #[16:20] for males, [16:20] for females
                #outfile2 = "Plot_matrix_" + infile[16:20] + "_"+e+".png"  #FOR COMBINED PLOTS  #[16:20] for males, [16:20] for females
                
                
                #Do not consider the commented code below
                '''
                #outfile3 = "Plot_graph_" + infile[6:13] + "_"+e+".png"
                #outfile4 = "Plot_matrix_"+infile[6:13]+"_"+e+".png"
                #outfile3 = "Plot_graph_" + infile[16:20] + "_" + e + ".png"  # FOR COMBINED PLOTS
                #outfile4 = "Plot_matrix_" + infile[16:20] + "_" + e + ".png"  # FOR COMBINED PLOTS
                '''
                
                
                print ('infile', infile)
                print ('outfile1', outfile1)
                print ('outfile2', outfile2)
                G = nx.read_pajek(path1+infile)
                #G = nx.DiGraph(G)
                print len(G.nodes())
                print len(G.edges())
                print G.edges()
                #func.plot_graph(G, path2, outfile1, outfile2, title)
                func.plot_graph_save(G, path2, outfile1, outfile2, outfile2)
                #func.plot_graph_save_undirected(G, path2, outfile3, outfile4, outfile4)
