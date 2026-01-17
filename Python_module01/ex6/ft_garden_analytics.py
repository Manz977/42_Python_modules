#!/opt/homebrew/bin/python3.10

class Plant:

    def __init__(self, name, height, plant_type):
        self.__plant_type = plant_type
        self.__name = name
        self.__height = 0
        self.set_height(height)
        self._growth_tracker = 0

    def get_name(self) -> str:
        return self.__name

    def get_height(self) -> int:
        return self.__height

    def get_plant_type(self) -> str:
        return self.__plant_type

    def get_growth_tracker(self) -> int:
        return self._growth_tracker

    def get_description(self):
        return f"{self.__name}: {self.__height}cm"

    def grow(self):
        self.__height += 1
        self._growth_tracker += 1
        print(f"{self.__name} grew 1cm")

    def set_height(self, new_height) -> bool:
        if new_height >= 0:
            self.__height = new_height
            return True
        else:
            return False


class FloweringPlant(Plant):
    def __init__(self, name, height, plant_type, color):
        super().__init__(name, height, plant_type)
        self.color = color

    def get_description(self):
        return f"{super().get_description()}, {self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, plant_type, color, prize_value):
        super().__init__(name, height, plant_type, color)
        self.prize_value = prize_value

    def get_description(self):
        return f"{super().get_description()}, Prize points: {self.prize_value}"


class GardenManager:
    total_gardens = 0

    def __init__(self):
        self.gardens = {}

    @classmethod
    def create_garden_network(cls):
        return cls()

    def create_garden(self, owner_name):
        self.gardens[owner_name] = []
        GardenManager.total_gardens += 1

    def add_plant(self, owner, plant):
        if owner in self.gardens:
            self.gardens[owner].append(plant)
            print(f"Added {plant.get_name()} to {owner}'s garden")
        else:
            print(f"Error: Garden for {owner} not found.")

    def help_grow(self, owner):
        print(f"\n{owner} is helping all plants grow...")
        for plant in self.gardens[owner]:
            plant.grow()
            
    def get_garden_score(self, owner):
        score = 0
        if owner in self.gardens:
            for plant in self.gardens[owner]:
                score += plant.get_height()
                if plant.get_plant_type() == "Prize":
                  score += plant.prize_value
        return score
      
    class GardenStats:
        @staticmethod
        def report(owner, plants):
            print(f"\n=== {owner}'s Garden Report ===")
            print("Plants in garden: ")

            total_growth = 0
            plant_count = 0
            types = {"regular": 0, "flowering": 0, "prize": 0}

            for p in plants:
                plant_count += 1

                print(f"- {p.get_description()}")
                total_growth += p.get_growth_tracker()
                p_type = p.get_plant_type()

                if p_type == "Prize":
                    types["prize"] += 1
                elif p_type == "Flowering":
                    types["flowering"] += 1
                else:
                    types["regular"] += 1

            print(f"\nPlants added: {plant_count}, Total growth: {total_growth}cm")
            print(f"Plant types: {types['regular']} regular, {types['flowering']} flowering, {types['prize']} prize flowers")


def main():
    print("=== Garden Management System Demo ===\n")

    manager = GardenManager.create_garden_network()
    manager.create_garden("Manar")
    manager.create_garden("Bob")

    p1 = Plant("Oak Tree", 100, "Regular")
    p2 = FloweringPlant("Rose", 25, "Flowering", "red")
    p3 = PrizeFlower("Sunflower", 50, "Prize", "yellow", 10)

    manager.add_plant("Manar", p1)
    manager.add_plant("Manar", p2)
    manager.add_plant("Manar", p3)

    manager.help_grow("Manar")

    GardenManager.GardenStats.report("Manar", manager.gardens["Manar"])

    print(f"\nHeight validation test: {p1.set_height(101)}")

    bob_plant = Plant("Bush", 92, "Regular")

    manager.gardens["Bob"].append(bob_plant)

    print(f"Garden scores- Manar: {manager.get_garden_score('Manar')}, Bob: {manager.get_garden_score('Bob')}")
    print(f"Total gardens managed: {GardenManager.total_gardens}")


if __name__ == "__main__":
    main()
