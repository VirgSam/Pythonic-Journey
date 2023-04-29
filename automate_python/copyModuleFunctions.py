import copy

spam = ["A", "B", "C", "D"]
print("Id memory reference for the list spam", id(spam))
cheese = copy.copy(spam)
print(
    "Id memory reference for the list cheese", id(cheese)
)  # Cheese is a different list with a different id reference
cheese[1] = 42
print(spam)
print(cheese)
# copy.deepcopy(listWithinLists)
