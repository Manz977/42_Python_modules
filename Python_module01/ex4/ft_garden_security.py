#!/opt/homebrew/bin/python3.10

class Secure_Plants:
  '''Here we are using encapsulation which means we are hiding the data from the public
      we use (name mangling) to make it private by adding underscores __ before a variable'''
  def __init__(self, name, height, age) -> None:
    self.__name = name
    self.set_height(height)
    self.set_age(age)

  '''This is how we set the getters allowed people to see the data without modifying it '''
  def get_name(self) -> str:
    return self.__name
  def get_height(self) -> int:
      return self.__height
  def get_age(self) -> int:
      return self.__age
    
  '''This is how we set setters allow people to request a change to the data'''
  def set_height(self, new_height) -> bool:
      if new_height >= 0:
        self.__height = new_height
        return True
      else:
        print(f"Security: Negative height rejected")
        return False
    
  def set_age(self, new_age):
    if new_age >= 0:
      self.__age = new_age
    else:
      print("Error: Age cannot be negative!")
      
def main():
   p_1 = Secure_Plants("Rose", 25, 30)
   
   print("=== Garden Security System ===")
   
   print(f"Plant created: {p_1.get_name()}\nHeight updated: {p_1.get_height()}cm \nAge updated: {p_1.get_age()} days\n")
   
   print("Invalid operation attempted: height -5cm \n", end="")
   success = p_1.set_height(-5)
   
   if success:
    print("[OK]")
   else:
    print("[REJECTED]")     
  
  
if __name__ == "__main__":
   main()