import plotly.express as px
from die import Die

# Create a D6 and D10 dice.
die_1 = Die()
die_2 = Die(10)
# Make some rolls, and store the results in a list.

results = []

for roll_mun in range (50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze thee results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
title = f"Results of Rolling a D6 and D10 dice {50,000} Times."
labels = {'x': 'Results', 'y': 'Frequency of Results'}
fig =px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customization of the chat.
fig.update_layout(xaxis_dtick=1)

fig.write_html('dice_vishuald6d10.html')