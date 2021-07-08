import matplotlib.pyplot as plt
import pandas as pd
fig, ax=plt.subplots()

data=pd.read_csv('Maharashtra Latest Covid Cases.csv')

ax.plot(data['Districts'], data['Positive Cases'], marker='v', linestyle='--', color='lightcoral', label='Positive cases')
ax.plot(data['Districts'], data['Recovered'], marker='o', linestyle='-', color='cyan', label='Recovered')
fig.autofmt_xdate()

ax.set_xlabel('Districts')
ax.set_ylabel('Number of cases')
ax.set_title('Covid cases')
ax.legend()
plt.show()