from ladderutils import Ladder


l = Ladder()
print (l.animal_at_rung(3))
print (l.animal_at_rung(5))
print (l.animal_at_rung(8))
print (l.animal_at_rung(15))
print (l.animal_at_rung(10))
print (l.get_animals_count())
print (l.animal_at_rung(3) == l.animal_at_rung(17))
print (type(l.animal_at_rung(3)) == type(l.animal_at_rung(17)))
print (l.animal_at_rung(8).fly())
print (l.animal_at_rung(3).fly())
print (l.hop(3))
print (l.animal_at_rung(3))
print (l.animal_at_rung(4))
print (l.hop(4))
print (l.animal_at_rung(4))
