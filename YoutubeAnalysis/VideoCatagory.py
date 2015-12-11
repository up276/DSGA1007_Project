Catagory_mapping = {2: 'Autos & Vehicles', 23: 'Comedy' , 27: 'Education', 24: 'Entertainment' , 1: 'Film & Animation', 20: 'Gaming' ,26: 'Howto & Style', 10: 'Music',25: 'News & Politics', 29:'Nonprofits & Activism' ,22:'People & Blogs', 15: 'Pets & Animals' , 28: 'Science & Technology', 17: 'Sports' , 19:'Travel & Events'}

class Catagory_Exception(Exception):
    '''
    User defined exception for the region class
    '''
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class VideoCatagory:


    def __init__(self,val):
        """
        Constructor for the class Region. It will be called at the time of object intialization
        """
        #try:
        global Catagory_mapping
        self.value = val
        self.name = Catagory_mapping[self.value]
        #self.region_income = self.data['income'].values
        #self.region_countries = self.data['Country'].values

        #except:
            #raise Catagory_Exception(" Initialization error ")