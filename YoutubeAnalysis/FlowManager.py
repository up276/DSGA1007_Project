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
import time

class FlowManager():


    def __init__(self):
        """
            Initialize the user interation prompting the instruction to the program
        """
        self.printProgramInfos()

    def InitiateFlow(self):
        self.InitialUserOptions()
        self.InitialUserInputLoop()


    def printProgramInfos(self):
        print "\n================================================"
        print "WELCOME TO THE YOUTUBE VIDEO ANALYSIS PROGRAM"
        print "================================================\n"

    def InitialUserOptions(self):
        print "\nYou are currently in the main menu. Please choose one of the options below\n \
               1) press 1 to visualize the data of the training data set \n \
               2) press 2 to explore the data \n \
               3) press 3 to predict the category of a YouTube video \n \
               4) Enter 'quit' to exit from the program "

    def InitialUserInputLoop(self):
        """
            Create a loop asking the user which action he or she wants to take. The loop is break (and the program ends) whenever the user type quit.
        """
        userInput=""
        try:
            while userInput != "quit":
                userInput = raw_input("\nPlease enter one of the number: ")
                if userInput == "1":
                    self.InitiateDataVisulizer()
                elif userInput == "2":
                    self.InitiateDataExplorer()
                elif userInput == "3":
                    self.InitiateDataSimulator()
                elif userInput == "quit":
                    self.ExitProgram()

        except KeyboardInterrupt:
            print "quitting..."
            sys.exit()


    def InitiateDataExplorer(self):
        self.DataExplorerUserInputLoop()

    def InitiateDataVisulizer(self):
        self.DataVisulizerUserInputLoop()

    def InitiateDataSimulator(self):
        self.DataSimulatorUserInputLoop()


    def printDataVisulizerOptions(self):
        print "\nThis part of the program will explain you what are the main characteristics of our data and will show you the first 5 rows of our dataframe\n \
               1) press 1 to start the Visualization \n \
               4) press 4 to go back to main menu \n \
               2) Enter 'quit' to exit from the program "


    def printDataExploreOptions(self):
        print "\nThis part of the program allows you to explore the data more deeply and perform many different analysis \n \
               1) press 1 for general analysis \n \
               2) press 2 for individual analyisis of each video catagory \n \
               3) press 3 for individual feature analysis \n \
               4) press 4 to go back to main menu \n \
               5) Enter 'quit' to exit from the program "

    def printDataSimulationOptions(self):
        print "\nThis part of the program will allow you to perform Video Category Prediction\n \
               1) press 1 to start the Video Category Prediction \n \
               2) press 4 to go back to main menu \n \
               3) Enter 'quit' to exit from the program "

    def printConfirmDataSimulationOptions(self):
        print "\nPlease be aware it will take time to build the model before you can perform any simulation (about 30 sec for 16 Gb of ram)\n \
               1) press 1 to confirm you want to perform the Video Category Prediction  \n \
               2) press 4 to go back to main menu \n \
               3) Enter 'quit' to exit from the program "

    def printPredictionOptions(self):
        print "\nThe predicting model is ready to operate. Please choose one of the following options\n \
               1) press 1 to perform a prediction \n \
               2) press 4 to go back to main menu \n \
               3) Enter 'quit' to exit from the program "


    def DataVisulizerUserInputLoop(self):
        """
            Create a loop asking the user which action he or she wants to take. The loop is break (and the program ends) whenever the user type quit.
        """
        userInput=""
        try:
            while userInput != "quit":
                self.printDataVisulizerOptions()
                userInput = raw_input("\nPlease provide the input : ")
                if userInput == "1":
                    DataExplorer.visualizeData(DataManager.cleaned_data)
                    self.InitiateFlow()
                elif userInput == "4":
                    self.InitiateFlow()
                elif userInput == "quit":
                    self.ExitProgram()
        except KeyboardInterrupt:
            print "quitting..."
            sys.exit()


    def DataExplorerUserInputLoop(self):
        """
            Create a loop asking the user which action he or she wants to take. The loop is break (and the program ends) whenever the user type quit.
        """
        userInput=""
        try:
            while userInput != "quit":
                self.printDataExploreOptions()
                userInput = raw_input("\nPlease provide the input : ")
                if userInput == "1":
                    DataExplorer.generalAnalysis(DataManager.cleaned_data,
                                                 DataManager.binaryTree(DataManager.cleaned_data))
                elif userInput == "2":
                    DataExplorer.printVideoCategories()
                    userInputVideoCatagory = raw_input("\nPlease provide the number of the Video Catagory : ")
                    DataExplorer.individual_videocatagory_analysis(DataManager.cleaned_data , userInputVideoCatagory)
                elif userInput == "3":
                    DataExplorer.printCategories()
                    userInputfeature = raw_input("\nPlease provide the number of the feature : ")
                    DataExplorer.individual_feature_analysis(DataManager.cleaned_data,userInputfeature)
                elif userInput == "4":
                    self.InitiateFlow()
                elif userInput == "quit":
                    self.ExitProgram()
        except KeyboardInterrupt:
            print "quitting..."
            sys.exit()


    def DataSimulatorUserInputLoop(self):
        """
            Create a loop asking the user which action he or she wants to take. The loop is break (and the program ends) whenever the user type quit.
        """
        userInput=""
        try:
            while userInput != "quit":
                self.printDataSimulationOptions()
                userInput = raw_input("\nPlease provide the input : ")
                if userInput == "1":
                    self.confirmDataSimulatorUserInputLoop()
                elif userInput == "4":
                    self.InitiateFlow()
                elif userInput == "quit":
                    self.ExitProgram()
        except KeyboardInterrupt:
            print "quitting..."
            sys.exit()


    def confirmDataSimulatorUserInputLoop(self):
        """
            Since this option require time to build the model, ask user confirmation he/she wants to pursue
        """
        userInput=""
        try:
            while userInput != "quit":
                self.printConfirmDataSimulationOptions()
                userInput = raw_input("\nPlease provide the input : ")

                if userInput == "1":

                    # Building the model
                    tree, model_count_title, model_count_description, count_vectorizer_title, count_vectorizer_description = Video.generatePredictingModel(DataManager.cleaned_data)

                    # Performing the predictions on the user inputs
                    try:
                        while userInput != "quit":
                            self.printPredictionOptions()
                            userInput = raw_input("\nPlease provide the input : ")
                            if userInput == "1":
                                print "\nNow please go on YoutTube, chose the video of your choice, and enter the title and the description of that video (for more information, please read the README file)"
                                time.sleep(1.5) # delay for 1.5 seconds
                                title = raw_input("\nPlease provide the title of your video : ")
                                description = raw_input("\nPlease provide the description of the video : ")
                                video = Video(title,description)
                                predicted_category_value = video.predictVideoCategory(tree, model_count_title,
                                                                                      model_count_description,
                                                                                      count_vectorizer_title,
                                                                                      count_vectorizer_description)
                                predicted_category_name = DataExplorer.Catagory_mapping[predicted_category_value]
                                print "\nMy prediction is that your video is a {} video".format(predicted_category_name)
                                time.sleep(3) # delay for 3 seconds

                            elif userInput == "4":
                                self.self.InitiateFlow()
                            elif userInput == "quit":
                                self.ExitProgram()
                    except KeyboardInterrupt:
                        print "quitting..."
                        sys.exit()

                elif userInput == "4":
                    self.self.InitiateFlow()
                elif userInput == "quit":
                    self.ExitProgram()
        except KeyboardInterrupt:
            print "quitting..."
            sys.exit()



    '''
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


    '''

    def ExitProgram(self):
        print "Exiting...See you soon :)"
        sys.exit()
        
        

if __name__=="__main__":
    DataManager=DataManager()
    DataExplorer=DataStatistics()
    flowManager=FlowManager()
    flowManager.InitiateFlow()