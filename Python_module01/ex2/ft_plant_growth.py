#!/opt/homebrew/bin/python3.10

class Plants:
      def __init__(self, name, height, age):
            self.name = name
            self.height = height
            self.age = age
            
      def grow(self, cm_growth):
          self.height = self.height + cm_growth
          
      def days_passed(self, days):
          self.age = self.age + days
          
      def get_info(self):
          return f"{self.name}: {self.height}cm, {self.age} days old"
          
          
def main():
    plant_1 = Plants("Rose", 25, 30)
    print("=== Day 1 ===")
    print(plant_1.get_info())
    
    growth_amount = 6
    days = 6
    plant_1.grow(growth_amount)
    plant_1.days_passed(days)
    
    print("=== Day 7 ===")
    print(plant_1.get_info())
    print(f"Growth this week: +{growth_amount}cm")
    
if __name__ == "__main__":
    main()
