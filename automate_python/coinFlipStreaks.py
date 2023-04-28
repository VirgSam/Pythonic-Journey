import random

numberOfStreaks = 0  # use individual results from non overlap to do calc.
tossRecord = []
pattern1 = [
    "T",
    "T",
    "T",
    "T",
    "T",
    "T",
]
pattern2 = [
    "H",
    "H",
    "H",
    "H",
    "H",
    "H",
]
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    if random.randint(0, 1) == 0:
        tossRecord.append("H")
    else:
        tossRecord.append("T")

tossRecord = "".join(str(x) for x in tossRecord)
patternTails = "".join(str(x) for x in pattern1)
patternHeads = "".join(str(x) for x in pattern2)
print(
    " Tails streaks with no overlap :", tossRecord.count(patternTails)
)  # for no overlapping
print(
    " Heads streaks with no overlap :", tossRecord.count(patternHeads)
)  # for no overlapping


def overlapping_occurences(string, sub):
    # Code that checks if there is a streak of 6 heads or tails in a row.
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count += 1
        else:
            return count


print("Tails streaks with overlap :", overlapping_occurences(tossRecord, patternTails))
print("Tails streaks with overlap :", overlapping_occurences(tossRecord, patternHeads))

print("Chance of streak: %s%%" % (numberOfStreaks / 100))
