#!/opt/homebrew/bin/python3.10

class Plants:
      def __init__(self, name, height, age):
            self.name = name
            self.height = str (height) + "cm,"
            self.age = age

def main():  
    plant_1 = Plants("Rose", 25, 30)
    plant_2 = Plants("Sunflower", 80, 45)
    plant_3 = Plants("Cactus", 15, 120)

    garden = [plant_1, plant_2, plant_3]

    print("=== Garden Plant Registry ===")

    for i in range(3):
  
      current_plant = garden[i]
  
      print(f"{current_plant.name}: " f"{current_plant.height} "  f"{current_plant.age} days old")

if __name__ == "__main__":
    main()