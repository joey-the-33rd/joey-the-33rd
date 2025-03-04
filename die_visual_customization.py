import plotly.express as px
from die import Die

# Create a D6.
die = Die()
# Make some rolls, and store the results in a list.

results = []

for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analyze the results.
frequencies = []
poss_results = range(1, die.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Show the results in a generated visualization.
# Pass a set of x-values and a set of y-values.
title = "Results of Rolling One D6 1000 times."
labels = {'x': 'Result', 'y': 'Frequency of Results'}
fig = px.bar(x=poss_results, y=frequencies, 
             title=title, labels=labels)
fig.show()
 