from io import TextIOWrapper

class Elf:
    def __init__(self):
        self.food_items = []

    def add_food(self, calories : int):
        self.food_items.append(calories)

    def add_backpack(self, contents : list):
        for item in contents:
            self.add_food(item)

    @property
    def calories(self):
        total_calories = 0
        for food_item in self.food_items:
            total_calories+=food_item
        return total_calories


class Elves:
    def __init__(self):
        self.elves = []
        self.most_calories = -1

    def add_elf(self, elf : Elf):
        self.elves.append(elf)
        if elf.calories > self.most_calories:
            self.most_calories = elf.calories


class Bagpacker: #wordplay on backpack and packing bags
    def __init__(self, file : TextIOWrapper):
        self.file_handle = file

    def get_next_backpack(self):
        backpack = []
        current_line = self.file_handle.readline().strip()
        if current_line == '':
            return None
        while not current_line == '':
            backpack.append(int(current_line))
            current_line = self.file_handle.readline().strip()
        return backpack

    def organise_pile_of_backpacks(self, pile : TextIOWrapper = None):
        if pile is not None:
            self.file_handle = pile
        backpack = self.get_next_backpack()
        all_elves = Elves()
        while backpack:
            new_elf = Elf()
            new_elf.add_backpack(backpack)
            all_elves.add_elf(new_elf)
            backpack = self.get_next_backpack()

        return all_elves