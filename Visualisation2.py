import matplotlib.pyplot as plt
import pandas as pd
plt.style.use('fast')

data=pd.read_csv('Maharashtra Latest Covid Cases.csv', index_col=0)
fig, ax=plt.subplots()

ax.bar(data.index, data['Recovered'], label='Recovered')
ax.bar(data.index, data['Deceased'], bottom=data['Recovered'], label='Deceased')
ax.set_xticklabels(data.index, rotation=90)


ax.set_xlabel('Districts')
ax.set_ylabel('Number of cases (mln)')
ax.set_title('Covid cases')
ax.legend()
plt.show()