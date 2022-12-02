from io import TextIOWrapper
from enum import Enum

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

    def add_elf(self, elf : Elf):
        self.elves.append(elf)

    @property
    def most_calories(self):
        self.elves.sort(key=lambda elf:elf.calories, reverse=True)
        return [self.elves[0].calories, sum(self.elves[x].calories for x in range(0,3))]


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

class HandPosition:
    rock = 1
    paper = 2
    scissor = 3

    def __init__(self, value : str = None):
        if value == 'A' or value ==  'X':
            self.state = self.rock
        elif value == 'B' or value ==  'Y':
            self.state = self.paper
        elif value == 'C' or value ==  'Z':
            self.state = self.scissor
        else:
            self.state = None

    def __gt__(self, other):
        if self == other:
            return False
        if self.state == self.rock:
            return True if other.state == self.scissor else False
        if self.state == self.paper:
            return True if other.state == self.rock else False
        if self.state == self.scissor:
            return True if other.state == self.paper else False

    def __lt__(self, other):
        if self == other:
            return False
        else:
            return not self > other

    def __eq__(self, other):
        if self.state == other.state:
            return True

    def __ne__(self, other):
        return not self.__eq__(other)

    @property
    def points(self):
        return self.state

class LizardSpock:
    def __init__(self):
        self.total_points = 0

    def reset(self):
        self.total_points = 0

    def play(self, me : HandPosition, them : HandPosition):
        to_add = 0
        to_add += me.state
        if me > them:
            to_add += 6
        elif me == them:
            to_add += 3
        self.total_points += to_add