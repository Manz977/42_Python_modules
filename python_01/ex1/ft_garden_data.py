#!/usr/bin/python3.10


class Plants:
    # When we use def inside a class we call it method
    def __init__(self, name, height, age):
        self.name = name
        self.height = str(height) + "cm"
        self.age = str(age) + " days old"


def main():
    plant_1 = Plants('Rose', 25, 30)
    plant_2 = Plants('Sunflower', 80, 45)
    plant_3 = Plants('Cactus', 15, 120)

    garden = [plant_1, plant_2, plant_3]

    print("=== Garden Plant Registry ===")

    for i in range(3):
        plant = garden[i]
        print(f"{plant.name}: "f"{plant.height}, " f"{plant.age} ")


if __name__ == "__main__":
    main()
