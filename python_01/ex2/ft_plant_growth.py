#!/usr/bin/python3.10
'''Everything is defined inside a class called methods'''


class Plants:

    '''init__ is an initializer.
    It runs automatically to create a new objects'''
    def __init__(self, name, height, age) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self, cm_growth) -> None:
        self.height = self.height + cm_growth

    def days_passed(self, days) -> None:
        self.age = self.age + days

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"


def main():
    rose = Plants("Rose", 25, 30)
    sunflower = Plants("Sunflower", 80, 45)
    cactus = Plants("Cactus", 15, 120)

    garden = [rose, sunflower, cactus]

    print("=== Current Garden Status Day 1 ===")
    for plant in garden:
        print(plant.get_info())

    growth = 6
    days = 6
    for plant in garden:
        plant.grow(growth)
    plant.days_passed(days)

    print("\n=== Current Garden Status Day 7 ===")
    for plant in garden:
        print(plant.get_info())

    print(f"\nGrowth this week: +{growth}cm")


if __name__ == "__main__":
    main()
