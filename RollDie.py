# coding: utf-8
import sys 
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import random
rolls = [random.randrange(1, 7) for i in range(int(sys.argv[1]))]
values, frequencies = np.unique(rolls, return_counts = True)
title = f'Rolling a Six-Sided Die {len(rolls):,} Times'
sns.set_style('darkgrid')
axes = sns.barplot(x = values, y= frequencies, palette ='bright')
plt.title(title)
plt.xlabel('Die Number')
plt.ylabel('Frequency')
plt.ylim(0, top=max(frequencies)* 1.10)
for bar, frequency in zip(axes.patches, frequencies):
    text_x = bar.get_x() + bar.get_width() / 2.0
    text_y = bar.get_height()
    text = f'{frequency:,}\n{frequency / len(rolls):.2%}'
    axes.text(text_x, text_y, text, fontsize=12,
               ha='center', va = 'bottom')
plt.show()