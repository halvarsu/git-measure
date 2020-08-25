#!/usr/bin/env python
# coding: utf-8

# In[27]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

with open('lengths.txt') as infile:
    txt = infile.read()

def split_line(line):
    parts = line.split()
    f = parts[0].split('/')[-1]
    num = int(parts[-2])
    prev = int(parts[-4])
    return f, num, prev
dates = []
files = []
lengths = []
prev_lengths = []
for t in txt.split('commit')[1:]:
    dates.append(t.split('\n')[2][8:])
    
    line1 = t.split('\n')[6]
    line2 = t.split('\n')[8]
    if line2:
        f, num, prev = split_line(line2)
    else:
        f, num, prev = split_line(line1)
    files.append(f)
    lengths.append(num)
    prev_lengths.append(prev)

df = pd.DataFrame()
df['lengths'] = lengths
df['prev_lengths'] = prev_lengths
df['change'] = df['lengths'] - df['prev_lengths']
df['dates'] = pd.to_datetime(dates)
df['files'] = files

plt.figure(figsize = [16,9])
for name, item in df.groupby('files'):
    if np.size(item['lengths']) > 1:
        plt.plot(item['dates'], item['lengths'], label = name)
    
df_change = df[['dates', 'change']].sort_values(by='dates').reset_index(drop=True)
df_change['total_length'] = df['change'].cumsum()
df_change
plt.plot(df_change['dates'], df_change['total_length'], label='total')
    
plt.grid()
plt.legend()
plt.show()


# In[ ]:




