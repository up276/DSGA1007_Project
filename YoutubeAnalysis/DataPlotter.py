'''
Created on Dec 5, 2015

@author: urjit0209,vec241, mc3784
'''
import matplotlib.pyplot as plt



class DataPlotting():
    def __init__(self):
        print "call to class that plot..."

def featuresBarPlot(barNames,barValues):
    plt.bar(range(0,len(barNames)),barValues)
    plt.xticks(range(0,len(barNames)), barNames,rotation='vertical')
    plt.show()