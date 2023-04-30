#
import random

messages = [
    "It is certain",
    "It is decidedly so",
    "Yes definitely",
    "Reply hazy try again",
    "Ask again later",
    "Concentrate and ask again",
    "My reply is no",
    "Outlook not so good",
    "Very doubtful",
]

print(messages[random.randint(0, len(messages) - 1)])

# Notice the expression you use as the index for messages: random.randint (0, len(messages) - 1).
# This produces a random number to use for the index, regardless of the size of messages.
# That is, you’ll get a random number between 0 and the value of len(messages) - 1.
# The benefit of this approach is that you can easily add and remove strings to the messages list
# without changing other lines of code. If you later update your code,
# there will be fewer lines you have to change and fewer chances for you to introduce bugs.
