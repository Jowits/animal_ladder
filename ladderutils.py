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