class Cat("pet"):
    def __init__(self,name,age,hunger,playful,place):
    Pet.___init___(self,name,age,hunger,playful)
    self.__favoritePlaceToSit = place

    def wantsToSit(self):
        if self.playful == False:
            print("The cat wants to sit in" ,self.FavoritePlace)
        else:
            print("The cat wants to play")

    def _str_(self):
        return(self.name + "likes to sit in" + self.FavoritePlace)
    
class Human:
    def _init_(self,name,pets):
        self.name = name
        self.Pets = pets

    def hasPets(self):
        if len(self.Pets) != 0:
            return "yes"
        else:
            return "no"
        



