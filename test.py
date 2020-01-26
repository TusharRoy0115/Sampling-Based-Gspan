from __future__ import print_function
import os, sys
import numpy as np
import random
from random import seed
from random import sample
from algorithms import g_span as gSpan
from algorithms import load_graphs
from sklearn.metrics import confusion_matrix 
from sklearn.metrics import accuracy_score 
from sklearn.metrics import classification_report
import time
start_time = time.time()
filepath = os.path.dirname(os.path.abspath(__file__))

def main(filename='data/Compound_422.txt', min_sup=300):
    filename = os.path.join(filepath, filename)
    graphs1 = load_graphs(filename)
    extensions = []
    print("original frequent pattern:")
    gSpan([], graphs1, min_sup=min_sup, extensions=extensions)
    for i, ext in enumerate(extensions):
        print('Pattern %d' % (i+1))
        for _c in ext:
            print(_c)
        print('')
        print("--- %s seconds ---" % (time.time() - start_time))
    extensions1=extensions
    print("original frequent pattern list:")
    print(extensions1)
    n = len(graphs1)
    print("total number of graph:")
    print(n)
    x=int(input('what percentage want to take:'))
    p=round((x/100)*n)
    print("graph size now is :")
    print(p)
    graphs = random.sample(graphs1, p)
    #print(graphs)
    #b=len(graphs)
    #print(b)
    extensions = []
    print("percentwise frequent pattern:")
    gSpan([], graphs, min_sup=175, extensions=extensions)
    for i, ext in enumerate(extensions):
        print('Pattern %d' % (i+1))
        for _c in ext:
            print(_c)
        print('')
    print("percentwise frequent pattern list:")
    
    print(extensions)
    l2=len(extensions)
    '''results = confusion_matrix(extensions1, extensions) 
    print ('Confusion Matrix :')
    print(results) 
    print ('Accuracy Score :',accuracy_score(extensions1, extensions) )
    print ('Report : ')
    print (classification_report(extensions1, extensions))'''
    tp1 = []
    fp1 = []
    
   
    for list in extensions:
        if list in extensions1:
            tp1.append(list)
    #print("differences")
    #print(differences)
    tp=len(tp1)
    #print("tp :",tp)
    l1=len(extensions1)
    #print("length of frqnt pattern:")
    #print(l1)
    for list in extensions:
        if list not in extensions1:
            fp1.append(list)
    fp=len(fp1)
   # print("fp :" ,fp)
    fn=l1-tp
    #print("fn :", fn)
    accuracy=(tp/l1)*100
    print("accuracy:",accuracy)
    prcn=tp/(fp+tp)
    print("precission",prcn)
    recall=tp/(tp+fn)
    print("recall",recall)
    jc=(tp/(l1+l2))*100
    print("jaccard coefficient",jc)
    f1score=2*((prcn*recall)/(prcn+recall))
    print("F1Score:" , f1score)
    
    

if __name__ == '__main__':
    if ('--help' in sys.argv) or ('-h' in sys.argv):
        print("")
        print("Finds possible frequent and canonical extensions of C in D, using")
        print("min_sup as lowest allowed support value.")
        print("Usage: %s FILENAME minsup" % (sys.argv[0]))
        print("")
        print("FILENAME: Relative path of graph data file.")
        print("minsup:   Minimum support value.")
    else:
        kwargs = {}
        if len(sys.argv) > 1:
            kwargs['filename'] = sys.argv[1]
        if len(sys.argv) > 2:
            kwargs['min_sup'] = sys.argv[2]
        if len(sys.argv) > 3:
            sys.exit("Not correct arguments provided. Use %s -h for more information" % (sys.argv[0]))
        main(**kwargs)



