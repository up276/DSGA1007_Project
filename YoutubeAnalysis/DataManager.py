import pandas as pd
import numpy as np


class DataManager:


    def __init__(self):
        """
            Initialize the user interation prompting the instruction to the program
        """

        raw_data = self.load_data()
        self.cleaned_data = self.clean_data(raw_data)
        #basic_analysis(cleaned_data)
        #binary_tree_analysis(cleaned_data)  #For numeric/catagorical data only
        #self.cleaned_data = self.remove_irrelavent_features(cleaned_data)


    def load_data(self):
        dataframe = pd.read_csv('../YouTubeData/train_sample.csv')
        df_reindex = dataframe.reindex(np.random.permutation(dataframe.index))
        return df_reindex

    def clean_data(self,data):
        '''
        remove unwanted colums, convert catagorical data into numeric data
        dimension : 2d -> 1 , 3d -> 0
        definition :: hd -> 1 , sd -> 0
        caption : True -> 1 , False -> 0
        licensedContent : True -> 1 , False -> 0
        '''
        data['dimension'] = (data['dimension'] == '2d')*1
        data['definition'] = (data['definition'] == 'hd')*1
        data['caption'] = (data['caption'])*1
        data['licensedContent'] = (data['licensedContent'])*1
        return data

    def remove_irrelavent_features(self,data):
        #As we can see from the feature Importances that "favoriteCount" and "dimension" have 0 importance. So we can just ignore these features
        df = data.drop('favoriteCount',axis = 1 )
        df = df.drop('dimension',axis = 1 )
        return df

'''
if __name__=="__main__":
    DataManager=DataManager()
    print DataManager.cleaned_data.head()

'''