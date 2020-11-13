class Band:
    def __init__(self, name, members=None):
        self.name = name
        self.members = members
    def __str__(self):
        return f"The band {self.name}"
    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"

class Musician:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"My name is {self.name} and I play {self.get_instrument()}"
    def get_instrument(self):
        return f"bleh"


class Guitarist(Musician):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"
    def get_instrument(self):
        return f"guitar"
    def play_solo(self):
        return f"face melting guitar solo"

class Bassist(Musician):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"
    def get_instrument(self):
        return f"bass"
    def play_solo(self):
        return f"bom bom buh bom"

class Drummer(Musician):
    def __init__ (self, name):
        self.name = name
    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"
    def get_instrument(self):
        return f"drums"
    def play_solo(self):
        return f"rattle boom crash"
    
