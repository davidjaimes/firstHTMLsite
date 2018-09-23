import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

results = pd.read_csv("ADS_results.csv")
results = results.groupby(['name', 'year']).sum().reset_index()
results['pct'] = 100 * results['count'] / results['total_count']

matplotlib.rc('axes', edgecolor='C7')
fig, ax = plt.subplots()

for name, group in results.groupby('name'):
    if name in ['R', 'C', 'Java', 'Julia']:
        continue
    group.plot.line(x='year', y='pct', ax=ax, label=name, linewidth=3)

ax.set(xlabel='Year of Publication',
       ylabel='Percent of Publications')

# text annotations
leg = plt.legend(loc=2, fontsize=16)
leg.get_frame().set_alpha(0)
for i, text in enumerate(leg.get_texts()):
    text.set_color("C" + str(i))
plt.xlabel("Year of publication", color="C7", size=16)
plt.ylabel("Percent of publications", color="C7", size=16)

# final layout options
plt.xticks(np.arange(1995, 2019, 2), color="C7")
plt.yticks(np.arange(0.0, 0.30, 0.05), color="C7")
plt.gca().set_xticks(np.arange(1995, 2018, 1), minor=True)
plt.gca().set_yticks(np.arange(0.0, 0.25, 0.01), minor=True)
plt.tick_params(which='minor', length=5, color="C7")
plt.tick_params(which='major', length=10, color="C7")
plt.gca().xaxis.set_ticks_position("both")
plt.gca().yaxis.set_ticks_position("both")
plt.grid(linestyle="dashed", linewidth=0.5)
plt.ylim(0.00, 0.25)
plt.tight_layout()
fig.savefig('ads-languages.png', transparent=True, dpi=300)
