from die import Die
# Create a D6.
die = Die()
# Make some rolls, and store the results in a list.

results = []

for roll_mun in range (1000):
    result = die.roll()
    results.append(result)

# Analyze thee results.
frequencies = []
poss_results = range(1, die.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Show the results of exactly how many times 
# each number appears.
print(frequencies)