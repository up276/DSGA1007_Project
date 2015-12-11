'''
Created on Dec 5, 2015
@author: urjit0209,vec241, mc3784
'''

import sys
from DataPlotter import DataPlotting
from DataExplorer import DataStatistics
from DataSimulator import  Video
import pandas as pd
import numpy as np
from DataManager import DataManager

class FlowManager():


    def __init__(self):
        """
            Initialize the user interation prompting the instruction to the program
        """
        self.printProgramInfos()


    def userInputLoop(self):
        """
            Create a loop asking the user which action he or she wants to take. The loop is break (and the program ends) whenever the user type quit.
        """
        userInput=""
        try:
            while userInput != "quit":
                userInput = raw_input("Please enter one of the number: ")
                if userInput == "1":
                    self.analizeData()
                elif userInput == "2":
                    DataExplorer.InitiateDataExplorer(DataManager.cleaned_data)
                    DataExplorer.userInputLoop()
                elif userInput == "3":
                    self.uploadVideo()
        except KeyboardInterrupt:
            print "quitting..."
            sys.exit()

    def plotResults(self):
        """
            This function could ask to the user which plots he wants to visualize and maybe ask for some parameter for the plot.
            Than it should instantiate the class DataPlotting with these parameters.
        """
        print "Here the program could ask the user which plot to visualize or it could just print all the plots..."
        dataPlotting = DataPlotting()


    def analizeData(self):
        """
            This function could ask to the user which data statistics and infos he wants to visualize and maybe ask for some parameter.
            Than it should instantiate the class DataStatistics with these parameters.
        """
        print "Here the program could ask the user which data statistics and infos to visualize or it could just visualize some default stuff"
        dataStatistics = DataStatistics()


    def uploadVideo(self):
        """
            Ask the user the information about a video, to simulate an upload.
            The function should validate the input and than instantiate the class Video and call its method assignLabel() to predict the video's label
        """

        print "To simulate the upload of a video you have to answer to some question about the videos characteristics. \n \
               Please respect the data's format specified in each questions."
        title       = ""
        description = ""
        try:
            title  = raw_input("Video's title (string): ")
            description  = raw_input("Video's description (string): ")
            published_at = raw_input("Video's upload date (MM-DD-YYYY HH:MM): ")
            viewCount  = raw_input("Video's count (integer): ")
            likeCount = raw_input("Video's likes count (integer): ")
            dislikeCount= raw_input("Video's dislike Count count (integer): ")
            favoriteCount=raw_input("Video's favorite Count count (integer): ")
            commentCount=raw_input("Video's comment Count count (integer): ")
            video = Video(title,description,published_at,viewCount,
                          likeCount,dislikeCount,favoriteCount,commentCount)
            print video.assignLabel()

        except KeyboardInterrupt:
            print "quitting..."
            sys.exit()

    def printProgramInfos(self):
        print "String with a short description of the program and how it works. Than the list of option...\n \
               1) press 1 to visualize the data of the training data set \n \
               2) press 2 to explore the data \n \
               3) press 3 to simulate the upload of a video"

if __name__=="__main__":
    DataManager=DataManager()
    DataExplorer=DataStatistics()
    data = DataManager.cleaned_data
    flowManager=FlowManager()
    flowManager.userInputLoop()


