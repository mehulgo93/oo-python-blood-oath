from .bloodoath import BloodOath

class Cult:

    all = []

    def __init__(self, name, location, founding_year, slogan):
        self._name = name
        self._location = location
        self._founding_year = founding_year
        self. _slogan = slogan
        self._followers = []
        Cult.all.append(self)

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
    
    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, value):
        self._location = value

    @property
    def slogan(self):
        return self._slogan
    
    @slogan.setter
    def slogan(self, value):
        self._slogan = value
    
    @property
    def founding_year(self):
        return self._founding_year
    
    def recruit_follower(self, follower):
        return self._followers.append(follower)
    
    def cult_population(self):
        return len(self._followers)
    
    def find_by_name(self, name):
        pass


    def find_by_location(self, location):
        pass


    def find_by_founding_year(self, founding_year):
        pass


    def average_age(self):
        total_age = sum(follower.age for follower in self._followers)
        average = total_age / len(self._followers)
        return average 
    
    def my_followers_mottos(self):
        for follower in self._followers:
            print(follower.life_motto)

    @classmethod
    def least_popular(cls):
        if not cls.cults_by_location:
            return None

        return min(cls.cults_by_location.values(), key=lambda cults: len(cults))

    @classmethod
    def most_common_location(cls):
        if not cls.cults_by_location:
            return None

        return max(cls.cults_by_location, key=lambda location: len(cls.cults_by_location[location]))

    
