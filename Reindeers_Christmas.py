reindeers = ["Comet","Dasher","Prancer","Vixen",
            "Donner","Cupid","Dancer","Blitzen",]

num_reindeers = []
while len(num_reindeers) <= 9:
    for reindeer in reindeers:

        if "Dasher" in reindeers:
            first = reindeers.index("Dasher")
            num_reindeers.append(first)

        if "Dancer" and "Prancer" in reindeers:
            second = reindeers.index("Dancer")
            third = "Prancer"
            num_reindeers.append(second)
            num_reindeers.append(third)

        if "Vixen" in reindeers:
            fourth = "Vixen"
            num_reindeers.append(fourth)

        if "Comet" in reindeers:
            fifth = reindeers.index("Comet")
            num_reindeers.append(fifth)

        if "Cupid" and "Donner" in reindeers:
            sixth = reindeers.index("Cupid")
            seventh = "Prancer"
            num_reindeers.append(sixth)
            num_reindeers.append(seventh)

        if "Blitzen" in reindeers:
            eight = "Blitzen"
            num_reindeers.append(eight)

    print(f" You know {reindeers[first]} and {reindeers[second]} and {third} and {fourth}!")
    print(f" {reindeers[fifth]} and {reindeers[sixth]} and {seventh} and {eight}")
    print(f" But do you recall \n The most famous reindeer of all?")
    print(f" - the Red-Nose Reindeer")

# Copy the code, and using a list method, add Rudolph and print out:
# Rudolph the Red-Nosed Reindeer
# Bonus, if you do not use:
# print("Rudolph")
