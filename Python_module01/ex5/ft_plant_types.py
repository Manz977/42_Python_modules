#!/opt/homebrew/bin/python3.10

class Plant:
  '''This is the parent class for the plants type
  Args:
      name, height, and the age of the plants.
  Returns: 
      None.
  Methods:
      display() method. This method automates the printing of plant' common features
  '''
  def __init__(self, name, height, age) -> None:
    self.name = name
    self.height = height
    self.age = age
    
  def display(self):
        print(f"{self.name} ({self.__class__.__name__}): {self.height}cm, {self.age} days,", end=" " )
  
  '''The code under we created three child classes of the plant class
      each class has a super() function which allows a child class
      to call methods from its parent class.
    Methods: 
      we added two different instance methods, one for a specific action 
      and one to display the common features from the parent class
  '''
class Flower(Plant):
  def __init__(self, name, height, age, color):
      super().__init__(name, height, age)
      self.color = color
      
  def bloom(self):
      print(self.name, "is blooming beautifully!\n")

  def display(self):
     super().display()
     print(f"{self.color} color")
     self.bloom()
    

class Tree(Plant):
  def __init__(self, name, height, age, trunk_diameter):
      super().__init__(name, height, age)
      self.trunk_diameter = trunk_diameter
     
  def produce_shade(self):
      print(self.name, "provides", self.trunk_diameter, "square meters of shade\n" )
      
  def display(self):
     super().display()
     print(f"{self.trunk_diameter}cm diameter")
     self.produce_shade()

class Vegetable(Plant):
  def __init__(self, name, height, age, harvest_season, nutritional_value):
     super().__init__(name, height, age)
     self.harvest_season = harvest_season
     self.nutritional_value = nutritional_value

  def display(self):
      super().display()
      print(self.harvest_season)
      print(self.name, "is rich in", self.nutritional_value, "\n")
  
  '''In the main we created a data structure to old the instances of the plant type.
    We used a for loop to loop through the array and print out the plant types
  ''' 
def main():
  garden_data = [
    Flower("Rose", 15, 1, "Red"),
    Flower("Lily", 10, 1, "White"),
    Tree("Oak", 500, 20, 2),
    Tree("Pine", 300, 5, 1),
    Vegetable("Carrot", 5, 1, "Autumn", "Vitamin A"),
    Vegetable("Kale", 8, 1, "Winter", "Iron")
  ]
  
  print("=== Garden Plant Types ===\n")
  
  for plant in garden_data:
      plant.display()

if __name__ == "__main__":
  main()