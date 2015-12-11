'''
Created on Dec 5, 2015

@author: urjit0209,vec241, mc3784
'''

class Video():
    title         =""
    description   = ""
    published_at  = ""
    viewCount     = -1
    likeCount     = -1
    dislikeCount  = -1
    favoriteCount = -1
#Other features to add:
#"commentCount",
#"duration",
#"dimension",
#"definition",
#"caption",
#"licensedContent",
#"topicIds",
#"relevantTopicIds"
    def __init__(self,title,description,published_at,viewCount,
                 likeCount,dislikeCount,favoriteCount,commentCount):
        """
            Video Constructor: initialize all the video's features.
        """
        self.title = title
        self.description = description
        self.published_at = published_at
        self.viewCount = viewCount
        self.likeCount = likeCount
        self.dislikeCount = dislikeCount
        self.favoriteCount = favoriteCount

    def assignLabel(self):
        """
            Write logic to perform the prediction of the label and return the label value
        """
        print "Performing label prediction for the inserted data..."
        return "label"
