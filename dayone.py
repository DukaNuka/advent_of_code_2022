from Elves import Bagpacker



filename = "inputs/DayOne.csv"

with open(filename) as infile:
    packer = Bagpacker(infile)
    print(packer.organise_pile_of_backpacks().most_calories)
