'''
Created on Dec 5, 2015

@author: urjit0209,vec241, mc3784
'''
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib import rc
import time
import DataManager


class DataPlotting():
    def __init__(self):
        print "call to class that plot..."

def featuresBarPlot(barNames,barValues):
    plt.bar(range(0,len(barNames)),barValues)
    plt.xticks(range(0,len(barNames)), barNames,rotation='vertical')
    plt.show()


def plotFeatureImportance(data,clf):
    '''
        Plot barchart showing numerical feature importance for determining video categories
        Input : classifier
        Output : barchart showing the importance of features
    '''

    # Keep dataframe with only numerical features
    # numerical_features = [x for x in df.columns if x in ('video_category_id', 'viewCount', 'dislikeCount', '
    # definition', 'dimension', 'favoriteCount', 'commentCount', 'caption', 'licensedCountent')]
    # useful_df = df[numerical_features]

    print "Generating the Feature Importance bar chart...\n"
    time.sleep(3) # delay for 3 seconds

    print "You can now retrieve the Feature Importance bar chart in YoutubeData folder.\n"
    time.sleep(3) # delay for 3 seconds

    # Plot
    predictor_var = ["viewCount", "likeCount", "dislikeCount", "favoriteCount","commentCount", "caption"]
    fig, ax = plt.subplots()
    width=0.7
    ax.bar(np.arange(len(clf.feature_importances_)), clf.feature_importances_, width, color='b')
    ax.set_xticks(np.arange(len(clf.feature_importances_)))
    ax.set_xticklabels(predictor_var,rotation=45)
    #plt.figure(figsize=(15,20))
    plt.title('Numerical Features Importance', fontsize=20)
    ax.set_ylabel('Normalized Entropy Importance')
    name = "../YoutubeData/feature_importance.pdf"
    plt.savefig(name)


def plotCorrelationMatrix(data):
    '''
        Print and plot correlation matrix of the features in the data
        Input : data
        Output : numerical and graphical correlation matrix
    '''

    # Display numerical correlation matrix

    corr = data.corr()
    print "Displaying numerical correlation matrix...\n"
    time.sleep(3) # delay for 3 seconds
    print corr


    # Display numerical correlation matrix

    time.sleep(3) # delay for 3 seconds
    print "\n"
    print "Generating the graphical correlation matrix...\n"
    time.sleep(3) # delay for 3 seconds

    print "You can now retrieve the graphical correlation matrix in YoutubeData folder.\n"
    time.sleep(3) # delay for 3 seconds

    # Plot
    f, ax = plt.subplots(figsize=(11, 9))
    # Generate a custom diverging colormap
    cmap = sns.diverging_palette(220, 10, as_cmap=True)
    # Draw the heatmap with the mask and correct aspect ratio
    sns.heatmap(corr, cmap=cmap,
                square=True, xticklabels=True, yticklabels=True,
                linewidths=.5, cbar_kws={"shrink": .5}, ax=ax)

    plt.title('Corellation Matrix', fontsize=30)
    ax.set_ylabel('Features', fontsize=20)
    ax.set_xlabel('Features', fontsize=20)
    name = "../YoutubeData/correlation_matrix.pdf"
    plt.savefig(name)