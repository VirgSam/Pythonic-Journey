# 51. Write a Python program to determine profiling of Python programs.
# Note: A profile is a set of statistics that describes how often and 
# for how long various parts of the program executed. These statistics
#  can be formatted into reports via the pstats module.

import cProfile
def sum():
    print(1+2)
cProfile.run('sum()')

# def joinerExercise():
#     basicList = ['We','didnt','start','the','fire','but','the','house','was','burning.']
#     join_elements = ' '.join(basicList)
#     print(join_elements)

# joinerExercise()
# cProfile.run('joinerExercise()')

# what is the utility for cProfile in programming?