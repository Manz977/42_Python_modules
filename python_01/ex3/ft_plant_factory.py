#!/usr/bin/python3.10

class Plants:
    def __init__(self, name, height, age) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> str:
        return f"Created: {self.name} ({self.height}cm, {self.age} days)"


def main():
    plant_data = [
     ("Rose", 25, 30),
     ("Oak", 200, 365),
     ("Cactus", 5, 90),
     ("Sunflower", 80, 45),
     ("Fern", 15, 120)
    ]

    garden = []

    print("=== Plant Factory Output ===")

    for name, height, age in plant_data:
        garden.append(Plants(name, height, age))

    number_of_plants = 0

    for plant in garden:
        number_of_plants += 1

        print(plant.get_info())

    print(f"\nTotal plants created: {number_of_plants}")


if __name__ == "__main__":
    main()
