from .bloodoath import BloodOath

class Follower:

    all = []

    def __init__(self, name, age, life_motto):
        self._name = name
        self._age = age
        self._cults = []
        self._life_motto = life_motto
        Follower.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        self._age = value
    
    @property
    def life_motto(self):
        return self._life_motto
    
    def join_cult(self, cult):
        if cult not in self.cults:
            self.cults.append(cult)
            cult.add_follower(self)
    

    
