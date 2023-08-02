class BloodOath:

    all = []

    def __init__(self, cult, follower,  date):
        self._date = date
        self._cult = cult
        self._follower = follower

    @property
    def date(self):
        return self._date
    
    @property
    def cult(self):
        return self._cult
    
    
