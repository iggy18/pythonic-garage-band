class Band:
    def __init__(self, name, members=None):
        self.name = name
        self.members = members
    def __str__(self):
        return f"The band {self.name}"
    def __repr__(self):
        return f"Band instance. name={self.name}, members={self.members}"
    def play_solos(self):
        solos = []
        for member in self.members:
            solos.append(member.play_solo())
            # could also use 'solos += [member.play_solo()]'
        return solos



class Musician:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"My name is {self.name} and I play {self.get_instrument()}"
    def get_instrument(self):
        return f"bleh"
    def __repr__(self):
        return f"{self.__class__.__name__} instance. Name = {self.name}"


class Guitarist(Musician):
    def __init__(self, name): 
        self.name = name
    def get_instrument(self):
        return f"guitar"
    def play_solo(self):
        return f"face melting guitar solo"


class Bassist(Musician):
    def __init__(self, name):
        self.name = name
    def get_instrument(self):
        return f"bass"
    def play_solo(self):
        return f"bom bom buh bom"


class Drummer(Musician):
    def __init__ (self, name):
        self.name = name
    def get_instrument(self):
        return f"drums"
    def play_solo(self):
        return f"rattle boom crash"
    
