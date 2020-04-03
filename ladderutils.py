# There is a ladder.
#  On the 3rd rung of the ladder is a monkey, 
# the 5th rung has a squirrel, 
# the 8th rung has a pigeon, 
# the 15th rung has an eagle, 
# the 17th rung has another monkey.

# The monkey has 2 eyes, 2 hands, 2 legs. 
# The squirrel has 2 eyes, 4 legs. 
# The pigeon has 2 eyes, 2 wings, 2 legs and can fly.
#  The eagle has 2 eyes, 2 wings, 2 legs and can fly.

class Animal(object):

  # creating an instance of class Animal
  def __init__(self,eyes,legs,hands,wings,fly):
    self.eyes= eyes
    self.legs= legs
    self.hands= hands
    self.wings= wings
    self.fly= fly
        
     
 #to be able to fly
  def fly(self):
    return self.fly

 class Monkey(Animal):
  
 # creating an instance of class Monkey with inheritance from class Animal
  def __init__(self,eyes,legs,hands):
    self.name = 'Monkey'
    Animal.__init__(self,eyes,legs,hands,0,False)

  
  def __repr__(self):
   return "Monkey <eyes: {self.eyes}, legs:{self.legs}, hands:{self.hands}>".format(self=self)
   

  # creating an instance of class Squirrel with inheritance from class Animal
class Squirrel(Animal):

  def __init__(self,eyes,legs):
    self.name = 'Squirrel'
    Animal.__init__(self,eyes,legs,0,0,False) 

  def __repr__(self):
   return "Squirrel <eyes:{self.eyes}, legs: {self.legs}>".format(self=self)       
  
  
        
  
# creating an instance of class Pigeon with inheritance from class Animal
class Pigeon(Animal):

  def __init__(self,eyes,legs,wings):
    self.name = 'Pigeon'
    Animal.__init__(self,eyes,legs,0,wings,True)
  
  def __repr__(self):
   return "Pigeon <eyes: {self.eyes}, legs:{self.legs}, wings:{self.wings}>".format(self=self)


# creating an instance of class Egale with inheritance from class Animal
class Eagle(Animal):

  def __init__(self,eyes,legs,wings):
    self.name = 'Eagle'
    Animal.__init__(self,eyes,legs,0,wings,True)

  def __repr__(self):
   return "Eagle <eyes:{self.eyes}, legs:{self.legs}, wings:{self.wings}>".format(self=self)
