class School:
  def __init__(self,name,level,number_of_students):
    self._name = name
    self._level = level
    self._number_of_students = number_of_students

  @property
  def name(self):
    return self._name
  @property
  def level(self):
    return self._level
  @property
  def number_of_students(self):
    return self._number_of_students

  @number_of_students.setter
  def number_of_students(self,students):
    self._number_of_students = students

  def __repr__(self):
    return f"A {self.level} school named {self.name} with {self.number_of_students} students!"

class PrimarySchool(School):
  def __init__(self,name,number_of_students,pick_up_policy):
    super().__init__(name,"primary",number_of_students)
    self._pick_up_policy = pick_up_policy

  @property
  def pick_up_policy(self):
    return self._pick_up_policy
  def __repr__(self):
    addition = super().__repr__()
    return addition + f" The pickup policy is {self.pick_up_policy}"

class HighSchool(School):
  def __init__(self,name,number_of_students,sports_team):
    super().__init__(name,"High",number_of_students)
    self._sports_team = sports_team
  @property
  def sports_team(self):
    return self._sports_team
  def __repr__(self):
    addition = super().__repr__()
    return addition + f" and their sports teams : {self.sports_team[0]} and {self.sports_team[1]} !"
  
a = School("Codecademy", "high", 100)
print(a) 
b = PrimarySchool("Codecademy", 300, "Pickup Allowed")
print(b)
c = HighSchool("Codecademy High", 500, ["Tennis", "Basketball"])
print(c)