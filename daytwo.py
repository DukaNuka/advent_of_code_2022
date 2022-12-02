from Elves import LizardSpock, HandPosition

filename = "inputs/DayTwo.csv"

evaluator = LizardSpock()


with open(filename) as infile:
    for line in infile:
        line = line.strip()
        line = line.split()
        me = HandPosition(value = line[1])
        them = HandPosition(value = line[0])
        evaluator.play(me, them)

print(evaluator.total_points)