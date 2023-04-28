# https://autbor.com/setdefault
message = "It was a bright cold day in April, and the clocks were striking thirteen."
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = (
        count[character] + 1
    )  # dictName[key]=> value, value is 0 from above
print(count)
