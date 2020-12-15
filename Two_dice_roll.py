# coding: utf-8
rolls = [sum([random.randint(1,6), random.randint(1,6)]) for i in range(36000000)]
roll, frequency = np.unique(rolls, return_counts = True)
sns.set_style('darkgrid')
axes = sns.barplot(x=frequency, y=roll, palette = 'bright', orient = "h")
title = f'Rolling of two dice ({len(rolls):,}) times'
plt.title(title, fontsize = 13)
plt.ylabel('Sum of the two Dice', fontsize=13)
plt.xlabel('Frequency of the Occurence', fontsize=13)
plt.xlim(right = max(frequency)*1.10)
for bar, freq in zip(axes.patches, frequency):
    text_x = bar.get_x() + bar.get_width() + 2.0
    text_y = bar.get_y() + bar.get_height() / 2.0
    text = f'{freq:,} \n {freq/len(rolls):.1%}'
    axes.text(text_x,text_y,text,
             fontsize=10, ha = 'left', va = 'center', )
plt.show()
