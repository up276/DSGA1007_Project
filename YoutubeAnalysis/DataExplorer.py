'''
Created on Dec 5, 2015

@authors: urjit0209,vec241, mc3784
'''

import sys
import matplotlib.pyplot as plt
import DataPlotter as dataplotter
import time

class DataStatistics():
    features = {"1":"viewCount", "2":"likeCount", "3":"dislikeCount", "4":"favoriteCount","5":"commentCount","6":"dimension", "7":"definition", "8":"caption"}
    Catagory_mapping = {2: 'Autos & Vehicles', 23: 'Comedy' , 27: 'Education', 24: 'Entertainment' , 1: 'Film & Animation', 20: 'Gaming' ,26: 'Howto & Style', 10: 'Music',25: 'News & Politics', 29:'Nonprofits & Activism' ,22:'People & Blogs', 15: 'Pets & Animals' , 28: 'Science & Technology', 17: 'Sports' , 19:'Travel & Events'}
    def __init__(self):
        print "Perform data analysiss..."


    def individual_videocatagory_analysis(self,data,video_id):
            dataframe = data
            #variable_names = ["viewCount", "likeCount", "dislikeCount", "favoriteCount","commentCount","dimension", "definition", "caption","licensedContent"]
            count_features = ["viewCount", "likeCount", "dislikeCount", "favoriteCount","commentCount"]
            #columnNames = dataframe.columns.values
            #print columnNames
            #video_ids = dataframe["video_category_id"].unique()


            #for video_id in video_ids:

            print "\n==============="
            print "Analysis for video catagory = ",video_id
            print "===============\n"
            video_id = int(video_id)
            VideoCatagoryData = dataframe[dataframe["video_category_id"]==video_id]
            VideoCatagory_CountData = VideoCatagoryData[count_features]
            description = VideoCatagoryData.describe()
            correlation = VideoCatagory_CountData.corr(method='pearson', min_periods=1)
            print "description of each feature - "
            print description
            print "correlation within count features - "
            print correlation

            print "\nCount for Binary features :------> \n"
            print "Dimension : 2d(1) , 3d(0)"
            dim=VideoCatagoryData.groupby('dimension')['video_category_id'].count()
            print dim
            print "definition : hd(1) , sd(0)"
            defi=VideoCatagoryData.groupby('definition')['video_category_id'].count()
            print defi
            print "caption : TRUE(1) , FALSE(0)"
            cap=VideoCatagoryData.groupby('caption')['video_category_id'].count()
            print cap
            print "caption : TRUE(1) , FALSE(0)"
            lic=VideoCatagoryData.groupby('licensedContent')['video_category_id'].count()
            print lic

    def printCategories(self):
        """
            Print the list of features in the dataset 
        """
        for key in self.features:
            print key, "-->", self.features[key]


    def printVideoCategories(self):
        for key in self.Catagory_mapping:
            print key, "-->", self.Catagory_mapping[key]


    def individual_feature_analysis(self,data,chosenFeature):
        """
            Compute a group by on the chosenFeature and call featuresBarPlot to plot the result 
        """
        print "chosen feature: ",self.features[chosenFeature]
        featuresMeans = data.groupby(['video_category_id'])[self.features[chosenFeature]].mean()
        featuresNames = [self.Catagory_mapping[x] for x in featuresMeans.index]
        dataplotter.featuresBarPlot(featuresNames,featuresMeans.values)


    def generalAnalysis(self,data,clf):

            dataplotter.plotFeatureImportance(data,clf)

            dataplotter.plotCorrelationMatrix(data)


    def visualizeData(self,data):


        print "\n The data we are using are metadata on YouTube videos..."
        time.sleep(3)
        print "\n The metadata we have on the videos are the following: "
        time.sleep(3)
        for col in data.columns:
            print "\n > " + col
            time.sleep(1.5)
        print "\n We use these data to build a model able to perform prediction on the category to which each video belong..."
        time.sleep(3)
        print "\n The possible categories to which a video can belong are the following (only one category per video): "
        time.sleep(3)
        print "\n > Autos & Vehicles, Comedy, Education, Entertainment, Film & Animation, Gaming, Howto & Style, Music, " \
              "News & Politics, Nonprofits & Activism, People & Blogs, Pets & Animals, Science & Technology, Sports, Travel & Events "
        time.sleep(6)
        print "\n In order to do that, we have a data set of about 240.000 YouTube videos..."
        time.sleep(3)
        print "\n Now here is what the first five rows of our data set look like --> ..."
        time.sleep(3)
        print "\n (You can always go check the full file : YouTubeData/train_sample.csv ...)"
        time.sleep(3)
        print data.head()
        time.sleep(6)






