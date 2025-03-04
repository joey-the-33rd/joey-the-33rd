import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go

# Die-rolling simulation
np.random.seed(42)
rolls = np.random.randint(1, 7, 1000)  # Roll a fair six-sided die 1000 times

# Matplotlib histogram for die rolls
plt.figure(figsize=(8, 5))
plt.hist(rolls, bins=np.arange(1, 8) - 0.5, edgecolor='black', alpha=0.75)
plt.xticks(range(1, 7))
plt.xlabel("Die Face")
plt.ylabel("Frequency")
plt.title("Die Rolling Simulation (1000 Rolls)")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()

# Random walk simulation
steps = np.random.choice([-1, 1], size=1000)  # Step left (-1) or right (+1)
position = np.cumsum(steps)  # Cumulative sum to get the walk

# Plotly visualization
fig = go.Figure()
fig.add_trace(go.Scatter(y=position, mode="lines", name="Random Walk"))
fig.update_layout(
    title="Random Walk Simulation",
    xaxis_title="Step Number",
    yaxis_title="Position",
    template="plotly_dark"
)
fig.show()
