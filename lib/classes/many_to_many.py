class Band:
    def __init__(self, name, hometown):
        self.name = name
        self._hometown = hometown

    @property
    def name(self):
        return self._name
    
    @name.setter 
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("name must be must be of type string")
        self._name = value
    
    @property 
    def hometown(self):
        return self._hometown
    
    #def hometown(self, value):
     #   if not isinstance(value, str) or len(value) == 0:
      #      raise ValueError("hometown must be must be of type string")
       # self._hometown = value

    
    def concerts(self):
        return [concert for concert in Concert.all_concerts if concert.band == self] or None

    def venues(self):
        if not self.concerts():
            return None
        return list({concert.venue for concert in self.concerts})

    def play_in_venue(self, venue, date):
        return Concert(date, self, venue)

    def all_introductions(self):
        if not self.concerts:
            return None
        return [concert.introduction() for concert in self.concerts]


class Concert:
    all_concerts = []

    def __init__(self, date, band, venue):
        self.date = date
        self.band = band
        self.venue = venue
        Concert.all_concerts.append(self)
    
    @property
    def date(self):
        return self._date
    
    @date.setter 
    def date(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("name must be must be of type string")
        self._date = value

    @property 
    def band(self):
        return self._band
    
    @band.setter
    def band(self, value):
        if not isinstance(value, Band):
            raise ValueError("Band must be an instance of Band")
        self._band = value

    @property 
    def venue(self):
        return self._venue 
    
    @venue.setter 
    def venue(self, value):
        if not isinstance(value, Venue):
            raise ValueError("venue must be instance of Venue")
        self._venue = value

    def hometown_show(self):
        return self.band.hometown == self.venue.city

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band,name} and we're from {self.band.hometown}"


class Venue:
    def __init__(self, name, city):
        self.name = name
        self.city = city
    
    @property
    def name(self):
        return self._name
    
    @name.setter 
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("name must be must be of type string")
        self._name = value

    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self, value):
        if not (value, str) or len(value) ==0:
            raise ValueError ("City must be a non empty string")
        self._city = value 

    def concerts(self):
        return [concert for concert in Concert.all_concerts if concert.venue == self] or None

    def bands(self):
        if not self.concerts():
            return None
        return list({concert.band for concert in self.concerts()})
    def concert_on(self, date):
        for concert in self.concerts() or []:
            if concert.date == date:
                return concert
        return None