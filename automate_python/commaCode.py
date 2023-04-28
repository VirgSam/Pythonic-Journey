spam = ["apples", "bananas", "tofu", "cats"]
spam2 = ["The", "rains", "in", "spain", "falls", "mainly", "on", "the", "plains."]


def commaCode(listParameter):
    """
    Takes a list,
    adds a comma after each individual item
    adds an 'and' prior to last item on the list
    - add try and except statements to capture empty list parameter error.

    """
    counter = 0
    joinItems = []
    for index, item in enumerate(listParameter):
        if counter < len(listParameter) - 1:
            joinItems.append(item + ",")
        counter += 1
        if counter == len(listParameter):
            joinItems.append("and " + item)

    joinItems = " ".join(joinItems)
    print(joinItems)


commaCode(spam)
commaCode(spam2)
