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

class Ladder:
  ladder_pos = {}

  # creating an instance of class Ladder
  def __init__(self):
    self.ladder_pos['3'] = Monkey(2,2,2)
    self.ladder_pos['5'] = Squirrel(2,4)
    self.ladder_pos['8'] = Pigeon(2,2,2)
    self.ladder_pos['15'] = Eagle(2,2,2)
    self.ladder_pos['17'] = Monkey(2,2,2)
  #which animal is at the rung
  def animal_at_rung(self,pos):
      if(str(pos) in self.ladder_pos):
        return self.ladder_pos[str(pos)]
      else:
        return ('None')

   #get number of all animals
  def get_animals_count(self):
    return len(self.ladder_pos)
  
  #is it empty or not
  def hop(self,pos):
    if(str(pos+1) in self.ladder_pos):
      return ("Not Empty")
    else:
      self.ladder_pos[str(pos+1)] = self.ladder_pos[str(pos)]
      del self.ladder_pos[str(pos)]
      return ('None')
